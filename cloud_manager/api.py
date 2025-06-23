import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_server_details(token, server_name):
    if not frappe.db.exists("Access Token", {"token": token, "is_active": 1}):
        frappe.throw("Invalid or inactive token")
    server = frappe.get_doc("Cloud Server", server_name)
    customer = frappe.get_value("Access Token", {"token": token}, "customer")
    if server.cloud_subscription.customer != customer:
        frappe.throw("Unauthorized access")
    return {
        "name": server.name,
        "resource_name": server.resource_name,
        "status": server.status,
        "usage_logs": server.usage_logs
    }

@frappe.whitelist()
def get_customer_data(customer):
    if not frappe.user.has_role("Cloud Admin") and frappe.session.user != frappe.db.get_value("Cloud Customer", customer, "email"):
        frappe.throw("Unauthorized access")
    customer_doc = frappe.get_doc("Cloud Customer", customer)
    cloud_subscriptions = frappe.get_all("Cloud Subscription", filters={"customer": customer}, fields=["name", "plan", "start_date", "status"])
    invoices = frappe.get_all("Cloud Invoice", filters={"customer": customer}, fields=["name", "total_amount", "invoice_date", "status"])
    return {
        "customer": customer_doc,
        "cloud_subscriptions": cloud_subscriptions,
        "invoices": invoices
    }