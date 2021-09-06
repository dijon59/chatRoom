from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class HtmlEmailSender(object):
    def __init__(self, subject, html_template, extra_context=None):
        # Email headers
        self.subject = subject
        self.sender = settings.DEFAULT_FROM_EMAIL

        # Email body
        self.html_template = html_template
        self.context = {}
        self.context.update(extra_context)

    def render_html_body(self):
        return render_to_string(self.html_template, self.context)

    def send(self, to, cc=None, bcc=None):
        msg = EmailMessage(
            subject=self.subject,
            body=self.render_html_body(),
            from_email=self.sender,
            to=to, cc=cc, bcc=bcc,
        )
        msg.content_subtype = "html"
        msg.send()


def send_welcome_email(user):
    HtmlEmailSender(
        subject='Welcome to Our chat Room!!',
        html_template='chat/emails/welcome_email.html',
        extra_context={},
    ).send(to=[user.email])
