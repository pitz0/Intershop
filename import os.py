#import untangle
#import os
# obj = untangle.parse('mfg_fix1.xml')

# print (obj.foo.bar['name'])
# print (obj.foo.bar.type['foobar'])
# obj.foo.bar.attributes={'name': "hshsh"}
#print (os.path.dirname('mfg_fix3'))ixing

import os 
import xml.etree.ElementTree as Et
file_name='MFG.xml'
base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path,file_name)
print('xml_file ---->',xml_file)
tree = Et.parse("C:/Users/admin/Desktop/Django_Project/tennis/data/MFG.xml")
root = tree.getroot()
count=0
for child in root:         #loops for each child
	count+=1
	child.attrib = {'pk':str(count),'model':'Meddata.medicine'}
	child.tag = "object"
	for element in child:   #loops for element is child
		#tags names will b cahnged to it
		element.attrib= {"name":element.tag}
		if (element.tag)=="COCD":
			element.attrib={"type":"PositiveInteger"}
		if (element.tag)=="NAME" or "Address" or "Phone":
			element.attrib={"type":"Charfield"}
		element.tag = "field"
		print(element.tag,"------->",element.text)  
tree.write(xml_file)      # to write the change