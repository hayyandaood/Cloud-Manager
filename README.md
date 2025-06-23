# Cloud Manager App for Frappe

This is a custom Frappe 15+ application to manage cloud infrastructure services like VPS, cloud storage, and billing — all in one place.

---

## Features

- Manage **Cloud Customers** and their contact info  
- Track active **Cloud Resources** (servers, storage)  
- Handle **Subscriptions** and recurring billing plans  
- Create and track **Invoices** and **Payments**  
- Log resource access with **Resource Access Logs**  
- Role-based access control: Staff vs Customer roles  
- Customer portal with dedicated pages for resources, invoices, and subscriptions

---

## Setup Instructions

### Prerequisites

- Frappe Framework 15+ installed and bench initialized  
- MariaDB/PostgreSQL database configured  

### Installation

1. Copy the `cloud_manager` folder to your bench apps folder:

```bash
cp -r cloud_manager ~/frappe-bench/apps/
