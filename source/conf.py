# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
Fortran-lang webpage configuration file.
"""

# pylint: disable=invalid-name, redefined-builtin

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import json
import yaml
import sys
import pathlib

root = pathlib.Path(__file__).parent.parent

data_files = {
    "fortran-learn": pathlib.Path(root, "_data", "fortran_learn.json"),
    "fortran-packages": pathlib.Path(root, "_data", "fortran_package.json"),
    "contributors": pathlib.Path(root, "_data", "contributor.json"),
    "intrinsics": pathlib.Path(root, "data", "intrinsics.yml"),
}

if not all(data.exists() for data in data_files.values()):
    sys.path.insert(0, str(root.absolute()))
    # pylint: disable=import-error, unused-import
    import fortran_package

with open(data_files["fortran-learn"], "r", encoding="utf-8") as f:
    conf = json.load(f)
with open(data_files["fortran-packages"], "r", encoding="utf-8") as f:
    fortran_tags = json.load(f)
with open(data_files["contributors"], "r", encoding="utf-8") as f:
    contributors = json.load(f)
with open(data_files["intrinsics"], "r", encoding="utf-8") as f:
    intrinsics = yaml.safe_load(f)

# -- Project information -----------------------------------------------------

project = "Fortran-lang.org website"
copyright = "2020-2022, Fortran Community"
author = "Fortran Community"

# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx_jinja",
]
if language == "en":
    extensions.append("sphinx_sitemap")

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    "dollarmath",
    "html_image",
]
myst_heading_anchors = 3


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
locale_dirs = ["../locale/"]
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.

language = str(sys.argv[-1][11:])
html_search_language = str(sys.argv[-1][11:])

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["learn/intrinsics/_pages/*.md"]
html_additional_pages = {}
suppress_warnings = ["myst.header"]

jinja_contexts = {
    "conf": conf,
    "fortran_index": fortran_tags,
    "contributors": contributors,
    "intrinsics": intrinsics,
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "favicons": [
        {
            "rel": "icon",
            "sizes": "256x256",
            "href": "images/favicon.ico",
        },
    ],
    "show_prev_next": False,
    "show_nav_level": 1,
    "show_toc_level": 0,
    "footer_items": ["copyright"],
    "navbar_align": "right",
    "navbar_start": ["navbar-logo","theme-switcher.html","version-switcher"],
    "switcher": {
        "json_url":"https://fortran-lang.org/",   
        "version_match": language,
    },
    "page_sidebar_items": ["inpage_toc.html"],
    "navbar_end": ["navbar-icon-links",  "search-field.html"],
    "search_bar_text": "Search",
    "icon_links": [
        {
            "name": "Discourse",
            "url": "https://fortran-lang.discourse.group/",
            "icon": "fab fa-discourse",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/fortranlang",
            "icon": "fab fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/fortran-lang",
            "icon": "fab fa-github",
        },
        {
            "name": "RSS",
            "url": "https://fortran-lang.org/en/news/atom.xml",
            "icon": "fas fa-rss",
        },
    ],
}

html_sidebars = {
    "news": [
        "tagcloud.html",
        "archives.html",
        "recentposts.html",
    ],
    "news/**": [
        "postcard.html",
        "recentposts.html",
        "archives.html",
    ],
    "learn/**": ["sidebar-nav-bs.html"],
    "learn": [],
    "index": ["index_sidebar.html"],
    "compilers": [],
    "packages": [],
    "community": [],
    "packages/**": [],
}
html_title = "Fortran Programming Language"
html_logo = "_static/images/fortran-logo-256x256.png"

master_doc = "index"

fontawesome_link_cdn = True

blog_path = "news"
blog_post_pattern = "news/**"
blog_baseurl = "https://fortran-lang.org/en/"
html_baseurl = "https://fortran-lang.org/"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

gettext_compact = "index"
