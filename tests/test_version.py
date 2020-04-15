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


def test_versions():
    assert version.version() == (version.major(), version.minor(), version.micro())


def test_version_string():
    assert version.string() == ".".join(map(str, version.version()))


def test_ensure_version_fct():
    @version.ensure_version(99, 99)
    def fct():
        pass

    with pytest.raises(NotImplementedError):
        fct()


def test_ensure_version_cls():
    @version.ensure_version(99, 99)
    class cls:
        pass

    with pytest.raises(NotImplementedError):
        cls()
