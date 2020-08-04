/* poppler-python: python binding to the poppler-cpp pdf lib
 * Copyright (C) 2020, Charles Brunet <charles@cbrunet.net>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <poppler-font.h>

namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(font, m)
{
    py::enum_<font_info::type_enum>(m, "type_enum")
        .value("unknown", font_info::type_enum::unknown)
        .value("type1", font_info::type_enum::type1)
        .value("type1c", font_info::type_enum::type1c)
        .value("type1c_ot", font_info::type_enum::type1c_ot)
        .value("type3", font_info::type_enum::type3)
        .value("truetype", font_info::type_enum::truetype)
        .value("truetype_ot", font_info::type_enum::truetype_ot)
        .value("cid_type0", font_info::type_enum::cid_type0)
        .value("cid_type0c", font_info::type_enum::cid_type0c)
        .value("cid_type0c_ot", font_info::type_enum::cid_type0c_ot)
        .value("cid_truetype", font_info::type_enum::cid_truetype)
        .value("cid_truetype_ot", font_info::type_enum::cid_truetype_ot)
        .export_values();

    py::class_<font_info>(m, "font_info")
        .def(py::init<>())
        .def("file", &font_info::file)
        .def("is_embedded", &font_info::is_embedded)
        .def("is_subset", &font_info::is_subset)
        .def("name", &font_info::name)
        .def("type", &font_info::type)
        ;

    py::class_<font_iterator>(m, "font_iterator")
        .def("current_page", &font_iterator::current_page)
        .def("has_next", &font_iterator::has_next)
        .def("next_", &font_iterator::next)
        ;
}

} // namespace poppler
