frappe.ui.form.on("Cloud Subscription Plan", {
    refresh: function(frm) {
        if (!frappe.user.has_role("Cloud Admin")) {
            frm.disable_form();
        }
    }
});