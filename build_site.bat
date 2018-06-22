mkdir docs_md\problems
for /r %%i in (problems\*.py) do python shared_lib\build_markdown.py %%i docs_md\problems\%%~ni.md
mkdir docs_md\shared_lib
for /r %%i in (shared_lib\*.py) do python shared_lib\build_markdown.py %%i docs_md\shared_lib\%%~ni.md

copy /y README.md docs_md\index.md

mkdocs build
