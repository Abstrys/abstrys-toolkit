
s3pub
=====

Publish files on Amazon S3. This script can also unpublish files (make them
private), upload files and publish them in one step, or just upload files while
keeping them private.

Usage
-----

There are three forms of usage:

* The basic form, which publishes local files to S3::

    scripts/s3pub [-y|r|u] <filespec> <s3_path>

* The publish/unpublish form, which changes the access of files already on S3::

    scripts/s3pub [-y|u] <s3_path>

* The argfile form, which takes a file of paths to publish to S3::

    scripts/s3pub [-y|u|f] <argfile> [s3_path]

Switches
--------

Switches, if provided, always precede the accompanying arguments.

**-h**
    Prints help. You can pipe the output of this command to rst2*.py to
    generate HTML, manpage, or other versions of this help.

**-r**
    Can be specified when you also specify local filespecs to publish or upload
    to S3. If one of the filespecs is a directory, then scripts/s3pub will
    recursively upload the directory's contents. If it contains subdirectories,
    their contents will also be uploaded. The directory structure will be
    preserved on S3.

**-u**
    When used with either local-file or argfile modes of operation, this flag
    will cause the normal publish operation to be upload-only. The files will
    remain private.

    When used with the publish/unpublish form to work with files already on S3,
    the flag will unpublish already-published files, reverting them to private.

**-y**
    The ``-y`` switch, when specified, tells #scripts/s3pub to automatically answer
    'yes' to any queries (of the form "are you sure you want to do this?"). If
    ``-y`` is specified:

    * s3 buckets that don't exist will automatically be created if necessary.

    * files will be published and/or overwritten without any confirmation.

    With great power comes great responsibility. Play carefully.

Arguments
---------

**filespec**
    A local file or directory, file-glob, or list of files to publish.  If a
    directory is specified, the ``-r`` switch can be used to copy all of the
    files in the directory recursively. The ``-u`` argument will cause the
    files to be uploaded only, and not published.

**s3_path**
    A bucket or path on S3. When a path is provided to s3pub by itself, it is
    assumed that the file already exists on S3 and should be made public. If
    the ``-u`` switch is provided, then the file is made unpublic (private),
    instead.

**argfile**
    A file containing local filepaths and s3 paths for publishing files, one
    set per line. To specify the argfile, you *must* precede it with the ``-f``
    switch, or it will be either be interpreted as an s3 path or as a file to
    upload.

    The ``-u`` switch will cause the files to be uploaded only, and not
    published.

    You can specify *both* an argfile and an s3 path. If so, the
    argfile is considered to be a simple list of filespecs to upload.

Notes
-----

Before using this script, you must provide your AWS credentials to the program,
with any one of the following methods:

* Set the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables
  with your AWS credentials.

* Provide a YAML-formatted file called `aws-config.txt` in the current
  directory with your aws credentials specified like this::

      ---
      access_key_id:     ACCESSKEYID
      secret_access_key: SECRETACCESKEY

  Replace ACCESSKEYID and SECRETACCESSKEY with your own AWS credentials.

  You can also specify the path to the config file by passing the
  ``--aws_config <config_file_path>`` argument with the path to the config file
  specified. You can use this argument to point to a config file with any name.

* Provide the command-line arguments: ``--access_key ACCESSKEYID`` and/or
  ``--secret_key SECRETACCESSKEY``, providing your own AWS credentials in place
  of ACCESSKEYID and SECRETACCESSKEY.


