The `<publicationStmt>` groups information concerning the publication or distribution of the text.

### Required Child Elements
`<publisher>`, `<date>`

###AEME Requirements

The `<publisher>` element should be `<publisher>Archive of Early Middle English</publisher>`. The only exceptions should be when the file is a duplicate of a text published elsewhere (such as the Auchinleck manuscript). It is also possible that we will have files that serve as metadata placeholders for external resources.

The `<date>` element should contain the `@when` attribute, which gives the date in the format `YYYY-MM-DD`. Content inside the `<date>` element should normally consist only of the year of publication. For example:

```xml
<date when="2001-02-01">2001</date>
```

Note that publication information may be given as prose inside a `<p>` element for development purposes but should be broken down into `<publisher>` and `<date>` before the file goes live.
