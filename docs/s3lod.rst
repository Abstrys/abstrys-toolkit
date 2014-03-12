
s3lod
=====

List or download the contents of S3 buckets.

Usage
-----

::

    scripts/s3lod [-i] [s3_path] ...

Depending on whether an s3 path (consisting of bucket_name/and/path/to/object).
is provided, one of the following actions will be taken:

* If no path is provided, then the list of buckets will be returned.

* If a path is specified and refers to a bucket, then a list of the contents of
  that bucket are returned.

* If the path is a partial path (does not match the name of an S3 object, but
  matches part of its path) then a list of all of the S3 objects that match the
  partial path are returned.

* If the path is to an actual S3 object, then you can download the object
  (default) or get its info (if the ``-i`` flag is provided.

Switches, if provided, always precede the accompanying arguments.

The s3 path can be repeated, so multiple buckets, partial paths or objects can
be provided at once.  If the ``-i`` flag is provided, it effects all of the
specified arguments: no files will be downloaded; only the object information
will be returned.

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


