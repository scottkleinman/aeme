# `msItem`

### Optional Child Elements

<a href="http://bancroft.berkeley.edu/digitalscriptorium/huntington/" target="_blank">Digital Scriptorium</a> may provide a useful model for child elements.

###AEME Requirements

`<msItem>` elements may be nested so that sub-texts may be listed. For instance, the *South English Legendary* may be designated as `<msItem n="3">`, and each vita would be listed as a separate `<msItem>` within `<msItem n="3">`.

`<msItem>` can take the `@class` attribute, which can be used to specify a set of recognised genres or text types. If there are multiple genres, they may be represented by separating them with a space: e.g. `<msItem class="#hagiography #romance">`. All terms used must be listed as keywords in `<profileDesc>`.

Inside the `<msItem>` element there can be one or more `<p>` elements containing a narrative description of the item. The description may contain other elements such as `<locus>` (the folio numbers of the text), `<title>`, `<incipit>` and `<explicit>`, or bibliographical references using `<listBibl>` (even if there is only one; don’t use `<biblStruct>` because it has some unnecessary structural requirements). Initially, we will include references to two external entities:

* LAEME Catalogue Categories (Documents, Literary Texts, Glosses). Since there is no clear URL for these categories, we will use the format `<ref type="LAEME">glosses</ref>`.
* Digital Index of Middle English Verse ID numbers. References will be given to the URL of the online version in the following format: `<ref type="DIMEV" target="http://path/to/dimev/id">$dimev-id</ref>`.
* The Middle English Compendium ID number (used by the Middle English Dictionary). References will be given to the URL of the online version in the following format: `<ref type="MEC" target="http://path/to/mec/id">$mec-id</ref>`.

Additionally, entries may include the print `Index of Middle English Verse` ID numbers, as these sometimes differ from the DIMEV entries.
For prose text, references should be given to the appropriate volume of the *Index of Middle English Prose* inside a `<bibl>` element. Works in Anglo-Norman should refer to Dean, Ruth J., and Maureen Barry McCann Boulton. *Anglo-Norman Literature: A Guide to Texts and Manuscripts*. London: Anglo-Norman Text Society, 1999.

## `locus`

The `locus` element defines a location within a manuscript or manuscript part. It is meant to contain a prose label (e.g. "ff. 1r-2v"), but it should also possess a `@target` attribute, the value of which should be the reference to the `@xml:id` of a `pb` element. For example:

```xml
<locus target="#boddlaudmisc108-1">f. 1r</locus>
```

Ranges can be handled by space, separated values:

```xml
<locus target="#boddlaudmisc108-1 #boddlaudmisc108-2 #boddlaudmisc108-3">ff. 1r-2r</locus>
```

The `locus` may also have `@from` and `@to` attributes providing range information (see the TEI guidelines <a href="http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-locus.html" target="_blank">locus</a> reference for usage). These attributes are not currently used by AEME and are so not required.

!!! warning
	As of March 26, 2017, the AEME platform targets the `@xml:id` of the `pb` element to retrieve facsimile information, rather than the surface listed in the `facsimile` element. This procedure is subject to change. See also the discussion under [surface](04_The_facsimile_Section/01_surface) and [pb](05_The_text_Section/01_body/01_Codicological_Structures_and_Mise-en-Page/02_pb).


## `listBibl`

References to print editions should be included wherever possible. These should be formatted following guidelines in *Chicago Manual of Style*, 16th edition. The code format consists of simple `<listBibl>` entries like the following:

```xml
<listBibl>
	<bibl corresp="#HorstmannC1873">Horstmann, Carl. <title>Leben 
	Jesu: ein Fragment, und Kindheit Jesu, &amp;c.</title>.
    M&uuml;nster: Regensberg, 1873.</bibl>
</listBibl>
```

The long title should be placed inside `<title>` tags. No other structured markup is required.
