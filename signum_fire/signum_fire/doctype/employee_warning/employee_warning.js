// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee Warning", {
	warning_type(frm) {
        frm.call({
            method: "validate_warning_selection",
            args : {
                'self' : frm.doc
            }
        })
	},
});
