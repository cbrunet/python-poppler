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

from poppler.cpp import rectangle


class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0, poppler_object=None):
        if poppler_object:
            self._rect = poppler_object
        elif all(map(lambda i: isinstance(i, int), (x, y, w, h))):
            self._rect = rectangle.rect(int(x), int(y), int(w), int(h))
        else:
            self._rect = rectangle.rectf(float(x), float(y), float(w), float(h))

    @classmethod
    def from_object(cls, poppler_object):
        return cls(poppler_object=poppler_object)

    @property
    def x(self):
        return self._rect.x()

    @property
    def y(self):
        return self._rect.y()

    def is_empty(self):
        return self._rect.is_empty()

    @property
    def height(self):
        return self._rect.height()

    @property
    def width(self):
        return self._rect.width()

    @property
    def bottom(self):
        return self._rect.bottom()

    @bottom.setter
    def bottom(self, value):
        self._rect.set_bottom(value)

    @property
    def left(self):
        return self._rect.left()

    @left.setter
    def left(self, value):
        self._rect.set_left(value)

    @property
    def right(self):
        return self._rect.right()

    @right.setter
    def right(self, value):
        self._rect.set_right(value)

    @property
    def top(self):
        return self._rect.top()

    @top.setter
    def top(self, value):
        self._rect.set_top(value)

    def as_tuple(self):
        return (self.left, self.top, self.right, self.bottom)
