.. _usage:

Using python-poppler
====================

.. py:currentmodule:: poppler

Quickstart
----------

.. code-block:: python

    from poppler import load_from_file, PageRenderer

    pdf_document = load_from_file("sample.pdf")
    page_1 = pdf_document.create_page(0)
    page_1_text = page_1.text()

    renderer = PageRenderer()
    image = renderer.render_page(page_1)
    image_data = image.data


The pdf file is loaded into a :class:`.Document`.
From the :class:`.Document`, you can extract general infos
such as propertise and font infos.
You can also extract :class:`.Page` objects, using the :meth:`.Document.create_page`
method.

From the :class:`.Page`, you get informations about transitions and page orientation,
and various methods to extract texts.

Using a :class:`.PageRenderer`, you can convert a :class:`.Page` to an :class:`.Image`.

Most used classes and functions are aliased directly in the :mod:`poppler` module.
Therefore, you usually do not need to import anything else than :mod:`poppler`.


Loading Document
----------------

A poppler :class:`.Document` can be created from a file path
using :func:`.load_from_file`, from binary data using
:func:`load_from_data`. There is also a more general :func:`load`
function, which can take either a file path, binary data, or a
file-like object as argument.

Working with password protected documents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two kinds of passwords than can by applied to a PDF document:
*User Password* and *Owner Password*.

The *User Password*, or *Document open password*, prevents to open or view the document.

The *Owner Password*, or *Permission password*, or *master password*, is used to set document restrictions,
such as printing, copying contents, editing, extracting pages, commenting, etc.
When this password is set, you need it to modify the document.

A PDF document can have a *User Password*, a *Owner Password*, or both.
When both passwords are set, you only need one of them to be able to open the document.
However, you need the *Owner Password* to be able to modify the document.






Document properties

Loading page

Extracting text

Rendering image
