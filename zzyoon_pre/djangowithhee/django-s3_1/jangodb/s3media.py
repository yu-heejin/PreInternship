from storages.backends.s3boto3 import S3Boto3Storage

# S3Boto3Storage를 상속받아서 사용
class MediaStorage(S3Boto3Storage):
    # s3 > media 폴더에 사진 저장됨
    location = 'media'