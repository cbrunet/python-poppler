cmake_minimum_required(VERSION 2.8.12)
project(python-poppler)

find_package(PkgConfig)
pkg_check_modules(POPPLER REQUIRED poppler-cpp>=0.62.0)
include_directories(${POPPLER_INCLUDE_DIRS})
link_directories(${POPPLER_LIBRARY_DIRS})

# find_package(pybind11)
add_subdirectory(pybind11)

pybind11_add_module(version src/cpp/version.cpp)
target_link_libraries(version PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(global_ src/cpp/global.cpp)
target_link_libraries(global_ PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(rectangle src/cpp/rectangle.cpp)
target_link_libraries(rectangle PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(image src/cpp/image.cpp)
target_link_libraries(image PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(document src/cpp/document.cpp)
target_link_libraries(document PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(page src/cpp/page.cpp)
target_link_libraries(page PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(page_renderer src/cpp/page_renderer.cpp)
target_link_libraries(page_renderer PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(page_transition src/cpp/page_transition.cpp)
target_link_libraries(page_transition PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(embedded_file src/cpp/embedded_file.cpp)
target_link_libraries(embedded_file PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(destination src/cpp/destination.cpp)
target_link_libraries(destination PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(toc src/cpp/toc.cpp)
target_link_libraries(toc PRIVATE ${POPPLER_LIBRARIES})

pybind11_add_module(font src/cpp/font.cpp)
target_link_libraries(font PRIVATE ${POPPLER_LIBRARIES})
