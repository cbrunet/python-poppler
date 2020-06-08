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

from poppler.image import Image
from poppler import PageRenderer


def test_invalid_image():
    image = Image()
    assert not image.is_valid
    assert image.format == image.Format.invalid


def test_supported_image_formats():
    formats = Image.supported_image_formats()
    assert "png" in formats
    assert "jpeg" in formats


def test_data_size(pdf_page):
    renderer = PageRenderer()
    image = renderer.render_page(pdf_page)
    data = image.data

    assert len(data) == image.bytes_per_row * image.height


def test_image_format_to_str():
    assert str(Image.Format.argb32) == "BGRA"
    assert str(Image.Format.invalid) == ""


def test_image_memory_view(pdf_page):
    renderer = PageRenderer()
    image = renderer.render_page(pdf_page)

    v = image.memoryview()

    assert v.ndim == 3
    assert v.shape == (image.height, image.width, 4)
    assert v.contiguous is True
    assert v.tobytes() == image.data
