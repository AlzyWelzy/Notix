from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.submissions.forms import SubmissionForm
from django.apps import apps
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from django.http import HttpResponse
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submissions"] = apps.get_model(
            "submissions", "SubmissionModel"
        ).objects.all()
        context["users"] = apps.get_model("accounts", "CustomUserModel").objects.all()
        return context
