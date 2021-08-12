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
#include <pybind11/stl.h>
#include <poppler-global.h>
#include <poppler-page.h>
#include <poppler-page-transition.h>
#include <poppler-rectangle.h>

namespace py = pybind11;

namespace poppler
{
py::tuple search(const page &p, const ustring &text, rectf &r, page::search_direction_enum direction, case_sensitivity_enum case_sensitivity, rotation_enum rotation = rotation_enum::rotate_0)
{
    bool result = p.search(text, r, direction, case_sensitivity, rotation);
    return py::make_tuple(result, r);
}

PYBIND11_MODULE(page, m)
{
    py::module::import("poppler.cpp.global_");
    py::module::import("poppler.cpp.page_transition");
    py::module::import("poppler.cpp.rectangle");

    py::enum_<page::orientation_enum>(m, "orientation_enum")
        .value("landscape", page::orientation_enum::landscape)
        .value("portrait", page::orientation_enum::portrait)
        .value("seascape", page::orientation_enum::seascape)
        .value("upside_down", page::orientation_enum::upside_down)
        .export_values();

    py::enum_<page::text_layout_enum>(m, "text_layout_enum")
        .value("physical_layout", page::text_layout_enum::physical_layout)
        .value("raw_order_layout", page::text_layout_enum::raw_order_layout)
#if HAS_VERSION(0, 88)
        .value("non_raw_non_physical_layout", page::text_layout_enum::non_raw_non_physical_layout)
#endif
        .export_values();

    py::enum_<page::search_direction_enum>(m, "search_direction_enum")
        .value("from_top", page::search_direction_enum::search_from_top)
        .value("next_result", page::search_direction_enum::search_next_result)
        .value("previous_result", page::search_direction_enum::search_previous_result)
        .export_values();

#if HAS_VERSION(0, 89)
    py::enum_<text_box::writing_mode_enum>(m, "writing_mode_enum")
        .value("invalid_wmode", text_box::writing_mode_enum::invalid_wmode)
        .value("horizontal_wmode", text_box::writing_mode_enum::horizontal_wmode)
        .value("vertical_wmode", text_box::writing_mode_enum::vertical_wmode)
        .export_values();
#endif

#if HAS_VERSION(0, 63)
    py::class_<text_box>(m, "text_box")
        .def("text", &text_box::text)
        .def("bbox", &text_box::bbox)
#if HAS_VERSION(0, 68)
        .def("rotation", &text_box::rotation)
#endif
        .def("char_bbox", &text_box::char_bbox, py::arg("i"))
        .def("has_space_after", &text_box::has_space_after)
#endif
#if HAS_VERSION(0, 89)
        .def("get_font_name", &text_box::get_font_name, py::arg("i")=0)
        .def("get_font_size", &text_box::get_font_size)
        .def("get_wmode", &text_box::get_wmode, py::arg("i")=0)
        .def("has_font_info", &text_box::has_font_info)
#endif
        ;

#if HAS_VERSION(0, 89)
    py::enum_<page::text_list_option_enum>(m, "text_list_option_enum")
        .value("text_list_include_font", page::text_list_option_enum::text_list_include_font)
        .export_values();
#endif

    py::class_<page>(m, "page")
        .def("duration", &page::duration)
        .def("label", &page::label)
        .def("orientation", &page::orientation)
        .def("page_rect", &page::page_rect, py::arg("box") = page_box_enum::crop_box)
        .def("search", &search, py::arg("text"), py::arg("r"), py::arg("direction"), py::arg("case_sensitivity"), py::arg("rotation") = rotation_enum::rotate_0)
        .def("text", (ustring(page::*)(const rectf &, page::text_layout_enum) const) & page::text, py::arg("rect"), py::arg("layout_mode"))
        .def("text", (ustring(page::*)(const rectf &) const) & page::text, py::arg("rect") = rectf())
#if HAS_VERSION(0, 63)
        .def("text_list", (std::vector<text_box>(page::*)() const) & page::text_list)
#endif
#if HAS_VERSION(0, 89)
        .def("text_list", (std::vector<text_box>(page::*)(int) const) & page::text_list, py::arg("opt_flag"))
#endif
        .def("transition", &page::transition, py::return_value_policy::reference);
}

} // namespace poppler
