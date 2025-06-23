frappe.ui.form.on("Support Ticket", {
    refresh: function(frm) {
        if (frm.doc.status === "Closed") {
            frm.disable_form();
        }
    }
});