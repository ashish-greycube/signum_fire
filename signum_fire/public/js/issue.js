frappe.ui.form.on("Issue",{
    setup: function(frm){
        frm.set_query("custom_issue_sub_type", function(){
            if (frm.doc.issue_type){
                return {
                    query: "signum_fire.api.get_issue_sub_type",
                    filters: {
                        issue_type: frm.doc.issue_type
                    },
                };
            }
        })

    },

    issue_type: function(frm){
        frm.set_value("custom_issue_sub_type", "")
    }
})