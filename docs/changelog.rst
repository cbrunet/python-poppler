.. _changelog:

Changelog
=========

0.2.2 (2020-10-03)
------------------

- Bugfix: Document can be corrupted by garbage collector when created from data (or from file handle) (Fixes :issue:`19`)
- Bugfix: Fix build with some compilers (Fixes :issue:`17`)
- Feature: Lower minimum required Python version to 3.6
- Feature: Lower minimum required poppler version to 0.26.0 (See :pr:`13`)  -- by Sandeep Mistry

0.2.1 (2020-06-19)
------------------

- Bugfix: Fixed byte order in image format string used for Pillow
- Bugfix: Prevent segmentation fault when performing some operations on locked documents (Fixes :issue:`4`)
- Bugfix: Fix include paths in C++ (Fixes :issue:`2`)
- Change namespace syntax to support old compilers (earlier than C++17) (Fixes :issue:`6`)  -- by bnewbold

0.2.0 (2020-06-04)
------------------

- Add the font infos to the :class:`.TextBox` object (Poppler 0.89.0)
- Added `__version__` to the Python package
- Added buffer interface to :class:`.Image`
- Added `__str__` method to :class:`.Image.Format` enum, for interoperability with pillow
- Bugfix: fixed the size of :attr:`.Image.data`

0.1.x
-----

Project was still in development, and had no formal changelog.

- 0.1.2: 2020-04-20
- 0.1.1: 2020-04-20
- 0.1.0: 2020-04-19 (initial version)
