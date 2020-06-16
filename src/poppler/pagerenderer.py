# poppler-python: python binding to the poppler-cpp pdf lib
# Copyright (C) 2020, Charles Brunet <charles@cbrunet.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from poppler.cpp import page_renderer
from poppler.cpp.global_ import rotation_enum as Rotation
from poppler.image import Image
from poppler.utilities import version, since

if version() >= (0, 65, 0):
    LineMode = page_renderer.line_mode_enum

RenderHint = page_renderer.render_hint
"""A flag of an option taken into account when rendering"""


class PageRenderer:
    """:class:`PageRenderer` allows to render a :class:`.Page` object
    to an :class:`.Image`.

    It is a wrapper for :class:`poppler.cpp.page_renderer.page_renderer`.

    """

    def __init__(self):
        self._renderer = page_renderer.page_renderer()

    @property
    @since(0, 65)
    def image_format(self):
        return self._renderer.image_format()

    @image_format.setter
    @since(0, 65)
    def image_format(self, format):
        self._renderer.set_image_format(format)

    @property
    @since(0, 65)
    def line_mode(self):
        return self._renderer.line_mode()

    @line_mode.setter
    @since(0, 65)
    def line_mode(self, mode):
        self._renderer.set_line_mode(mode)

    @property
    def paper_color(self):
        return self._renderer.paper_color()

    @paper_color.setter
    def paper_color(self, color):
        self._renderer.set_paper_color(color)

    @property
    def render_hints(self):
        return self._renderer.render_hints()

    @render_hints.setter
    def render_hints(self, hints):
        self._renderer.set_render_hints(hints)

    def render_page(
        self,
        page,
        xres=72.0,
        yres=72.0,
        x=-1,
        y=-1,
        w=-1,
        h=-1,
        rotate=Rotation.rotate_0,
    ):
        img = self._renderer.render_page(page._page, xres, yres, x, y, w, h, rotate)
        return Image.from_object(img)

    def set_render_hint(self, hint, on=True):
        self._renderer.set_render_hint(hint, on)

    @staticmethod
    def can_render():
        """Tell whether poppler was compiled with the Splash render backend.

        This should always return True. If it returns False,
        :meth:`.render_page` will systematically return
        an invalid :class:`.Image`.

        Returns:
            bool: whether a render backend was compiled with poppler.

        """
        return page_renderer.can_render()
