# Documentation

TBD. Right, these are just some notes and references for development.

## Configuration

### Server-Side

```python
demoMode = True
```

`demoMode` prevents changes in the code editor from being saved. In general, it should be used for server installations, as code editing should only take place when working locally.

It is also possible to configure instances of the app with different language/settings. Currently, there are two template configuration files in the `language` folder. Variables configured in these files are available in Python and Jinja templates. `app.py` also constructs a JSON object containing all configuration keywords that are entirely in upper case. This object is passed to the layout template, so the language is available in the format `language.ABOUT.title` to any of the Javascript functions. NB. I tried to set the client-side `appFolder` this way, but it causes problems with the menu. Something to be investigated. For now, the site path needs to be configured on the client side. **Update:** From what I can tell, accessing the language on the client side screws things up unless you kill and restart the server process. An inconvenience, but it works.

### Client-Side

```javascript
var debug = false;
var noImage = false;
var appFolder = ""; // e.g. "/aeme"
```

`debug` displays debugging information. `noImage` turns off image load, which can make development easier. `appFolder` allows you to set the path to the app's folder on the server, which may be different from the default.