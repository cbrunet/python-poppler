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

from poppler import version

if version() >= (0, 74, 0):
    from poppler import DestinationType

pytestmark = pytest.mark.skipif(
    version() < (0, 74, 0), reason="Requires at least Poppler 0.74.0"
)


def test_destination_map_keys(sample_document):
    destinations = sample_document.create_destination_map()

    assert "Doc-Start" in destinations
    assert "Navigation1" in destinations
    assert "Outline0.1" in destinations
    assert "page.1" in destinations


def test_destination_map_page(sample_document):
    destinations = sample_document.create_destination_map()

    for i in range(1, 10):
        k = f"page.{i}"
        assert destinations[k].page_number == i


def test_destination_map_properties(sample_document):
    destinations = sample_document.create_destination_map()
    destination = destinations["Outline0.1"]

    assert destination.bottom == 0.0
    assert destination.top == 245.3
    assert destination.left == 28.346
    assert destination.right == 0.0
    assert destination.zoom == 0.0
    assert destination.type == DestinationType.xyz
    assert destination.is_change_left
    assert destination.is_change_top
    assert not destination.is_change_zoom
    assert destination.page_number == 2
