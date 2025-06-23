frappe.ui.form.on("Cloud Customer", {
    // refresh: function(frm) {
    //     if (!frm.doc.__islocal && frm.doc.customer_user && frappe.user.has_role("Cloud Admin")) {
    //         frm.add_custom_button(__("Send Welcome Email"), function() {
    //             frappe.call({
    //                 method: "cloud_manager.cloud_manager.doctype.cloud_customer.cloud_customer.send_welcome_email",
    //                 args: { customer: frm.doc.name },
    //                 callback: function(r) {
    //                     frappe.msgprint(__("Email sent!"));
    //                 }
    //             });
    //         });
    //     }
    // },
    validate: function(frm) {
        if (frm.doc.email && !frappe.utils.validate_type(frm.doc.email, "email")) {
            frappe.msgprint(__("Please enter a valid email address"));
            frm.set_value("email", "");
        }
    }
});