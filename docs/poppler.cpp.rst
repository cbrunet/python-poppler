poppler.cpp package
===================

The poppler.cpp package is the direct binding to the poppler-cpp library.
You usually do not need to interract directly with it, as all objects
are wrapped using native Python objects in the :mod:`poppler` module.


This module mostly follows the C++ code. Therefore, you can refer
to the `poppler-cpp documentation <https://poppler.freedesktop.org/api/cpp/>`_.


Module contents
---------------

.. py:currentmodule:: poppler

.. py:module:: poppler.cpp

.. py:module:: poppler.cpp.page_renderer

.. py:class:: render_hint

   A flag of an option taken into account when rendering.
   You can combine options by adding them.

   .. py:attribute:: antialiasing
      :type: int
      :value: 1

   .. py:attribute:: text_antialiasing
      :type: int
      :value: 2

   .. py:attribute:: text_hinting
      :type: int
      :value: 4


.. py:class:: page_renderer

   .. py:method:: render_page()

      Render a page as image.
