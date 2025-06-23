import frappe

@frappe.whitelist(allow_guest=True)
def get_dashboard_data():
    if not frappe.session.user or frappe.session.user == "Guest":
        return {"error": "Please log in"}
    
    user = frappe.session.user
    customer = frappe.get_all("Cloud Customer", filters={"email": user}, fields=["name", "customer_name"])
    if not customer:
        return {"error": "No customer found"}
    
    customer_id = customer[0].name
    servers = frappe.get_all("Cloud Server", filters={"customer_id": customer_id}, fields=["server_name", "server_type", "status"])
    storage_plans = frappe.get_all("Storage Plan", filters={"customer_id": customer_id}, fields=["plan_name", "storage_size", "status"])
    billing_records = frappe.get_all("Billing Record", filters={"customer_id": customer_id}, fields=["resource_type", "amount", "status", "due_date"])
    access_keys = frappe.get_all("Access Key", filters={"customer_id": customer_id}, fields=["key_name", "permissions", "status"])
    
    return {
        "customer": customer[0],
        "servers": servers,
        "storage_plans": storage_plans,
        "billing_records": billing_records,
        "access_keys": access_keys
    }