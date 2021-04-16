# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cheque"
app_title = "Cheque"
app_publisher = "erpcloud.systems"
app_description = "cheque management system"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mg@erpcloud.systems"
app_license = "MIT"
doctype_js = { "doctype": "Custom Script", "filters": [ ["name", "in", ( "Cheque-Client","Payment Entry-Client","Journal Entry-Client", )] ] }
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cheque/css/cheque.css"
# app_include_js = "/assets/cheque/js/cheque.js"

# include js, css files in header of web template
# web_include_css = "/assets/cheque/css/cheque.css"
# web_include_js = "/assets/cheque/js/cheque.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cheque/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cheque.install.before_install"
# after_install = "cheque.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cheque.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cheque.tasks.all"
# 	],
# 	"daily": [
# 		"cheque.tasks.daily"
# 	],
# 	"hourly": [
# 		"cheque.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cheque.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cheque.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cheque.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cheque.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cheque.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

