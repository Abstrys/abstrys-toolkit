
s3pub
=====

Publish files on Amazon S3.

Usage
-----

There are three forms of usage:

* The basic form::

    scripts/s3pub [-r] <filespec> <s3_path>

* The publish/unpublish form::

    scripts/s3pub [-r] [-u] <s3_path>

* The argfile form::

    scripts/s3pub [-u] -f <argfile> [s3_path]

Switches, if provided, always precede the accompanying arguments.

The ``-y`` switch can be used with any of these forms to automatically answer
'yes' to any queries (of the form "are you sure you want to do this?"). If
``-y`` is specified:

* s3 buckets that don't exist will automatically be created if necessary.

* files will be published and/or overwritten without confirmation.

Arguments
---------

**filespec**
    A local file or directory, file-glob, or list of files to publish.  If a
    directory is specified, the ``-r`` switch can be used to copy all of the
    files in the directory recursively.

**s3_path**
    A bucket or path on S3. When a path is provided to s3pub by itself, it is
    assumed that the file already exists on S3 and should be made public. If
    the ``-u`` switch is provided, then the file is made unpublic (private),
    instead.

**argfile**
    A file containing s3pub arguments, one set per line. The argument lines,
    just as arguments passed via the command-line, can begin with a switch such
    as ``-r`` or ``-u``, but must obey all of the normal rules for specifying
    arguments (if a filename has spaces in it, it must be quoted, etc.). You
    cannot nest another argfile argument within this file, however.

    To specify the argfile, you *must* precede it with the ``-f`` switch, or it
    will be either be interpreted as an s3 path or as a file to upload.

    You can specify *both* an argfile and an s3 path. If so, the argfile is
    considered to be a simple list of filespecs to upload.

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


