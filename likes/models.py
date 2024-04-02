from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
    # 1toM relationship: parent: User (above import)
    # one user can have many LikedItem
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Generic relationship:
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
