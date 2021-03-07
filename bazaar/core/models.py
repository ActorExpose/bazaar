from django.conf import settings
from django.db import models
import uuid


class Yara(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    is_private = models.BooleanField(default=False)


# makemigrations --> génère le modèle de la DB
# migrate --> applique la modèle à la DB
