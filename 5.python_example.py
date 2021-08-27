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
