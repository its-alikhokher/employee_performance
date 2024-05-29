// Copyright (c) 2024, ali@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Dynamic Doctype Report"] = {
    "filters": [
        {
            "fieldname": "doctype",
            "label": __("Doctype"),
            "fieldtype": "Link",
            "options": "DocType",
            "reqd": 1,
            "default": ""
        }
    ]
};
