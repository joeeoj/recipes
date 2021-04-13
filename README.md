# Recipes

Original "super minimal recipe website" by [Jeff Thompson](https://github.com/jeffThompson) and then modified by [kvpsky](https://github.com/kvpsky) to be used with GitHub Pages, then slightly tweaked be me and deployed via Netlify. Credit also to [AN0DA](https://github.com/AN0DA).

Examples:

* Original -- [http://jeffreythompson.org/recipes/](http://jeffreythompson.org/recipes/)
* GitHub Pages -- [http://kvpsky.github.io/Recipes-GHPages](http://kvpsky.github.io/Recipes-GHPages)
* Netlify -- [http://whatsfordinner.recipes](http://whatsfordinner.recipes)

## Adding recipes

Add markdown files to the recipes folder. You can copy an existing recipe or use `template.md` as a guide.

## Local development

```bash
# first build it
$ python3 generate.py
$ cd build
# start local http server to view (http://localhost:8000 by default)
$ python3 -m http.server
```

Also good to open up the developer console and make sure there are no errors loading content.

## Deployment

The original website was a php website that dynamically generated pages from the markdown in the recipes folder. It was cleverly converted by [kvpsky](https://github.com/kvpsky) into an html site with some javascript modifications and the addition of the `generate.py` script. This eliminates the need for server-side php and allows the site to be published as a static site with tools like GitHub Pages or Netlify.

### Netlify

Steps taken from [A Step-by-Step Guide: Deploying on Netlify](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/):

1. Log into Netlify and select `New Site from Git`
2. Select GitHub, Authorize Netlify, and select the repo
3. Configure Your Settings (the important part)
    * Build command: `python generate.py`
    * Publish directory: `build`
