# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../src'))
# print(os.path.abspath("../src"))


# -- Project information -----------------------------------------------------

project = 'python-poppler'
copyright = '2020, Charles Brunet'
author = 'Charles Brunet'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_issues',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_theme_options = {
#     'description': "Python binding to poppler-cpp library, to read and render PDF documents.",
#     'github_button': True,
#     'github_user': 'cbrunet',
#     'github_repo': 'python-poppler',
#     'badge_branch': 'master',
#     'extra_nav_links': {
#         "GitHub": "https://github.com/cbrunet/python-poppler",
#         "Issues tracker": "https://github.com/cbrunet/python-poppler/issues",
#         "PyPI": "https://pypi.org/project/python-poppler/",
#     }
# }

html_theme_options = {
    'nav_title': "Python poppler",
    'logo_icon': "&#x1F4D7",
    'base_url': "https://cbrunet.github.io/python-poppler",
    'repo_url': "https://github.com/cbrunet/python-poppler",
    'repo_name': "python-poppler",

    'globaltoc_depth': 2,
    'globaltoc_collapse': False,
    'globaltoc_includehidden': True,

    'nav_links': [
        {'title': "Issues tracker", 'href': "https://github.com/cbrunet/python-poppler/issues", 'internal': False},
        {'title': "PyPI", 'href': "https://pypi.org/project/python-poppler/", 'internal': False},
    ],

}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}


intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}


issues_github_path = "cbrunet/python-poppler"
