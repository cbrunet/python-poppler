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
#include <poppler-page-renderer.h>
#include <poppler-global.h>
#include <poppler-image.h>
#include <poppler-page.h>

namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(page_renderer, m)
{
    py::module::import("poppler.cpp.global_");
    py::module::import("poppler.cpp.image");
    py::module::import("poppler.cpp.page");

#if HAS_VERSION(0, 65)
    py::enum_<page_renderer::line_mode_enum>(m, "line_mode_enum")
        .value("default", page_renderer::line_mode_enum::line_default)
        .value("solid", page_renderer::line_mode_enum::line_solid)
        .value("shape ", page_renderer::line_mode_enum::line_shape)
        .export_values();
#endif

    py::enum_<page_renderer::render_hint>(m, "render_hint", py::arithmetic())
        .value("antialiasing", page_renderer::render_hint::antialiasing)
        .value("text_antialiasing", page_renderer::render_hint::text_antialiasing)
        .value("text_hinting", page_renderer::render_hint::text_hinting)
        .export_values();

    py::class_<page_renderer>(m, "page_renderer")
        .def(py::init<>())
#if HAS_VERSION(0, 65)
        .def("image_format", &page_renderer::image_format)
        .def("line_mode", &page_renderer::line_mode)
#endif
        .def("paper_color", &page_renderer::paper_color)
        .def("render_hints", &page_renderer::render_hints)
        .def("render_page", &page_renderer::render_page, py::arg("p"), py::arg("xres") = 72.0, py::arg("yres") = 72.0, py::arg("x") = -1, py::arg("y") = -1, py::arg("w") = -1, py::arg("h") = -1, py::arg("rotate") = rotation_enum::rotate_0)
#if HAS_VERSION(0, 65)
        .def("set_image_format", &page_renderer::set_image_format, py::arg("format"))
        .def("set_line_mode", &page_renderer::set_line_mode, py::arg("mode"))
#endif
        .def("set_paper_color", &page_renderer::set_paper_color, py::arg("color"))
        .def("set_render_hint", &page_renderer::set_render_hint, py::arg("hint"), py::arg("on") = true)
        .def("set_render_hints", &page_renderer::set_render_hints, py::arg("hints"));

    m.def("can_render", &page_renderer::can_render);
}

} // namespace poppler
