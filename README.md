# poc-pyinstaller

POC using PyInstaller with Github Actions to generate binaries from a python script.


## Demo

Workflow run: https://github.com/GuillaumeFalourd/poc-pyinstaller/actions/runs/1505378109

![Screen Shot 2021-11-25 at 19 11 39](https://user-images.githubusercontent.com/22433243/143503852-364abe39-e817-4ef5-af8e-536e54d6a46d.png)

## Workflow

```yaml
name: PyInstaller

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: ['windows-latest', 'ubuntu-latest', 'macos-latest']

    steps:
    - uses: actions/checkout@v2.3.4
    - uses: actions/setup-python@v2
      with:
        python-version: 3.7

    - run: pip install -r requirements.txt pyinstaller
    - run: pyinstaller poc.py
    # Optional to check the files
    - run: |
        cd ./dist/poc
        ls
    - uses: actions/upload-artifact@v2
      with:
        name: artifact-${{ matrix.os }}
        path: dist/*
```
