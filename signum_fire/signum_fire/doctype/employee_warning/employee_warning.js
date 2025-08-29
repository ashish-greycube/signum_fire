// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee Warning", {
    warning_type(frm) {
        if (frm.doc.employee == null && frm.doc.warning_type != ""){
            frm.set_value('warning_type', "")
            frappe.throw("Please Select Employee First.")
        }

        frm.call({
            method: "validate_warning_selection",
            args: {
                'self': frm.doc
            }
        })
    },

    print(frm) {
        if (frm.is_dirty()){
            frappe.throw("Please Save Form To Open PDF")
        }

        frm.call({
            method: "open_pdf",
            args: {
                'docname': frm.doc.name,
                'print_format': frm.doc.warning_type,
            },
            callback: function (res) {
                console.log(res.message)
                var w = window.open(
                    res.message
                );
            }
        })
    },


    setup(frm) {
        frm.set_query("previous_letter_number", function() {
            return {
                filters: {
                    'employee' : frm.doc.employee
                }
            }
        })
    }
});
