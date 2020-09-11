.. _installation:

Installation
============

Requirements
------------

python-poppler requires at least Python 3.7.

This package is currently distributed as source only,
and is currently tested on Linux only (using Arch Linux
on my personal machine, and Ubuntu 18.04 using GitHub actions.

It requires poppler version 0.26 or higher.
Beware that poppler version scheme changed to date based version numbers,
starting in August, 2020. Therefore, it jumped from 0.90 (July, 2020) to 20.08
(August, 2020).

Because we need to compile and link cpp files, you need
the headers files for poppler and for python.
For Arch Linux, the
`poppler <https://security.archlinux.org/package/poppler>`_
package should be sufficient.
On Ubuntu, you need
`libpoppler-cpp-dev <https://packages.ubuntu.com/bionic/libpoppler-cpp-dev>`_.

The cpp binding is done using pybind11, which is included with the package.
To build the package, you need the usual development tools (gcc, cmake...)


Installing from PyPI
--------------------

Installing from PyPI is the easiest way to install python-poppler.
Be sure to have all the requirements installed.
Ideally, you should install the package inside a Python virtual environment.

.. code-block:: bash

    pip install python-poppler



Installing from git
-------------------

When you clone the repository, you must include submodules:

.. code-block:: bash

    git clone --recurse-submodules https://github.com/cbrunet/python-poppler.git

Alternatively, you can fetch the submodules later, using:

.. code-block:: bash

    git submodule update --init --recursive

Then you simply need to use the ``setup.py`` script to perform
the usual tasks. For instance:

.. code-block:: bash

    python setup.py install

The `setup.py` script will invoke cmake, compile the binding,
and install all the files at the right place.




Compiling your own version of Poppler
-------------------------------------

If you want to use a poppler version more recent than
what is provided by your distribution,
you need to compile it from sources.

First you need to install all the required libraries.
A easy way to do it is to install the distribution version of poppler,
to be sure all its dependencies are installed.

Then you need to clone the poppler repository, and to checkout the
desired version (or you can stay on the HEAD of master if this is what you want):

.. code-block:: bash

    $ git clone https://gitlab.freedesktop.org/poppler/poppler.git
    $ cd poppler
    $ git checkout poppler-0.89.0

Next, you need to compile poppler. This is done using cmake.
You may want to specify the `CMAKE_INSTALL_PREFIX` path if you want
to install it in another place than in the default `/usr/local`:

.. code-block:: bash

    $ mkdir build
    $ cd build
    $ cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr/local \
        -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
        -DBUILD_GTK_TESTS=OFF \
        -DBUILD_QT5_TESTS=OFF \
        -DBUILD_CPP_TESTS=OFF \
        -DENABLE_CPP=ON \
        -DENABLE_GLIB=OFF \
        -DENABLE_GOBJECT_INTROSPECTION=OFF \
        -DENABLE_GTK_DOC=OFF \
        -DENABLE_QT5=OFF \
        -DBUILD_SHARED_LIBS=ON \
        ..
    $ make

Finally, you must install the lib. You may need `sudo` or not,
depending on the install prefix path you used:

.. code-block:: bash

    $ sudo make install

Before building python-poppler, you need to ensure it uses the version
you just installed. poppler uses pkg_config. Therefore, you can set
the `PKG_CONFIG_PATH` environment variable to the path where are located
the pkg_config files. For instance:

.. code-block:: bash

    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

Now you can install python-poppler, using either `pip` or from
the git sources.

If the poppler library is not located in a standard place,
it is possible that python-poppler is not able to find it.
you can use the `LD_LIBRARY_PATH` environment variable to tell
the system where to search for the poppler shared libraries:

.. code-block:: bash

    $ export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

Finally, you can test that everything is working by printing the poppler version:

>>> import poppler
>>> poppler.version()
(0, 89, 0)

