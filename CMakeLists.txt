cmake_minimum_required(VERSION 3.6)
project(python-poppler)

list(APPEND Targets "version" "rectangle" "image" "document" "page")
list(APPEND Targets "page_renderer" "page_transition")
list(APPEND Targets "embedded_file" "destination" "toc" "font")


# find_package(pybind11)
add_subdirectory(pybind11)


find_package(PkgConfig REQUIRED)
pkg_check_modules(POPPLERCPP REQUIRED IMPORTED_TARGET poppler-cpp>=0.62.0)
pkg_check_modules(POPPLER REQUIRED IMPORTED_TARGET poppler>=0.62.0)

add_library(global_ MODULE src/cpp/global.cpp)
target_include_directories(global_ BEFORE PRIVATE ${POPPLER_INCLUDEDIR})
target_link_libraries(global_ PRIVATE pybind11::module PkgConfig::POPPLER PkgConfig::POPPLERCPP )
set_target_properties(global_ PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
                                         SUFFIX "${PYTHON_MODULE_EXTENSION}")

foreach (Target ${Targets})
    add_library(${Target} MODULE src/cpp/${Target}.cpp)
    target_include_directories(${Target} BEFORE PRIVATE ${POPPLER_INCLUDEDIR})
    target_link_libraries(${Target} PRIVATE pybind11::module PkgConfig::POPPLER PkgConfig::POPPLERCPP )
    set_target_properties(${Target} PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
                                               SUFFIX "${PYTHON_MODULE_EXTENSION}")
endforeach ()
