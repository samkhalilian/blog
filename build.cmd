rmdir -r _build
sphinx-multiversion . _build/html
sphinx-build . _build/html -c . -D master_doc=index
echo "Done! Open build/html/index.html"

python -m http.server -d _build/html
start http://localhost:8000/index.html
