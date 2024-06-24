import frappe
from frappe.contacts.doctype.address.address import get_default_address,render_address

@frappe.whitelist()
def get_company_bank_address(doc):
    doc = frappe.get_list('Bank Account', filters={'is_default': 1, 'is_company_account':1}, 
                          fields=['name'], limit=1)
    bank_address_name=get_default_address('Bank Account',doc[0].name)
    address = render_address(bank_address_name)
    return address

@frappe.whitelist()
def get_supplier_bank_address(doc):
    supplier_bank = frappe.get_list('Bank Account', 
	filters={'party_type':'Supplier', 'party': doc}, fields=['name'], limit=1)
    bank_address_name=get_default_address('Bank Account',supplier_bank[0].name)
    supplier_address = render_address(bank_address_name)
    return supplier_address

@frappe.whitelist()
def get_unique_hsc_code_of_item(parent, hsn_code):
    po_items = frappe.get_list('Purchase Order Item', parent_doctype='Purchase Order', 
						filters={'parent': parent}, 
						fields=['description', 'gst_hsn_code', 'qty'])
    unique_hsn_code = []
    for item in po_items:
        if item.gst_hsn_code not in unique_hsn_code:
            unique_hsn_code.append(item.gst_hsn_code)	

    print(unique_hsn_code, '---unique_hsn_code')
    decs = []
    for hsn in unique_hsn_code:
        if hsn == hsn_code:
            for values in po_items:
                decs.append(values.description)
    
    print(decs, '--------desc')
    return decs