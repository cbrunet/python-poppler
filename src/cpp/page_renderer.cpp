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
#include <poppler/cpp/poppler-page-renderer.h>
#include <poppler/cpp/poppler-global.h>
#include <poppler/cpp/poppler-image.h>
#include <poppler/cpp/poppler-page.h>


namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(_page_renderer, m)
{
    py::module::import("poppler._global");
    py::module::import("poppler._image");
    py::module::import("poppler._page");

    py::class_<page_renderer>(m, "page_renderer")
        .def(py::init<>())
        .def("render_page", &page_renderer::render_page, py::arg("p"), py::arg("xres")=72.0, py::arg("yres")=72.0, py::arg("x")=-1, py::arg("y")=-1, py::arg("w")=-1, py::arg("h")=-1, py::arg("rotate")=rotation_enum::rotate_0)
        ;

    m.def("can_render", &page_renderer::can_render);
}


}
