project(
    'python-poppler', 
    'cpp', 
    version: '0.4.1', 
    license: 'GNU General Public License v2 (GPLv2)', 
    license_files: 'LICENSE.txt',
    meson_version: '>=1.1.0',
    default_options : ['cpp_std=c++11']
)

poppler_dep = dependency('poppler-cpp', version: '>=0.26.0')

python_mod = import('python')
python3 = python_mod.find_installation('python3', pure: false)

pybind11_proj = subproject('pybind11')
pybind11_dep = pybind11_proj.get_variable('pybind11_dep')

subdir('src')
