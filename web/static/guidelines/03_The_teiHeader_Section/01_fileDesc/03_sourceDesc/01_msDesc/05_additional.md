# `additional`

The `<additional>` element groups additional information, combining bibliographic information about a manuscript or surrogate copies of it with curatorial or administrative information.

### AEME Requirements
Currently, the `<additional>` element is used to contain LAEME and DIMEV references to the entire manuscript. Hence the `<listBibl>` element (with its acceptable child elements) is required in AEME editions.

For Oxford, Bodleian Library, Laud Misc. 108, the formulation is as follows:

```xml
<additional>
	<listBibl>
		<bibl>
			<ref type="LAEME">All items belong to the LAEME 
			<term>literary</term> category.</ref>
		</bibl>
		<bibl>
			<ref type="DIMEV">http://www.cddc.vt.edu/host/imev/record.php?recID=2605#wit-2605-1</ref>
		</bibl>
	</listBibl>
</additional>
```

Note the use of `<term>` for the LAEME category, as defined in `<profileDesc>` (see below). This may help expose these categories for searching.
Since `<additional>` may be used to store other information, AEME also allows `<p>` elements as child elements.
