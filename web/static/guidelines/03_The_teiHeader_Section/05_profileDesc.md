# `profileDesc`

The `<profileDesc>` provides a detailed description of non-bibliographic aspects of a text, specifically the languages and sublanguages used, the situation in which it was produced, the participants, and their setting.

### AEME Requirements

Currently, AEME uses `<profileDesc>` to define key words (normally genre terms) that describe the content of the entire manuscript. AEME requires the inclusion of at least one of the text classes (Documents, Literary Texts, Glosses) listed in the *Catalogue of Sources for a Linguistic Atlas of Early Medieval English*. These are identified by `@scheme` with a reference to the taxonomy ID for LAEME listed in `<encodingDesc>`. Additional keywords may be listed at the editors’ discretion. The format of `<profileDesc>` is as follows:

```xml
<profileDesc>
	<textClass>
		<keywords scheme="#LAEME">
			<term>literary</term>
		</keywords>
		<keywords>
			<term>hagiography</term>
			<term>romance</term>
		</keywords>
	</textClass>
</profileDesc>
```

In the above example the keyword “literary” is drawn from LAEME. The keywords “hagiography” and “romance” are defined within the edition itself. Other possible keywords might be: devotional, religious writing, historiography (life writing), doctrinal, chorography, chronicle, religious writing, historiography (life writing), doctrinal, chorography, chronicle, poetry, lyric, song, diagram, music, didactic, genealogy, drama, debate, rolls/codices, fabliau, proverb, satire, romance, prayer, heraldry, hagiography, riddle, macaronic, liturgical, or biblical.
