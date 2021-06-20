# Singer Family Recipes

The Singer Family website is currently at: [Singer Recipes](https://modest-morse-a556e2.netlify.app/) Please feel free to add recipes!

Original "super minimal recipe website" by [Jeff Thompson](https://github.com/jeffThompson) and then modified by [kvpsky](https://github.com/kvpsky) to be used with GitHub Pages, then slightly tweaked by [joeeoj] and deployed via Netlify, with credit also to [AN0DA](https://github.com/AN0DA) at [whatsfordinner.recipes](https://whatsfordinner.recipes).

Other examples:

* Original - [http://jeffreythompson.org/recipes/](http://jeffreythompson.org/recipes/)
* GitHub Pages - [http://kvpsky.github.io/Recipes-GHPages](http://kvpsky.github.io/Recipes-GHPages)

## Adding recipes

Add markdown files to the recipes folder. You can copy an existing recipe or use `template.md` as a guide.

## Local development

```bash
# runs the build script, then starts a simple python http server
$ ./serve.sh
```

You have to cancel and restart the script to rebuild and see changes.

It's also a good idea to open up the developer console and make sure there are no hidden errors loading content.

## Deployment

The original website was a php website that dynamically generated pages from the markdown in the recipes folder. It was cleverly converted by [kvpsky](https://github.com/kvpsky) into an html site with some javascript modifications and the addition of the `generate.py` script. This eliminates the need for server-side php and allows the site to be published as a static site with tools like GitHub Pages or Netlify.

### Netlify

Steps taken from [A Step-by-Step Guide: Deploying on Netlify](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/):

1. Log into Netlify and select `New Site from Git`
2. Select GitHub, Authorize Netlify, select the repo, and point to the main repo
3. Configure Your Settings (the important part)
    * Build command: `python3 generate.py`
    * Publish directory: `build`

That should be it assuming there are no errors with the build. It will rebuild every time you push to main.

#### Custom domain

If you did not purchase your domain with Netlify, you'll need to log into your domain registrar's website and point your domain's DNS nameservers to Netlify. You can find the Netlify nameservers in the DNS settings menu of the site you just setup. It might take awhile when you first set it up (24 hours to full propagate). Netlify will also give you an SSL/TLS certificate for free (made possible by [Let's Encrypt](https://letsencrypt.org/donate/)).
