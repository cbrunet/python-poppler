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

from poppler.cpp.font import font_info
from poppler.cpp.font import type_enum as FontType  # noqa


class FontInfo:
    def __init__(self, info=None):
        self._info = info or font_info()

    @property
    def file(self):
        return self._info.file()

    @property
    def is_embedded(self):
        return self._info.is_embedded()

    @property
    def is_subset(self):
        return self._info.is_subset()

    @property
    def name(self):
        return self._info.name()

    @property
    def type(self):
        return self._info.type()


class FontIterator:
    def __init__(self, it):
        self._it = it

    @property
    def current_page(self):
        return self._it.current_page()

    @property
    def has_next(self):
        return self._it.has_next()

    def next_(self):
        return [FontInfo(i) for i in self._it.next_()]

    def __iter__(self):
        while self._it.has_next():
            yield self.current_page, self.next_()
