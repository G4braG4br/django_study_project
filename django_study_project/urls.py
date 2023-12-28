"""
URL configuration for django_study_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django_study_project.settings import BASE_DOMAIN, DEBUG, MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns.append(path('', include('django_prometheus.urls'))),
urlpatterns.append(path('api/', include('api.urls')))


api_docs_schema_view = get_schema_view(
    openapi.Info(
        title="Vana module API",
        default_version="v1",
    ),
    patterns=[path("api/", include("api.urls"))],
    public=True,
    url=f"{BASE_DOMAIN}",
    permission_classes=[
        permissions.AllowAny,
    ],
)

api_docs_urlpatterns = [
    path(
        "api/swagger/",
        api_docs_schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    )
]

urlpatterns = urlpatterns + api_docs_urlpatterns

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
