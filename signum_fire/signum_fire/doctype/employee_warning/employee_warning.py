# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.desk.form.utils import get_pdf_link
from frappe.model.document import Document

class EmployeeWarning(Document):
	def validate(self):
		validate_warning_selection(self)

@frappe.whitelist()
def open_pdf(docname, print_format):
	doc = frappe.get_doc("Employee Warning", docname)
	pdf = get_pdf_link(doc.doctype, doc.name, print_format, no_letterhead=0)
	pdf = pdf + "&letterhead=Letterhead-General"
	print(pdf)
	return pdf
	
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
				"docstatus" : 1
			},
			fields = ["name"]
		)
		if first_warning == None or first_warning == []:
			frappe.throw("Cannot create Second Warning before creation of First Warning")

		both_are_created = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : ["in", ["First Letter Of Warning For Neglecting The Duties", "Second Letter Of Warning For Neglecting The Duties"]],
				"docstatus" : 1
			},
			fields = ["name"]
		)
		if len(both_are_created) >= 2:
			frappe.throw("First and Second Warnings already created.")

	elif selected_warning == "First Letter Of Warning For Neglecting The Duties":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : ["in", ["First Letter Of Warning For Neglecting The Duties", "Second Letter Of Warning For Neglecting The Duties"]],
				'docstatus' : 1
			},
			fields = ["name"]
		)
		if len(first_warning) >= 2:
			frappe.throw("First and Second Warnings already created.")

		is_one_created = frappe.db.get_value("Employee Warning", {'employee':self.employee, 'warning_type':'First Letter Of Warning For Neglecting The Duties', 'docstatus' : 1}, ['name'])
		if is_one_created != None and is_one_created != self.name: 
			frappe.throw("First Warning Letter is already created. Cannot create it again.")

	elif selected_warning == "Second Letter For Breach Of Discipline Coming Late":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : "First Warning Letter For Late Coming",
				"docstatus" : 1
			},
			fields = ["name"]
		)
		if first_warning == None or first_warning == []:
			frappe.throw("Cannot create Second Warning before creation of First Warning")

		both_are_created = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : ["in", ["First Warning Letter For Late Coming", "Second Letter For Breach Of Discipline Coming Late"]],
				"docstatus" : 1
			},
			fields = ["name"]
		)
		if len(both_are_created) >= 2:
			frappe.throw("First and Second Warnings already created.")
			
	elif selected_warning == "First Warning Letter For Late Coming":
		first_warning = frappe.db.get_all(
			doctype = "Employee Warning",
			filters = {
				"employee" : self.employee,
				"warning_type" : ["in", ["First Warning Letter For Late Coming", "Second Letter For Breach Of Discipline Coming Late"]],
				'docstatus' : 1
			},
			fields = ["name"]
		)
		if len(first_warning) >= 2:
			frappe.throw("First and Second Warnings already created.")


		is_one_created = frappe.db.get_value("Employee Warning", {'employee':self.employee, 'warning_type':'First Warning Letter For Late Coming', 'docstatus' : 1}, ['name'])
		if  is_one_created != None and is_one_created != self.name: 
			frappe.throw("First Warning Letter is already created. Cannot create it again.")