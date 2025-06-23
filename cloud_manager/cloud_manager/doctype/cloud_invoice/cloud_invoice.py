import frappe
from frappe.model.document import Document

class CloudInvoice(Document):
    def before_save(self):
        total = sum(item.amount for item in self.items)
        self.total_amount = total

    def on_submit(self):
        self.status = "Unpaid"
        self.save()

    def validate(self):
        if not self.items:
            frappe.throw("At least one invoice item is required")