import frappe
from frappe.model.document import Document

class ResourceAccessLog(Document):
    def validate(self):
        if not frappe.db.exists("Cloud Server", self.resource):
            frappe.throw("Invalid Cloud Server")
        if not frappe.db.exists("User", self.user):
            frappe.throw("Invalid User")