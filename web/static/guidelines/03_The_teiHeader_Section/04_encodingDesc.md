The `<encodingDesc>` element documents the relationship between an electronic text and the source or sources from which it derives.

### AEME Requirements

Currently, AEME uses `<encodingDesc>` only to define a taxonomical ID for the *Catalogue of Sources for a Linguistic Atlas of Early Medieval English*. The form is as follows:

```xml
<encodingDesc>
	<classDecl>
		<taxonomy xml:id="LAEME">
			<bibl>
				<title>Catalogue of Sources for a Linguistic 
				Atlas of Early Medieval English</title>
				<author>Margaret Laing</author>
				<edition>1993</edition>
			</bibl>
		</taxonomy>
	</classDecl>
</encodingDesc>
```

LAEME can then be referenced using `#LAEME` in the `<profileDesc>` section, where it is required, but it may also be used anywhere in the file. Eventually the taxonomy element will be replaceable by `<taxonomy corresp="#LAEME"/>`, and the citation will be stored in a stand-off document.
