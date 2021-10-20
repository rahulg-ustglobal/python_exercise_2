"""
Program - 5
Write a program to read xml file.
Read parent tag and child tag inside that parent tag.
Read the attribute of that child tag and print the value of that attribute.
Use xml.dom.minidom library
Example - from xml.dom.minidom import parse
Copy the below xml text and save it as .xml file
Use parse(path of xml file) to read xml file from path
<odoo>
<template id="_assets_backend_helpers" inherit_id="web._assets_backend_helpers">
<xpath expr="//link" position="before">
<link rel="stylesheet" type="text/scss"
href="/account/static/src/scss/variables.scss"/>
</xpath>
</template>
<template id="assets_backend" name="account assets" inherit_id="web.assets_backend">
<xpath expr="." position="inside">
<link rel="stylesheet"
href="/account/static/src/css/account_bank_and_cash.css"/>
<link rel="stylesheet" href="/account/static/src/css/account.css"/>
<link rel="stylesheet" type="text/scss"
href="/account/static/src/scss/account_reconciliation.scss"/>
<link rel="stylesheet" type="text/scss"
href="/account/static/src/scss/account_journal_dashboard.scss"/>
<link rel="stylesheet" type="text/scss"
href="/account/static/src/scss/account_dashboard.scss"/>
<link rel="stylesheet"
href="/account/static/src/scss/section_and_note_backend.scss"/>
<script type="text/javascript"
src="/account/static/src/js/reconciliation/reconciliation_action.js"/>
<script type="text/javascript"
src="/account/static/src/js/reconciliation/reconciliation_model.js"/>
<script type="text/javascript"
src="/account/static/src/js/reconciliation/reconciliation_renderer.js"/>
<script type="text/javascript"
src="/account/static/src/js/reconciliation/tour_reconciliation.js"/>
<script type="text/javascript"
src="/account/static/src/js/account_payment_field.js"/>
<script type="text/javascript" src="/account/static/src/js/bank_statement.js"/>
<script type="text/javascript"
src="/account/static/src/js/section_and_note_fields_backend.js"/>
<script type="text/javascript" src="/account/static/src/js/tour.js"/>
</xpath>
</template>
<template id="assets_frontend" name="account assets" inherit_id="web.assets_frontend">
<xpath expr="." position="inside">
<script type="text/javascript"
src="/account/static/src/js/account_portal_sidebar.js"/>
</xpath>
</template>
<template id="qunit_suite" name="account_reconciliation tests"
inherit_id="web.qunit_suite">
<xpath expr="//script[contains(@src, '/web/static/tests/views/kanban_tests.js')]"
position="after">
<script type="text/javascript"
src="/account/static/tests/reconciliation_tests.js"/>
<script type="text/javascript"
src="/account/static/tests/account_payment_field_tests.js"/>
</xpath>
</template>
</odoo>
"""

from xml.dom.minidom import parse

xmldoc = parse('5.python_example.xml')

print()
print("For <1)template ----> id,position,link--->variables.scss> tag ")
print()

template = xmldoc.getElementsByTagName('template')
print("ID:=", template[0].attributes['id'].value)
xpath = xmldoc.getElementsByTagName('xpath')
print("xpath_position:=", xpath[0].attributes['position'].value)
link = xmldoc.getElementsByTagName('link')
print("href:=", link[0].attributes['href'].value.rsplit('/', 1)[-1])

print()
print("For <2)template> ----> <xpath ----> position,link(last_part)> tag ")
print()

template = xmldoc.getElementsByTagName('template')
print("ID:=", template[1].attributes['id'].value)
xpath = xmldoc.getElementsByTagName('xpath')
print("xpath_position:=", xpath[1].attributes['position'].value)
xpath = xmldoc.getElementsByTagName('xpath')
print(xpath[1].attributes['position'].value)
link = xmldoc.getElementsByTagName('link')
for href in link:
    print("href-->last_part|", href.attributes['href'].value.rsplit('/', 1)[-1])
print()

script = xmldoc.getElementsByTagName('script')
for src in script:
    print("Temp-->xpath-->script|", src.attributes['src'].value.rsplit('/', 1)[-1])
    # print(script[1].attributes['src'].value.rsplit('/', 1)[-1])

print()
print("For <3)template> ----> <xpath> ----> <link ----> href....path name(last)> tag ")
print()

template = xmldoc.getElementsByTagName('template')
print("ID:=", template[2].attributes['id'].value)
xpath = xmldoc.getElementsByTagName('xpath')
print("xpath_position:=", xpath[2].attributes['position'].value)
xpath = xmldoc.getElementsByTagName('xpath')
print(xpath[2].attributes['position'].value)
link = xmldoc.getElementsByTagName('link')
for href in link:
    print("href-->last_part|", href.attributes['href'].value.rsplit('/', 1)[-1])
print()



print()
print("For <template> ----> <xpath> ----> <script ----> src....path name(last)> tag ")
print()

script = xmldoc.getElementsByTagName('script')
print(script[0].attributes['src'].value.rsplit('/', 1)[-1])
for src in script:
    print(src.attributes['src'].value.rsplit('/', 1)[-1])
