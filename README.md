pelican_javascript
===============

This Pelican plugin makes it easy to embed Javascript files and CSS stylesheets into individual Pelican blog articles.

Credit
------
This plugin was inspired by and adopted from the work of [Rob Story](https://github.com/wrobstory) at [pelican_dynamic](https://github.com/wrobstory/pelican_dynamic). I decided to create a similar project on my own instead of forking that one because I'd like to make breaking changes.

Installation
------------
To install the plugin, [follow the instructions on the Pelican plugin page.](https://github.com/getpelican/pelican-plugins) My settings look like the following:

```python
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['pelican_javascript']
```

Directory Structure
-------------------
Create ```js``` and ```css``` directories in your ```content``` directory:
```
website/
├── content
│   ├── js/
│   │   └── my_vis_1.js
│   │   └── my_vis_2.js
│   ├── css/
│   │   └── my_styles.css
│   ├── article1.rst
│   ├── cat/
│   │   └── article2.md
│   └── pages
│       └── about.md
└── pelicanconf.py
```

and then specify each resource as a comma-separated file name in the ```JavaScripts``` and ```StyleSheets``` keys: (note that these key names are case-insensitive, so ```javascripts``` and ```stylesheets``` would work just fine)

```
Title: Pelican blog post with dynamic javascript components
Date: 2015-06-20
Category: Blog
Tags: interactive visualization
Slug: awesome-vis
Author: Mortada Mehyar
JavaScripts: my_vis_1.js, my_vis_2.js
Stylesheets: my_styles.css
```

You can also include javascript libraries from a web resource without having to carry the files on your own. If the string starts with `http://` or `https://` it will be treated like a web resource, otherwise the plugin will look for the file under `content/js` for javascript files, and `content/css` for CSS stylesheets.

```
Title: Pelican blog post with dynamic javascript components
Date: 2015-06-20
Category: Blog
Tags: interactive visualization
Slug: awesome-vis
Author: Mortada Mehyar
JavaScripts: https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js, my_vis_1.js, my_vis_2.js
Stylesheets: my_styles.css
```

Note that the files will be included in the same order specified.

Additions to Templates
----------------------
Finally, in your base template (likely named ```base.html```), you need to add the following in your ```<head>``` section of the HTML:
```
{% if article %}
    {% if article.stylesheets %}
        {% for stylesheet in article.stylesheets %}
{{ stylesheet }}
        {% endfor %}
    {% endif %}
{% endif %}
```
and the following *after* your ```</body>``` tag:
```
{% if article %}
    {% if article.javascripts %}
        {% for javascript in article.javascripts %}
{{ javascript }}
        {% endfor %}
    {% endif %}
{% endif %}
```

That's it! Run your standard ```make html``` or ```make publish``` commands and your JSS/CSS will be moved and referenced in the output HTML.
