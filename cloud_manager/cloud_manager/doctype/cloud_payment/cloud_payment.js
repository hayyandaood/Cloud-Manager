frappe.ui.form.on("Cloud Payment", {
    cloud_invoice: function(frm) {
        if (frm.doc.cloud_invoice) {
            frappe.db.get_value("Cloud Invoice", frm.doc.cloud_invoice, "total_amount", amount => {
                frm.set_value("amount", amount.total_amount);
            });
        }
    }
});