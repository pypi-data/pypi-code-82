from django.urls import path

from NEMO_billing.invoices.views import invoices, project

urlpatterns = [
    path("invoices/", invoices.invoices, name="invoices"),
    path("invoices/<int:invoice_id>/", invoices.view_invoice, name="view_invoice"),
    path("invoices/<int:invoice_id>/review/", invoices.review_invoice, name="review_invoice"),
    path("invoices/<int:invoice_id>/send/", invoices.send_invoice, name="send_invoice"),
    path("invoices/<int:invoice_id>/void/", invoices.void_invoice, name="void_invoice"),
    path("invoices/zip/", invoices.zip_invoices, name="zip_invoices"),
    path("invoices/generate_monthly_invoices/", invoices.generate_monthly_invoices, name="generate_monthly_invoices"),
    path("invoice_payment/<int:invoice_id>/received", invoices.invoice_payment_received, name="invoice_payment_received"),
    path("invoice_payment/<int:payment_id>/processed", invoices.invoice_payment_processed, name="invoice_payment_processed"),
    path("invoices/send_invoice_payment_reminder/", invoices.send_invoice_payment_reminder, name="send_invoice_payment_reminder"),

    # Overriding NEMO's create project URLs
    path("create_project/", project.edit_project, name='invoices_create_project'),
    path("projects/<int:project_id>/edit/", project.edit_project, name='invoices_edit_project'),
    # Here we are simply adding a little icon for edit
    path("project/<int:identifier>/", project.custom_project_view, name='custom_project_view'),
]
