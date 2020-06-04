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

from poppler.cpp import page, global_
from poppler.cpp.global_ import rotation_enum as Rotation
from poppler.pagetransition import PageTransition
from poppler.rectangle import Rectangle
from poppler.utilities import since, version


class _MetaTextBox(type):
    def __new__(mcs, classname, bases, dictionary):
        if version() >= (0, 89, 0):
            dictionary["WritingMode"] = page.writing_mode_enum
        return type.__new__(mcs, classname, bases, dictionary)


@since(0, 63)
class TextBox(metaclass=_MetaTextBox):
    def __init__(self, text_box):
        self._text_box = text_box

    @property
    def text(self):
        return str(self._text_box.text())

    @property
    def bbox(self):
        return Rectangle.from_object(self._text_box.bbox())

    @property
    @since(0, 68)
    def rotation(self):
        return self._text_box.rotation()

    def char_bbox(self, i):
        return Rectangle.from_object(self._text_box.char_bbox(i))

    @property
    def has_space_after(self):
        return self._text_box.has_space_after()

    @property
    @since(0, 89)
    def has_font_info(self):
        return self._text_box.has_font_info()

    @since(0, 89)
    def get_font_name(self, i=0):
        return self._text_box.get_font_name(i)

    @since(0, 89)
    def get_font_size(self):
        return self._text_box.get_font_size()

    @since(0, 89)
    def get_wmode(self, i=0):
        return self._text_box.get_wmode(i)


class _MetaPage(type):
    def __new__(mcs, classname, bases, dictionary):
        if version() >= (0, 89, 0):
            dictionary["TextListOption"] = page.text_list_option_enum
        return type.__new__(mcs, classname, bases, dictionary)


class Page(metaclass=_MetaPage):

    Orientation = page.orientation_enum
    PageBox = global_.page_box_enum
    SearchDirection = page.search_direction_enum
    TextLayout = page.text_layout_enum

    def __init__(self, poppler_page):
        self._page = poppler_page

    @property
    def duration(self):
        return self._page.duration()

    @property
    def label(self):
        return str(self._page.label())

    @property
    def orientation(self):
        return self._page.orientation()

    def page_rect(self, box=PageBox.crop_box):
        rectf = self._page.page_rect(box)
        return Rectangle.from_object(rectf)

    def search(self, text, r, direction, case_sensitivity, rotation=Rotation.rotate_0):
        utext = global_.ustring(text)
        found, found_rect = self._page.search(
            utext, r._rect, direction, case_sensitivity, rotation
        )
        if found:
            return Rectangle.from_object(found_rect)
        return None

    def text(self, rect=None, layout_mode=None):
        r = rect or Rectangle(0.0, 0.0, 0.0, 0.0)
        if layout_mode is None:
            t = self._page.text(r._rect)
        else:
            t = self._page.text(r._rect, layout_mode)
        return str(t)

    @since(0, 63)
    def text_list(self, opt_flag=None):
        if opt_flag is not None and version() >= (0, 89, 0):
            boxes = self._page.text_list(opt_flag)
        else:
            boxes = self._page.text_list()
        return [TextBox(b) for b in boxes]

    def transition(self):
        transition = self._page.transition()
        return PageTransition(transition) if transition else None
