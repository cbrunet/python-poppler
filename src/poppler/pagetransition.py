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


from poppler.cpp import page_transition


class PageTransition:

    Alignment = page_transition.alignment_enum
    Direction = page_transition.direction_enum
    Type = page_transition.type_enum

    def __init__(self, transition):
        self._transition = transition

    @property
    def alignment(self):
        return self._transition.alignment()

    @property
    def angle(self):
        return self._transition.angle()

    @property
    def direction(self):
        return self._transition.direction()

    @property
    def duration(self):
        return self._transition.duration()

    @property
    def is_rectangular(self):
        return self._transition.is_rectangular()

    @property
    def scale(self):
        return self._transition.scale()

    @property
    def type(self):
        return self._transition.type()
