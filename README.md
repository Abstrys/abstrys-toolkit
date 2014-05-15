abstrys-toolkit
===============

Useful command-line tools and scripts. Designed for tech writers, usable by anyone.

Included in the toolkit are the following tools:

- **camel2snake** - 
- **[cleanjson][]** - cleans up messy json
- **[clinks][]** - check href links in HTML files.
- **fix-filenames** - modifies filenames on the system to snake_case
- **music-album-renamer** - modifies filenames on the system to snake_case
- **rompy** - Runs an arbitrary command when a tracked file's modification time changes
- **[s3del][]** - Deletes Amazon S3 buckets or keys.
- **[s3lod][]** - Lists Or Downloads the contents of Amazon S3 buckets
- **[s3up][]** - Publishes (upload and make public) any file from the local system to an Amazon S3 bucket
- **[snippetize][]** - cut a file into snippets (or remove snippet markers)
- **[srep][]** - search and replace in files given a filespec (either file names or a glob, ex. *.xml)

## Installing the toolkit

You can install the Abstrys toolkit with pip or easy_install:

    easy_install abstrys-toolkit

or

    pip install abstrys-toolkit

Alternatively, you can [download the .zip archive][zip], unpack it and enter the following command in its directory:

    python setup.py install

**Note**: If you're on a Linux, Unix, or Mac OS X system, you'll likely need to run this with `sudo`.

## License

This software is provided under the [BSD 3-Clause][license] license. See the [LICENSE file][license-file] for more details.

## For more information

Contact [eron@abstrys.com](mailto:eron@abstrys.com?Subject=abstrys-toolkit).

[cleanjson]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/cleanjson.md
[clinks]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/clinks.rst
[license-file]: https://github.com/Abstrys/abstrys-toolkit/blob/master/LICENSE
[license]: http://opensource.org/licenses/BSD-3-Clause
[s3del]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/s3del.rst
[s3lod]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/s3lod.rst
[s3pub]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/s3pub.rst
[snippetize]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/snippetize.md
[srep]: https://github.com/Abstrys/abstrys-toolkit/blob/master/docs/srep.rst
[zip]: https://github.com/Abstrys/abstrys-toolkit/archive/master.zip

