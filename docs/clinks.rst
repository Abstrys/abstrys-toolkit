
clinks.py
=========

Check for broken links in HTML files in the current directory.

Usage:
------

::

  clinks [-i file] [-r] [filespecs]

If no filespecs are provided, then all files ending in '.html' or '.htm' will
be searched.

If the filespec is a directory, then all files within it will be searched.

Switches:
---------

**-i | --ignore**
    Specifies a filename that includes terms that will cause a link to be
    ignored. This file should be a simple text file with the terms provided
    one-per-line.

    By default, no terms are ignored.

**-r | --recurse**
    Recurse into directories. If not specified, then only the current
    directory, or directories provided on the command-line, will be searched.

Examples:
---------

::

  clinks -r -i links_to_ignore.txt

This will check all .html and .htm files in the current directory and all
subdirectories, ignoring all of the links that include terms in the
'links_to_ignore.txt' file.

