import frappe
from frappe.model.document import Document

class CloudPayment(Document):
    def validate(self):
        invoice = frappe.get_doc("Cloud Invoice", self.cloud_invoice)
        if self.amount > invoice.total_amount:
            frappe.throw("Payment amount cannot exceed invoice total")
        if invoice.status == "Paid":
            frappe.throw("Invoice is already paid")

    def on_submit(self):
        invoice = frappe.get_doc("Cloud Invoice", self.cloud_invoice)
        invoice.status = "Paid"
        invoice.save()