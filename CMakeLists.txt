cmake_minimum_required(VERSION 2.8.12)
project(python-poppler)

find_package(PkgConfig)
pkg_check_modules(POPPLER REQUIRED poppler-cpp>=0.62.0)
include_directories(${POPPLER_INCLUDE_DIRS})
link_directories(${POPPLER_LIBRARY_DIRS})

# find_package(pybind11)
add_subdirectory(pybind11)

pybind11_add_module(_version src/cpp/version.cpp)
target_link_libraries(_version PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_global src/cpp/global.cpp)
target_link_libraries(_global PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_rectangle src/cpp/rectangle.cpp)
target_link_libraries(_rectangle PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_image src/cpp/image.cpp)
target_link_libraries(_image PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_document src/cpp/document.cpp)
target_link_libraries(_document PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_page src/cpp/page.cpp)
target_link_libraries(_page PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_page_renderer src/cpp/page_renderer.cpp)
target_link_libraries(_page_renderer PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_page_transition src/cpp/page_transition.cpp)
target_link_libraries(_page_transition PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_embedded_file src/cpp/embedded_file.cpp)
target_link_libraries(_embedded_file PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_destination src/cpp/destination.cpp)
target_link_libraries(_destination PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(_toc src/cpp/toc.cpp)
target_link_libraries(_toc PRIVATE ${POPPLER_LIBRARIES})
