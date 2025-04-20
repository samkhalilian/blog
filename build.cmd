#!/bin/bash

# Clean build
rm -rf build/

# Build all versions
sphinx-multiversion source build/html

# Build landing page
sphinx-build . build/html -c source -D master_doc=index

echo "Done! Open build/html/index.html"
