frappe.ui.form.on("Cloud Invoice", {
    refresh: function(frm) {
        if (frm.doc.status === "Draft" && frappe.user.has_role("Cloud Admin")) {
            frm.add_custom_button(__("Submit Invoice"), function() {
                frm.call("submit").then(() => frm.reload_doc());
            });
        }
    },
    items: function(frm) {
        let total = 0;
        frm.doc.items.forEach(item => {
            total += item.amount || 0;
        });
        frm.set_value("total_amount", total);
    }
});