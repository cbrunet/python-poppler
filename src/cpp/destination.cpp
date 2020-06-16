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

#include "version.h"
#include <pybind11/pybind11.h>
#if HAS_VERSION(0, 74)
#include <poppler-destination.h>
#endif

namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(destination, m)
{
#if HAS_VERSION(0, 74)
    py::enum_<destination::type_enum>(m, "type_enum")
        .value("unknown", destination::type_enum::unknown)
        .value("xyz", destination::type_enum::xyz)
        .value("fit", destination::type_enum::fit)
        .value("fit_h", destination::type_enum::fit_h)
        .value("fit_v", destination::type_enum::fit_v)
        .value("fit_r", destination::type_enum::fit_r)
        .value("fit_b", destination::type_enum::fit_b)
        .value("fit_b_h", destination::type_enum::fit_b_h)
        .value("fit_b_v", destination::type_enum::fit_b_v)
        .export_values();

    py::class_<destination>(m, "destination")
        .def("bottom", &destination::bottom)
        .def("is_change_left", &destination::is_change_left)
        .def("is_change_top", &destination::is_change_top)
        .def("is_change_zoom", &destination::is_change_zoom)
        .def("left", &destination::left)
        .def("page_number", &destination::page_number)
        .def("right", &destination::right)
        .def("top", &destination::top)
        .def("type", &destination::type)
        .def("zoom", &destination::zoom);
#endif
}

} // namespace poppler