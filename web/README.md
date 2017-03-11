# Documentation

TBD. Right, these are just some notes and references for development.

## Configuration

### Server-Side

Now uses [ordbok](https://github.com/eriktaubeneck/ordbok) to handle configuration. See the `configuration` folder files.

`DEMOMODE` prevents changes in the code editor from being saved. In general, it should be used for server installations, as code editing should only take place when working locally.

Language to be passed to scripts in the `/js` folder needs to be loaded `layout.html` with code like `var about = {{ config.ABOUT|tojson|safe }};`. The values are then available through `about["title"]`. Note that for some reason, each object has to be accessed by index, so `about[0]["title"]`, `about[1]["message"]` may be necessary.

Sometimes changes don't take effect until you kill and restart the server process. An inconvenience, but it works.

### Client-Side

```javascript
var debug = false;
var noImage = false;
var appFolder = ""; // e.g. "/aeme"
```

`debug` displays debugging information. `noImage` turns off image load, which can make development easier. `appFolder` allows you to set the path to the app's folder on the server, which may be different from the default.