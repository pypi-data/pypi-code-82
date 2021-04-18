import ntpath
import os
from datetime import datetime
from decimal import Decimal
from typing import Optional

from NEMO.fields import MultiEmailFormField
from NEMO.utilities import send_mail
from NEMO.views.customization import get_media_file_contents
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.formats import number_format
from django.utils.text import slugify


def get_invoice_document_filename(invoice, filename):
    account_name = slugify(invoice.project_details.project.account.name)
    project_name = slugify(invoice.project_details.name)
    now = datetime.now()
    # generated_date = now.strftime("%Y-%m-%d_%H-%M-%S")
    year = now.strftime("%Y")
    ext = os.path.splitext(filename)[1]
    return f"invoices/{year}/{account_name}/{project_name}/{slugify(invoice.invoice_number)}_{project_name}{ext}"


def get_merchant_logo_filename(configuration, filename):
    name = slugify(configuration.name + "_merchant_logo")
    ext = os.path.splitext(filename)[1]
    return f"merchant_logos/{name}{ext}"


def display_amount(amount: Optional[Decimal], configuration=None) -> str:
    # We need to specifically check for None since amount = 0 will evaluate to False
    if amount is None:
        return ""
    currency = (
        f"{configuration.currency_symbol}"
        if configuration and configuration.currency_symbol
        else f"{configuration.currency} "
        if configuration
        else ""
    )
    if amount < 0:
        return f"({currency}{number_format(abs(amount), decimal_pos=2)})"
    else:
        return f"{currency}{number_format(amount, decimal_pos=2)}"


def render_and_send_email(template_prefix, context, from_email, to=None, bcc=None, cc=None, attachments=None) -> int:
    subject = render_template_from_media("{0}_subject.txt".format(template_prefix), context)
    # remove superfluous line breaks
    subject = " ".join(subject.splitlines()).strip()
    subject = format_email_subject(subject)
    template_name = "{0}_message.html".format(template_prefix)
    content = render_template_from_media(template_name, context).strip()
    return send_mail(
        subject=subject, content=content, from_email=from_email, to=to, bcc=bcc, cc=cc, attachments=attachments
    )


def format_email_subject(subject):
    prefix = getattr(settings, "INVOICE_EMAIL_SUBJECT_PREFIX", "")
    return prefix + force_str(subject)


def render_template_from_media(template_name, context):
    """ Try to find the template in media folder. if it doesn't exists, look in project templates """
    file_name = ntpath.basename(template_name)
    email_contents = get_media_file_contents(file_name)
    if email_contents:
        return Template(email_contents).render(Context(context))
    else:
        # otherwise look in templates
        return render_to_string(template_name, context)


def render_combine_responses(request, original_response: HttpResponse, template_name, context):
    """ Combines contents of an original http response with a new one """
    additional_content = render(request, template_name, context)
    original_response.content += additional_content.content
    return original_response


def prepare_value(self, value):
    if value is None:
        return value
    return self.separator.join(value)


# Set this to fix rendering issues with multi email fields in forms (until it is added to NEMO)
setattr(MultiEmailFormField, "prepare_value", prepare_value)
