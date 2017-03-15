The discussion below demonstrates how TEI P5 may be used to main separate markup for the diplomatic and critical views. TEI P5 provides two groups of abbreviation tags: `<abbr>` and `<expan>` for abbreviations that should be expanded to whole words, and `<am>` and `<ex>` for abbreviation markers that are expanded alone. The use of the former implies a separation between diplomatic and critical markup.

```xml
<choice>
    <abbr>pp</abbr>
    <expan>propter</expan>
</choice>
```
If the initial *p* were flourished, it could be represented with an entity like `&#xA753;` (`&pflour;`). If there is a need to represent the *p*-flourish and the *p* as separate abbreviation makers, they should be placed in separate `<am>` tags instead.

`<am>` and `<ex>` can exist within `<orig>` and `<reg>` tags. This is particularly important for cases like the word “prophetes” beginning with a *p*-flourish:

```xml
<choice>
	<orig><am>&pflour;</am>phetes</orig>
	<reg><ex ref="#g_pflour">pro</ex>phetes</reg>
</choice>
```

Here the `<orig>` element contains the diplomatic reading of the abbreviation mark. However, it can be toggled with the expanded form housed in the `<reg>` element (since the expansion is also what we would want to see in the critical view). The `@ref` value may be used to reference a *p*-flourish glyph that has been defined in `<encodingDesc>` (see the [TEI Guidelines for &lt;g&gt;](http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-g.html)).
