![Python build and tests](https://github.com/cbrunet/python-poppler/workflows/Python%20build%20and%20tests/badge.svg?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# How to build

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


# Usage

The package is installed as `poppler`. It follows the interface of `poppler-cpp`. Therefore, you can refer to the [documentation of the C++ library](https://poppler.freedesktop.org/api/cpp/namespacepoppler.html).


Example:

```python
from poppler.document import load_from_file
from poppler.pagerenderer import PageRenderer

pdf_document = load_from_file("sample.pdf")
page_1 = pdf_document.create_page(0)
page_1_text = page_1.text()

renderer = PageRenderer()
image = renderer.render_page(page_1)
image_data = image.data
```
