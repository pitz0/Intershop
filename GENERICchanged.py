
#import os
# obj = untangle.parse('mfg_fix1.xml')

# print (obj.foo.bar['name'])
# print (obj.foo.bar.type['foobar'])
# obj.foo.bar.attributes={'name': "hshsh"}
#print (os.path.dirname('mfg_fix3'))ixing

import os 
import xml.etree.ElementTree as Et

file_name='GENERIC.xml'
base_path = os.path.dirname(os.path.realpath(__file__))    #base file location 
xml_file = os.path.join(base_path,file_name)               #this will join base file and xml file
print('xml_file ---->',xml_file)                           #print directory
tree = Et.parse(xml_file)                                  #parse the file
root = tree.getroot()                                      #create the root for tree

count=0
for child in root:         #loops for each child
	count+=1
	child.attrib = {'pk':str(count),'model':'Meddata.GENERIC'}
	child.tag = "object"
	for element in child:   #loops for element is child
			#tags names will b cahnged to it
		print(element.tag,"------->",element.text)
		if element.tag in ["HPRate","Rate","MRP","HMARGIN","RMARGIN","TAX","MST","CST","OCT","EXICE"]: #check type and allot it
			element.attrib={"name":element.tag, "type":"Decimalfield"}
		elif element.tag in ["PACK","SHRTNM","Address","Phone","NAME","GDESC","Descr","STRENGTH","MFG","CATEGORY","PIS","PISNO","GnCode","ItemCode","MfgCode","COCD"]:
			element.attrib={"name":element.tag,"type":"Charfield"}
		elif element.tag in ["PISDATE","EntryDt"]:
			element.attrib={"name":element.tag,"type":"DateTimeField"}
		element.tag = "field"		  
tree.write(xml_file)      # to write the changeS

