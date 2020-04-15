#pragma once

#include <poppler/cpp/poppler-version.h>


#define HAS_VERSION(major,minor) (POPPLER_VERSION_MAJOR > major) || (POPPLER_VERSION_MAJOR == major && POPPLER_VERSION_MINOR >= minor)
