#!/usr/bin/env python
import boto
 
BUCKET_NAME = "bucket-name"
DELETE_DATE = "2016-09-15"
counter = 0
 
bucket = boto.connect_s3().get_bucket(BUCKET_NAME)
 
for v in bucket.list_versions():
    if (isinstance(v, boto.s3.deletemarker.DeleteMarker) and
            v.is_latest and
            DELETE_DATE in v.last_modified):
		counter += 1
		bucket.delete_key(v.name, version_id=v.version_id)

print counter
