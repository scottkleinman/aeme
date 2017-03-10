# Documentation

TBD.

## Configuration

### Client-Side

```javascript
var debug = false;
var noImage = false;
var appFolder = ""; // e.g. "/aeme"
```

`debug` displays debugging information. `noImage` turns off image load, which can make development easier. `appFolder` allows you to set the path to the app's folder on the server, which may be different from the default.

### Server-Side

```python
demoMode = True
```

`demoMode` prevents changes in the code editor from being saved. In general, it should be used for server installations, as code editing should only take place when working locally.