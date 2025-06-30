frappe.ui.form.on("Cloud Invoice", {
    refresh: function(frm) {
        frm.set_query('cloud_subscription', function() {
            return {
                filters: {
                    'customer': frm.doc.customer || ''
                }
            };
        });

        frm.set_query('server', 'items', function(doc, cdt, cdn) {
            return {
                filters: {
                    'cloud_subscription': frm.doc.cloud_subscription || ''
                }
            };
        });
    },
    customer: function(frm) {
        // Refresh cloud_subscription field when customer changes
        frm.set_value('cloud_subscription', '');
        frm.refresh_field('cloud_subscription');
    },

    cloud_subscription: function(frm) {
        // Refresh server field in child table when cloud_subscription changes
        frm.refresh_field('items');
    },
    items: function(frm) {
        let total = 0;
        frm.doc.items.forEach(item => {
            total += item.amount || 0;
        });
        frm.set_value("total_amount", total);
    }
});
