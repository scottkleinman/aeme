Poetic lines are contained within the `<l>` element. In the critical view, each poetic line in each manuscript in the Archive has been assigned its own number, which is the `@xml:id` attribute value for that line and must therefore be globally unique. The format of `@xml:id` will be the manuscript abbreviation plus the `<msItem>` number plus the line number. E.g. “bodllaudmisc108.0001.1”, “bodllaudmisc108.0001.2”, etc.

Poetic lines can be grouped using the `<lg>` element. A poetic strophe is a typical use:

```xml
<lg type="strophe">
… multiple <l> elements …
</lg>
<lg> may also be used to designate spans of poetic lines written out as prose, as in the following example from Laȝamon’s Brut.
<lg type="continuous">
<l>An p&rrot;reo&slong;t wes on 
   <lb/>leoden<pc>&punctelev;</pc> la&yogh;amon 
   <lb/>we<add place="supralinear">s</add> ihoten<pc>&punctus;</pc>
</l>
<l>he wes 
   <lb/>leouena&eth;es &slong;one;
   <lb/>li&eth;e him beo <choice>
     <orig>d&rrot;iht<am>&emacr;</am></orig>
	 <reg>Driht<ex>en</ex></reg>
    </choice><pc>&punctus;</pc>
</l>
...
</lg>
```

Note that in this case, `<lb/>` should be inserted at appropriate points in the text, as in the example above. 
In some manuscripts, strophes are marked with skipped lines. These should be recorded with `<lb/>`.
