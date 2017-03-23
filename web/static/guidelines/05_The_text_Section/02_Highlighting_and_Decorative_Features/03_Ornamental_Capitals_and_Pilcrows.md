# Ornamental Capitals and Pilcrows

Ornamental capitals and pilcrows are encoded with the `<hi>` element and `@rend="h2"`, `@rend="h3"`, etc. to represent 2 and 3 lines of height respectively. This convention is formally equivalent to the use of `@rend="o2"`, `@rend="o3"`, etc. replaces the <a href="http://www3.iath.virginia.edu/seenet/piers/protocoltran.html" target="_blank">*Piers Plowman Electronic Archive*</a>. Additionally, the editor can optionally use `@rend="narrow"`, `@rend="wide"` to indicate width relative to other letters (not to scale) in the text.

AEME allows the editor to encode a precise measurement of the height and width of ornamental letters with the custom attributes `@glyphHeight` and `@glyphWidth`, the value of which should be given in millimeters. It can be used in tandem with `@rend` to give a precise measurement of width alongside a relative width. For instance, a wide, blue “R” that is 4 lines high and 50mm in width (considered relatively wide by the editor) would be encoded:

```xml
<hi rend="h4 wide blue-ink" glyphWidth="50">R</hi>
```

The use of `@glyphHeight` and `@glyphWidth` is optional.

Tracery or other features of an ornamental capital can be described in `<decoNote>`. Individual items can be referenced in `<decoNote>` with a `<ref>` element targeting the capital’s containing `div`.
