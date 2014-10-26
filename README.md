pixels
======

Generate markdown to display photo albums using reveal.js

####Details
The script scans a folder and creates an album for every subfolder with one or more jpg or tif file. It generates markdown for the albums to display using reveal.js.

Reveal.js can use the following html to read the markdown dynamically.

```html
<div class="reveal">
    <div class="slides">
        <section data-markdown="albums.md"
                 data-separator="----"
                 data-vertical="---"
                 data-notes="^Note:"
                 data-charset="iso-8859-15">
        </section>
    </div>
</div>
```
