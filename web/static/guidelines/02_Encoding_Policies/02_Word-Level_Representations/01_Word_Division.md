Medieval texts often differ from modern ones in word spacing. In general, medieval texts may (a) separate morphological elements of a single word that would be combined today or (b) combine words that would be separated today. In AEME editions, these are managed with the custom `<sg/>` (Shadow Gap) element, which combines the functions of the TEI `<gap>` and `<supplied>` elements. `<sg/>` is TEI-conformant because it can easily be converted to structures employing these two standard TEI elements. 

Ambiguous cases of word division should receive commentary with the `<note>` element.

# `<sg/>` for Combining Morphological Elements
Medieval manuscripts may leave gaps between morphological elements of a word, as in “a bout”. AEME editorial policy is to preserve the gap in the diplomatic view and to remove it—at the editor’s discretion—in the critical view in order to increase readability. The mechanism is to replace the space with `<sg/>`, which can be rendered as a space by the diplomatic view stylesheet and ignored by the critical view stylesheet. Hence “a bout” would be encoded as `a<sg/>bout`. This use of `<sg/>` can be converted to standard TEI structures in a number of ways:

1. ```xml
a<gap reason="shadowHyphen"/>bout
```
2. ```xml
a<sic> </sic>bout
```
3. ```xml 
<choice>
	<orig>a bout</orig>
	<reg>about</reg>
</choice>
```

In the first example, the term “shadowHyphen” is borrowed from the [*Piers Plowman Electronic Archive*](http://www3.iath.virginia.edu/seenet/piers/protocoltran.html) and implies that the gap is a semantic unit that some modern editors (but not AEME) choose to replace with a hyphen.

Where the gap is the direct result of a line break, the line break becomes the content of `<sg/>` (which, being no longer an empty element, requires a closing tag):

```xml
a<sg><lb/></sg>bout
```

It is possible to use `<sg/>` to indicate morphological separations of more than a single space by using `@quantity`. Hence `a<sg quantity="2"/>bout` would indicate that the gap after a consists of two spaces.

# `<sg/>` for Separating Morphological Elements

Medieval manuscripts also frequently combine morphological elements which are treated as separate words in modern orthography. In these instances, the editor may choose to render them as separate words in the critical view. In such cases, `<sg/>` functions like the TEI `<supplied>` element. For example, the editor may wish “atones” to appear as “at ones” in the critical view. This is achieved by the use of `<sg> </sg>`.

```xml
at<sg> </sg>ones
```

The `<sg/>` element will be ignored by the stylesheet for the diplomatic view. This is formally equivalent to the following TEI structures:

1. ```xml
at<supplied reason="wordBreak"/>ones
```
2. ```xml
<choice>
	<orig>atones</orig>
	<reg>at ones</reg>
</choice>
```

The term “wordBreak” above is an arbitrary one adopted for the purposes of exemplification. It should be noted that the `<sg/>` content need not be a space. It is also possible to use, for example, a hyphen: `at<sg>-</sg>ones`. The precise content of the `<sg/>` is at the editor’s discretion.

# `<sg/>` for *Litterae Notabiliores*

A special case may be made for gaps between the first letter of a line and the rest of the word. Line-initial letters are often positioned in a separate column to function as *litterae notabiliores*. AEME recognizes this conceptual distinction by the use of `@type="ln"`. Hence, at the beginning of a line “A bout” would be encoded as `<l>A<sg type="ln"/>bout…</l>`. White space after `<sg type="ln"/>` will be retained in the diplomatic view.