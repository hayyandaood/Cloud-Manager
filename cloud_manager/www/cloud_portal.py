# import frappe
# from frappe.website.website_generator import WebsiteGenerator

# class CloudPortal(WebsiteGenerator):
#     def get_context(self, context):
#         customer = frappe.form_dict.get("customer") or frappe.db.get_value("Cloud Customer", {"email": frappe.session.user}, "name")
#         if customer:
#             context["customer"] = frappe.get_doc("Cloud Customer", customer)
#         context.no_cache = True


import frappe
from frappe import _

def get_context(context):
    # Log to see if function is called (for debugging)
    frappe.log_error("DEBUG: cloud_portal.get_context called", "CloudPortal")

    # Only allow users with role "Cloud Customer"
    if "Cloud Customer" not in frappe.get_roles():
        frappe.throw(_("Access denied. Please log in as a Cloud Customer."), frappe.PermissionError)

    # Try to get customer ID from form_dict (URL params)
    customer_id = frappe.form_dict.get("customer")

    # If no customer ID in URL, check cache/session for stored customer ID
    if not customer_id:
        customer_id = frappe.cache().get_value(f"user_customer_{frappe.session.user}")

    # If still no customer ID, try to detect from logged in user's email
    if not customer_id:
        customer_id = frappe.db.get_value("Cloud Customer", {"email": frappe.session.user}, "name")
        if not customer_id:
            frappe.throw(_("Customer not found for user {0}").format(frappe.session.user))
        # Store customer_id in cache for this user for next requests
        frappe.cache().set_value(f"user_customer_{frappe.session.user}", customer_id)

    # If URL param and cache differ, you can choose to update cache or redirect, here we trust detected customer_id

    try:
        # Fetch full customer doc
        customer = frappe.get_doc("Cloud Customer", customer_id)

        # Fetch related subscriptions
        subscriptions = frappe.get_all(
            "Cloud Subscription",
            filters={"customer": customer_id},
            fields=["name", "plan", "start_date", "end_date", "status"]
        )

        # Fetch related servers (only those linked to the subscriptions)
        servers = frappe.get_all(
            "Cloud Server",
            filters={"cloud_subscription": ["in", [s.name for s in subscriptions]]},
            fields=["name", "resource_name", "cloud_subscription"]
        )

        # Fetch invoices for the customer
        invoices = frappe.get_all(
            "Cloud Invoice",
            filters={"customer": customer_id},
            fields=["name", "invoice_date", "total_amount", "status"]
        )

        # Pass data to the template context
        context.customer = customer
        context.subscriptions = subscriptions
        context.servers = servers
        context.invoices = invoices
        context.no_cache = 1

    except Exception as e:
        frappe.log_error(f"Error in cloud_portal.get_context: {str(e)}", "CloudPortal")
        frappe.throw(_("An error occurred while fetching your data. Please try again later."))
