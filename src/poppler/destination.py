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

from poppler.utilities import version, since

if version() >= (0, 74, 0):
    from poppler.cpp.destination import type_enum as DestinationType  # noqa


@since(0, 74)
class Destination:

    def __init__(self, destination):
        self._destination = destination

    @property
    def bottom(self):
        return self._destination.bottom()

    @property
    def is_change_left(self):
        return self._destination.is_change_left()

    @property
    def is_change_top(self):
        return self._destination.is_change_top()

    @property
    def is_change_zoom(self):
        return self._destination.is_change_zoom()

    @property
    def left(self):
        return self._destination.left()

    @property
    def page_number(self):
        return self._destination.page_number()

    @property
    def right(self):
        return self._destination.right()

    @property
    def top(self):
        return self._destination.top()

    @property
    def type(self):
        return self._destination.type()

    @property
    def zoom(self):
        return self._destination.zoom()
