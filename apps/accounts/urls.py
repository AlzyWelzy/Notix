from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="profile", permanent=True)),
    path(
        "profile/", TemplateView.as_view(template_name="profile.html"), name="profile"
    ),
    path("", include("allauth.urls")),
]
