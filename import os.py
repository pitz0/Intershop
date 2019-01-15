import os 
import xml.etree.ElementTree as Et
file_name='mfg_fix.xml'
full_file=os.path.abspath(os.path.join('data',file_name)) #location offile
tree = Et.parse(full_file)
root = tree.getroot()
for child in root:         #loops for each child
	for element in child:   #loops for element is child
		element.tag = "field" #tags names will b cahnged to it
tree.write(full_file)        # to write the changes


        
    


