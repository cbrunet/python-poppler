python_sources = [
    '__init__.py',
    # '_version.py',
    'destination.py',
    'document.py',
    'embeddedfile.py',
    'font.py',
    'image.py',
    'page.py',
    'pagerenderer.py',
    'pagetransition.py',
    'rectangle.py',
    'toc.py',
    'utilities.py',
    'cpp/__init__.py',
]

version_file = configure_file(
    input: '_version.py.in',
    output: '_version.py',
    configuration: {
        'version': meson.project_version(),
    }
)

python3.install_sources(
    python_sources, version_file,
    subdir: 'poppler',
    preserve_path: true,
)
