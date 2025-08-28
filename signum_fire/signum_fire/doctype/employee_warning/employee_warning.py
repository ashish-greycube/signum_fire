# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class EmployeeWarning(Document):
	pass
@frappe.whitelist()
def validate_warning_selection(self):
	self = frappe.parse_json(self)
	selected_warning = self.warning_type
	if selected_warning == "Second Letter Of Warning For Neglecting The Duties":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : "First Letter Of Warning For Neglecting The Duties",
			},
			fields = ["name"]
		)
		if first_warning == None or first_warning == []:
			frappe.throw("Cannot create Second Warning before creation of First Warning")

	elif selected_warning == "First Letter Of Warning For Neglecting The Duties":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : ["in", ["First Letter Of Warning For Neglecting The Duties", "Second Letter Of Warning For Neglecting The Duties"]],
			},
			fields = ["name"]
		)
		if len(first_warning) == 2:
			frappe.throw("First and Second Warnings already created.")

	elif selected_warning == "Second Letter For Breach Of Discipline Coming Late":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : "First Warning Letter For Late Coming",
			},
			fields = ["name"]
		)
		if first_warning == None or first_warning == []:
			frappe.throw("Cannot create Second Warning before creation of First Warning")
			
	elif selected_warning == "First Warning Letter For Late Coming":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : ["in", ["First Warning Letter For Late Coming", "Second Letter For Breach Of Discipline Coming Late"]],
			},
			fields = ["name"]
		)
		if len(first_warning) == 2:
			frappe.throw("First and Second Warnings already created.")