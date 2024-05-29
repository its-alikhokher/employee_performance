// Copyright (c) 2024, ali@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Performance Evaluation"] = {
	"filters": [
		{
            "fieldname": "employee_name",
            "label": __("Employee Name"),
            "fieldtype": "Link",
            "options": "Employee"
        }
    ]
};