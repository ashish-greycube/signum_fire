import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_issue_sub_type(doctype, txt, searchfield, start, page_len, filters):
	issue_type = filters.get("issue_type")
	return frappe.get_all(
		"Issue Sub Type Details",
		parent_doctype="Issue Type",
		filters={"parent": issue_type,"issue_sub_type": ("like", f"{txt}%")},
		fields=["distinct issue_sub_type"],
		as_list=1,
	)