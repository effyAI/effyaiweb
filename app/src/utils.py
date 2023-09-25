import boto3

class AwsBackNFro():
    def __init__(self):
        self.aws_access_key_id = "AKIAVZBVXJWJLAWNRCWZ"
        self.aws_secret_access_key="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"
        self.region_name="us-east-1"

        self.s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key,
                              region_name=self.region_name)

        self.bucket_name = 'effy-voicecloning'

    def upload(self, file_obj, file_path):
        self.s3.upload_fileobj(file_obj, self.bucket_name, file_path)
        s3_url = f'https://{self.bucket_name}.s3.amazonaws.com/{file_obj.filename}'
        return s3_url

    def download(self, file_path, local_file_path):
        self.s3.download_file(self.bucket_name, file_path, local_file_path)
        return local_file_path