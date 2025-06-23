frappe.ui.form.on("Access Token", {
    refresh: function(frm) {
        if (frm.doc.token && frm.is_new()) {
            frappe.msgprint(__("Token created: " + frm.doc.token + ". Copy it now as it won't be shown again."));
            frm.set_df_property("token", "hidden", 1);
        }
    }
});