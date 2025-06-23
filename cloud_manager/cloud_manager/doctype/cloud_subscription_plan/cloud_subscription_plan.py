import frappe
from frappe.model.document import Document

class CloudSubscriptionPlan(Document):
    def validate(self):
        if self.cpu_cores <= 0 or self.ram_gb <= 0 or self.storage_gb <= 0 or self.monthly_price <= 0:
            frappe.throw("CPU cores, RAM, storage, and price must be positive")