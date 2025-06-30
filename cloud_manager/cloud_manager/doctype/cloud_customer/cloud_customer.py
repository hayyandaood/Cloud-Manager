import frappe
from frappe.model.document import Document

class CloudCustomer(Document):
    def validate(self):
        if self.is_new() and frappe.db.exists("Cloud Customer", {"email": self.email, "name": ["!=", self.name]}):
            frappe.throw("Email already exists")

    def on_update(self):
        self.add_user()
        pass

    def add_user(self):
        if not self.customer_user:
            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.customer_name,
                "enabled": 1,
                "user_type": "Website User",
                "send_welcome_email": 0
            })
            user.append("roles", {"role": "Cloud Customer"})
            user.insert(ignore_permissions=True)
            self.customer_user = user.name
        else:
            frappe.db.set_value("User", self.customer_user, "first_name", self.customer_name)
        

    @staticmethod
    @frappe.whitelist()
    def send_welcome_email(customer):
        customer_doc = frappe.get_doc("Cloud Customer", customer)
        frappe.sendmail(
            recipients=[customer_doc.email],
            subject="Welcome to Cloud Manager",
            message="Dear {0},<br>Welcome to Cloud Manager! Access your portal at /cloud-portal.".format(customer_doc.customer_name)
        )
    