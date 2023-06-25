import boto3

s3 = boto3.client('s3')

s3.upload_file('test_text.txt', 'jlamere-boto-06212023', 'test_text.txt_upload.txt', ExtraArgs={'ContentType':'text/plain'})
  