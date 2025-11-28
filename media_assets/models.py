from django.db import models
from django.conf import settings
import cloudinary # media management - files cloudinary -url -store to db
from cloudinary.models import CloudinaryField
# Create your models here.
class MediaAsset(models.Model):
    # class variables for media assets choices
    CATEGORY_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    ]
    # object attributes/table fields
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='Uploaded and maintained by MediaHub')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='image')
    media_file = CloudinaryField('media', resource_type='auto') # cloudinary in use
    # relationship attribute - one user can have many uploads
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='media_assets')
    created_at = models.DateTimeField(auto_now_add=True)  # automatically capture the time the record is inserted
    updated_at = models.DateTimeField(auto_now=True)  # automatically capture the time the record was last updated
    is_public = models.BooleanField(default=True)  # by default all uploads are public
    views_count = models.PositiveIntegerField(default=0)  # to track number of views for each media asset

    # always display objects in order of upload time - latest first
    class Meta:
        ordering = ['-created_at']  # latest uploads first

    # edit rights
    def can_edit(self, user):
        """ Check if the given user can update this media asset """
        return user == self.uploaded_by or user.is_teacher() or user.is_superuser  # allow if owner or teacher or admin

    # string representation
    def __str__(self):  # string representation of the object
        return self.title  # display the title of the media asset
