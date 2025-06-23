import frappe
from frappe.model.document import Document

class CloudManagerSettings(Document):
    def validate(self):
        if self.support_email and not frappe.utils.validate_type(self.support_email, "email"):
            frappe.throw("Invalid Support Email")