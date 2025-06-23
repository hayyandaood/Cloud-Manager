frappe.ui.form.on("Dashboard Configuration", {
    refresh: function(frm) {
        if (frappe.user.has_role("Cloud Admin")) {
            frm.add_custom_button(__("Preview Dashboard"), function() {
                frappe.msgprint(__("Dashboard preview would load here with selected options."));
            });
        }
    }
});