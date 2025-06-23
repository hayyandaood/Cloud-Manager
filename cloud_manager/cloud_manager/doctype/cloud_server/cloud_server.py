import frappe
from frappe.model.document import Document

class CloudServer(Document):
    def validate(self):
        if not self.cloud_subscription:
            frappe.throw("Cloud Subscription is mandatory")

    def before_save(self):
        cloud_subscription = frappe.get_doc("Cloud Subscription", self.cloud_subscription)
        plan = frappe.get_doc("Cloud Subscription Plan", cloud_subscription.plan)
        self.cpu_cores = plan.cpu_cores
        self.ram_gb = plan.ram_gb
        self.storage_gb = plan.storage_gb

    @staticmethod
    @frappe.whitelist()
    def log_usage(docname, cpu, ram, storage):
        server = frappe.get_doc("Cloud Server", docname)
        server.append("usage_logs", {
            "timestamp": frappe.utils.now(),
            "cpu_usage": cpu,
            "ram_usage": ram,
            "storage_usage": storage
        })
        server.save()