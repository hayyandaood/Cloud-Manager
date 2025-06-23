import frappe
from frappe.model.document import Document

class DashboardConfiguration(Document):
    def validate(self):
        if not frappe.db.exists("Cloud Customer", self.customer):
            frappe.throw("Invalid customer")