The `<surface>` element designates the two-dimensional space of the page image. According to the TEI documentation, it can contain coordinate attributes which can then be used for placing separate zones with multiple images on the page. At present, AEME does not exploit this capability. Thus, at present, AEME requires only that `<surface>` have an `@xml:id`. The only other requirement is a `<graphic>` child element to provide the URL of the image.

### Required Child Elements

`<graphic>`
