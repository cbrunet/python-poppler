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

from datetime import datetime
import functools

from poppler.cpp.version import version_major, version_minor, version_micro


def from_time_type(timestamp):
    if timestamp == 2 ** 32 - 1:
        return None
    return datetime.fromtimestamp(timestamp)


def to_time_type(date_time):
    return int(date_time.timestamp()) if date_time else 2 ** 32 - 1


def version():
    return version_major(), version_minor(), version_micro()


def since(maj, min):
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
