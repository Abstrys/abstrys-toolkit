
s3del
=====

Delete an S3 bucket or its contents.

Usage
-----

::

    scripts/s3del [s3_path] ...

The s3 path can be repeated, so multiple buckets, partial paths or objects can
be provided at once.

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


