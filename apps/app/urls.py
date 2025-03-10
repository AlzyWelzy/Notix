from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("accounts/", include("apps.accounts.urls")),
    path("submissions/", include("apps.submissions.urls")),
]
