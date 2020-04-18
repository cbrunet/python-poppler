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

from poppler import TransitionType as Type
from poppler import Alignment, Direction


@pytest.mark.parametrize(
    "page_num,transition_type,alignment,direction",
    [
        (3, Type.blinds, Alignment.horizontal, Direction.inward),
        (4, Type.blinds, Alignment.vertical, Direction.inward),
        (5, Type.box, Alignment.horizontal, Direction.inward),
        (6, Type.box, Alignment.horizontal, Direction.outward),
        (7, Type.cover, Alignment.horizontal, Direction.inward),
        (8, Type.dissolve, Alignment.horizontal, Direction.inward),
        (9, Type.fade, Alignment.horizontal, Direction.inward),
        (10, Type.glitter, Alignment.horizontal, Direction.inward),
        (11, Type.push, Alignment.horizontal, Direction.inward),
        (12, Type.replace, Alignment.horizontal, Direction.inward),
        (13, Type.split, Alignment.vertical, Direction.inward),
        (14, Type.split, Alignment.vertical, Direction.outward),
        (15, Type.split, Alignment.horizontal, Direction.inward),
        (16, Type.split, Alignment.horizontal, Direction.outward),
        (17, Type.wipe, Alignment.horizontal, Direction.inward),
        (18, Type.uncover, Alignment.horizontal, Direction.inward),
    ],
)
def test_transition_type(
    sample_document, page_num, transition_type, alignment, direction
):
    page = sample_document.create_page(page_num)
    transition = page.transition()

    assert transition is not None
    assert transition.type == transition_type
    assert transition.alignment == alignment
    assert transition.direction == direction
    assert transition.is_rectangular is False
    assert transition.scale == 1.0


@pytest.mark.parametrize(
    "page_num,angle", [(7, 0), (10, 315), (11, 90), (17, 180), (18, 270)]
)
def test_transition_angle(sample_document, page_num, angle):
    page = sample_document.create_page(page_num)
    transition = page.transition()

    assert transition.angle == angle


@pytest.mark.parametrize("page_num,duration", [(3, 0), (4, 1), (5, 1), (6, 2), (7, 15)])
def test_transition_duration(sample_document, page_num, duration):
    page = sample_document.create_page(page_num)
    transition = page.transition()

    assert transition.duration == duration
