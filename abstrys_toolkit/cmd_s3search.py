#!/usr/bin/env python
import boto3
import sys
import fnmatch

def list_buckets():
    s3client = boto3.client('s3')
    bucket_list = s3client.list_buckets()
    for b in bucket_list['Buckets']:
        bucket_name = b['Name']
        print(bucket_name)

def list_bucket_contents(bucket_name, object_path=None, glob='*'):
    s3client = boto3.client('s3')
    continuation_token = None
    finished = False
    object_names = []
    while not finished:
        try:
            if continuation_token == None:
                object_list = s3client.list_objects_v2(
                    Bucket=bucket_name)
            else:
                object_list = s3client.list_objects_v2(
                    Bucket=bucket_name,
                    ContinuationToken=continuation_token)
        except Exception as e:
            sys.stderr.write('Error while trying to list objects in bucket "%s":\n' % bucket_name)
            sys.stderr.write('%s\n' % e)
            sys.exit(1)

        if object_list['IsTruncated']:
            continuation_token = object_list['NextContinuationToken']
        else:
            finished = True

        if 'Contents' in object_list:
            for o in object_list['Contents']:
               object_names.append(o['Key'])

    if object_path == '':
        object_path == None

    if object_path != None:
        object_names = fnmatch.filter(object_names, '%s/%s' % (object_path, glob))
    else:
        object_names = fnmatch.filter(object_names, glob)

    # print the remaining names.
    for name in object_names:
        print(name)


def main():
    # strip the first argument (executable name)
    args = sys.argv[1:]

    # if no arguments, list the buckets
    if len(args) == 0:
        list_buckets()
        return

    # TODO use args.

    # if a bucket name, list its contents
    for filespec in args:
        bucket_name = None
        object_path = None
        glob = '*'

        if '/' in filespec:
            # grab the bucket name
            (bucket_name, the_rest) = filespec.split('/', 1)
            if '/' in the_rest:
                # split on the *last* separator
                (object_path, glob) = the_rest.rsplit('/', 1)
            else:
                glob = the_rest
        else:
            bucket_name = filespec

        if bucket_name:
            #print('bucket_name = %s, object_path = %s, glob = %s' % (bucket_name, object_path, glob))
            list_bucket_contents(bucket_name, object_path, glob)


if __name__ == '__main__':
    main()

