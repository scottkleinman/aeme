# The Facsimile Section

The `<facsimile>` section immediately follows the `<teiHeader>` element. This section forms the basis for a representation of the manuscript as an image or a set of images. For AEME document objects, these images are treated in parallel to the transcription. That is, each page of the transcription is linked directly to a `<surface>` child element of `<facsimile>`. This in turn is linked to the equivalent page in the transcription through the `@facs` attribute of the `<pb/>` element.

### Required Child Elements

`<surface>`

An entire AEME `<facsimile>` might look like the following:

```xml
<facsimile>
	<surface xml:id="1r">
		<graphic url="http://www.aeme.org/images/bodllaudmisc108_img_bau0009.tif"/>
	</surface>
	<surface xml:id="1v">
		<graphic url="http://www.aeme.org/images/bodllaudmisc108_img_bau0010.tif"/>
	</surface>
</facsimile>
…
<pb facs="1r"/>
<pb facs="1v"/>
```