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

from poppler._global import set_data_dir
from poppler._utilities import version
from poppler._version import version_string
from poppler.document import load, load_from_file, load_from_data
from poppler.pagerenderer import PageRenderer
from poppler.rectangle import Rectangle

from poppler._document import page_layout_enum as PageLayout
from poppler._document import page_mode_enum as PageMode

from poppler._font import type_enum as FontType

from poppler._global import case_sensitivity_enum as CaseSensitivity
from poppler._global import page_box_enum as PageBox
from poppler._global import permission_enum as Permission
from poppler._global import rotation_enum as Rotation

from poppler._image import format_enum as ImageFormat

from poppler._page import orientation_enum as PageOrientation
from poppler._page import search_direction_enum as SearchDirection
from poppler._page import text_layout_enum as TextLayout

from poppler._page_renderer import render_hint as RenderHint

from poppler._page_transition import alignment_enum as Alignment
from poppler._page_transition import direction_enum as Direction
from poppler._page_transition import type_enum as TransitionType


__all__ = [
    "version",
    "version_string",
    "set_data_dir",
    "load",
    "load_from_data",
    "load_from_file",
    "PageRenderer",
    "Rectangle",
    "Alignment",
    "CaseSensitivity",
    "Direction",
    "FontType",
    "ImageFormat",
    "PageBox",
    "PageLayout",
    "PageMode",
    "PageOrientation",
    "Permission",
    "RenderHint",
    "Rotation",
    "SearchDirection",
    "TextLayout",
    "TransitionType",
]

if version() >= (0, 65, 0):
    from poppler._page_renderer import line_mode_enum as LineMode  # noqa/

    __all__.append("LineMode")

if version() >= (0, 74, 0):
    from poppler._destination import type_enum as DestinationType  # noqa

    __all__.append("DestinationType")
