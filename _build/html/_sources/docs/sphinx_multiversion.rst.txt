Sphinx Multiversion
===================

https://sphinx-contrib.github.io/multiversion/main/index.html#

Step-by-Step Guide
1. Install Sphinx and sphinx-multiversion
bash
Copy
Edit
pip install sphinx sphinx-multiversion
2. Create a Sphinx project
bash
Copy
Edit
sphinx-quickstart hello-docs
You can accept most defaults, but ensure:

Separate source and build directories? → Yes

Project name, Author → anything you like

3. Write your "Hello World" page
Edit hello-docs/source/index.rst:

rst
Copy
Edit
Hello World
===========

Welcome to the Hello World documentation!

.. toctree::
   :maxdepth: 1
Or add another .rst file and link it in the toctree.

4. Enable sphinx-multiversion
Edit hello-docs/source/conf.py, and add:

python
Copy
Edit
extensions.append("sphinx_multiversion")

# Optional: control which branches/tags are included
smv_tag_whitelist = r"^v\d+\.\d+$"  # Tags like v1.0, v2.0
smv_branch_whitelist = r"^(main|master|v\d+\.\d+)$"
smv_remote_whitelist = r"^origin$"
5. Initialize Git & create branches
Inside your project folder:

bash
Copy
Edit
git init
git add .
git commit -m "Initial commit"

git checkout -b v1.0
echo "Version 1.0" >> hello.txt
git add hello.txt
git commit -m "v1.0 changes"
Create another version:

bash
Copy
Edit
git checkout -b v2.0
echo "Version 2.0" >> hello.txt
git commit -am "v2.0 changes"
6. Build your multiversion docs
From the project root:

bash
Copy
Edit
sphinx-multiversion source build/html
7. View the output
Open build/html/index.html in your browser. You should see a version switcher in the sidebar!

