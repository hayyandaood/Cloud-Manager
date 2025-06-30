# import frappe
# from frappe.website.website_generator import WebsiteGenerator

# class CloudPortal(WebsiteGenerator):
#     def get_context(self, context):
#         customer = frappe.form_dict.get("customer") or frappe.db.get_value("Cloud Customer", {"email": frappe.session.user}, "name")
#         if customer:
#             context["customer"] = frappe.get_doc("Cloud Customer", customer)
#         context.no_cache = True


import frappe

def get_context(context):
    customer_id = frappe.form_dict.get("customer") or frappe.session.user
    if not customer_id:
        frappe.throw("Customer ID or user session required")
    
    if frappe.db.exists("Cloud Customer", {"customer_user": customer_id}):
        customer_id = frappe.db.get_value("Cloud Customer", {"customer_user": customer_id}, "name")
    
    if not frappe.db.exists("Cloud Customer", customer_id):
        frappe.throw("Customer not found")
    
    context.customer = frappe.get_doc("Cloud Customer", customer_id)
    context.no_cache = 1