from django.contrib import admin

from models_app.models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass
