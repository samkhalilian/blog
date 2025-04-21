import json
import os
import sys


##########################################
# diagnostics
print(">>> [conf.py top] __file__ =", __file__)
print(">>> [conf.py top] SPHINX_MULTIVERSION_NAME =", os.environ.get("SPHINX_MULTIVERSION_NAME"))
print(">>> [conf.py top] GIT HEAD =", os.popen('git rev-parse --abbrev-ref HEAD').read().strip())
print(">>> [conf.py top] Is .git here? =", os.path.isdir(".git"))
##########################################


# print(__file__)
# print(">>> DEBUG: SPHINX_MULTIVERSION_NAME =", os.environ.get("SPHINX_MULTIVERSION_NAME"))
# print(">>> DEBUG: SPHINX_MULTIVERSION_LIST =", os.environ.get("SPHINX_MULTIVERSION_LIST"))

# print(">>> ENV DEBUG")
# for key, value in os.environ.items():
#     if key.startswith("SPHINX_"):
#         print(f"{key} = {value}")
# print(">>> END DEBUG")

# Add the `_ext` directory to the Python path
sys.path.insert(0, os.path.abspath("_ext"))

#!/usr/bin/env python

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Learn to Code"
copyright = '2024, Sam Khalilian'
author = 'Sam Khalilian'
# version = 'v6.0'
version = os.environ.get("SPHINX_MULTIVERSION_NAME")#, "local")
# release = '1.0.0'
# version = os.environ.get("SPHINX_MULTIVERSION_NAME", "local")
release = version

# source_encoding = 'utf-8'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'ablog',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',

    'sphinx.ext.githubpages',
    'sphinxcontrib.youtube',
    'sphinx.ext.mathjax',
    # 'sphinx_tags',
    'sphinx_copybutton',
    'sphinx.ext.graphviz',
    # 'sphinx.ext.plot',
    "sphinx_design",
    # "sphinx_comments",
    "sphinxemoji.sphinxemoji",
    "sphinx_multiversion",    
    # "sphinxcontrib.disqus",
    # "sphinx_comments",
    # "github_issues", # turn as requires internet connection to build and csv already saved
    # "github_discussions", # turn as requires internet connection to build and csv already saved
    # "sphinxcontrib.datatemplates", # this dont work created own extension instead to create csv table
    # "my_extension",
]    
# extensions = [
#     'sphinx.ext.extlinks',
#     'sphinx.ext.intersphinx',
#     'sphinx.ext.todo',
#     'sphinx.ext.extlinks',
#     'alabaster',
#     'ablog',
#     'sphinxcontrib.youtube',
#     'sphinx.ext.mathjax',
#     'sphinx-mathjax-offline',
#     # 'matplotlib.sphinxext.only_directives',
#     # 'matplotlib.sphinxext.plot_directive',
#     'numpydoc',
#     'notfound.extension',
#     'sphinx_last_updated_by_git',
#     # 'sphinxnotes.isso',
#     # "sphinx_github_changelog",
#     # "sphinx.ext.graphviz",
#     "sphinx_copybutton",
#     # "sphinx_codeautolink",
#     # 'sphinx_code_tabs',
# ]

templates_path = ['_templates']
exclude_patterns = [
    ".*",
    "requirements.txt",
    "README.rst",
    "TODO.rst",
     "_drafts",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = "sphinx_book_theme"
# html_theme = "classic"
# html_theme = "alabaster"
# html_theme = "sphinx_rtd_theme"
# html_theme = 'sphinx_book_theme'
html_theme = "pydata_sphinx_theme"

html_static_path = ['_static']

today_fmt = "%d %b %Y %H:%M"
# today_fmt = "%d %b %Y"

html_title = "Learn to Code"
# html_last_updated_fmt = "%d %b %Y at %H:%M"
html_last_updated_fmt = "%d %b %Y %H:%M"

html_theme_options = {
    # "repository_provider": "github",
    # "repository_url": "https://github.com/samkhalilian",
    # "use_repository_button": True,
    
    # "repository_branch": "https://github.com/samkhalilian/blog",
    # "use_source_button": True,
    
    # "use_issues_button": True,

    # "use_sidenotes": True, # makes foot notes into side notes. side notes are not supported in the theme

    # "show_source": True,
    "back_to_top_button": True,
    # 'show_version': True,  # This enables the version display in the footer
    # 'show_date': True,  
    "show_version_warning_banner": True,

    "logo": {
        # "text": "Learn to Code",
        "alt_text": "Learn to Code",
        "image_light": "_static/logo_learn_to_code_light.jpg",
        "image_dark": "_static/logo_learn_to_code_dark.jpg",
    },

    # 'home_page_in_toc': True,

    "announcement": "These pages are under construction.  Please report any issues to <a href='https://github.com/samkhalilian/blog/issues'>https://github.com/samkhalilian/blog/issues</a>",
    # "show_version_warning_banner": True,
    # "announcement": "If you would like to contribute to these docs check out <a href='https://github.com/samkhalilian/blog'>GitHub repository!</a>",

    # "show_version_dropdown": True,
    
    # "navbar_start": ["navbar-logo", "version-switcher"], 
    "navbar_end": [
        # "search-field.html",
        "version-switcher",
        "theme-switcher",
        "navbar-icon-links.html", 
        ],

    "switcher": {
        "json_url": "_static/versions.json",
        "version_match": version,    
    },

    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/samkhalilian/blog",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/sam-khalilian-453704146",
            "icon": "fa-brands fa-linkedin-in",
        },
        {
            "name": "SouncCloud",
            "url": "https://soundcloud.com/samkhalilian",
            "icon": "fa-brands fa-soundcloud",
        },
        {
            "name": "Pinterest",
            "url": "https://uk.pinterest.com/samkhalilian/",
            "icon": "fa-brands fa-pinterest",
        },
    ],

    "footer_start": ["footer"],

}

# includng sidebars overrides logo
html_sidebars = {
    # "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    '**': [ 
        # 'about.html',   # this blocks book them logo
        # 'navbar-logo.html', # display logo
        # 'search-button-field.html',
        # 'searchbox.html',
        # 'postcard.html', 
        # 'navigation.html',
        # 'recentposts.html', 
        # 'categories.html',  
        # 'tagcloud.html',
        # 'archives.html',
        # 'authors.html',
        
        "ablog/recentposts.html", 
        # "ablog/categories.html",  
        "ablog/tagcloud.html",
        "ablog/archives.html",
        "ablog/authors.html", # required by ablog else warning message on rendering
        
        # 'locations.html',
        # 'ethicalads.html',
        # "sidebar-nav-bs.html",
        # 'sbt-sidebar-nav.html', # not clear what this does? # shows toc in sidebar
        # "comments.html",
        # "custom_sidebar_github.html",
        # "custom_discussions.html",
    ],
}

html_context = {
    "github_user": "samkhalilian",
    "github_repo": "blog",
    "github_issues": "https://github.com/samkhalilian/blog/issues",
    "github_discussions": "https://github.com/samkhalilian/blog/discussions",
    "this_github_pages": "https://samkhalilian.github.io/blog/",
    "this_home_page": "https://samkhalilian.dev",
}
# html_context = {
#     "github_user": "ORG",  # Replace with your GitHub username/org
#     "github_repo": "REPO",  # Replace with your GitHub repo name
#     "github_discussions": "https://github.com/ORG/REPO/discussions"
# }



# html_context = {
#     "disqus_shortname": "www. samkhalilian.github.io",
#     "comments_in_footer": True,
# }


# html_context = {
#     "github_user": "<your-github-org>",
#     "github_repo": "<your-github-repo>",
#     "github_version": "<your-branch>",
#     "doc_path": "<path-from-root-to-your-docs>",

#    # ...
# #    "default_mode": "dark"
#    "default_mode": "light" # use to det default light dark mode and use system
# }

# tags_create_tags = True
# tags_overview_title = ""#"Tags overview"
# # tags_intro_text = "2"
# tags_page_title = "Tag"
# tags_page_header = "Pages with this tag"

# numfig = True

# html_css_files = [
#     "custom.css",
# ]

# html_show_sourcelink = True

# comments_config = {
#     "utterances": {
#         "repo": "https://github.com/samkhalilian/blog",
#         "issue-term": "pathname",  # Links comments to page URLs
#     }
# }

# comments_config = {
#    "utterances": {
#       "repo": "https://github.com/samkhalilian/blog",
#    }
# }
comments_config = {
    # "utterances": {
    #     "repo": "samkhalilian/blog",
    #     "issue-term": "url",
    #     # "issue-term": "pathname",
    #     "label": "💬 Comment",
    #     "theme": "github-light",
    # },

    # https://giscus.app/
    "giscus": {
        "repo": "samkhalilian/blog",
        "repo_id": "R_kgDOJGG8hQ",
        "category": "Announcements",
        "category_id": "DIC_kwDOJGG8hc4CnR9A",
        # "mapping": "pathname",
        "mapping": "url",
        "reactions_enabled": "1",
        "theme": "light",
    }
}

##################################################################
# sphinx_multiversion
# Optional: control which branches/tags are included
# smv_tag_whitelist = r"^v\d+\.\d+$"  # Tags like v1.0, v2.0
# # smv_branch_whitelist = r"^(main|master|v\d+\.\d+)$"
# smv_branch_whitelist = r"^(v\d+\.\d+)$"
# smv_remote_whitelist = r"^origin$"
smv_tag_whitelist = r'^(v4\.0|v5\.0)$'
smv_remote_whitelist = r'^origin$'
smv_branch_whitelist = r"^(v4\.0|v5\.0)$"

# import os
# import json

# html_static_path = ["_static"]

# print(">>> SPHINX_MULTIVERSION_NAME =", os.environ.get("SPHINX_MULTIVERSION_NAME"))
# print(">>> Generating versions.json:", os.environ.get("SPHINX_MULTIVERSION_LIST"))

# if "SPHINX_MULTIVERSION_NAME" in os.environ and "SPHINX_MULTIVERSION_LIST" in os.environ:
#     try:
#         versions = []
#         for item in json.loads(os.environ["SPHINX_MULTIVERSION_LIST"]):
#             versions.append({
#                 "version": item["name"],
#                 "url": f"/{item['name']}/",  # or "" if building for root
#             })

#         os.makedirs("_static", exist_ok=True)
#         with open("_static/versions.json", "w") as f:
#             json.dump({"versions": versions}, f, indent=2)

#     except Exception as e:
#         print(f"⚠️ Failed to generate versions.json: {e}")


# def setup(app):
#     import os
#     print(">>> LATE LOAD: SPHINX_MULTIVERSION_NAME =", os.environ.get("SPHINX_MULTIVERSION_NAME"))
def setup(app):
    print(f">>> [setup()] {__file__}")
    print(">>> [setup()] SPHINX_MULTIVERSION_NAME =", os.environ.get("SPHINX_MULTIVERSION_NAME"))
    print(">>> [setup()] SPHINX_MULTIVERSION_LIST =", os.environ.get("SPHINX_MULTIVERSION_LIST"))

    if "SPHINX_MULTIVERSION_LIST" in os.environ:
        try:
            versions = []
            refs = json.loads(os.environ["SPHINX_MULTIVERSION_LIST"])
            for ref in refs:
                versions.append({
                    "version": ref["name"],
                    "url": f"/{ref['name']}/"
                })

            os.makedirs("_static", exist_ok=True)
            with open("_static/versions.json", "w") as f:
                json.dump({"versions": versions}, f, indent=2)

            print(">>> ✅ versions.json generated!")

        except Exception as e:
            print(">>> ❌ Error generating versions.json:", e)
