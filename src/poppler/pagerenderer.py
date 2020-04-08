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

from poppler._page_renderer import page_renderer, can_render
from poppler import Rotation
from poppler.image import Image


class PageRenderer(object):
    def __init__(self):
        self._renderer = page_renderer()

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

    @staticmethod
    def can_render():
        return can_render()
