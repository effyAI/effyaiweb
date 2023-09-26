# # database.py
# from flask_sqlalchemy import SQLAlchemy
# import boto3

# db = SQLAlchemy()


# def upload_image_to_s3(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, object_key,
#                        local_image_path):
#     try:
#         # Initialize the S3 client
#         s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
#                           region_name=region_name)

#         # Upload the image to S3
#         s3.upload_file(local_image_path, bucket_name, object_key)

#         print(f'Successfully uploaded {local_image_path} to S3 bucket {bucket_name} with key {object_key}')
#         return True
#     except Exception as e:
#         print(f'Error uploading the image: {e}')
#         return False

# # Example usage:
# # aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
# # aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
# # region_name = 'YOUR_REGION_NAME'  # e.g., 'us-east-1'
# # bucket_name = 'YOUR_BUCKET_NAME'
# # object_key = 'path/to/your/image.jpg'
# # local_image_path = 'path/to/your/local/image.jpg'
# # upload_image_to_s3(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, object_key, local_image_path)
