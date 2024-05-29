# Copyright (c) 2024, ali@gmail.com and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    doctype = filters.get("doctype")
    if not doctype:
        frappe.throw("Please select a Doctype to generate the report.")

    # Fetch metadata for the selected doctype
    meta = frappe.get_meta(doctype)
    
    # Collecting only valid fields that can be directly queried
    valid_fieldtypes = ['Data', 'Int', 'Float', 'Date', 'Datetime', 'Currency', 'Check', 'Link', 'Select', 'Text', 'Small Text', 'Long Text', 'Read Only', 'Time']
    fields = [
        df.fieldname for df in meta.fields 
        if df.fieldtype in valid_fieldtypes and df.fieldname != "show_document"
    ]
    fields.insert(0, "name")  # Always include the name field

    # Generate columns for the report
    columns = [{"fieldname": field, "label": field.replace('_', ' ').title(), "fieldtype": "Data"} for field in fields]
    
    try:
        # Fetch data from the doctype using the valid fields
        data = frappe.get_all(doctype, fields=fields)
    except Exception as e:
        frappe.throw(str(e))
    
    return columns, data

