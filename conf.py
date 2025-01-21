import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'InstallTurboTax.com'
copyright = f'{datetime.now().year}, Your Name or Company'
author = 'Your Name or Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Autodoc extension for API documentation
    'sphinx.ext.napoleon',  # Google-style docstrings support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
