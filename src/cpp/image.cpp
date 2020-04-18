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
#include <poppler/cpp/poppler-image.h>
#include <poppler/cpp/poppler-rectangle.h>

namespace py = pybind11;

namespace poppler
{

    void set_data(image& img, char* data)
    {
        char* img_data = img.data();
        img_data = data;
    }

    py::bytes data(image& img)
    {
        char* img_data = img.data();
        return py::bytes(img_data);
    }

PYBIND11_MODULE(image, m)
{
    py::enum_<image::format_enum>(m, "format_enum")
        .value("invalid", image::format_enum::format_invalid)
        .value("mono", image::format_enum::format_mono)
        .value("rgb24", image::format_enum::format_rgb24)
        .value("argb32", image::format_enum::format_argb32)
#if HAS_VERSION(0, 65)
        .value("gray8", image::format_enum::format_gray8)
        .value("bgr24", image::format_enum::format_bgr24)
#endif
        .export_values();

    py::class_<image>(m, "image")
        .def(py::init<>())
        .def(py::init<char*, int, int, image::format_enum>(), py::arg("idata"), py::arg("iwidth"), py::arg("iheight"), py::arg("iformat"))
        .def(py::init<int, int, image::format_enum>(), py::arg("iwidth"), py::arg("iheight"), py::arg("iformat"))
        .def("bytes_per_row", &image::bytes_per_row)
        // .def("const_data", &image::const_data)
        .def("copy", &image::copy, py::arg("rect")=rect())
        .def("data", &data)
        .def("set_data", &set_data)
        .def("format", &image::format)
        .def("height", &image::height)
        .def("is_valid", &image::is_valid)
        .def("save", &image::save, py::arg("file_name"), py::arg("out_format"), py::arg("dpi")=-1)
        .def("width", &image::width)
        ;
    
    m.def("supported_image_formats", &image::image::supported_image_formats);
}

}