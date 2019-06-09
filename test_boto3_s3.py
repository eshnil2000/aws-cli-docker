mport boto3
s3 = boto3.resource('s3')
s3client = boto3.client('s3')

for bucket in s3.buckets.all():
        print(bucket.name)
        for obj in bucket.objects.all():
                print(obj.key)

print(s3)
print(s3client)
#for bucket in s3.buckets.all():
#       print(bucket.name)
#       theobjects = s3client.list_objects_v2(Bucket=bucket[bucket.name])
#       for object in theobjects["Contents"]:
#               print(object["Key"])

# Boto 3
s3.Object(bucket.name, 'hello.txt').put(Body=open('/project/hello.txt', 'rb'))
