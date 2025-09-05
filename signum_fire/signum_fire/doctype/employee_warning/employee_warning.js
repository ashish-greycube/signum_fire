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
        if (frm.is_dirty()) {
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
        frm.set_query("previous_letter_number", function () {

            if (frm.doc.warning_type == "Second Letter For Breach Of Discipline Coming Late") {
                warning_type_selected = "First Warning Letter For Late Coming"
            }
            else if (frm.doc.warning_type == 'Second Letter Of Warning For Neglecting The Duties') {
                warning_type_selected = 'First Letter Of Warning For Neglecting The Duties'
            }

            return {
                filters: {
                    'employee': frm.doc.employee,
                    'warning_type': warning_type_selected,
                    'docstatus' : 1
                }
            }
        })

        if (frm.doc.docstatus == 2) {
            frm.set_df_property("print", "hidden", 1)
        }
        else if (frm.doc.docstatus != 2) {
            frm.set_df_property("print", "hidden", 0)
        }
    },

    previous_letter_number(frm) {
        if (frm.doc.previous_letter_number != null) {
            frappe.db.get_value("Employee Warning", frm.doc.previous_letter_number, "warning_date").then(res => {
                console.log(res)
                frm.set_value("previous_letter_date", res.message.warning_date)
            })
        }
    }
});
