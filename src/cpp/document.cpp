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
#include <poppler/cpp/poppler-document.h>

namespace py = pybind11;

namespace poppler
{

py::object pdf_id(const document& doc)
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

py::tuple pdf_version(const document& doc)
{
    int major, minor;
    doc.get_pdf_version(&major, &minor);
    return py::make_tuple(major, minor);
}

PYBIND11_MODULE(_document, m)
{
    py::module::import("poppler._global");

    py::class_<document>(m, "document")
        // create_destination_map
        // create_font_iterator
        // create_page
        // create_toc
        // embedded_files
        // fonts
        .def("get_author", &document::get_author)
        .def("get_creation_date", &document::get_creation_date)
        .def("get_creator", &document::get_creator)
        .def("get_keywords", &document::get_keywords)
        .def("get_modification_date", &document::get_modification_date)
        .def("get_pdf_id", &pdf_id)
        .def("get_pdf_version", &pdf_version)
        .def("get_producer", &document::get_producer)
        .def("get_subject", &document::get_subject)
        .def("get_title", &document::get_title)
        .def("has_embedded_files", &document::has_embedded_files)
        .def("has_permission", &document::has_permission, py::arg("which"))
        .def("info_date", &document::info_date, py::arg("key"))
        .def("info_key", &document::info_key, py::arg("key"))
        .def("info_keys", &document::info_keys)
        .def("is_encrypted", &document::is_encrypted)
        .def("is_linearized", &document::is_linearized)
        .def("is_locked", &document::is_locked)
        .def("metadata", &document::metadata)
        // page_mode
        .def("pages", &document::pages)
        .def("remove_info", &document::remove_info)
        // save
        // save_a_copy
        .def("set_author", &document::set_author, py::arg("author"))
        .def("set_creation_date", &document::set_creation_date, py::arg("creation_date"))
        .def("set_creator", &document::set_creator, py::arg("creator"))
        .def("set_info_date", &document::set_info_date, py::arg("key"), py::arg("val"))
        .def("set_info_key", &document::set_info_key, py::arg("key"), py::arg("val"))
        .def("set_keywords", &document::set_keywords, py::arg("keywords"))
        .def("set_modification_date", &document::set_modification_date, py::arg("modification_date"))
        .def("set_producer", &document::set_producer, py::arg("producer"))
        .def("set_subject", &document::set_subject, py::arg("subject"))
        .def("set_title", &document::set_title, py::arg("title"))
        // unlock
        ;

    // m.def("load_from_data", &document::load_from_data, py::arg("file_data"), py::arg("owner_password")="", py::arg("user_password")="");
    m.def("load_from_file", &document::load_from_file, py::arg("file_name"), py::arg("owner_password")="", py::arg("user_password")="");
    // m.def("load_from_raw_data", &document::load_from_raw_data);

}

} // namespace poppler