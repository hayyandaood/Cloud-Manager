frappe.ui.form.on("Cloud Manager Settings", {
    refresh: function(frm) {
        if (!frappe.user.has_role("Cloud Admin")) {
            frm.disable_form();
        }
    }
});