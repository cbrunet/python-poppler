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

import functools

from poppler import _version


def version():
    return _version.version_major(), _version.version_minor(), _version.version_micro()


def major():
    return _version.version_major()


def minor():
    return _version.version_minor()


def micro():
    return _version.version_micro()


def string():
    return _version.version_string()


def ensure_version(maj, min):
    def wrapper(fct):
        @functools.wraps(fct)
        def wrapped(*args, **kwargs):
            if version() < (maj, min, 0):
                raise NotImplementedError(
                    "This functionality requires at least Poppler version {}".format(
                        ".".join(map(str, (maj, min, 0)))
                    )
                )
            return fct(*args, **kwargs)

        return wrapped

    return wrapper
