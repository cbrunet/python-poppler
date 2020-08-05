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


# Documentation

https://cbrunet.github.io/python-poppler/

Documentation is currently a work-in-progress. Here you will find information about
installation of the package, compilation from sources, and usage.

Meanwhile, because it follows the interface of `poppler-cpp`, you can refer to the [documentation of the C++ library](https://poppler.freedesktop.org/api/cpp/namespacepoppler.html).



# Usage

The package is installed as `poppler`. 

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

Please provide unit tests covering the new feature, or proving
that a bug is corrected, when possible.
