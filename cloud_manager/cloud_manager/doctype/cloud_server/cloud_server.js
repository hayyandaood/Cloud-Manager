frappe.ui.form.on("Cloud Server", {
    refresh: function(frm) {
        if (frappe.user.has_role("Cloud Admin")) {
            frm.add_custom_button(__("Log Sample Usage"), function() {
                frappe.call({
                    method: "cloud_manager.cloud_manager.doctype.cloud_server.cloud_server.log_usage",
                    args: {
                        docname: frm.doc.name,
                        cpu: 50,
                        ram: 4,
                        storage: 100
                    },
                    callback: function(r) {
                        frm.reload_doc();
                    }
                });
            });
        }
    },
    subscription: function(frm) {
        if (frm.doc.subscription) {
            frappe.db.get_doc("Cloud Subscription", frm.doc.subscription).then(sub => {
                frappe.db.get_doc("Cloud Subscription Plan", sub.plan).then(plan => {
                    frm.set_value("cpu_cores", plan.cpu_cores);
                    frm.set_value("ram_gb", plan.ram_gb);
                    frm.set_value("storage_gb", plan.storage_gb);
                });
            });
        }
    }
});