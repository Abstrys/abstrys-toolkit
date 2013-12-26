rom.py - run-on-modify in Python
================================

Runs a given command whenever you update a tracked file. Options exist
that allow you to pass arbitrary arguments to the command, and to
specify the rate at which the tracked file is checked for changes.

rom.py can either be used as a programmable Python module, or can be run
from the command-line.

Usage
-----

    rom.py <run_what> <on_what> [with_args] [at_rate_s]

**Where**:

*run\_what*
  ~ (Required) Executable to run when the target file is modified.

*on\_what*
  ~ (Required) Target file to check for modification.

*with\_args*
  ~ (Optional) Arguments to be added to the command-line.

*at\_rate\_s*
  ~ (Optional) The rate at which the file will be checked for
    modification, in seconds. You can specify either an integer or
    floating-point value. If no value is entered, a rate of one (1)
    second is used.

Examples
--------

**Pandoc example**:

    rompy `which pandoc` index.md "-o index.html" &

This will run [pandoc](http://johnmacfarlane.net/pandoc/) on `index.md`,
(re)generating `index.html` every time `index.md` changes. Using `&` at
the end of the line forks the process on Linux/Mac OS X, returning
control to the command-line.

**To convert reST files**:

    rompy `which rst2html.py` hello.rst '>hello.html' &

Converts `hello.rst` to `hello.html`, using similar semantics to the
Pandoc example. This time, using `rst2html.py` from the
[reStructuredText](http://docutils.sourceforge.net/rst.html) tools.

