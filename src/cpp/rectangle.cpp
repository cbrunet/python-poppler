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
#include <poppler-rectangle.h>

namespace py = pybind11;

namespace poppler
{


PYBIND11_MODULE(rectangle, m)
{
    py::class_<rect>(m, "rect")
        .def(py::init<int, int, int, int>(), py::arg("x"), py::arg("y"), py::arg("w"), py::arg("h"))
        .def("bottom", &rect::bottom)
        .def("height", &rect::height)
        .def("is_empty", &rect::is_empty)
        .def("left", &rect::left)
        .def("right", &rect::right)
        .def("set_bottom", &rect::set_bottom, py::arg("value"))
        .def("set_left", &rect::set_left, py::arg("value"))
        .def("set_right", &rect::set_right, py::arg("value"))
        .def("set_top", &rect::set_top, py::arg("value"))
        .def("top", &rect::top)
        .def("width", &rect::width)
        .def("x", &rect::x)
        .def("y", &rect::y)
        ;
    
    py::class_<rectf>(m, "rectf")
        .def(py::init<double, double, double, double>(), py::arg("x"), py::arg("y"), py::arg("w"), py::arg("h"))
        .def("bottom", &rectf::bottom)
        .def("height", &rectf::height)
        .def("is_empty", &rectf::is_empty)
        .def("left", &rectf::left)
        .def("right", &rectf::right)
        .def("set_bottom", &rectf::set_bottom, py::arg("value"))
        .def("set_left", &rectf::set_left, py::arg("value"))
        .def("set_right", &rectf::set_right, py::arg("value"))
        .def("set_top", &rectf::set_top, py::arg("value"))
        .def("top", &rectf::top)
        .def("width", &rectf::width)
        .def("x", &rectf::x)
        .def("y", &rectf::y)
        ;
}

}
