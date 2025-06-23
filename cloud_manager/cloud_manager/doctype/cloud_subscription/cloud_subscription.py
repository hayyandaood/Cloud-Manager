import frappe
from frappe.model.document import Document

class CloudSubscription(Document):
    def validate(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            frappe.throw("End Date must be after Start Date")
        if self.status == "Active" and not self.end_date:
            frappe.throw("Active subscriptions must have an End Date")