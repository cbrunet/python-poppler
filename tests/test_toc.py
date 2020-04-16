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


def test_toc_root(sample_document):
    toc = sample_document.create_toc()

    assert toc is not None
    assert toc.root.is_open
    assert toc.root.title == ""


def test_toc_children(sample_document):
    toc = sample_document.create_toc()
    children = toc.root.children()

    assert len(children) == 3
    assert not children[0].is_open
    assert children[0].title == "Outline"


def test_toc_iter(sample_document):
    toc = sample_document.create_toc()
    it = iter(toc.root)
    for _ in range(3):
        c = next(it)

    assert c.title == "Transitions Tests"

    with pytest.raises(StopIteration):
        next(it)
