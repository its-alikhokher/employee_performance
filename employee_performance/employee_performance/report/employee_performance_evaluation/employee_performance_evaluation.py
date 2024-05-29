# Copyright (c) 2024, ali@gmail.com and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    columns = [
        {
            "fieldname": "employee_name",
            "label": "Employee Name",
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname": "task",
            "label": "Task",
            "fieldtype": "Link",
            "options": "ToDo"
        },
        {
            "fieldname": "attendance",
            "label": "Attendance",
            "fieldtype": "Data"
        },
        {
            "fieldname": "employee_performance_feedback",
            "label": "Employee Performance Feedback",
            "fieldtype": "Link",
            "options": "Employee Performance Feedback"
        },
        {
            "fieldname": "employee_skill_map",
            "label": "Employee Skill Map",
            "fieldtype": "Link",
            "options": "Employee Skill Map"
        }
    ]
    return columns

def get_data(filters):
    data = []

    my_filter = {}
    if filters.get("employee_name"):
        my_filter["employee_name"] = filters["employee_name"]
    # if filters.get("task"):
    #     my_filter["task"] = filters["task"]
    # if filters.get("attendance"):
    #     my_filter["attendance"] = filters["attendance"]
    # if filters.get("employee_performance_feedback"):
    #     my_filter["employee_performance_feedback"] = filters["employee_performance_feedback"]
    # if filters.get("employee_skill_map"):
    #     my_filter["employee_skill_map"] = filters["employee_skill_map"]

    employees = frappe.get_all("Employee", fields=["*"], filters=my_filter)

    for emp in employees:
        todos = frappe.get_all("ToDo", filters={"allocated_to": emp.user_id}, fields=["*"])
        for todo in todos:
            attendance = frappe.get_all("Attendance", filters={"employee_name": emp.employee_name}, fields=["*"],limit=1)
            for atten in attendance:
                # attendance_date = str(atten.attendance_date)
                feedback = frappe.get_all("Employee Performance Feedback", filters={"employee_name": emp.employee_name}, fields=["*"])
                for feed in feedback:
                    skill_map = frappe.get_all("Employee Skill Map", filters={"employee_name": emp.employee_name}, fields=["*"])
                    for skUll in skill_map:
                            data.append({
                            "employee_name": emp.employee_name,
                            "task": todo.name,
                            "attendance":  " " + atten.status,
                            "employee_performance_feedback": feed.name,
                            "employee_skill_map":skUll.name
                            })

    return data
