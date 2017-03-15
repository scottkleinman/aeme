The `<text>` section contains the edited transcription of the manuscript’s linguistic content, along with associated editorial apparatus (e.g. notes). In TEI, this element may contain the text directly, or it may contain a `<group>` element with multiple `<text>` elements nested inside for sub-texts of a collection. Since AEME edits at the codex level, if possible, the preference is to place each text in a numbered div element inside the body of a single `<text>` element. For instance, in Oxford, Bodleian Library, MS Laud Misc. 108, the South English Legendary will be in `<div1>`, whilst each separate vita will be in `<div2>`.

## Required Child Elements

`<body>`
