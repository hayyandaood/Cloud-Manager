import frappe
import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def import_fixtures(file_path, doctype=None):
    if not os.path.exists(file_path):
        logging.error(f"Fixture file not found: {file_path}")
        return
    try:
        with open(file_path, 'r') as f:
            fixtures = json.load(f)
        for doc in fixtures:
            try:
                doctype = doc.get('doctype')
                if not frappe.db.exists('DocType', doctype):
                    logging.error(f"DocType {doctype} does not exist. Skipping {doc.get('name')}")
                    continue
                if frappe.db.exists(doctype, doc.get('name')):
                    logging.info(f"Skipping existing {doctype}: {doc.get('name')}")
                    continue
                new_doc = frappe.get_doc(doc)
                new_doc.insert(ignore_permissions=True)
                logging.info(f"Imported {doctype}: {doc.get('name')}")
            except Exception as e:
                logging.error(f"Error importing {doctype}: {doc.get('name')} - {str(e)}")
        frappe.db.commit()
    except Exception as e:
        logging.error(f"Failed to process fixture file {file_path}: {str(e)}")

def main():
    frappe.init(site='dev-test')
    frappe.connect()
    
    # Dynamically resolve the app path
    app_path = os.path.join(frappe.get_app_path('cloud_manager'), 'fixture')
    
    # Import Cloud Subscription Plan first
    fixture_path = os.path.join(app_path, 'cloud_subscription_plan.json')
    import_fixtures(fixture_path, doctype='Cloud Subscription Plan')
    
    # Import dummy data
    fixture_path = os.path.join(app_path, 'dummy_data.json')
    import_fixtures(fixture_path)

if __name__ == "__main__":
    main()
