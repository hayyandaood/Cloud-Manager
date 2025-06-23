import frappe
import secrets
from frappe.model.document import Document

class AccessToken(Document):
    def before_insert(self):
        self.token = secrets.token_hex(32)
        self.created_at = frappe.utils.now()

    def validate(self):
        if not frappe.db.exists("Cloud Customer", self.customer):
            frappe.throw("Invalid customer")