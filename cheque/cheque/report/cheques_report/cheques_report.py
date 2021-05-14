# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters,columns)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Payment"),
			"fieldname": "payment_entry",
			"fieldtype": "Link",
			"options": "Payment Entry",
			"width": 120
		},
		{
			"label": _("Cheques No"),
			"fieldname": "reference_no",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Party Type"),
			"fieldname": "party_type",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Party"),
			"fieldname": "party",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Cheque Status"),
			"fieldname": "cheque_status",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Transaction Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Reference Date"),
			"fieldname": "reference_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Clearance Date"),
			"fieldname": "clearance_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Amount"),
			"fieldname": "paid_amount",
			"fieldtype": "Currency",
			"width": 120
		},
		{
			"label": _("Bank"),
			"fieldname": "bank",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Forwarded"),
			"fieldname": "party_",
			"fieldtype": "Data",
			"width": 120
		}
	]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data

def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("type"):
		conditions += " and a.payment_type=%(type)s"
	if filters.get("status"):
		conditions += " and a.cheque_status=%(status)s"
	if filters.get("from_date"):
		conditions += " and a.reference_date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and a.reference_date<=%(to_date)s"
	if filters.get("bank"):
		conditions += " and a.bank_acc=%(bank)s"

	item_results = frappe.db.sql("""
		select
			a.name as payment_entry,
			a.reference_no as reference_no,
			a.party_type as party_type,
			a.Party as party,
			a.cheque_status as cheque_status,
			a.posting_date as posting_date,
			a.reference_date as reference_date,
			a.clearance_date as clearance_date,
			a.paid_amount as paid_amount,
			a.account as bank,
			a.party_ as party_
		from `tabPayment Entry` a
		where
			a.mode_of_payment = "شيك"
			and docstatus =1
			{conditions}
		"""
		.format(conditions=conditions), filters, as_dict=1)

	#price_list_names = list(set([item.price_list_name for item in item_results]))

	#buying_price_map = get_price_map(price_list_names, buying=1)
	#selling_price_map = get_price_map(price_list_names, selling=1)

	result = []
	if item_results:
		for item_dict in item_results:
			data = {
				'payment_entry': item_dict.payment_entry,
				'reference_no': item_dict.reference_no,
				'party_type': item_dict.party_type,
				'party': item_dict.party,
				'cheque_status': item_dict.cheque_status,
				'posting_date': item_dict.posting_date,
				'reference_date': item_dict.reference_date,
				'clearance_date': item_dict.clearance_date,
				'paid_amount': item_dict.paid_amount,
				'bank': item_dict.bank,
				'party_': item_dict.party_
			}
			result.append(data)

	return result

def get_price_map(price_list_names, buying=0, selling=0):
	price_map = {}

	if not price_list_names:
		return price_map

	rate_key = "Buying Rate" if buying else "Selling Rate"
	price_list_key = "Buying Price List" if buying else "Selling Price List"

	filters = {"name": ("in", price_list_names)}
	if buying:
		filters["buying"] = 1
	else:
		filters["selling"] = 1

	pricing_details = frappe.get_all("Item Price",
		fields = ["name", "price_list", "price_list_rate"], filters=filters)

	for d in pricing_details:
		name = d["name"]
		price_map[name] = {
			price_list_key :d["price_list"],
			rate_key :d["price_list_rate"]
		}

	return price_map


