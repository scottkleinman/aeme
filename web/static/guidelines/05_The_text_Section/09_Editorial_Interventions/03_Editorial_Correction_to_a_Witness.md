TEI permits several different ways of marking corrections to the base manuscript by an editor. AEME employs the `<sic>` and `<corr>` tags in tandem to show the manuscript reading and editorial emendation, respectively, because this provides the widest range of display options.

AEME differs from the [*Piers Plowman Electronic Archive*](http://www3.iath.virginia.edu/seenet/piers/protocoltran.html), which places brackets around corrected text: `<sic>for</sic><corr>for [hem]</corr>`. Instead, AEME encloses only the corrected text in `<corr>`. The equivalent encoding for AEME would be

```xml
for <choice>
    <sic/>
    <corr>hem</corr>
  </choice>
```

Note that `<choice>` should always be used when `<sic>` and `<corr>` are used in tandem. An editorial insertion can be encoded above, or an editorial deletion can be encoded with an empty `<corr/>` element. The use of `<corr>` to supply missing text implies that the missing text is the result of scribal error. If this is not the case, the `<supplied>` element should be used.

A `<sic>` tag may be used without `<corr>`, and vice versa, if the editor elects not to correct the text.

The editor may indicate responsibility and certainty for corrections with `@resp` and `@cert`. Since TEI does not provide attributes indicating the reasons for corrections, these should be supplied using `<note>`.
