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
#if HAS_VERSION(0, 74)
#include <poppler-destination.h>
#endif
#include <poppler-document.h>
#include <poppler-embedded-file.h>
#include <poppler-font.h>
#include <poppler-page.h>
#include <poppler-toc.h>

#ifdef _MSC_VER
#include <BaseTsd.h>
typedef SSIZE_T ssize_t;
#endif

namespace py = pybind11;

namespace poppler
{

namespace binding
{
py::object pdf_id(const document &doc)
{
    std::string permanent_id, update_id;
    bool result = doc.get_pdf_id(&permanent_id, &update_id);
    if (result)
    {
        return py::make_tuple(permanent_id, update_id);
    }
    else
    {
        return py::object();
    }
}

py::tuple pdf_version(const document &doc)
{
    int major, minor;
    doc.get_pdf_version(&major, &minor);
    return py::make_tuple(major, minor);
}

document *load_from_data(py::bytes file_data, const std::string &owner_password = std::string(), const std::string &user_password = std::string())
{
    char *buffer;
    ssize_t length;
    if (PYBIND11_BYTES_AS_STRING_AND_SIZE(file_data.ptr(), &buffer, &length))
        pybind11::pybind11_fail("Unable to extract bytes contents!");
    return document::load_from_raw_data(buffer, length, owner_password, user_password);
}

} // namespace binding

PYBIND11_MODULE(document, m)
{
#if HAS_VERSION(0, 74)
    py::module::import("poppler.cpp.destination");
#endif
    py::module::import("poppler.cpp.embedded_file");
    py::module::import("poppler.cpp.font");
    py::module::import("poppler.cpp.global_");
    py::module::import("poppler.cpp.page");
    py::module::import("poppler.cpp.toc");

    py::enum_<document::page_layout_enum>(m, "page_layout_enum")
        .value("no_layout", document::page_layout_enum::no_layout)
        .value("single_page", document::page_layout_enum::single_page)
        .value("one_column", document::page_layout_enum::one_column)
        .value("two_column_left", document::page_layout_enum::two_column_left)
        .value("two_column_right", document::page_layout_enum::two_column_right)
        .value("two_page_left", document::page_layout_enum::two_page_left)
        .value("two_page_right", document::page_layout_enum::two_page_right)
        .export_values();

    py::enum_<document::page_mode_enum>(m, "page_mode_enum")
        .value("use_none", document::page_mode_enum::use_none)
        .value("use_outlines", document::page_mode_enum::use_outlines)
        .value("use_thumbs", document::page_mode_enum::use_thumbs)
        .value("fullscreen", document::page_mode_enum::fullscreen)
        .value("use_oc", document::page_mode_enum::use_oc)
        .value("use_attach", document::page_mode_enum::use_attach)
        .export_values();

    py::class_<document>(m, "document")
#if HAS_VERSION(0, 74)
        .def("create_destination_map", &document::create_destination_map)
#endif
        .def("create_font_iterator", &document::create_font_iterator, py::arg("start_page")=0)
        .def("create_page", (page * (document::*)(int)const) & document::create_page, py::arg("index"))
        .def("create_page", (page * (document::*)(const ustring &)const) & document::create_page, py::arg("label"))
        .def("create_toc", &document::create_toc)
        .def("embedded_files", &document::embedded_files)
        .def("fonts", &document::fonts)
#if HAS_VERSION(0, 46)
        .def("get_author", &document::get_author)
        .def("get_creator", &document::get_creator)
        .def("get_keywords", &document::get_keywords)
#if HAS_VERSION(22, 5)
        .def("get_creation_date", &document::get_creation_date_t)
        .def("get_modification_date", &document::get_modification_date_t)
#else
        .def("get_creation_date", &document::get_creation_date)
        .def("get_modification_date", &document::get_modification_date)
#endif
#endif
#if HAS_VERSION(22, 5)
        .def("info_date", &document::info_date_t, py::arg("key"))
#else
        .def("info_date", &document::info_date, py::arg("key"))
#endif
        .def("get_pdf_id", &binding::pdf_id)
        .def("get_pdf_version", &binding::pdf_version)
#if HAS_VERSION(0, 46)
        .def("get_producer", &document::get_producer)
        .def("get_subject", &document::get_subject)
        .def("get_title", &document::get_title)
#endif
        .def("has_embedded_files", &document::has_embedded_files)
        .def("has_permission", &document::has_permission, py::arg("which"))
        .def("info_key", &document::info_key, py::arg("key"))
        .def("info_keys", &document::info_keys)
        .def("is_encrypted", &document::is_encrypted)
        .def("is_linearized", &document::is_linearized)
        .def("is_locked", &document::is_locked)
        .def("metadata", &document::metadata)
        .def("page_layout", &document::page_layout)
        .def("page_mode", &document::page_mode)
        .def("pages", &document::pages)
#if HAS_VERSION(0, 46)
        .def("remove_info", &document::remove_info)
        .def("save", &document::save, py::arg("file_name"))
        .def("save_a_copy", &document::save_a_copy, py::arg("file_name"))
        .def("set_author", &document::set_author, py::arg("author"))
    #if HAS_VERSION(22, 5)
        .def("set_creation_date", &document::set_creation_date_t, py::arg("creation_date"))
        .def("set_modification_date", &document::set_modification_date_t, py::arg("modification_date"))
        .def("set_info_date", &document::set_info_date_t, py::arg("key"), py::arg("val"))
    #else
        .def("set_creation_date", &document::set_creation_date, py::arg("creation_date"))
        .def("set_modification_date", &document::set_modification_date, py::arg("modification_date"))
        .def("set_info_date", &document::set_info_date, py::arg("key"), py::arg("val"))
    #endif
        .def("set_creator", &document::set_creator, py::arg("creator"))
        .def("set_info_key", &document::set_info_key, py::arg("key"), py::arg("val"))
        .def("set_keywords", &document::set_keywords, py::arg("keywords"))
        .def("set_producer", &document::set_producer, py::arg("producer"))
        .def("set_subject", &document::set_subject, py::arg("subject"))
        .def("set_title", &document::set_title, py::arg("title"))
#endif
        .def("unlock", &document::unlock, py::arg("owner_password"), py::arg("user_password"));

    m.def("load_from_data", &binding::load_from_data, py::arg("file_data"), py::arg("owner_password") = "", py::arg("user_password") = "");
    m.def("load_from_file", &document::load_from_file, py::arg("file_name"), py::arg("owner_password") = "", py::arg("user_password") = "");
}

} // namespace poppler