.. _changelog:

Changelog
=========

0.4.1 (2023-04-21)
------------------

- Fix non-pure build for meson-python (:issue:`74` / :pr:`75`)
- Fix build on Mac OS (:issue:`76` / :pr:`77`)
- Tested with Python 3.11 and Poppler 23.04.0

0.4.0 (2023-03-21)
------------------

- Minimal supported Python version is now 3.7
- Tested with Python 3.11 and Poppler 23.03.0
- Build system is now ``meson``, and package is PEP-517 compliant (:pr:`70`)

0.3.0 (2022-04-12)
------------------

- Updated pybind11 to 2.9.2
- Tested with Python 3.10 and Poppler 22.04.0
- EmbeddedFile data() and checksum() now return bytes (See :pr:`32`) -- by Bence Cs
- Bugfix: Fixed typos in EmbeddedFile.modification_date and EmbeddedFile.is_valid
- Bugfix: Fixed typo in page.search (Fixes :issue:`37`)  -- by Bohumír Zámečník
- Bugfix: Fix underscore position in two attributes of the Rotation Enum, thereby
  making it consistent with the upstream ``poppler-cpp`` (:issue:`42` / :pr:`44`) -- by mara004
- Bugfix: Reading pdf_version now requires unlocked document (Fixes :issue:`39`)
- Bugfix: Ensure document was loaded before creating Document object (Fixes :issue:`48`)

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
