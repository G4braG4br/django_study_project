from django.db import models

from models_app.models.base import BaseModel
from models_app.utils.file_uploader import uploaded_file_path


class History(BaseModel):
    imported_file = models.FileField(
        verbose_name="Imported File",
        upload_to=uploaded_file_path,
        blank=True,
        null=True
    )
    result = models.TextField()

    class Meta:
        db_table = "history"
        verbose_name = "History"
        verbose_name_plural = "History"
