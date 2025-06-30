import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_customer_data(customer_id):
    if not customer_id:
        frappe.throw(_("Customer ID is required"))
    
    if not frappe.db.exists("Cloud Customer", customer_id):
        frappe.throw(_("Customer not found"))
    
    user_roles = frappe.get_roles(frappe.session.user)
    if not ("Cloud Admin" in user_roles or 
            "Cloud Staff" in user_roles or 
            frappe.db.get_value("Cloud Customer", customer_id, "customer_user") == frappe.session.user):
        frappe.throw(_("Unauthorized access"))
    
    customer = frappe.get_doc("Cloud Customer", customer_id)
    subscriptions = frappe.get_all("Cloud Subscription", filters={"customer": customer_id}, 
                                  fields=["name", "plan", "status"])
    servers = frappe.get_all("Cloud Server", filters={"cloud_subscription": ["in", 
                            [sub["name"] for sub in subscriptions]]}, 
                            fields=["resource_name", "resource_type", "status"])
    invoices = frappe.get_all("Cloud Invoice", filters={"customer": customer_id}, 
                             fields=["name", "total_amount", "status"])
    
    return {
        "customer": customer.as_dict(),
        "subscriptions": subscriptions,
        "servers": servers,
        "invoices": invoices
    }