import pytest


@pytest.fixture
def replay_event_init(default_project):
    event_id = "163c16e78a5049a5b64829cc1e263d9b"
    return {
        "type": "replay_event",
        "payload": b'{"event_id":"163c16e78a5049a5b64829cc1e263d9b","level":"error","version":"7","type":"replay_event","transaction":"sentry-replay","logger":"","platform":"javascript","timestamp":1649965212.374942,"start_timestamp":1649965212.374942,"received":1649965212.376442,"environment":"production","user":{"ip_address":"127.0.0.1"},"request":{"url":"https://75030aaee25f.ngrok.io/","headers":[["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"]]},"contexts":{"browser":{"name":"Chrome","version":"100.0.4896","type":"browser"},"device":{"family":"Mac","model":"Mac","brand":"Apple","type":"device"},"os":{"name":"Mac OS X","version":"10.15.7","type":"os"},"trace":{"trace_id":"ffb5344a41dd4b219288187a2cd1ad6d","span_id":"ba1586800b803058","status":"unknown","tags":{"isReplayRoot":"yes"},"type":"trace"}},"breadcrumbs":{"values":[{"timestamp":1649965212.328442,"type":"default","category":"console","level":"info","message":"%c prev state color: #9E9E9E; font-weight: bold [object Object]","data":{"arguments":["%c prev state","color: #9E9E9E; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649965212.329442,"type":"default","category":"console","level":"info","message":"%c action     color: #03A9F4; font-weight: bold [object Object]","data":{"arguments":["%c action    ","color: #03A9F4; font-weight: bold",{"payload":"[Object]","type":"@@router/LOCATION_CHANGE"}],"logger":"console"}},{"timestamp":1649965212.329442,"type":"default","category":"console","level":"info","message":"%c next state color: #4CAF50; font-weight: bold [object Object]","data":{"arguments":["%c next state","color: #4CAF50; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649965212.332442,"type":"default","category":"console","level":"info","message":"%c prev state color: #9E9E9E; font-weight: bold [object Object]","data":{"arguments":["%c prev state","color: #9E9E9E; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649965212.332442,"type":"default","category":"console","level":"info","message":"%c action     color: #03A9F4; font-weight: bold [object Object]","data":{"arguments":["%c action    ","color: #03A9F4; font-weight: bold",{"payload":null,"skipTracking":true,"token":null,"type":"APP_LOAD"}],"logger":"console"}},{"timestamp":1649965212.332442,"type":"default","category":"console","level":"info","message":"%c next state color: #4CAF50; font-weight: bold [object Object]","data":{"arguments":["%c next state","color: #4CAF50; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649965212.338442,"type":"default","category":"console","level":"warning","message":"Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s App, ConnectedRouter, Route, Router, Switch","data":{"arguments":["Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s","App, ConnectedRouter, Route, Router, Switch"],"logger":"console"}},{"timestamp":1649965212.338442,"type":"default","category":"console","level":"warning","message":"Warning: componentWillReceiveProps has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move data fetching code or side effects to componentDidUpdate.\\n* If you\'re updating state whenever props change, refactor your code to use memoization techniques or move it to static getDerivedStateFromProps. Learn more at: https://fb.me/react-derived-state\\n* Rename componentWillReceiveProps to UNSAFE_componentWillReceiveProps to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s App, Route, Router, Switch","data":{"arguments":["Warning: componentWillReceiveProps has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move data fetching code or side effects to componentDidUpdate.\\n* If you\'re updating state whenever props change, refactor your code to use memoization techniques or move it to static getDerivedStateFromProps. Learn more at: https://fb.me/react-derived-state\\n* Rename componentWillReceiveProps to UNSAFE_componentWillReceiveProps to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s","App, Route, Router, Switch"],"logger":"console"}},{"timestamp":1649965212.346442,"type":"default","category":"console","level":"info","message":"%c prev state color: #9E9E9E; font-weight: bold [object Object]","data":{"arguments":["%c prev state","color: #9E9E9E; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649965212.346442,"type":"default","category":"console","level":"info","message":"%c action     color: #03A9F4; font-weight: bold [object Object]","data":{"arguments":["%c action    ","color: #03A9F4; font-weight: bold",{"subtype":"HOME_PAGE_LOADED","type":"ASYNC_START"}],"logger":"console"}},{"timestamp":1649965212.347442,"type":"default","category":"console","level":"info","message":"%c next state color: #4CAF50; font-weight: bold [object Object]","data":{"arguments":["%c next state","color: #4CAF50; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649965212.350442,"type":"default","category":"console","level":"warning","message":"Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s Home","data":{"arguments":["Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s","Home"],"logger":"console"}}]},"tags":[["isReplayRoot","yes"] ,["skippedNormalization","True"],["transaction","/"]],"extra":{"normalizeDepth":3},"sdk":{"name":"sentry.javascript.react","version":"6.18.1","integrations":["InboundFilters","FunctionToString","TryCatch","Breadcrumbs","GlobalHandlers","LinkedErrors","Dedupe","UserAgent","Replay","BrowserTracing"],"packages":[{"name":"npm:@sentry/react","version":"6.18.1"}]},"errors":[{"type":"clock_drift","name":"timestamp","sdk_time":"2022-04-07T20:14:38.483+00:00","server_time":"2022-04-14T19:40:12.376441670+00:00"}],"key_id":"3","project":3,"grouping_config":{"enhancements":"eJybzDRxY3J-bm5-npWRgaGlroGxrpHxBABcYgcZ","id":"newstyle:2019-10-29"},"spans":[],"_metrics":{"bytes.ingested.event":8793,"sample_rates":[{}]},"_meta":{"breadcrumbs":{"values":{"0":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"10":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"2":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"3":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"5":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"8":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}}}},"timestamp":{"":{"err":[["clock_drift",{"sdk_time":"2022-04-07T20:14:38.483+00:00","server_time":"2022-04-14T19:40:12.376441670+00:00"}]]}}}}',
        "start_time": 1649965212,
        "event_id": event_id,
        "project_id": default_project.id,
        "remote_addr": "127.0.0.1",
    }


@pytest.fixture
def replay_event_update(default_project):
    event_id = "01c6da09759e4f5b8efb34da7ae1e1a0"
    return {
        "type": "replay_event",
        "payload": b'{"event_id":"01c6da09759e4f5b8efb34da7ae1e1a0","level":"error","version":"7","type":"replay_event","transaction":"sentry-replay-event","logger":"","platform":"javascript","timestamp":1649966344.514961,"start_timestamp":1649966344.458561,"received":1649966344.515561,"environment":"production","user":{"ip_address":"127.0.0.1"},"request":{"url":"https://75030aaee25f.ngrok.io/","headers":[["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"]]},"contexts":{"browser":{"name":"Chrome","version":"100.0.4896","type":"browser"},"device":{"family":"Mac","model":"Mac","brand":"Apple","type":"device"},"os":{"name":"Mac OS X","version":"10.15.7","type":"os"},"trace":{"trace_id":"c0056b1e75834053a40a79e261dc39bc","span_id":"b55a07156ae2d7b3","parent_span_id":"a54ac78b6616947a","status":"ok","tags":{"replayId":"163c16e78a5049a5b64829cc1e263d9b"},"type":"trace"}},"breadcrumbs":{"values":[{"timestamp":1649966344.464561,"type":"default","category":"console","level":"info","message":"%c prev state color: #9E9E9E; font-weight: bold [object Object]","data":{"arguments":["%c prev state","color: #9E9E9E; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649966344.465561,"type":"default","category":"console","level":"info","message":"%c action     color: #03A9F4; font-weight: bold [object Object]","data":{"arguments":["%c action    ","color: #03A9F4; font-weight: bold",{"payload":"[Object]","type":"@@router/LOCATION_CHANGE"}],"logger":"console"}},{"timestamp":1649966344.465561,"type":"default","category":"console","level":"info","message":"%c next state color: #4CAF50; font-weight: bold [object Object]","data":{"arguments":["%c next state","color: #4CAF50; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649966344.468561,"type":"default","category":"console","level":"info","message":"%c prev state color: #9E9E9E; font-weight: bold [object Object]","data":{"arguments":["%c prev state","color: #9E9E9E; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649966344.468561,"type":"default","category":"console","level":"info","message":"%c action     color: #03A9F4; font-weight: bold [object Object]","data":{"arguments":["%c action    ","color: #03A9F4; font-weight: bold",{"payload":null,"skipTracking":true,"token":null,"type":"APP_LOAD"}],"logger":"console"}},{"timestamp":1649966344.468561,"type":"default","category":"console","level":"info","message":"%c next state color: #4CAF50; font-weight: bold [object Object]","data":{"arguments":["%c next state","color: #4CAF50; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649966344.474561,"type":"default","category":"console","level":"warning","message":"Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s App, ConnectedRouter, Route, Router, Switch","data":{"arguments":["Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s","App, ConnectedRouter, Route, Router, Switch"],"logger":"console"}},{"timestamp":1649966344.474561,"type":"default","category":"console","level":"warning","message":"Warning: componentWillReceiveProps has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move data fetching code or side effects to componentDidUpdate.\\n* If you\'re updating state whenever props change, refactor your code to use memoization techniques or move it to static getDerivedStateFromProps. Learn more at: https://fb.me/react-derived-state\\n* Rename componentWillReceiveProps to UNSAFE_componentWillReceiveProps to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s App, Route, Router, Switch","data":{"arguments":["Warning: componentWillReceiveProps has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move data fetching code or side effects to componentDidUpdate.\\n* If you\'re updating state whenever props change, refactor your code to use memoization techniques or move it to static getDerivedStateFromProps. Learn more at: https://fb.me/react-derived-state\\n* Rename componentWillReceiveProps to UNSAFE_componentWillReceiveProps to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s","App, Route, Router, Switch"],"logger":"console"}},{"timestamp":1649966344.482561,"type":"default","category":"console","level":"info","message":"%c prev state color: #9E9E9E; font-weight: bold [object Object]","data":{"arguments":["%c prev state","color: #9E9E9E; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649966344.482561,"type":"default","category":"console","level":"info","message":"%c action     color: #03A9F4; font-weight: bold [object Object]","data":{"arguments":["%c action    ","color: #03A9F4; font-weight: bold",{"subtype":"HOME_PAGE_LOADED","type":"ASYNC_START"}],"logger":"console"}},{"timestamp":1649966344.483561,"type":"default","category":"console","level":"info","message":"%c next state color: #4CAF50; font-weight: bold [object Object]","data":{"arguments":["%c next state","color: #4CAF50; font-weight: bold",{"article":"[Object]","articleList":"[Object]","auth":"[Filtered]","common":"[Object]","editor":"[Object]","home":"[Object]","profile":"[Object]","router":"[Object]","settings":"[Object]"}],"logger":"console"}},{"timestamp":1649966344.486561,"type":"default","category":"console","level":"warning","message":"Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s Home","data":{"arguments":["Warning: componentWillMount has been renamed, and is not recommended for use. See https://fb.me/react-unsafe-component-lifecycles for details.\\n\\n* Move code with side effects to componentDidMount, and set initial state in the constructor.\\n* Rename componentWillMount to UNSAFE_componentWillMount to suppress this warning in non-strict mode. In React 17.x, only the UNSAFE_ name will work. To rename all deprecated lifecycles to their new names, you can run `npx react-codemod rename-unsafe-lifecycles` in your project source folder.\\n\\nPlease update the following components: %s","Home"],"logger":"console"}},{"timestamp":1649966344.511561,"type":"default","category":"sentry.transaction","level":"info","message":"163c16e78a5049a5b64829cc1e263d9b","event_id":"163c16e78a5049a5b64829cc1e263d9b"}]},"tags":[["replayId","163c16e78a5049a5b64829cc1e263d9b"],["skippedNormalization","True"],["transaction","/"]],"extra":{"normalizeDepth":3},"sdk":{"name":"sentry.javascript.react","version":"6.18.1","integrations":["InboundFilters","FunctionToString","TryCatch","Breadcrumbs","GlobalHandlers","LinkedErrors","Dedupe","UserAgent","Replay","BrowserTracing"],"packages":[{"name":"npm:@sentry/react","version":"6.18.1"}]},"errors":[{"type":"clock_drift","name":"timestamp","sdk_time":"2022-04-07T20:14:38.486+00:00","server_time":"2022-04-14T19:59:04.515561029+00:00"}],"key_id":"3","project":3,"grouping_config":{"enhancements":"eJybzDRxY3J-bm5-npWRgaGlroGxrpHxBABcYgcZ","id":"newstyle:2019-10-29"},"spans":[{"timestamp":1649966344.499761,"start_timestamp":1649966344.488161,"description":"https://fonts.gstatic.com/s/titilliumweb/v14/NaPDcZTIAOhVxoMyOr9n_E7ffHjDGItzY5abuWI.woff2","op":"resource.css","span_id":"aaff479ec0791c50","parent_span_id":"b55a07156ae2d7b3","trace_id":"c0056b1e75834053a40a79e261dc39bc","data":{"size":12044}}],"_metrics":{"bytes.ingested.event":9333,"sample_rates":[{}]},"_meta":{"breadcrumbs":{"values":{"0":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"10":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"2":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"3":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"5":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}},"8":{"data":{"arguments":{"2":{"auth":{"":{"rem":[["@password:filter","s",0,10]],"len":8}}}}}}}},"timestamp":{"":{"err":[["clock_drift",{"sdk_time":"2022-04-07T20:14:38.486+00:00","server_time":"2022-04-14T19:59:04.515561029+00:00"}]]}}}}',
        "start_time": 1649966344,
        "event_id": event_id,
        "project_id": default_project.id,
        "remote_addr": "127.0.0.1",
    }


@pytest.fixture
def replay_event_init_parsed(default_project):
    return {
        "data": {
            "event_id": "163c16e78a5049a5b64829cc1e263d9b",
            "level": "error",
            "version": "7",
            "type": "replay_event",
            "transaction": "sentry-replay",
            "logger": "",
            "platform": "javascript",
            "timestamp": 1649965212.374942,
            "start_timestamp": 1649965212.374942,
            "received": 1649965212.376442,
            "environment": "production",
            "user": {"ip_address": "127.0.0.1"},
            "request": {
                "url": "https://75030aaee25f.ngrok.io/",
                "headers": [
                    [
                        "User-Agent",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
                    ]
                ],
            },
            "contexts": {
                "browser": {"name": "Chrome", "version": "100.0.4896", "type": "browser"},
                "device": {"family": "Mac", "model": "Mac", "brand": "Apple", "type": "device"},
                "os": {"name": "Mac OS X", "version": "10.15.7", "type": "os"},
                "trace": {
                    "trace_id": "ffb5344a41dd4b219288187a2cd1ad6d",
                    "span_id": "ba1586800b803058",
                    "status": "unknown",
                    "tags": {"isReplayRoot": "yes"},
                    "type": "trace",
                },
            },
            "breadcrumbs": {
                "values": [
                    {
                        "timestamp": 1649965212.328442,
                        "type": "default",
                        "category": "console",
                        "level": "info",
                        "message": "%c prev state color: #9E9E9E; font-weight: bold [object Object]",
                        "data": {
                            "arguments": [
                                "%c prev state",
                                "color: #9E9E9E; font-weight: bold",
                                {
                                    "article": "[Object]",
                                    "articleList": "[Object]",
                                    "auth": "[Filtered]",
                                    "common": "[Object]",
                                    "editor": "[Object]",
                                    "home": "[Object]",
                                    "profile": "[Object]",
                                    "router": "[Object]",
                                    "settings": "[Object]",
                                },
                            ],
                            "logger": "console",
                        },
                    },
                ]
            },
            "tags": [
                ["isReplayRoot", "yes"],
                ["skippedNormalization", "True"],
                ["transaction", "/"],
            ],
            "extra": {"normalizeDepth": 3},
            "sdk": {
                "name": "sentry.javascript.react",
                "version": "6.18.1",
                "integrations": [
                    "InboundFilters",
                    "FunctionToString",
                    "TryCatch",
                    "Breadcrumbs",
                    "GlobalHandlers",
                    "LinkedErrors",
                    "Dedupe",
                    "UserAgent",
                    "Replay",
                    "BrowserTracing",
                ],
                "packages": [{"name": "npm:@sentry/react", "version": "6.18.1"}],
            },
            "errors": [
                {
                    "type": "clock_drift",
                    "name": "timestamp",
                    "sdk_time": "2022-04-07T20:14:38.483+00:00",
                    "server_time": "2022-04-14T19:40:12.376441670+00:00",
                }
            ],
            "key_id": "3",
            "project": default_project.id,
            "grouping_config": {
                "enhancements": "eJybzDRxY3J-bm5-npWRgaGlroGxrpHxBABcYgcZ",
                "id": "newstyle:2019-10-29",
            },
            "spans": [],
            "_metrics": {"bytes.ingested.event": 8793, "sample_rates": [{}]},
            "_meta": {
                "breadcrumbs": {
                    "values": {
                        "0": {
                            "data": {
                                "arguments": {
                                    "2": {
                                        "auth": {
                                            "": {
                                                "rem": [["@password:filter", "s", 0, 10]],
                                                "len": 8,
                                            }
                                        }
                                    }
                                }
                            }
                        },
                    }
                },
                "timestamp": {
                    "": {
                        "err": [
                            [
                                "clock_drift",
                                {
                                    "sdk_time": "2022-04-07T20:14:38.483+00:00",
                                    "server_time": "2022-04-14T19:40:12.376441670+00:00",
                                },
                            ]
                        ]
                    }
                },
            },
        },
        "start_time": 1649965212.0,
    }


@pytest.fixture
def replay_event_update_parsed(default_project):
    return {
        "data": {
            "event_id": "01c6da09759e4f5b8efb34da7ae1e1a0",
            "level": "error",
            "version": "7",
            "type": "replay_event",
            "transaction": "sentry-replay-event",
            "logger": "",
            "platform": "javascript",
            "timestamp": 1649966344.514961,
            "start_timestamp": 1649966344.458561,
            "received": 1649966344.515561,
            "environment": "production",
            "user": {"ip_address": "127.0.0.1"},
            "request": {
                "url": "https://75030aaee25f.ngrok.io/",
                "headers": [
                    [
                        "User-Agent",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
                    ]
                ],
            },
            "contexts": {
                "browser": {"name": "Chrome", "version": "100.0.4896", "type": "browser"},
                "device": {"family": "Mac", "model": "Mac", "brand": "Apple", "type": "device"},
                "os": {"name": "Mac OS X", "version": "10.15.7", "type": "os"},
                "trace": {
                    "trace_id": "c0056b1e75834053a40a79e261dc39bc",
                    "span_id": "b55a07156ae2d7b3",
                    "parent_span_id": "a54ac78b6616947a",
                    "status": "ok",
                    "tags": {"replayId": "163c16e78a5049a5b64829cc1e263d9b"},
                    "type": "trace",
                },
            },
            "breadcrumbs": {
                "values": [
                    {
                        "timestamp": 1649966344.464561,
                        "type": "default",
                        "category": "console",
                        "level": "info",
                        "message": "%c prev state color: #9E9E9E; font-weight: bold [object Object]",
                        "data": {
                            "arguments": [
                                "%c prev state",
                                "color: #9E9E9E; font-weight: bold",
                                {
                                    "article": "[Object]",
                                    "articleList": "[Object]",
                                    "auth": "[Filtered]",
                                    "common": "[Object]",
                                    "editor": "[Object]",
                                    "home": "[Object]",
                                    "profile": "[Object]",
                                    "router": "[Object]",
                                    "settings": "[Object]",
                                },
                            ],
                            "logger": "console",
                        },
                    }
                ]
            },
            "tags": [
                ["replayId", "163c16e78a5049a5b64829cc1e263d9b"],
                ["skippedNormalization", "True"],
                ["transaction", "/"],
            ],
            "extra": {"normalizeDepth": 3},
            "sdk": {
                "name": "sentry.javascript.react",
                "version": "6.18.1",
                "integrations": [
                    "InboundFilters",
                    "FunctionToString",
                    "TryCatch",
                    "Breadcrumbs",
                    "GlobalHandlers",
                    "LinkedErrors",
                    "Dedupe",
                    "UserAgent",
                    "Replay",
                    "BrowserTracing",
                ],
                "packages": [{"name": "npm:@sentry/react", "version": "6.18.1"}],
            },
            "errors": [
                {
                    "type": "clock_drift",
                    "name": "timestamp",
                    "sdk_time": "2022-04-07T20:14:38.486+00:00",
                    "server_time": "2022-04-14T19:59:04.515561029+00:00",
                }
            ],
            "key_id": "3",
            "project": default_project.id,
            "grouping_config": {
                "enhancements": "eJybzDRxY3J-bm5-npWRgaGlroGxrpHxBABcYgcZ",
                "id": "newstyle:2019-10-29",
            },
            "spans": [
                {
                    "timestamp": 1649966344.499761,
                    "start_timestamp": 1649966344.488161,
                    "description": "https://fonts.gstatic.com/s/titilliumweb/v14/NaPDcZTIAOhVxoMyOr9n_E7ffHjDGItzY5abuWI.woff2",
                    "op": "resource.css",
                    "span_id": "aaff479ec0791c50",
                    "parent_span_id": "b55a07156ae2d7b3",
                    "trace_id": "c0056b1e75834053a40a79e261dc39bc",
                    "data": {"size": 12044},
                }
            ],
            "_metrics": {"bytes.ingested.event": 9333, "sample_rates": [{}]},
            "_meta": {
                "breadcrumbs": {
                    "values": {
                        "0": {
                            "data": {
                                "arguments": {
                                    "2": {
                                        "auth": {
                                            "": {
                                                "rem": [["@password:filter", "s", 0, 10]],
                                                "len": 8,
                                            }
                                        }
                                    }
                                }
                            }
                        },
                    }
                },
                "timestamp": {
                    "": {
                        "err": [
                            [
                                "clock_drift",
                                {
                                    "sdk_time": "2022-04-07T20:14:38.486+00:00",
                                    "server_time": "2022-04-14T19:59:04.515561029+00:00",
                                },
                            ]
                        ]
                    }
                },
            },
        },
        "start_time": 1649966344.0,
    }