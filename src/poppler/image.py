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

from poppler.cpp import image
from poppler.rectangle import Rectangle


class Image:

    Format = image.format_enum

    def __init__(
        self, width=0, height=0, iformat=Format.invalid, data=None, poppler_object=None
    ):
        if poppler_object is not None:
            self._image = poppler_object
        elif data is not None:
            self._image = image.image(data, width, height, iformat)
        elif width > 0:
            self._image = image.image(width, height, iformat)
        else:
            self._image = image.image()

    @classmethod
    def from_object(cls, poppler_object):
        return cls(poppler_object=poppler_object)

    @property
    def bytes_per_row(self):
        return self._image.bytes_per_row()

    @property
    def const_data(self):
        return self._image.data()

    def copy(self, rect=None):
        image = self._image.copy(rect or Rectangle()._rect)
        return Image.from_object(image)

    @property
    def data(self):
        return self._image.data()

    @data.setter
    def data(self, data):
        self._image.set_data(data)

    @property
    def format(self):
        return self._image.format()

    @property
    def height(self):
        return self._image.height()

    @property
    def is_valid(self):
        return self._image.is_valid()

    def save(self, file_name, out_format, dpi=-1):
        return self._image.save(str(file_name), out_format, dpi)

    @property
    def width(self):
        return self._image.width()

    def memoryview(self):
        return memoryview(self._image)

    @staticmethod
    def supported_image_formats():
        return image.supported_image_formats()
