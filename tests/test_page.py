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

import pytest

from poppler.page import Page
from poppler.rectangle import Rectangle
from poppler import version
from poppler import CaseSensitivity


def test_page_duration(pdf_page):
    assert pdf_page.duration == -1.0


@pytest.mark.skipif(version() < (0, 46, 0), reason="Requires at least Poppler 0.46.0")
def test_page_label(pdf_page):
    assert pdf_page.label == "1"


def test_page_orientation(pdf_page):
    assert pdf_page.orientation == Page.Orientation.portrait


def test_page_rect(pdf_page):
    r = pdf_page.page_rect()
    assert r.as_tuple() == (0.0, 0.0, 612.0, 792.0)


@pytest.mark.parametrize(
    "box",
    [
        Page.PageBox.media_box,
        Page.PageBox.crop_box,
        Page.PageBox.bleed_box,
        Page.PageBox.trim_box,
        Page.PageBox.art_box,
    ],
)
def test_page_rect_box(pdf_page, box):
    r = pdf_page.page_rect(box)
    assert r.as_tuple() == (0.0, 0.0, 612.0, 792.0)


def test_text(pdf_page):
    text = pdf_page.text()
    if version() < (0, 46, 0):
        expected = "Page "
    elif version() < (0, 88, 0):
        expected = "Page 1"
    else:
        expected = "Page 1\n\x0c"
    assert text == expected


@pytest.mark.skipif(version() < (0, 63, 0), reason="Requires at least Poppler 0.63.0")
def test_text_list(pdf_page):
    text_list = pdf_page.text_list()
    assert len(text_list) == 2

    text_box = text_list[0]
    assert text_box.text == "Page"
    assert pytest.approx(text_box.bbox.as_tuple(), abs=0.1) == (56.8, 57.2, 80.1, 70.5)
    if version() >= (0, 68, 0):
        assert text_box.rotation == 0
    assert pytest.approx(text_box.char_bbox(0).as_tuple(), abs=0.1) == (
        56.8,
        57.2,
        63.5,
        70.5,
    )
    assert text_box.has_space_after is True


@pytest.mark.xfail(version() <= (0, 62, 0), reason="Is it a bug in Poppler 0.62?")
def test_search_found(pdf_page):
    r = Rectangle(0.0, 0.0, 0.0, 0.0)
    result = pdf_page.search(
        "Page", r, Page.SearchDirection.from_top, CaseSensitivity.case_sensitive
    )

    assert isinstance(result, Rectangle)
    assert pytest.approx(result.as_tuple(), abs=0.1) == (56.8, 57.2, 80.1, 70.5)


def test_search_not_found(pdf_page):
    r = Rectangle(0.0, 0.0, 612.0, 792.0)
    result = pdf_page.search(
        "Stchroumph", r, Page.SearchDirection.from_top, CaseSensitivity.case_sensitive
    )

    assert result is None


def test_page_transition(pdf_page):
    assert pdf_page.transition() is None


@pytest.mark.skipif(version() < (0, 89, 0), reason="Requires at least Poppler 0.89.0")
def test_text_box_font_info(pdf_page):
    boxes = pdf_page.text_list(pdf_page.TextListOption.text_list_include_font)
    box = boxes[0]

    assert box.has_font_info
    assert box.get_font_name().endswith("LiberationSerif")
    assert pytest.approx(box.get_font_size(), abs=0.1) == 12.0
    assert box.get_wmode() == box.WritingMode.horizontal_wmode
