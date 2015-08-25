# coding=utf-8
#
# config do S3 https://aws.amazon.com/articles/3998

import boto

s3 = boto.connect_s3()
bucket = s3.create_bucket('media.yourdomain.com')  # bucket names must be unique
key = bucket.new_key('armario/inceres_data-repository.attic')
key.set_contents_from_filename('/home/armario/inceres_data-repository.attic')
#key.set_acl('public-read')

#####requiere credit card...pufff