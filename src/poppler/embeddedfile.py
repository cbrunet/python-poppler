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

from poppler.utilities import from_time_type


class EmbeddedFile:
    def __init__(self, file):
        self._file = file

    @property
    def checksum(self):
        return self._file.checksum()

    @property
    def creation_date(self):
        return from_time_type(self._file.creation_date())

    @property
    def data(self):
        return self._file.data()

    @property
    def description(self):
        return str(self._file.description())

    @property
    def is_valid(self):
        return self._file_is_valid()

    @property
    def mime_type(self):
        return self._file.mime_type()

    @property
    def modification_date(self):
        return from_time_type(self._file.modification_date())

    @property
    def name(self):
        return self._file.name()

    @property
    def size(self):
        return self._file.size()
