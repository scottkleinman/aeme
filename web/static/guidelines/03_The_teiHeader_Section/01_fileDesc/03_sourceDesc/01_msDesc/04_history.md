# `history`

The use of the `<history>` element is detailed in the TEI docs, and no further documentation is currently available here.

### Required Child Elements

`<origin>`, `<provenance>`, `<acquisition>`

### Optional Sub-Elements

`<listBibl>`

### AEME Requirements

Within the TEI `<origin>`, `<provenance>`, and `<acquisition>` divisions, AEME editions will tag named entity elements (e.g. `<name type="person">`), places (e.g. `<name type="place">`), and dates (with `<date>`). For named persons or repositories, the `@role="owner"` designation may be added. Acknowledgement of sibling publications (e.g. printed editions and facsimiles) by other entities should be placed in `<listBibl>` (see the TEI Guidelines). Use `<listBibl>` even if there is only one publication.
