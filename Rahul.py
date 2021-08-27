from xml.dom.minidom import parse

xmldoc = parse('5.python_example.xml')

id = xmldoc.getElementsByTagName("template")
m = xmldoc.getElementsByTagName("xpath")

# position = xmldoc.getElementsByTagName("")
for i in id:
    print(i.getAttribute("id"))
    for j in m:
        print(j.getAttribute("position"))
#
#     print(j.getAttribute("position"))

