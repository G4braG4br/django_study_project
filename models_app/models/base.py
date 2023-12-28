from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def show_info(self):
        """Custom method to show record fields inside the console"""
        print("-" * 20)
        fields = [field.name for field in list(self._meta.fields)]
        for field in [f"{field}: {getattr(self, field)}" for field in fields]:
            print(field, end="\n")
        print("-" * 20)

    class Meta:
        abstract = True
