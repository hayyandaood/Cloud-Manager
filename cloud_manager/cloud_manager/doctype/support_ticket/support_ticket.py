import frappe
from frappe.model.document import Document

class SupportTicket(Document):
    def on_update(self):
        settings = frappe.get_single("Cloud Manager Settings")
        if settings.support_email and self.status == "Open":
            frappe.sendmail(
                recipients=[settings.support_email],
                subject=f"New Support Ticket: {self.subject}",
                message=self.description
            )