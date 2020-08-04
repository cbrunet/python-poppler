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
#include <poppler-embedded-file.h>

namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(embedded_file, m)
{
    py::class_<embedded_file>(m, "embedded_file")
        .def("checksum", &embedded_file::checksum)
        .def("creation_date", &embedded_file::creation_date)
        .def("data", &embedded_file::data)
        .def("description", &embedded_file::description)
        .def("is_valid", &embedded_file::is_valid)
        .def("mime_type", &embedded_file::mime_type)
        .def("modification_data", &embedded_file::modification_date)
        .def("name", &embedded_file::name)
        .def("size", &embedded_file::size)
        ;
}

}