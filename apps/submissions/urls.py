from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.SubmissionListView.as_view(), name="submissions"),
    path("create/", views.SubmissionCreateView.as_view(), name="submissions-create"),
    path(
        "<int:pk>/update/",
        views.SubmissionUpdateView.as_view(),
        name="submissions-update",
    ),
    path(
        "<int:pk>/delete/",
        views.SubmissionDeleteView.as_view(),
        name="submissions-delete",
    ),
    path("<int:pk>/", views.SubmissionDetailView.as_view(), name="submissions-detail"),
]
