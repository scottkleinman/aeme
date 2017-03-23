# `head`

`<head>` should be used exclusively for material at the beginning of a text section (generally a numbered `div`). It is typically used for incipits, as in the following example:

```xml
<div1>
	<head xml:lang="lat">Incipit vita Haveloci</head>
	<l>Herken&thorn; to me gode men</l>
	…
</div1>
```

`<head>` will often contain a more elaborate representation of the material given in `<rubric>` if the latter is present in an `<msItem>` entry. The two may optionally be linked by `@corresp`.

If there appear to be multiple heads, select one as the primary and use `hi[@rend]` to make others resemble it in the output. Alternatively, use a different block element (e.g. `<seg>`, `<ab>`), and do not designate a head.

Page headings, which are generally extra-textual elements in the top margin, should be encoded with `<fw>` or `<ab>`.
