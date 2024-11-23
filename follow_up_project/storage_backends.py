from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'  # This is where static files will be stored in your S3 bucket
    default_acl = 'public-read'  # Ensures that the files are publicly accessible

class MediaStorage(S3Boto3Storage):
    location = 'media'  # This is where uploaded media files will be stored in your S3 bucket
    file_overwrite = False  # Prevent overwriting files with the same name
