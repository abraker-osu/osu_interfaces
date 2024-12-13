@echo off

echo Removing ".eggs/..."
rd /s /q .eggs

echo Removing "pycache..."
py -Bc "import pathlib; import shutil; [ shutil.rmtree(path) for path in pathlib.Path('.').rglob('__pycache__') ]"

echo [ DONE ]
