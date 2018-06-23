@echo off

mkdir docs_md\problems
for /r %%i in (problems\*.py) do python -m utils.markdown %%i docs_md\problems\%%~ni.md
mkdir docs_md\utils
for /r %%i in (utils\*.py) do python -m utils.markdown %%i docs_md\utils\%%~ni.md
mkdir docs_md\documentation
for /r %%i in (utils\markdown\*.py) do python -m utils.markdown %%i docs_md\documentation\%%~ni.md

copy /y README.md docs_md\index.md

mkdocs build
