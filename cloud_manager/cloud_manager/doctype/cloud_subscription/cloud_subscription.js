 frappe.ui.form.on("Cloud Subscription", {
         refresh: function(frm) {
             if (frappe.user.has_role("Cloud Admin")) {
                 frm.add_custom_button(__("Generate Invoice"), function() {
                     frappe.call({
                         method: "cloud_manager.cloud_manager.doctype.cloud_subscription.cloud_subscription.generate_invoice",
                         args: { docname: frm.doc.name },
                         callback: function(r) {
                             if (r.message) {
                                 frappe.msgprint(__("Invoice generated: ") + r.message);
                                 frappe.set_route('Form', 'Cloud Invoice', r.message);
                             } else {
                                 frappe.msgprint(__("Failed to generate invoice: No response from server."));
                             }
                         },
                         error: function(err) {
                             frappe.msgprint(__("Error generating invoice: ") + (err.message || "Unknown error"));
                         }
                     });
                 });
             }
         }
     });