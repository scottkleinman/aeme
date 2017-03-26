# `surface`

The `<surface>` element designates the two-dimensional space of the page image. According to the TEI documentation, it can contain coordinate attributes which can then be used for placing separate zones with multiple images on the page. At present, AEME does not exploit this capability. Thus, at present, AEME requires only that `<surface>` have an `@xml:id`. The only other requirement is a `<graphic>` child element to provide the URL of the image.

!!! warning
	As of March 26, 2017, the AEME viewing platform retrieves facsimile images from the `@facs` attribute of the `pb` element. This renders the facsimile `surface` element optional. The temporary recommendation for encoding `surface` is that given at the end of <a href="http://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PH-bov" target="_blank">section 11.2.1</a> of the TEI Guidelines. That is, it should have an `@start` attribute pointing to the `@xml:id` of the `pb` element containing the reference to the targeted facsimile image. In other words, it should look something like: `<surface start="#bodllaudmisc108f1">...</surface>`. See the guidelines for the [pb](05_The_text_Section/01_body/01_Codicological_Structures_and_Mise-en-Page/02_pb) element and the discussion of `locus` under [msItem](03_The_teiHeader_Section/01_fileDesc/03_sourceDesc/01_msDesc/02_msContents/01_msItem) for further information about linking the transcription and facsimile.

### Required Child Elements

`<graphic>`
