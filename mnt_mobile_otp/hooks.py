# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mnt_mobile_otp"
app_title = "MNT Mobile OTP"
app_publisher = "MN Technique"
app_description = "Frappe OAuth 2.0 based app for Mobile/OTP login"
app_icon = "fa fa-mobile"
app_color = "orange"
app_email = "support@mntechnique.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mnt_mobile_otp/css/mnt_mobile_otp.css"
# app_include_js = "/assets/mnt_mobile_otp/js/mnt_mobile_otp.js"

# include js, css files in header of web template
# web_include_css = "/assets/mnt_mobile_otp/css/mnt_mobile_otp.css"
# web_include_js = "/assets/mnt_mobile_otp/js/mnt_mobile_otp.js"

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

# Website user home page (by function)
# get_website_user_home_page = "mnt_mobile_otp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mnt_mobile_otp.install.before_install"
# after_install = "mnt_mobile_otp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mnt_mobile_otp.notifications.get_notification_config"

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
# 		"mnt_mobile_otp.tasks.all"
# 	],
# 	"daily": [
# 		"mnt_mobile_otp.tasks.daily"
# 	],
# 	"hourly": [
# 		"mnt_mobile_otp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mnt_mobile_otp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mnt_mobile_otp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mnt_mobile_otp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mnt_mobile_otp.event.get_events"
# }

