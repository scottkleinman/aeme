# Rubricated and Color-Highlighted Text

The following taxonomy of values is taken from the <a href="http://www3.iath.virginia.edu/seenet/piers/protocoltran.html" target="_blank">*Piers Plowman Electronic Archive*</a>. Longer but more human readable values proposed by AEME are given in brackets.

| Feature  | PPEA Value | Proposed AEME Value |
| ------------- | ------------- | ------------- |
| Brown Ink | br | brown-ink |
| Green Ink | gr | green-ink |
| Blue Ink | bl | blue-ink |
| Rubricated | rb | rubricated |
| Touched in Red | tr | touched-red |
| Touched in Green | tg | touched-green |
| Textura | tx | textura |
| Underlined (with colour unspecified or text ink) | ul | underlined |
| Underlined in Red | ur | underlined-red |
| Underlined and Overlined (with colour unspecified or text ink) | ulANDol | underlined-overlined |
| Underlined and Overlined in Red | ulrANDolr | underlined-red-overlined-red |
| Boxed (with colour unspecified or text ink) | boxed | boxed |
| Boxed in Red | BinR | boxed-red |

At present, both *PPEA* and proposed AEME values may be used since they may be easily converted using this table of equivalents.

Note that, although editors are not restricted to only the above values, other values will not be rendered on the front end by the stylesheets. Therefore, any values not found in the above taxonomy must be described in notes and in the `<decoDesc>` section of the `<teiHeader>`. In some cases, it may be possible to piggy-back on existing rendition instructions. For instance `<hi rend="pointed-red red-ink">A</hi>` will style the letter in red. Editors may request that the editorial board update stylesheets to create new rendition instructions.
