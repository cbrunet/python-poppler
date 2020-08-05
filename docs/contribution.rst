.. _contributing:

Contributing
====================


Reporting bugs
--------------

Bugs are reported using the `Issue tracker on GitHub <https://github.com/cbrunet/python-poppler/issues>`.

When you report a bug, try to be as specific as possible, and provide all the relevant information:

* Version of poppler
* Version of python-poppler
* Operating system name and version
* Python version

If an exception occured, provide the entire stack trace.

Before submitting a new bug, please verify it is not already reported. If it is, verify if
you can provide additional information.


If you can, consider pull_request_.




Requesting features
-------------------

Suggestions and feature requests can be submitted using the `Issue tracker on GitHub <https://github.com/cbrunet/python-poppler/issues>` as well.

However, you should understand that the main goal of **python-poppler** is to provide a Python binding
to the poppler-cpp library. Therefore, if you need a feature that is not currently in poppler-cpp,
we will probably not implement it in python-poppler. But if you integrate a new feature in poppler-cpp,
we will certainly add it to python-poppler.




.. _pull_request:

Submiting a pull request
-------------------------

Pull requests are the prefered way for submitting patches, bug corrections, and new features.

When you submit a pull request, verify the following points:

* You agree that the submitted code is under GPL 2.0 license;
* Code is formatted using `black <https://github.com/psf/black>`. Ensure everything
  is well formated, using `tox -e lint` command;
* Please provide tests proving the bug is corrected, or covering the new feature, when it's possible;
* Ensure that all unit tests pass, using the `tox` command;
* Add a line to the changelog, in the NEWS.txt file;
* Update the documentation, when it applies.
