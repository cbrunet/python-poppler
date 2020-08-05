.. python-poppler documentation master file, created by
   sphinx-quickstart on Mon Jun  8 21:41:45 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-poppler's documentation!
==========================================

.. toctree::
   :hidden:

   installation
   usage
   contribution
   modules


**python-poppler** is a Python binding to the poppler-cpp library.
It allows to read PDF documents, render them, and to modify some
informations inside the documents.

You can use python-poppler for a variaty of tasks. For example:

* To extract text from a PDF file
* To render pages of a PDF document as images
* To read and modify the properties of a PDF document
* To build a simple PDF viewer to perform special operations using PDF documents

This is a personal project, in the sense I'm not affiliated in any way
to the Poppler library. I did this for my own needs, because I didn't find
other Python library to *easily* display PDF files. I'm not aware of other
Python library interfacing especially the *poppler-cpp* library.

python-poppler is licensed **GPL v2.0**. This is because Poppler itself
(and the original xpdf code base) also is licensed using GPL.
Before using this software, be sure to understand what are the implications
of this license.

Contents
--------

* :ref:`installation` section is about installing or compiling python-poppler.

* :ref:`usage` section is about how to actually use the python-poppler library.

* :ref:`contributing` section is about submiting bugs or pull requests to the project.

* :ref:`reference` lists all modules, classes, and methods. The reference section is still a work in progress...

About poppler
-------------

`Poppler`_ is a PDF rendering library based on the xpdf-3.0 code base.
It consists in a private backend (libpoppler), and in multiple frontends:

* `cpp <https://poppler.freedesktop.org/api/cpp/>`_ (libppoppler-cpp): A cpp library, without additional requirements
* `glib <https://poppler.freedesktop.org/api/glib/>`_ (libpoppler-glib): A GTK library
* `qt5 <https://poppler.freedesktop.org/api/qt5/>`_ (libpoppler-qt5): A Qt library

Poppler is used by many PDF viewers:

* evince (using poppler-glib)
* okular and qpdfview (using poppler-qt5)


Useful links
^^^^^^^^^^^^

Here are few useful links related to the Poppler library:

* `Poppler`_ homepage
* `API documentation <https://poppler.freedesktop.org/api/cpp/>`_ for poppler-cpp
* `Git repository <https://gitlab.freedesktop.org/poppler/poppler>`_
* `Issue tracker <https://gitlab.freedesktop.org/poppler/poppler/-/issues>`_
* `Poppler Changelog <https://poppler.freedesktop.org/releases.html>`_


.. _Poppler: https://poppler.freedesktop.org/



Alternatives and related Python libraries
-----------------------------------------

Here is a (non-exaustive) list of related Python library for working with PDF files.

Other poppler bindings
^^^^^^^^^^^^^^^^^^^^^^

`python-poppler-qt5 <https://pypi.org/project/python-poppler-qt5/>`_
    This binding is based on poppler-qt5. This is probably the best poppler python binding,
    but I wansn't able to properly install it in a Python virtual environment, because
    of the complexity of the compilation. The binding is done using the sip library.

`python-poppler-qt4 <https://pypi.org/project/python-poppler-qt4/>`_
    Older version, using Qt4. You should use Qt5 version instead. Latest version is from 2015...

`python-poppler <https://launchpad.net/poppler-python>`_
    Binding based on poppler-glib. Latest version is from 2009...


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


