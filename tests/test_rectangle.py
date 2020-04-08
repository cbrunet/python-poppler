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

from poppler.rectangle import Rectangle


def test_init_from_int():
    x, y, w, h = 10, 12, 30, 40
    rectangle = Rectangle(x, y, w, h)

    assert rectangle.x == x
    assert rectangle.y == y
    assert rectangle.width == w
    assert rectangle.height == h


def test_init_from_float():
    x, y, w, h = 5.5, 10.1, 20.2, 30.3
    rectangle = Rectangle(x, y, w, h)

    assert pytest.approx(rectangle.x, 0.0001) == x
    assert pytest.approx(rectangle.y, 0.0001) == y
    assert pytest.approx(rectangle.width, 0.0001) == w
    assert pytest.approx(rectangle.height, 0.0001) == h


def test_init_default():
    rectangle = Rectangle()
    assert rectangle.is_empty()


def test_getters():
    rectangle = Rectangle(10, 20, 30, 40)
    assert rectangle.left == 10
    assert rectangle.right == 40
    assert rectangle.top == 20
    assert rectangle.bottom == 60


def test_setters():
    rectangle = Rectangle()
    rectangle.left = 10
    rectangle.right = 20
    rectangle.top = 30
    rectangle.bottom = 50

    assert rectangle.x == 10
    assert rectangle.y == 30
    assert rectangle.width == 10
    assert rectangle.height == 20


def test_rect_as_tuple():
    rectangle = Rectangle(10, 20, 30, 40)
    t = rectangle.as_tuple()
    assert t == (10, 20, 40, 60)
