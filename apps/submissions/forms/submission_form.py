from django.forms import ModelForm
from django.apps import apps


class SubmissionForm(ModelForm):
    class Meta:
        model = apps.get_model("submissions", "SubmissionModel")
        fields = ["title", "description"]


class AdminSubmissionForm(SubmissionForm):
    class Meta:
        model = apps.get_model("submissions", "SubmissionModel")
        fields = ["title", "description", "status"]
