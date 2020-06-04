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



# How to build

This package is currently distributed as source only, and is currently tested on Linux only.
It requires poppler 0.62 or higher (but 0.87 or higher is recommended).
I will provide a WIndows build once I figure out how to compile poppler for Windows.

You need poppler-cpp with headers, python (3.7 or 3.8) with headers, and cmake.
On Arch linux, you need the [poppler](https://security.archlinux.org/package/poppler) package.
On Ubuntu, you need to install [libpoppler-cpp-dev](https://packages.ubuntu.com/bionic/libpoppler-cpp-dev).

The whole build process is handled by the `setup.py` file.

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
    -DCMAKE_INSTALL_PREFIX:PATH=/ \
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
$ make DESTDIR=../dist install
```

You can omit the `git checkout` step if you want to work on HEAD.
Instead of using a custom `DESTDIR`, you could also install to `/usr/local`
by omiting the `CMAKE_INSTALL_PREFIX` option and using `sudo make install`
to install it.

To compile python-poppler using a custom location for Poppler,
set the env var `POPPLER_DIR` to the installation prefix you used.
In our example, it would be something like:

```
$ export POPPLER_DIR=/path/to/poppler/dist
$ cd python-poppler
$ python setup.py bdist_wheel
```

To build the wheel, you need the `wheel` package, if not already installed. 
Alternatively, you could simply do `python setup.py install`, preferabily
in a virtual environment.

You now need to tell the system where to find the Poppler shared libraries.

```
$ export LD_LIBRARY_PATH=/path/to/poppler/dist/usr/lib:$LD_LIBRARY_PATH
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
