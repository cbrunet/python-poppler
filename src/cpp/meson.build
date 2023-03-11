sources = {
    'global_': 'global.cpp',
    'destination': 'destination.cpp',
    'document': 'document.cpp',
    'embedded_file': 'embedded_file.cpp',
    'font': 'font.cpp',
    'global': 'global.cpp',
    'image': 'image.cpp',
    'page_renderer': 'page_renderer.cpp',
    'page_transition': 'page_transition.cpp',
    'page': 'page.cpp',
    'rectangle': 'rectangle.cpp',
    'toc': 'toc.cpp',
    'version': 'version.cpp',
}

python_modules = []
foreach module, source : sources
    python_modules += python3.extension_module(
        module, 
        source, 
        dependencies: [poppler_dep, pybind11_dep],
        install: true,
        subdir: 'poppler/cpp',
    )
endforeach
