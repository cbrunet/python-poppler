![Python build and tests](https://github.com/cbrunet/python-poppler/workflows/Python%20build%20and%20tests/badge.svg?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# python-poppler

**python-poppler** is a Python binding to the poppler-cpp library. It allows to read, render, or modify PDF documents.
More specifically, it currently allows to:
- read an modify document meta data;
- list and read embedded documents;
- list the fonts used by the document;
- search or extract text on a given page of the document;
- render a page to a raw image;
- get info about transitions effects between the pages;
- read the table of contents of the document.


# Download

## Requirements

You nedd Python version 3.7 or 3.8.
You will also need the usual build tools (cmake, gcc...)

This package is currently distributed as source only, and is currently tested on Linux only.
It requires poppler 0.62 or higher (but 0.87 or higher is recommended).
I will provide a WIndows build once I figure out how to compile poppler for Windows.

You need poppler-cpp with headers, python (3.7 or 3.8) with headers, and cmake.
On Arch linux, you need the [poppler](https://security.archlinux.org/package/poppler) package.
On Ubuntu, you need to install [libpoppler-cpp-dev](https://packages.ubuntu.com/bionic/libpoppler-cpp-dev).


## Install from PyPI

Package is [available on PyPI](https://pypi.org/project/python-poppler/).
To install, you simply need to issue the following command, preferabily in a python virtual environment:

```
$ pip install python-poppler
```

## Install from git sources

Sources are [available on GitHub](https://github.com/cbrunet/python-poppler):

```
git clone --recurse-submodules https://github.com/cbrunet/python-poppler.git
```

[pybind11](https://pybind11.readthedocs.io/en/stable/) sources are included as submodule.
If you cloned the repository without the submodules, you can
get them with the command

```
git submodule update --init --recurse
```

If you want to use an installed version of pybind11
instead of the submodule, you can replace `add_subdirectory(pybind11)`
by `find_package(pybind11)` in the [CMakeLists.txt] file.

The whole build process is handled by the `setup.py` file.
It will invoke the needed cmake commands, and install the files
at the right place.

For instance, to install in the current environment:

```
$ python setup.py install
```

This will compile the binary packages, and install the library.

Tests are run using [tox](https://tox.readthedocs.io/en/latest/):

```
$ tox
```


## Building from Poppler sources

```
$ git clone https://gitlab.freedesktop.org/poppler/poppler.git
$ cd poppler
$ git checkout poppler-0.89.0
$ mkdir build
$ cd build
$ cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr/local \
    -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
    -DBUILD_GTK_TESTS=OFF \
    -DBUILD_QT5_TESTS=OFF \
    -DBUILD_CPP_TESTS=OFF \
    -DENABLE_CPP=ON \
    -DENABLE_GLIB=OFF \
    -DENABLE_GOBJECT_INTROSPECTION=OFF \
    -DENABLE_GTK_DOC=OFF \
    -DENABLE_QT5=OFF \
    -DBUILD_SHARED_LIBS=ON \
    ..
$ make
$ mkdir ../dist
$ sudo make install
```

You can omit the `git checkout` step if you want to work on HEAD.

To find the right version of poppler when compiling python-poppler,
you can set the `PKG_CONFIG_PATH` env var:

```
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
$ cd python-poppler
$ python setup.py bdist_wheel
```

To build the wheel, you need the `wheel` package, if not already installed. 
Alternatively, you could simply do `python setup.py install`, preferabily
in a virtual environment.

You may need to tell the system where to find the Poppler shared libraries,
by setting the `LD_LIBRARY_PATH` env var:

```
$ export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
$ python
>>> import poppler
>>> poppler.version()
(0, 89, 0)
```


# Usage

The package is installed as `poppler`. It follows the interface of `poppler-cpp`. Therefore, you can refer to the [documentation of the C++ library](https://poppler.freedesktop.org/api/cpp/namespacepoppler.html).


Example:

```python
from poppler import load_from_file, PageRenderer

pdf_document = load_from_file("sample.pdf")
page_1 = pdf_document.create_page(0)
page_1_text = page_1.text()

renderer = PageRenderer()
image = renderer.render_page(page_1)
image_data = image.data
```


# Contributing

Contributions are welcome.

Please use the [GitHub issue tracker](https://github.com/cbrunet/python-poppler/issues)
to report bugs or request features.
You can also submit Pull requests.

Code is formatted using [black](https://github.com/psf/black).
Ensure that everything is well formatted. You can use

```
tox -e lint
```

to lint your code.

Please ensure that all tests pass, by running `tox`.

Please provide unit tests covering the new feature, or prooving
that a bug is corrected, when possible.
