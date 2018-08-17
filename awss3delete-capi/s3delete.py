#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3delete.py
# s3delete is an example that handles S3 buckets on AWS
# It uses Client API (low-level) of Boto3
# Delete a S3 bucket
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

import sys
import boto3
import botocore

def main():

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if len(args) < 1:
    print 'Not enough parameters. Proper Usage is: python s3delete.py <BUCKET_NAME>'
    sys.exit(1)

  bucket_name = args[0]
  print 'Bucket name: ' + bucket_name

  # Create an S3 Client
  s3client = boto3.client('s3')

  # Delete the bucket object
  try:
    print 'Deleting bucket...'
    response = s3client.delete_bucket(Bucket=bucket_name)
    print response
    print '\nDeleted'
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "NoSuchBucket":
      print("Error: Bucket does not exist!!")
    else:
      raise

  return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()