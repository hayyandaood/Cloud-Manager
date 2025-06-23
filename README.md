Cloud Manager App
A Frappe-based application for managing cloud infrastructure services, including customers, servers, billing, and support.
Features

Customer Management: Store and manage customer details with portal access.
Cloud Servers: Track VPS/storage instances with usage and access logs.
Cloud Subscriptions: Manage subscription plans and billing cycles.
Billing: Generate itemized invoices and record payments.
Customer Portal: Unified dashboard with resources, cloud subscriptions, and invoices.
Support: Raise and track support tickets.
API: Secure REST endpoints with token-based authentication.
Dashboard: Customizable dashboard for customer usage and status visualization.

Installation

Install Frappe v15+ and MariaDB/PostgreSQL.
Clone the repository: git clone https://github.com/your-repo/cloud_manager.git
Install the app: bench --site site_name install-app cloud_manager
Run migrations: bench --site site_name migrate
Load fixtures: bench --site site_name import-fixtures

Usage

Admin Access: Log in to the Frappe Desk with the Cloud Admin role.
Customer Portal: Access at /cloud-portal with the Cloud Customer role.
API: Use endpoints like /api/method/cloud_manager.api.get_server_details with access tokens.

Fixtures
Sample Cloud Subscription Plan data in fixtures/cloud_subscription_plan.json.
Permissions

Cloud Admin: Full access to all DocTypes.
Cloud Staff: Read/write/create access to most DocTypes, no delete/submit.
Cloud Customer: Restricted access to their own data with user_permission_applies.

Development Notes

Built with Frappe v15+, leveraging built-in web framework for the portal.
Child tables (Server Usage Log, Invoice Item) ensure scalability.
Secure API with token-based authentication.
