$(document).ready(function() {
    var customer = frappe.utils.get_url_arg("customer");
    frappe.call({
        method: "cloud_manager.cloud_manager.api.get_customer_data",
        args: { customer: customer },
        callback: function(r) {
            var data = r.message;
            $("#customer-profile").append("<h3>Welcome, " + data.customer.customer_name + "</h3>");
            var sub_html = "<ul>";
            data.cloud_subscriptions.forEach(sub => {
                sub_html += "<li>" + sub.plan + " | " + sub.start_date + " (" + sub.status + ")</li>";
            });
            $("#cloud_subscriptions").html(sub_html + "</ul>");
            var inv_html = "<ul>";
            data.invoices.forEach(inv => {
                inv_html += "<li>" + inv.name + " - " + inv.total_amount + " - " + inv.invoice_date + " (" + inv.status + ")</li>";
            });
            $("#invoices").html(inv_html + "</ul>");
        }
    });
});