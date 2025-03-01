from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.submissions.forms import SubmissionForm, AdminSubmissionForm
from django.apps import apps
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.http import HttpResponse
from django.urls import reverse_lazy
from django_filters import rest_framework as filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


class SubmissionFilter(filters.FilterSet):
    class Meta:
        model = apps.get_model("submissions", "SubmissionModel")
        fields = [
            "title",
            "status",
        ]


class SubmissionListView(ListView):
    model = apps.get_model("submissions", "SubmissionModel")
    template_name = "submissions/submissions.html"
    context_object_name = "submissions"
    queryset = model.objects.all()
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return super().get_queryset()
        result = super().get_queryset().filter(user=self.request.user)
        self.filterset = SubmissionFilter(self.request.GET, queryset=result)
        return self.filterset.qs


class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = apps.get_model("submissions", "SubmissionModel")
    form_class = SubmissionForm
    template_name = "submissions/submission_form.html"
    success_url = reverse_lazy("submissions")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SubmissionDetailView(DetailView):
    model = apps.get_model("submissions", "SubmissionModel")
    template_name = "submissions/submission_detail.html"
    context_object_name = "submission"


class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    model = apps.get_model("submissions", "SubmissionModel")
    form_class = SubmissionForm
    template_name = "submissions/submission_form.html"
    success_url = reverse_lazy("submissions")

    def get_form_class(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return AdminSubmissionForm
        return super().get_form_class()


class SubmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = apps.get_model("submissions", "SubmissionModel")
    template_name = "submissions/submission_delete.html"
    success_url = reverse_lazy("submissions")
    context_object_name = "submission"
    # def delete(self, request, *args, **kwargs):
    #     submission = self.get_object()
    #     submission.delete()
    #     return redirect("submissions-list")
