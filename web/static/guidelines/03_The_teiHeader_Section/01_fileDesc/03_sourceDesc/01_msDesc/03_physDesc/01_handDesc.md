The `<handDesc>` element contains a description of all the different kinds of writing used in a manuscript. The number of hands is given in `@hands`.

### Required Child Elements

`<handNote>`

### AEME Requirements

All hands represented in the AEME corpus will be listed with IDs in AEME’s entities file. These IDs will correspond to the hands listed in this section. Each hand will have a corresponding <handNote>. For instance:

```xml
<handDesc hands="2">
    <handNote xml:id="0012" n="1" scope="major">
        <p>The majority of the manuscript is in a <term>compact textura</term> hand of the 
		<date from="1200-01-01" to="1225-12-31">first quarter of the thirteenth century</date>.</p>
    </handNote>
    <handNote xml:id="0013" n="2" scope="minor">
        <p>The <locus>top of f. 238</locus> is in a hand of the <date from="1400-01-01" 
		to="1499-12-31">fifteenth century</date>.</p>
    </handNote>
</handDesc>
```

`@n` indicates the hand number within the manuscript. It does not necessarily have to be a number; it can be a letter if the traditional notation is something like “Scribe A”, or some other type of identifier. `@scope` (optional) provides an indicator of the hand’s contribution (another possible value is “sole”). The example above shows useful tags for content within the `<handNote>`; however, AEME currently has no requirements for structured markup in this section.
