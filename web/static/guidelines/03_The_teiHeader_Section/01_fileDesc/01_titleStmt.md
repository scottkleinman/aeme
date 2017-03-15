The `<titleStmt>` groups information about the title of a work and those responsible for its content.

### Required Child Elements
`<title>`

### Optional Child Elements
`<respStmt>`

### AEME Requirements
AEME uses `@type` in the `<title>` element to distinguish titles supplied by AEME editors from alternative titles supplied by other editors or medieval scribes. Possible values include “codexfull” (the title of the full codex), “main”, and “alt” (alternative title). Main and alternative titles (there may be more than one of the latter) are child elements of full codex titles. For example:

```xml
<title type="codexfull">
    <title type="main">Oxford, Bodleian Library, MS Laud Misc. 108</title>
    <title type="alt">An Alternative Title, e.g. the Laud Manuscript</title>
    <title type="alt">Another alternative, perhaps one attributed to a scribe.</title>
</title>
```

In other words, the `<title>` element has `@type="codexfull"`. The primary title, which will be the full MS name (and specific folios if incomplete), will be `@type="main"`, and any alternative titles will be `@type="alt"`.

The abbreviation “MS” must be present in the `<title>` element if it is part of the common identifier for the manuscript.
