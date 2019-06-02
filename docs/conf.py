# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else. 
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_sphinx" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import sys
import os
import datetime

import sphinx_rtd_theme
import sphinx_gallery
import matplotlib.sphinxext.plot_directive

sys.path.insert(0, os.path.abspath("_helpers"))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
    'emcee': ('http://dan.iel.fm/emcee/current/', None)
    }

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.mathjax',
    'sphinx.ext.linkcode',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    matplotlib.sphinxext.plot_directive.__name__
]

numpydoc_show_class_members = False
autosummary_generate = True
autoclass_content = "class"
autodoc_default_flags = ["members", "inherited-members"]
autodoc_docstring_signature = False
sphinx_gallery_conf = {
    'examples_dirs': '_examples',  # path to examples scripts
    'gallery_dirs': 'examples',   # path to gallery generated examples
    'backreferences_dir': 'modules/generated',  # path to store the module
                                             # using example template
    'doc_module': ('sncosmo',),  # documented module(s)
    'download_section_examples': False,
    'download_all_examples': False,  # don't package up examples.
    'default_thumb_file': os.path.join(os.path.dirname(__file__), '_logo',
                                       'spectral_white_bkg.png')
}

    
# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'


# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = 'sncosmo'
author = 'Kyle Barbary and contributors'
current_year = datetime.datetime.now().year
copyright = '2013-{:d}, {}'.format(current_year, author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

import sncosmo
# The short X.Y version.
version = sncosmo.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = sncosmo.__version__

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'obj'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [sphinx_gallery.glr_path_static()]

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
from os.path import join
html_favicon = join('_static','sncosmo_logo_32.ico')

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{0} v{1}'.format(project, release)

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# Add local templates path to modify autosummary templates
#templates_path = ['_templates']

# Static files to copy after template files
html_static_path = ['_static']
#html_style = 'sncosmo.css'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]


# -----------------------------------------------------------------------------
# Source code links
#
# Lifted from numpy docs conf.py
# -----------------------------------------------------------------------------

import inspect
from os.path import relpath, dirname

def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except:
        fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.findsource(obj)
    except:
        lineno = None

    if lineno:
        linespec = "#L%d" % (lineno + 1)
    else:
        linespec = ""

    fn = relpath(fn, start=dirname(sncosmo.__file__))

    if 'dev' in sncosmo.__version__:
        return "http://github.com/sncosmo/sncosmo/blob/master/sncosmo/%s%s" % (
           fn, linespec)
    else:
        return "http://github.com/sncosmo/sncosmo/blob/v%s/sncosmo/%s%s" % (
           sncosmo.__version__, fn, linespec)
