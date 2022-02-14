# from rest_framework import serializers

# from s3api.models import UploadedFile


# class UploadedFilePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

#     def get_queryset(self):
#         request = self.context['request']
#         return UploadedFile.objects.filter(user=request.user)

# from django.db.models import Field
# from s3api.widgets import S3DirectWidget


# class S3DirectField(Field):
#     def __init__(self, *args, **kwargs):
#         dest = kwargs.pop('dest', None)
#         self.widget = S3DirectWidget(dest=dest)
#         super(S3DirectField, self).__init__(*args, **kwargs)

#     def get_internal_type(self):
#         return 'TextField'

#     def formfield(self, *args, **kwargs):
#         kwargs['widget'] = self.widget
#         return super(S3DirectField, self).formfield(*args, **kwargs)