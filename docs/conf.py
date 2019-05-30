# -*- coding: utf-8 -*-
#
# tabu documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from io import open
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# -- General configuration ------------------------------------------------
# import sphinx
# if sphinx.__version__  # can check here

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'recommonmark',
]

autosummary_generate = True

# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}

# The master toctree document.
master_doc = 'index'

# Mock the C++ extension on RtD (where we can't build_ext)
if os.getenv('READTHEDOCS'):
    autodoc_mock_imports = ["tabu.tabu_search"]

# Load package info, without importing the package
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
package_info_path = os.path.join(basedir, "tabu", "package_info.py")
package_info = {}
try:
    with open(package_info_path, encoding='utf-8') as f:
        exec(f.read(), package_info)
except SyntaxError:
    execfile(package_info_path, package_info)

# General information about the project.
project = package_info['__title__']
copyright = package_info['__copyright__']
author = package_info['__author__']
version = package_info['__version__']
release = package_info['__version__']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None


add_module_names = False
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

modindex_common_prefix = ['dwave-tabu.']

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

def setup(app):
   app.add_stylesheet('cookie_notice.css')
   app.add_javascript('cookie_notice.js')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'dimod': ('https://docs.ocean.dwavesys.com/projects/dimod/en/latest/', None),
    'binarycsp': ('https://docs.ocean.dwavesys.com/projects/binarycsp/en/latest/', None),
    'cloud-client': ('https://docs.ocean.dwavesys.com/projects/cloud-client/en/latest/', None),
    'neal': ('https://docs.ocean.dwavesys.com/projects/neal/en/latest/', None),
    'networkx': ('https://docs.ocean.dwavesys.com/projects/dwave-networkx/en/latest/', None),
    'system': ('https://docs.ocean.dwavesys.com/projects/system/en/latest/', None),
    'penaltymodel': ('https://docs.ocean.dwavesys.com/projects/penaltymodel/en/latest/', None),
    'minorminer': ('https://docs.ocean.dwavesys.com/projects/minorminer/en/latest/', None),
    'qbsolv': ('https://docs.ocean.dwavesys.com/projects/qbsolv/en/latest/', None),
    'oceandocs': ('https://docs.ocean.dwavesys.com/en/latest/', None),
    'sysdocs_gettingstarted': ('https://docs.dwavesys.com/docs/latest/', None),
}
