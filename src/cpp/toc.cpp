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
#include <poppler-global.h>
#include <poppler-toc.h>

namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(toc, m)
{
    py::module::import("poppler.cpp.global_");

    py::class_<toc_item>(m, "toc_item")
        .def("children", &toc_item::children)
        .def("__iter__", [](const toc_item &item) {
                return py::make_iterator(item.children_begin(), item.children_end());
            },
            py::keep_alive<0, 1>())
        .def("is_open", &toc_item::is_open)
        .def("title", &toc_item::title);

    py::class_<toc>(m, "toc")
        .def("root", &toc::root, py::return_value_policy::reference);
}

} // namespace poppler