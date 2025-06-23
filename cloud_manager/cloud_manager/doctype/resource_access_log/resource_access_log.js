frappe.ui.form.on("Resource Access Log", {
    refresh: function(frm) {
        if (!frappe.user.has_role("Cloud Admin")) {
            frm.disable_form();
        }
    }
});