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

Working with documents
----------------------

Loading Document
^^^^^^^^^^^^^^^^

A poppler :class:`.Document` can be created from a file path
using :func:`load_from_file`, from binary data using
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

You can provide the password when loading the document, or later using the :meth:`.Document.unlock` method.
The :meth:`.Document.is_locked` property tells you if you have the permission to view the document.
If you load a document with the wrong password, an error message is printed on the error console.

The possible document restrictions are given by the :class:`.Permissions` enum.
You can check each permission using the :meth:`.Document.has_permission` method.
If the document was opened with the right owner password, then each permission will be True.
Otherwise, it will depend on the permissions set on the document itself.


Document properties
^^^^^^^^^^^^^^^^^^^

The :meth:`.Document.infos` method is a convenient way to get all the document meta infos as
a Python dict. Otherwise, you can follow the poppler-cpp API, and retreive the list of available
keys using :meth:`.Document.info_keys`, get individual key values using :meth:`.Document.info_key`
or :meth:`.Document.info_date`, and set them using :meth:`.Document.set_info_key` or :meth:`.Document.set_info_date`.

The infos are also available via individual properties: :attr:`.Document.author`, :attr:`.Document.creation_date`,
:attr:`.Document.creator`, :attr:`.Document.keywords`, :attr:`.Document.metadata`, :attr:`.Document.modification_date`,
:attr:`.Document.producer`, :attr:`.Document.subject`, and :attr:`.Document.title`.
All those properties can be read or written.


Loading pages
^^^^^^^^^^^^^

You can query the number of pages a document has using :attr:`.Document.pages`.
Pages are indexed from 0.
You can create a :class:`.Page` object using the :meth:`.Document.create_page` method.
This method can take the page index, or a page label, as argument. However, it is more
convenient to use an index, since you cannot know the label before the page is created.


Working with pages
------------------

:class:`.Page` objects are used to extract text, and to query information about
transitions.

The :attr:`.Page.label` property gives you the page name; its usually the displayed page number.
:meth:`.Page.page_rect` allows you to query the page about its size.

Page transitions are mainly used for presentation softwares.
:meth:`.Page.transition` gives you information about the kind of page transition,
and :attr:`.Page.duration` gives you the duration of the transition.

Extracting text
^^^^^^^^^^^^^^^

The :meth:`.Page.text` method allows to query the :class:`.Page`
about all the texts it contains, or about the texts in a given area.
For more precise informations, :meth:`.Page.text_list` allows
to get the position of each text, and the position of each character
in a text box. Finally, the :meth:`.Page.search` method allows you
to search for a given text in a :class:`.Page`.


Getting font information
^^^^^^^^^^^^^^^^^^^^^^^^

You can get the list of fonts in a :class:`.Document` using :meth:`.Document.create_font_iterator`.
It returns an object you can iterate to get the list of fonts:

.. code-block:: python

   font_iterator = document.create_font_iterator()
   for page, fonts in font_iterator:
       print(f"Fonts for page {page}")
       for font in fonts:
           print(f"- {font.name}"


Since Poppler 0.89, yo can also get font information associated with a :class:`.TextBox`.
To get the information, you need to pass the text_list_include_font option
to the :meth:`.Page.text_list` method.

.. code-block:: python

    boxes = pdf_page.text_list(pdf_page.TextListOption.text_list_include_font)
    box = boxes[0]

    assert box.has_font_info
    print(box.get_font_name())
    print(box.get_font_size())



Rendering image
^^^^^^^^^^^^^^^

Rendering is the process of converting a :class:`.Page` to an :class:`.Image`.
To render a :class:`.Page`, you first need to create a :class:`.PageRenderer` object.
Then you give the :class:`.Page` to the :meth:`.PageRenderer.render_page`
method to obtain an  :class:`.Image` object.


Working with images
-------------------

Given that ``image`` object is an instance of :class:`.Image`,
you can convert it to different formats,
to interract with other libraries. Here are some examples.


Converting to PIL or Tk image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:class:`.ImageFormat` can be converted to a string representation,
compatible with the PIL raw importer:

.. code-block:: python
   
   from PIL import Image, ImageTk

   pil_image = Image.frombytes(
       "RGBA",
       (image.width, image.height),
       image.data,
       "raw",
       str(image.format),
    )
    tk_image = ImageTk.PhotoImage(pil_image)

Unfortunately, it is not possible to build a PIL image using the
buffer interface. A copy of the image data in unavoidable.

If you need to use the image with Tk, you creeate if from a PIL image.


Converting to QImage
^^^^^^^^^^^^^^^^^^^^

There is no builtin map for the image formats,
mainly to avoid introducing a dependency on Qt.
However, it is easy to build it if needed, as in the following example:

.. code-block:: python

   P2QFormat = {
       ImageFormat.invalid: QtGui.QImage.Format_Invalid,
       ImageFormat.argb32: QtGui.QImage.Format_ARGB32,
       ImageFormat.bgr24: QtGui.QImage.Format_BGR888,
       ImageFormat.gray8: QtGui.QImage.Format_Grayscale8,
       ImageFormat.mono: QtGui.QImage.Format_Mono,
       ImageFormat.rgb24: QtGui.QImage.Format_RGB888,
   }
   qimg = QtGui.QImage(data, image.width, image.height,
                       image.bytes_per_row,
                       P2QFormat[image.format])


Converting image to numpy array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:class:`.Image` supports buffer protocol through
`memoryview <https://docs.python.org/3/library/stdtypes.html#memoryview>`_. 
It allows to access the image buffer directly from Python, without
copying it.

You can create a numpy array using the :meth:`.memoryview` method.
If you modify the array, image data will be automaticall modified as well.

.. code-block:: python

   a = numpy.array(image.memoryview(), copy=False)
   print(a[0, 0, 0])
   print(image.data[0])  # Value of the first byte of the image

   a[0, 0, 0] = 0
   print(image.data[0])  # It is now 0




.. Converting to OpenCV image
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^

