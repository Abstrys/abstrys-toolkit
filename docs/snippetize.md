snippetize - cut a file into snippets (or remove snippet markers)

Usage:
======

> snippetize [-u] [file1] [file2] ...

-   If *no arguments* are given, then all of the files in the `src` dir
    will be processed.
-   If a *directory* is provided as input, then all files in the given
    directory will be processed.
-   All snipped files will be written to the `snips` directory.
-   If -u is specified, then the files will be "unsnipped"--all of the
    snip markers will be removed from the file and the resulting file
    will be saved in the `unsnips` dir.

Making snippets:
================

1.  To make a snippet in a source file, simply delimit the beginning of
    your snippet like this:

        ~~| snippet_name

    The *snippet\_name* is a unique name within the file that you use to
    refer to the snippet. The resulting snippet file will be named like
    this:

        file_name-snippet_name.file_ext

2.  End your snip with the end-snip delimiter:

        |~~

    Any lines between the delimiters will be copied into the resulting
    snippet file.

Begin-snip and end-snip delimiters are usually placed within comments in
the source files. For example, in a C++ or Java source file, you might
have:

    // ~~| first_snip
    ... some code here ...
    // |~~

In Python, Ruby, or in a bash script, you would have:

    # ~~| first_snip
    ... some code here ...
    # |~~
