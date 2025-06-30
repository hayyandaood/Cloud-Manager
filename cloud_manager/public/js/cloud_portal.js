frappe.ready(function() {
    var customer_id = frappe.utils.get_url_arg("customer") || customer_id;
    if (!customer_id) {
        frappe.msgprint("Customer ID required");
        return;
    }
    
    frappe.call({
        method: "cloud_manager.api.get_customer_data",
        args: { customer_id: customer_id },
        callback: function(r) {
            if (r.message) {
                var data = r.message;
                $("#customer-profile").html(`
                    <p><strong>Name:</strong> ${data.customer.customer_name}</p>
                    <p><strong>Email:</strong> ${data.customer.email}</p>
                    <p><strong>Phone:</strong> ${data.customer.phone}</p>
                    <p><strong>Address:</strong> ${data.customer.address}</p>
                `);
                
                var subscriptions_html = data.subscriptions.map(sub => `
                    <p>${sub.name}: ${sub.plan} (${sub.status})</p>
                `).join("");
                $("#cloud_subscriptions").html(subscriptions_html);
                
                var servers_html = data.servers.map(server => `
                    <p>${server.resource_name}: ${server.resource_type} (${server.status})</p>
                `).join("");
                $("#servers").html(servers_html);
                
                var invoices_html = data.invoices.map(inv => `
                    <p>${inv.name}: ${inv.total_amount} (${inv.status})</p>
                `).join("");
                $("#invoices").html(invoices_html);
            }
        }
    });
});