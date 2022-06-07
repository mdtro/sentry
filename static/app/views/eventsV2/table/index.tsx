import {PureComponent} from 'react';
import styled from '@emotion/styled';
import {Location} from 'history';

import {EventQuery} from 'sentry/actionCreators/events';
import {Client, resolveUrl} from 'sentry/api';
import Pagination from 'sentry/components/pagination';
import {t} from 'sentry/locale';
import {Organization} from 'sentry/types';
import {metric, trackAnalyticsEvent} from 'sentry/utils/analytics';
import {TableData} from 'sentry/utils/discover/discoverQuery';
import EventView, {
  isAPIPayloadSimilar,
  LocationQuery,
} from 'sentry/utils/discover/eventView';
import Measurements from 'sentry/utils/measurements/measurements';
import parseLinkHeader from 'sentry/utils/parseLinkHeader';
import {SPAN_OP_BREAKDOWN_FIELDS} from 'sentry/utils/performance/spanOperationBreakdowns/constants';
import {decodeScalar} from 'sentry/utils/queryString';
import withApi from 'sentry/utils/withApi';

import TableView from './tableView';

type TableProps = {
  api: Client;
  confirmedQuery: boolean;
  eventView: EventView;
  location: Location;
  onChangeShowTags: () => void;
  organization: Organization;
  setError: (msg: string, code: number) => void;
  showTags: boolean;
  title: string;
};

type TableState = {
  error: null | string;
  isLoading: boolean;
  pageLinks: null | string;
  tableData: TableData | null | undefined;
  tableFetchID: symbol | undefined;
};

/**
 * `Table` is a container element that handles 2 things
 * 1. Fetch data from source
 * 2. Handle pagination of data
 *
 * It will pass the data it fetched to `TableView`, where the state of the
 * Table is maintained and controlled
 */
class Table extends PureComponent<TableProps, TableState> {
  state: TableState = {
    isLoading: true,
    tableFetchID: undefined,
    error: null,

    pageLinks: null,
    tableData: null,
  };

  componentDidMount() {
    this.fetchData();
  }

  componentDidUpdate(prevProps: TableProps) {
    // Reload data if we aren't already loading, or if we've moved
    // from an invalid view state to a valid one.
    if (
      (!this.state.isLoading && this.shouldRefetchData(prevProps)) ||
      (prevProps.eventView.isValid() === false && this.props.eventView.isValid()) ||
      prevProps.confirmedQuery !== this.props.confirmedQuery
    ) {
      this.fetchData();
    }
  }

  shouldRefetchData = (prevProps: TableProps): boolean => {
    const thisAPIPayload = this.props.eventView.getEventsAPIPayload(this.props.location);
    const otherAPIPayload = prevProps.eventView.getEventsAPIPayload(prevProps.location);

    return !isAPIPayloadSimilar(thisAPIPayload, otherAPIPayload);
  };

  fetchData = () => {
    const {eventView, organization, location, setError, confirmedQuery} = this.props;

    if (!eventView.isValid() || !confirmedQuery) {
      return;
    }

    // note: If the eventView has no aggregates, the endpoint will automatically add the event id in
    // the API payload response

    const shouldUseEvents = organization.features.includes(
      'discover-frontend-use-events-endpoint'
    );
    const url = shouldUseEvents
      ? resolveUrl('organization-events', organization)
      : `/organizations/${organization.slug}/eventsv2/`;
    const tableFetchID = Symbol('tableFetchID');

    // adding user_modified property. this property will be removed once search bar experiment is complete
    const apiPayload = eventView.getEventsAPIPayload(location) as LocationQuery &
      EventQuery & {user_modified?: string};
    apiPayload.referrer = 'api.discover.query-table';

    const queryUserModified = decodeScalar(location.query.userModified);
    if (queryUserModified !== undefined) {
      apiPayload.user_modified = queryUserModified;
    }

    setError('', 200);

    this.setState({isLoading: true, tableFetchID});
    metric.mark({name: `discover-events-start-${apiPayload.query}`});

    this.props.api.clear();
    this.props.api
      .requestPromise(url, {
        method: 'GET',
        includeAllArgs: true,
        query: apiPayload,
      })
      .then(([data, _, resp]) => {
        // We want to measure this metric regardless of whether we use the result
        metric.measure({
          name: 'app.api.discover-query',
          start: `discover-events-start-${apiPayload.query}`,
          data: {
            status: resp && resp.status,
          },
        });
        if (this.state.tableFetchID !== tableFetchID) {
          // invariant: a different request was initiated after this request
          return;
        }

        const {fields, ...nonFieldsMeta} = data.meta ?? {};
        // events api uses a different response format so we need to construct tableData differently
        const tableData = shouldUseEvents
          ? {
              ...data,
              meta: {...fields, nonFieldsMeta},
            }
          : data;

        this.setState(prevState => ({
          isLoading: false,
          tableFetchID: undefined,
          error: null,
          pageLinks: resp ? resp.getResponseHeader('Link') : prevState.pageLinks,
          tableData,
        }));
      })
      .catch(err => {
        metric.measure({
          name: 'app.api.discover-query',
          start: `discover-events-start-${apiPayload.query}`,
          data: {
            status: err.status,
          },
        });

        const message = err?.responseJSON?.detail || t('An unknown error occurred.');
        this.setState({
          isLoading: false,
          tableFetchID: undefined,
          error: message,
          pageLinks: null,
          tableData: null,
        });

        trackAnalyticsEvent({
          eventKey: 'discover_search.failed',
          eventName: 'Discover Search: Failed',
          organization_id: this.props.organization.id,
          search_type: 'events',
          search_source: 'discover_search',
          error: message,
        });

        setError(message, err.status);
      });
  };

  render() {
    const {eventView} = this.props;
    const {pageLinks, tableData, isLoading, error} = this.state;

    const isFirstPage = pageLinks
      ? parseLinkHeader(pageLinks).previous.results === false
      : false;

    return (
      <Container>
        <Measurements>
          {({measurements}) => {
            const measurementKeys = Object.values(measurements).map(({key}) => key);

            return (
              <TableView
                {...this.props}
                isLoading={isLoading}
                isFirstPage={isFirstPage}
                error={error}
                eventView={eventView}
                tableData={tableData}
                measurementKeys={measurementKeys}
                spanOperationBreakdownKeys={SPAN_OP_BREAKDOWN_FIELDS}
              />
            );
          }}
        </Measurements>
        <Pagination pageLinks={pageLinks} />
      </Container>
    );
  }
}

export default withApi(Table);

const Container = styled('div')`
  min-width: 0;
`;
