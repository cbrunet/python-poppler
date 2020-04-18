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


class TocItem:
    def __init__(self, toc_item):
        self._item = toc_item

    def children(self):
        return [TocItem(i) for i in self._item]

    def __iter__(self):
        for item in self._item:
            yield TocItem(item)

    @property
    def is_open(self):
        return self._item.is_open()

    @property
    def title(self):
        return str(self._item.title())


class Toc:
    def __init__(self, toc):
        self._toc = toc

    @property
    def root(self):
        return TocItem(self._toc.root())
