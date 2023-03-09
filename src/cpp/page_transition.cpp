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
#include <poppler-page-transition.h>

namespace py = pybind11;

namespace poppler
{

PYBIND11_MODULE(page_transition, m)
{
    py::enum_<page_transition::alignment_enum>(m, "alignment_enum")
        .value("horizontal", page_transition::alignment_enum::horizontal)
        .value("vertical", page_transition::alignment_enum::vertical)
        .export_values();

    py::enum_<page_transition::direction_enum>(m, "direction_enum")
        .value("inward", page_transition::direction_enum::inward)
        .value("outward", page_transition::direction_enum::outward)
        .export_values();

    py::enum_<page_transition::type_enum>(m, "type_enum")
        .value("replace", page_transition::type_enum::replace)
        .value("split", page_transition::type_enum::split)
        .value("blinds", page_transition::type_enum::blinds)
        .value("box", page_transition::type_enum::box)
        .value("wipe", page_transition::type_enum::wipe)
        .value("dissolve", page_transition::type_enum::dissolve)
        .value("glitter", page_transition::type_enum::glitter)
        .value("fly", page_transition::type_enum::fly)
        .value("push", page_transition::type_enum::push)
        .value("cover", page_transition::type_enum::cover)
        .value("uncover", page_transition::type_enum::uncover)
        .value("fade", page_transition::type_enum::fade)
        .export_values();

    py::class_<page_transition>(m, "page_transition")
        .def("alignment", &page_transition::alignment)
        .def("angle", &page_transition::angle)
        .def("direction", &page_transition::direction)
#if HAS_VERSION(22, 5)
        .def("duration", &page_transition::durationReal)
#else
        .def("duration", &page_transition::duration)
#endif
        .def("is_rectangular", &page_transition::is_rectangular)
        .def("scale", &page_transition::scale)
        .def("type", &page_transition::type)
        ;
}

}
