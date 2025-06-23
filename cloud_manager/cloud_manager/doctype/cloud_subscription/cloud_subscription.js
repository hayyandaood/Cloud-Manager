frappe.ui.form.on("Cloud Subscription", {
    refresh: function(frm) {
        if (frappe.user.has_role("Cloud Admin")) {
            frm.add_custom_button(__("Generate Invoice"), function() {
                frappe.call({
                    method: "cloud_manager.cloud_manager.doctype.cloud_subscription.cloud_subscription.generate_invoice",
                    args: { cloud_subscription: frm.doc.name },
                    callback: function(r) {
                        frappe.msgprint(__("Invoice generated: " + r.message));
                    }
                });
            });
        }
    }
});