app_name = "gh"
app_title = "Gh"
app_publisher = "slnee"
app_description = "this app for gh company"
app_email = "rashed.alqadi@slnee.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gh/css/gh.css"
# app_include_js = "/assets/gh/js/gh.js"

# include js, css files in header of web template
# web_include_css = "/assets/gh/css/gh.css"
# web_include_js = "/assets/gh/js/gh.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gh/public/scss/website"

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "gh.utils.jinja_methods",
# 	"filters": "gh.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gh.install.before_install"
# after_install = "gh.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gh.uninstall.before_uninstall"
# after_uninstall = "gh.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "gh.utils.before_app_install"
# after_app_install = "gh.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "gh.utils.before_app_uninstall"
# after_app_uninstall = "gh.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gh.notifications.get_notification_config"

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

doc_events = {
	"Quotation": {
		"validate": "gh.overrides.quotation_common.override_calculate_taxes_and_totals",
        "after_insert":"gh.overrides.quotation_common.recalculate_item_values",
        "before_submit":"gh.overrides.quotation_common.recalculate_item_values",
	},
    "Sales Order":{
        "validate": "gh.overrides.quotation_common.override_calculate_taxes_and_totals",
        "after_insert":"gh.overrides.quotation_common.recalculate_item_values",
        "before_submit":"gh.overrides.quotation_common.recalculate_item_values",
	},
    "Sales Invoice":{
        "validate": "gh.overrides.quotation_common.override_calculate_taxes_and_totals",
        "after_insert":"gh.overrides.quotation_common.recalculate_item_values",
        "before_submit":"gh.overrides.quotation_common.recalculate_item_values",
	},
    "Delivery Note":{
        "validate": "gh.overrides.quotation_common.override_calculate_taxes_and_totals",
        "after_insert":"gh.overrides.quotation_common.recalculate_item_values",
        "before_submit":"gh.overrides.quotation_common.recalculate_item_values",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gh.tasks.all"
# 	],
# 	"daily": [
# 		"gh.tasks.daily"
# 	],
# 	"hourly": [
# 		"gh.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gh.tasks.weekly"
# 	],
# 	"monthly": [
# 		"gh.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "gh.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gh.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gh.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gh.utils.before_request"]
# after_request = ["gh.utils.after_request"]

# Job Events
# ----------
# before_job = ["gh.utils.before_job"]
# after_job = ["gh.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"gh.auth.validate"
# ]
