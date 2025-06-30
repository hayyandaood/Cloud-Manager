import frappe
from frappe.model.document import Document
import logging
from datetime import datetime

class CloudSubscription(Document):
    def validate(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            frappe.throw("End Date must be after Start Date")
        if self.status == "Active" and not self.end_date:
            frappe.throw("Active subscriptions must have an End Date")

@frappe.whitelist()
def generate_invoice(docname):
    try:
        subscription = frappe.get_doc("Cloud Subscription", docname)

        # Validate subscription
        if not subscription.customer or not subscription.plan:
            frappe.throw(f"Customer and Plan are required for subscription {subscription.name}")

        plan = frappe.get_doc("Cloud Subscription Plan", subscription.plan)
        if not plan.monthly_price:
            frappe.throw(f"No monthly price defined for plan {subscription.plan}")

        servers = frappe.db.get_list(
            "Cloud Server",
            filters={"cloud_subscription": subscription.name},
            fields=["name", "resource_name"]
        )
        if not servers:
            frappe.throw(f"No servers found for subscription {subscription.name}")

        invoice = frappe.get_doc({
            "doctype": "Cloud Invoice",
            "customer": subscription.customer,
            "cloud_subscription": subscription.name,
            "invoice_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "Draft",
            "items": []
        })

        total_amount = 0
        for server in servers:
            item = {
                "doctype": "Cloud Invoice Item",
                "description": f"Subscription: {subscription.plan} for {server.resource_name}",
                "server": server.name,
                "amount": plan.monthly_price
            }
            invoice.append("items", item)
            total_amount += plan.monthly_price

        invoice.total_amount = total_amount
        invoice.insert(ignore_permissions=True)
        frappe.db.commit()

        logging.info(f"Generated invoice {invoice.name} for subscription {subscription.name}")
        return invoice.name

    except Exception as e:
        logging.error(f"Error generating invoice for subscription {docname}: {str(e)}")
        frappe.throw(f"Failed to generate invoice: {str(e)}")
