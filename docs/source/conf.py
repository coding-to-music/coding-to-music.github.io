# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.abspath("./_ext"))
sys.path.insert(0, os.path.abspath("../../../python-source/bareos/"))
sys.path.insert(0, os.path.abspath("./_extensions"))
sys.path.insert(0, os.path.abspath("./_ext"))
# import sphinx_gallery

from sphinx_gallery.sorting import ExplicitOrder  
from sphinx_gallery.sorting import ExampleTitleSortKey  

# sys.path.append(os.path.dirname(__file__))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

# from django.conf import settings
# from django.utils import timezone

# import django
# django.setup()

featureflags = 'ManyAvailable'

from time import strftime, localtime
# strftime("%a, %d %b %Y %I:%M %p %Z", localtime())

# There are two options for replacing |today|:

# 1. If you set today to some non-false value, then it is used:

today = ''
# 2. Otherwise, today_fmt is used as the format for a strftime call.

##today_fmt = '%B %d, %Y'
today_fmt = "%a, %d %b %Y %I:%M %p %Z"

gitstamp_fmt = "%a, %d %b %Y %I:%M %p %Z"

# Date format for git timestamps
# gitstamp_fmt = "%b %d, %Y"

git_last_updated_timezone = 'EST'

# extensions = ['todo','sphinx.ext.todo']

todo_include_todos = True

# Enable numref
numfig = True

# -- Project information -----------------------------------------------------

project = u'all-knowledge'
author = 'Thomas Connors and Contributors'
copyright = '2020-2021, Thomas Connors and Contributors'
# copyright = '{}, {}'.format(datetime.datetime.now().year, author)
# copyright = '2020-{}, Thomas Connors and Contributors'.format(
#     time.now().year
# )
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''
# The short X.Y version.
# version = trackhub.__version__
# The full version, including alpha/beta/rc tags.
# release = version

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# ...
# extensions = [
#     # ...
#     "sphinx_issues"
# ]

# True to prefix each section label with the name of the document it is in, followed by a colon.
# For example, index:Introduction for a section called Introduction that appears in document index.rst.
# Useful for avoiding ambiguity when the same section heading appears in different documents.
autosectionlabel_prefix_document = True

plantuml_output_format = "svg_img"

#
# code-block highlighting
#
from sphinx.highlighting import lexers
from bareos_lexers import *

lexers["bareosconfig"] = BareosConfigLexer()
lexers["bconsole"] = BareosConsoleLexer()
lexers["bareoslog"] = BareosLogLexer()
lexers["bareosmessage"] = BareosMessageLexer()


# Add sphinxext.delta to your extensions list in your conf.py

# extensions = [
#     sphinxext.delta,
# ]
# Options
# There are 2 required and 1 optional configurations:

# delta_doc_path
# REQUIRED: Relative path to your articles. IE: source/docs
# delta_doc_path='source/docs'
# delta_inject_location
# OPTIONAL: Relative location for the toctree to be injected. Defaults to master_doc.

# extensions = ['todo','sphinx.ext.todo']
# extensions = [
#     'todo',
#     'sphinx_tabs.tabs',
#     'sphinx-prompt',
#     'sphinx.ext.coverage', 
#     'sphinx.ext.napoleon',
#     "sphinxext.opengraph",
#     'sphinxcontrib.images',
#     'sphinx.ext.autodoc'] 
#     "crate.sphinx.csv",  # create filters on CSV files to include exclude rows
#     "bareos-ext",
#     'sphinxext-delta',
#     "sphinxext-opengraph2",


extensions = [
    "sphinx_rtd_theme",
    # "sphinx_material",
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    "sphinxcontrib.actdiag",
    "sphinxcontrib.blockdiag",
    "sphinxcontrib.contentui",
    "sphinx_copybutton",
    "sphinx.ext.coverage",
    'sphinxcontrib.images',
    "sphinx_issues",
    'sphinx_gallery.gen_gallery',
    "sphinx_gitstamp",
    "sphinxext.linkcheckdiff",
    "sphinxcontrib.nwdiag",
    "sphinxcontrib.plantuml",
    'sphinx_panels',
    'sphinx-prompt',
    "sphinx.ext.intersphinx",  # Link to other project's documentation (see mapping below)
    "sphinx.ext.napoleon",
    'notfound.extension',
    "sphinxcontrib.seqdiag",
    'sphinx_tabs.tabs',
    'todo',
    "sphinx.ext.viewcode",  # Add a link to the Python source code for classes, functions etc.
    "sphinxext.remoteliteralinclude",
    "hoverxref.extension",
    "sphinx_sitemap",
]

    # "readthedocs_sphinx_ext",
    # "sphinx_tabs",

# extensions = [
#     "sphinx_rtd_theme",
#     "sphinx_material",
#     'sphinx_tabs.tabs',
#     "sphinxcontrib_actdiag",
#     "sphinxcontrib_blockdiag",
#     "sphinxcontrib_contentui",
#     "sphinxcontrib_seqdiag",
#     "sphinxcontrib_nwdiag",
#     "sphinxcontrib_plantuml",
#     "sphinx-prompt",
#     "sphinxext-remoteliteralinclude",
#     "sphinx-copybutton",
#     "sphinx-Hoverxref",
#     "sphinx_issues",
#     "sphinx-gallery",
#     "sphinxcontrib-images",
#     "sphinx-gitstamp",
#     "sphinx-notfound-page",
#     "sphinx_sitemap",
#     "sphinx-Jinja",   
# ]


# {% if check_meta and 'github_url' in meta %}
#     <!-- User defined GitHub URL -->
#     <a href="{{ meta['github_url'] }}" class="fa fa-github"> {{ _('Edit on GitHub') }}</a>
# {% else %}
#     <a href="https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/{{ theme_vcs_pageview_mode|default("blob") }}/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}" class="btn btn-neutral" title="{{ _('Edit Page on GitHub') }}" rel="{{ _('Edit Page on GitHub') }}"><span style="padding-left: 0.5em" >Edit on<i style="margin-left: 0.5em" class="fa fa-github"></i></span></a>
#     <a href="https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/commits/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}" class="btn btn-neutral" title="{{ _('Page History') }}" rel="{{ _('Page History') }}"><span class="fa fa-clock-o"></span></a>
#     <a href="https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blame/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}" class="btn btn-neutral" title="{{ _('Page Contributors') }}" rel="{{ _('Page Contributors') }}"><span class="fa fa-users"></span></a>

# my_first_path = "https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/"


# extensions.append('sphinx_material')
# html_theme_path = sphinx_material.html_theme_path()
# html_context = sphinx_material.get_html_context()

html_js_files = ['js/expand_tabs.js']
html_title = project
html_short_title = project
# material theme options (see theme.conf for more information)

repo_url = 'https://github.com/coding-to-music/coding-to-music.github.io'
repo_name = 'coding-to-music.github.io'

repo_user = 'coding-to-music'

base_url = 'https://pandemic-overview.readthedocs.io'
# base_url += 'latest/' if full_version == version else 'devel/'

# github_url = 

# Github repo
# issues_github_path = "sloria/marshmallow"
# issues_github_path = "source/bareos/bareos"

issues_github_path = "coding-to-music/coding-to-music.github.io"

# equivalent to
issues_uri = "https://github.com/coding-to-music/coding-to-music.github.io/issues/{issue}"
issues_pr_uri = "https://github.com/coding-to-music/coding-to-music.github.io/pull/{pr}"
issues_commit_uri = "https://github.com/coding-to-music/coding-to-music.github.io/commit/{commit}"

material_html_theme_options = {

    # Set the name of the project to appear in the navigation.

    'nav_title': 'all-knowledge.info',
    # 'nav_title': 'pandemic-overview {0}'.format(version),
    # 'nav_title': 'statsmodels {0}'.format(version),

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': base_url,


    # Set the repo location to get a badge with stats
    'repo_url': repo_url,
    'repo_name': repo_name,


    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 1,
    # If False, expand all TOC entries
    # 'globaltoc_collapse': True,
    'collapse': True,
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,


    # Set the color and the accent color
    'color_primary': 'indigo',
    'color_accent': 'blue',

    'master_doc': False,

    # I don't know about these items
    'nav_links': [],

    'heroes': {'index': 'Making Sense of the Pandemic '
                        '',
               'examples/index': 'examples and tutorials to get started with '
                                 'statsmodels'},
    "version_dropdown": True,
    "version_json": "_static/versions.json",
}

#     'prev_next_buttons_location': 'both'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '_static/images/statsmodels/statsmodels-logo-v2-bw.svg'
html_logo = '_static/ska-telescope/logo.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/images/statsmodels/favicon.ico'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
# }

html_sidebars = {
    "**": ["logo-text.html", "localtoc.html", "searchbox.html"]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, 'Created using Sphinx' is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, '(C) Copyright ...' is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. '.xhtml').
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'pandemic-overview-doc'

language = 'en'
# html_last_updated_fmt = ''
html_last_updated_fmt = "%a, %d %b %Y %I:%M %p %Z"

# html_theme = 'sphinx_material'

# Material theme options (see theme.conf for more information)
# html_material_theme_options_example = {

    # this is needed, is available from RTD them
    # 'prev_next_buttons_location': 'both'

    # Set the name of the project to appear in the navigation.
    # 'nav_title': 'Project Name',

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    # 'base_url': 'https://project.github.io/project',

    # Set the color and the accent color
    # 'color_primary': 'blue',
    # 'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    # 'repo_url': 'https://github.com/project/project/',
    # 'repo_name': 'Project',

    # Visible levels of the global TOC; -1 means unlimited
    # 'globaltoc_depth': 3,
    # If False, expand all TOC entries
    # 'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    # 'globaltoc_includehidden': False,
# }

#    "sphinxcontrib.twitter",
#   "sphinx_rediraffe",
#    "sphinx_jinja",
# "sphinxnotes.lilypond", 
# 'python-twitter',
#    "limitation",
# "sphinx.ext.todo",

# Set each document name as prefix to avoid duplication
autosectionlabel_prefix_document = True

# 404 page configuration
notfound_context = {
    "body": "<h3>Unfortunately, we couldn't locate the object you are searching for, yet!</h3> <p> In the meantime, please feel free to explore the rest of the Portal!</p>",
}

notfound_no_urls_prefix = True

hoverxref_auto_ref = True
hoverxref_domains = ['py']
hoverxref_roles = [
    'option',
    'doc',
]
hoverxref_role_types = {
    'mod': 'modal',  # for Python Sphinx Domain
    'doc': 'modal',  # for whole docs
    'class': 'tooltip',  # for Python Sphinx Domain
    'ref': 'tooltip',  # for hoverxref_auto_ref config
    'confval': 'tooltip',  # for custom object
}

# Enable hover content on glossary term
# hoverxref_roles = ["term"]

# Redirect branch
rediraffe_branch = "master~1"

# File containing redirects
rediraffe_redirects = "redirects.txt"

# Required accuracy for redirect writer
rediraffe_auto_redirect_perc = 80

# Configure linkcheck diff branch
linkcheckdiff_branch = "origin/master"

# Disable following anchors in URLS for linkcheck
linkcheck_anchors = False

# Linkcheck Exclusions
linkcheck_ignore = [
    r".*kauailabs.com.*",
    r".*wpilibpi.local.*",
    r".*andymark.com.*",
    r".*ti.com/lit/an/spma033a/spma033a.pdf.*",
    r".*wpilibpi.local.*",
]

# Sets linkcheck timeout in seconds
linkcheck_timeout = 30
linkcheck_retries = 3
linkcheck_workers = 1

# Specify files to ignore during SizeCheck
IMAGE_SIZE_EXCLUSIONS = [
    "docs/networking/networking-introduction/diagrams/mixing-static-dynamic.drawio.svg",
    "docs/software/vision-processing/wpilibpi/diagrams/vision-code-on-a-coprocessor.drawio.svg",
    "docs/software/vision-processing/introduction/diagrams/vision-code-on-a-coprocessor.drawio.svg",
    "docs/controls-overviews/images/frc-control-system-layout.svg",
]
sitemap_locales = [None]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# material_html_theme_options = {
#     'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
#     'analytics_anonymize_ip': False,
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
#     'style_nav_header_background': 'white',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
# }

# #0a0e12 - is GitHub with dark theme
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'rtd_dark.css'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_theme = 'sphinx_material'

# import sphinx_material

#     'titles_only': False
#     'style_nav_header_background': 'white',
#     'collapse_navigation': True,

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# Read the Docs theme options
# html_theme_options = {
#     'prev_next_buttons_location': 'both'
# }

    # 'collapse': True,

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'both',    
    'collapse_navigation': True,
    'globaltoc_collapse': True,
    'globaltoc_includehidden': False,
    "sticky_navigation": False,
    "titles_only": True,
}

# repo_url = 'https://github.com/coding-to-music/coding-to-music.github.io'
# repo_name = 'coding-to-music.github.io'
# repo_user = 'coding-to-music'
# base_url = 'https://pandemic-overview.readthedocs.io'

html_context = {
    'display_github': True,
    'github_user': repo_user,
    'github_repo': repo_name,
    'github_version': 'master/source/',
    'favicon': "ska-telescope/favicon.ico",
    'logo': "ska-telescope/logo.jpg",
    "theme_logo_only": True,
    # "display_gitlab": True,  # Integrate Gitlab
    # "gitlab_version": "master",  # Version
    # "conf_py_path": "/src/",  # Path in the checkout to the docs root
    # workaround for https://github.com/readthedocs/sphinx_rtd_theme/issues/701
    "theme_vcs_pageview_mode": "edit",
}

html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['nstatic']

html_static_path = ['_static']
html_images_path = ['_images']
html_extra_path = ["_html"]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = ['robots.txt']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = 'obj'

# Disable having a separate return type row
napoleon_use_rtype = False

# Disable google style docstrings
napoleon_google_docstring = False

try:
    import sphinxcontrib.spelling
except ImportError:
    pass
else:
    extensions.append("sphinxcontrib.spelling")

spelling_work_list_filename='worlist.txt'

sphinx_gallery_conf = {
    'examples_dirs': 'examples',   # path to your example source/bareos/scripts
    'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
    'backreferences_dir': os.path.join('generated', 'modules'),
    'filename_pattern': '^((?!skip_).)*$',
    'examples_dirs': os.path.join('..', 'examples'),
    'subsection_order': ExplicitOrder([
        '../../examples/test1',
        '../../examples/test2',
        '../examples/test1',
        '../examples/test2',
        '/assets/lockdowns',
        '/assets/masks'
    ]),
    'within_subsection_order': ExampleTitleSortKey,
    'gallery_dirs': os.path.join('generated', 'gallery'),
    # Comes from the theme.
    # "default_thumb_file": os.path.join(html_static_path[0], "img", "zotero_128x128x32.png"),
    'abort_on_example_error': False,
    'plot_gallery': 'True',
    'remove_config_comments': True,
    'doc_module': ('sunpy'),
    'only_warn_on_example_error': True,
}



# ogp_custom_meta_tags = [
#     '<meta property="og:ignore_canonical" content="true" />',
# ]

html_baseurl="https://pandemic-overview.readthedocs.io/en/latest/"
# _images="https://pandemic-overview.readthedocs.io/en/latest/_images"
ogp_type = "article"
ogp_site_url = "https://pandemic-overview.readthedocs.io"
ogp_image = "https://pandemic-overview.readthedocs.io/en/latest/_images/Coming_Attractions-780x683.jpg"
ogp_description_length = 140
ogp_use_first_image=True
og_site_name="All-Knowlege.info" 
og_locale="en_US"
og_headline="All-Knowlege.info"

# page-specific

# og:title="Links 3/8/2021 | naked capitalism"
# og:description="Our popular daily Links" 
# og:headline="Our popular daily Links" 
# article:published_time" content="2021-03-08T11:55:38+00:00" 
# article:modified_time" content="2021-03-08T12:48:53+00:00" 




# This is what another website has:
# og:locale="en_US"
# og:title="Links 3/8/2021 | naked capitalism"
# og:description="Our popular daily Links" 
# og:url="https://www.nakedcapitalism.com/2021/03/links-3-8-2021.html" 
# og:site_name="All-Knowlege.info" 
# article:published_time" content="2021-03-08T11:55:38+00:00" 
# article:modified_time" content="2021-03-08T12:48:53+00:00" 
# og:image=

# ogp_site_url="This config option is very important, set it to the URL the site is being hosted on."
# ogp_image="This is not required. Link to image to show."
# ogp_description_length="Configure the amount of characters taken from a page. The default of 200 is probably good for most people. If something other than a number is used, it defaults back to 200."
# ogp_type="This sets the ogp type attribute, for more information on the types available please take a look at https://ogp.me/#types. By default it is set to website, which should be fine for most use cases."

# ogp_site_name="This is not required. Name of the site. This is displayed above the title."
# ogp_image_alt="This is not required. Alt text for image. Defaults to using ogp_site_name or the document's title as alt text, if available. Set to False if you want to turn off alt text completely."
# ogp_use_first_image="This is not required. Set to True to use each page's first image, if available. If set to True but no image is found, Sphinx will use ogp_image instead."
# ogp_custom_meta_tags="This is not required. List of custom html snippets to insert."

#   <meta property="og:title" content="WHO World Health Organization" />
#   <meta property="og:type" content="article" />

#   <meta property="og:url" content="http://all-knowledge.info/WHO World Health Organization.html" />
#   <meta property="og:description" content="Vaccine Definition Merriam-Webster Feb-5-2021 vs Mar-31-2019: Vaccine Definition Merriam-Webster Feb-5-2021 vs Mar-31-2019 Source: Something interesting to notice- If something doesn’t fall under a certain description outlined for indemnity, what do you do? Why, you change the definition to cover..." />

#   <meta property="og:image" content="https://pandemic-overview.readthedocs.io/en/latest/_images/CDC-653-Deaths-12697-Reported-Injuries-Following-Experimental-mRNA-COVID-Injections.jpg" />

#   <meta property="og:image:alt" content="WHO World Health Organization" />

#   <meta property="og:ignore_canonical" content="true" />

#   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
#   <title>WHO World Health Organization &mdash; all-knowledge 0.0.1 documentation</title>

# about <isonum.txt>, see
# http://docutils.sourceforge.net/docs/ref/rst/definitions.html#substitution-definitions
# http://docutils.sourceforge.net/docutils/parsers/rst/bareos/include/isonum.txt


# rst_epilog = """
# .. |org_brand| replace:: Read the Docs Community
# .. |com_brand| replace:: Read the Docs for Business
# """

rst_epilog = """
.. include:: <isonum.txt>
.. |org_brand| replace:: Read the Docs Community
.. |com_brand| replace:: Read the Docs for Business
.. |checkmark| unicode:: U+2713
.. |configCharsToQuote| replace:: ``&<>()@^|``
.. |bareosFd| replace:: Bareos File Daemon
.. |fd| replace:: Bareos File Daemon
.. |bareosSd| replace:: Bareos Storage Daemon
.. |sd| replace:: Bareos Storage Daemon
.. |bareosDir| replace:: Bareos Director
.. |dir| replace:: Bareos Director
.. |bconsole| replace:: Bareos Console
.. |bareosTraymonitor| replace:: Bareos Traymonitor
.. |traymonitor| replace:: Bareos Traymonitor
.. |bareosWebui| replace:: Bareos Webui
.. |webui| replace:: Bareos WebUI
.. |mysql| replace:: MySQL/MariaDB
.. |postgresql| replace:: PostgreSQL
.. |sqlite| replace:: Sqlite
.. |vmware| replace:: VMware
.. |vsphere| replace:: VMware vSphere
"""

# .. |ndmpbareos| replace:: :ref:`section-NdmpBareos`
# .. |ndmpnative| replace:: :ref:`section-NdmpNative`


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#    '**': [
#        'about.html',
#        'navigation.html',
#        'relations.html',  # needs 'show_related': True theme option to display
#        'searchbox.html',
#        'donate.html',
#    ]
# }

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'all-knowledgedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'all-knowledge.tex', 'all-knowledge Documentation',
     'Thomas Connors', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'all-knowledge', 'all-knowledge Documentation',
     [u'Thomas Connors'], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'all-knowledge', 'all-knowledge Documentation',
     author, 'all-knowledge', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

#
# code-block highlighting
#
from sphinx.highlighting import lexers
from bareos_lexers import *

lexers["bareosconfig"] = BareosConfigLexer()
lexers["bconsole"] = BareosConsoleLexer()
lexers["bareoslog"] = BareosLogLexer()
lexers["bareosmessage"] = BareosMessageLexer()


# generate rst.inc files from json files
import subprocess
import os

os.chdir("..")
subprocess.call(["pwd"])
# subprocess.call(
#     [
#         "source/bareos/scripts/generate-resoure-descriptions.py",
#         "--sphinx",
#         "source/bareos/include/autogenerated/bareos-dir-config-schema.json",
#     ]
# )
# subprocess.call(
#     [
#         "source/bareos/scripts/generate-resoure-descriptions.py",
#         "--sphinx",
#         "source/bareos/include/autogenerated/bareos-sd-config-schema.json",
#     ]
# )
# subprocess.call(
#     [
#         "source/bareos/scripts/generate-resoure-descriptions.py",
#         "--sphinx",
#         "source/bareos/include/autogenerated/bareos-fd-config-schema.json",
#     ]
# )
# subprocess.call(
#     [
#         "source/bareos/scripts/generate-resoure-descriptions.py",
#         "--sphinx",
#         "source/bareos/include/autogenerated/bconsole-config-schema.json",
#     ]
# )
# subprocess.call(
#     [
#         "source/bareos/scripts/generate-resoure-descriptions.py",
#         "--sphinx",
#         "source/bareos/include/autogenerated/bareos-tray-monitor-config-schema.json",
#     ]
# )
# subprocess.call(
#     "source/bareos/scripts/generate-bareos-package-info.py --out source/bareos/include/autogenerated/ source/bareos/data/bareos-*-packages.json",
#     shell=True,
# )
# NBSphinx options
nbsphinx_execute = "never"

# Example configuration for intersphinx: refer to the Python standard library.
# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'python': ('https://docs.python.org/3/', None),
    'pydagogue': ('https://matthew-brett.github.io/pydagogue/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'sphinx': ('https://sphinx.readthedocs.io/', None),
    'requests': ('https://requests.readthedocs.io/en/master', None),
    'sphinxnotes-lilypond': ('https://pandas.readthedocs.io/', None),
    'sphinx-Jinja': ('https://jinja.palletsprojects.com/en/3.0.x/', None),
    'bareos': ('https://docs.bareos.org/', None),
}


    # 'sphinxcontrib-contentui': ('https://sphinxcontrib-contentui.readthedocs.io/', None),
    # 'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    # 'sphinx-copybutton': ('https://sphinx-copybutton.readthedocs.io/', None),
    # 'sphinx-gitstamp': ('https://sphinx-gitstamp.readthedocs.io/', None),
    # 'sphinx-Timeline': ('https://sphinx-Timeline.readthedocs.io/', None),
    # 'sphinx-Hoverxref': ('https://sphinx-Hoverxref.readthedocs.io/', None),
# x    'docutils': ('https://docutils.readthedocs.io/', None),
# x    'sphinx_rtd_theme': ('https://sphinx_rtd_theme.readthedocs.io/', None),
# x    'readthedocs-sphinx-ext': ('https://readthedocs-sphinx-ext.readthedocs.io/', None),
# x    'sphinx_material': ('https://sphinx_material.readthedocs.io/', None),
# x    'sphinx-panels': ('https://sphinx-panels.readthedocs.io/', None),
# x    'sphinx-tabs': ('https://sphinx-tabs.readthedocs.io/', None),
# x    'sphinxcontrib-actdiag': ('https://sphinxcontrib-actdiag.readthedocs.io/', None),
# x    'sphinxcontrib-blockdiag': ('https://sphinxcontrib-blockdiag.readthedocs.io/', None),
# x    'sphinxcontrib-seqdiag': ('https://sphinxcontrib-seqdiag.readthedocs.io/', None),
# x    'sphinxcontrib-nwdiag': ('https://sphinxcontrib-nwdiag.readthedocs.io/', None),
# x    'sphinxcontrib-plantuml': ('https://sphinxcontrib-plantuml.readthedocs.io/', None),
# x    'sphinx-prompt': ('https://sphinx-prompt.readthedocs.io/', None),
# x    'sphinxext-remoteliteralinclude': ('https://sphinxext-remoteliteralinclude.readthedocs.io/', None),
# x    'sphinxext-linkcheckdiff': ('https://sphinxext-linkcheckdiff.readthedocs.io/', None),
# x    'sphinx_issues': ('https://sphinx_issues.readthedocs.io/', None),
# x    'sphinx-gallery': ('https://sphinx-gallery.readthedocs.io/', None),
# x    'sphinxcontrib-images': ('https://sphinxcontrib-images.readthedocs.io/', None),
# x    'sphinx-notfound-page': ('https://sphinx-notfound-page.readthedocs.io/', None),
# x    'sphinxext.rediraffe': ('https://sphinxext.rediraffe.readthedocs.io/', None),
# x    'sphinx-Sitemap': ('https://github.com/jdillard/sphinx-sitemap', None),

# plot_basedir = join(dirname(dirname(os.path.abspath(__file__))), 'source')


# repo_url = 'https://github.com/coding-to-music/coding-to-music.github.io'
# repo_name = 'coding-to-music.github.io'
# repo_user = 'coding-to-music'


# github-issue config
github_project_url = repo_url

# example_context = yaml.safe_load(open('examples/landing.yml'))
# html_context.update({'examples': example_context})

# --------------- DOCTEST -------------------
# doctest_global_setup = """
# import statsmodels.api as sm
# import statsmodels.tsa.api as tsa
# import statsmodels.formula.api as smf
# import numpy as np
# import scipy.stats as stats
# import matplotlib.pyplot as plt
# import pandas as pd
# """

# extlinks = {'pr': ('https://github.com/statsmodels/statsmodels/pull/%s',
#                    'PR #'),
#             'issue': ('https://github.com/statsmodels/statsmodels/issues/%s',
#                       'Issue #')
#             }

autosectionlabel_prefix_document = True

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # http://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return
    src = source[0]
    # Skip converted notebooks
    if 'nbconvert_exporter' in src:
        return
    try:
        rendered = app.builder.templates.render_string(src,
                                                       app.config.html_context)
        source[0] = rendered
    except Exception as exc:
        from sphinx.util import logging
        logger = logging.getLogger(__name__)
        logger.warning(exc)
        logger.warning(source[0])


def setup(app):
    app.add_css_file('css/custom.css')
    app.add_css_file("css/frc-rtd.css")
    app.connect("source-read", rstjinja)
    return {'parallel_read_safe': True,
            'parallel_write_safe': True}
