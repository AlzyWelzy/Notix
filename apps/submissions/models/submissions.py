from apps.app.models import BaseModel
from django.db import models


class SubmissionModel(BaseModel):
    STATUS = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "rejected"),
    )
    user = models.ForeignKey(
        "accounts.CustomUserModel", on_delete=models.CASCADE, related_name="submissions"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS, default="pending")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"
        db_table = "submissions"

    @property
    def get_status_display(self):
        return self.status.capitalize()
