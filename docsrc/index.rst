.. python-poppler documentation master file, created by
   sphinx-quickstart on Mon Jun  8 21:41:45 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-poppler's documentation!
==========================================

**python-poppler** is a Python binding to the poppler-cpp library.
It allows to read PDF documents, render them, and to modify some
informations inside the documents.


About poppler
-------------

Poppler is a PDF rendering library based on the xpdf-3.0 code base.
It consists in a private backend (libpoppler), and in multiple frontends:

- cpp (libppoppler-cpp): A cpp library, without additional requirements
- glib (libpoppler-glib): A GTK library
- qt5 (libpoppler-qt5): A Qt library

Poppler is used by many PDF viewers:

- evince (using poppler-glib)
- okular and qpdfview (using poppler-qt5)



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
