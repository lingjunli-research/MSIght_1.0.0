# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MSIght'
copyright = '2024, Li Lab (UW-Madison)'
author = 'Li Lab (UW-Madison)'
release = 'December 2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []

#language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output



import os
import sys


sys.path.insert(0, os.path.abspath('..'))  # Add your project's root directory so autodoc can find your modules

extensions = [
    'sphinx.ext.autodoc',      # For automatic documentation of docstrings
    'sphinx.ext.napoleon',     # If you use Google or NumPy style docstrings
    'sphinx.ext.viewcode',     # Links to source code
    'sphinx.ext.autosummary',  # Summaries of modules/classes
    'sphinx_rtd_theme' #theme
]
autosummary_generate = True # Ensure that autosummary generates .rst files automatically

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']