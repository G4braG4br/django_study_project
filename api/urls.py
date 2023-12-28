from django.urls import path
from api.views.history import HistoryView

urlpatterns = [
    path("test/", HistoryView.as_view())
]
