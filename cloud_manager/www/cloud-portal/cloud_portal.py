import frappe
from frappe.website.website_generator import WebsiteGenerator

class CloudPortal(WebsiteGenerator):
    def get_context(self, context):
        customer = frappe.form_dict.get("customer") or frappe.db.get_value("Cloud Customer", {"email": frappe.session.user}, "name")
        if customer:
            context["customer"] = frappe.get_doc("Cloud Customer", customer)
        context.no_cache = True