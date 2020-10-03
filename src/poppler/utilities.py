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


"""This module contains utility functions that are not part of
poppler-cpp, but that helps interacting with it.
"""

from datetime import datetime
import functools

from poppler.cpp.version import version_major, version_minor, version_micro


def from_time_type(timestamp):
    """Convert a timestamp to a :class:`datetime.datetime` object.

    Args:
        timestamp (int): a positive integer, to be interpreted as 32 bits complement 2.

    Returns:
        Optional[datetime.datetime]: the date and time,
                                     or None if the timestamp is equivalent to -1.

    """
    if timestamp == 2 ** 32 - 1:
        return None
    return datetime.fromtimestamp(timestamp)


def to_time_type(date_time):
    """Convert a Python :class:`datetime.datetime` object
    to a timestamp compatible with poppler.

    Args:
        date_time (Optional[datetime.datetime]): the date and time, or None

    Returns:
        int: the timestamp

    """
    return int(date_time.timestamp()) if date_time else 2 ** 32 - 1


def version():
    """Get poppler version, as a tuple

    Returns:
        Tuple[int, int, int]: (major, minor, micro)

    """
    return version_major(), version_minor(), version_micro()


def since(major, minor):
    """Decorator used to mark the minimum required version of poppler
    needed to execute a function.

    If poppler version is lower than the specified version,
    it raises a NotImplementedError when called.

    Args:
        major (int): major version number
        minor (int): minor version number

    """
    def wrapper(fct):
        @functools.wraps(fct)
        def wrapped(*args, **kwargs):
            if version() < (major, minor, 0):
                raise NotImplementedError(
                    "This functionality requires at least Poppler version {}".format(
                        ".".join(map(str, (major, minor, 0)))
                    )
                )
            return fct(*args, **kwargs)

        return wrapped

    return wrapper
