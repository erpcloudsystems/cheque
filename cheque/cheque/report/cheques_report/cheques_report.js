// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Cheques Report"] = {
	"filters": [
		{
			"fieldname":"type",
			"label": __("Type"),
			"fieldtype": "Select",
			"options": ["Pay","Receive","Internal Transfer"]
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options":  ["جديد","مظهر","تحت التحصيل","محصل","مرفوض بالبنك","حافظة شيكات مرجعة","مردود","مدفوع","محصل فوري"]
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date")
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_end_date")
		},
		{
			"fieldname":"bank",
			"label": __("Bank"),
			"fieldtype": "Link",
			"options": "Bank Account"
		}
	]
}
