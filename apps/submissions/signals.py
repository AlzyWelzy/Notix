from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.apps import apps
from django.conf import settings


@receiver(post_save, sender=apps.get_model("submissions", "SubmissionModel"))
def send_submission_email(sender, instance, **kwargs):
    email_host = f"noreply <{settings.EMAIL_HOST}>"
    subject = "Submission Status Update"
    message = f"Submission {instance.title} has been {instance.get_status_display}"

    send_mail(
        subject,
        message,
        email_host,
        [instance.user.email],
        fail_silently=False,
    )
