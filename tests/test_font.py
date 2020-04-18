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

from poppler.font import FontInfo, FontType


def test_invalid_font_info():
    font_info = FontInfo()

    assert font_info.type == FontType.unknown


def test_font_iterator(sample_document):
    font_iterator = sample_document.create_font_iterator()

    assert font_iterator.has_next
    assert font_iterator.current_page == 0

    fonts = font_iterator.next_()

    assert len(fonts) == 3
    assert font_iterator.current_page == 1


def test_font_iterator_interface(sample_document):
    font_iterator = sample_document.create_font_iterator()

    for i, (page, _) in enumerate(font_iterator):
        assert i == page


def test_font_info(sample_document):
    fonts = sample_document.fonts()
    font = fonts[0]

    assert font.file == ""
    assert font.is_embedded
    assert font.is_subset
    assert font.name == "SBNSFQ+CMSS8"
    assert font.type == FontType.type1
