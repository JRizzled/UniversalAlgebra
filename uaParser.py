from re import L
import xml 
import xml.etree.ElementTree as xet
import xmlformatter
import sys


class ParseUA:
	def __init__(self) -> None:
		pass
	

def parseTree(fl_name, m_num, hi_num):
	card_num = m_num + 2
	tree = getTree(fl_name)
	root = tree.getroot()
	ars = []
	for i in tree.iter():
		if i.tag == "algName":
			name = i
		if i.tag == "cardinality":
			card = i
		if i.tag == "desc":
			desc = i
		if i.text == "join":
			joinn = i
		if i.text == "meet":
			meet = i
		if i.tag == "intArray":
			ars.append(i)
	
	jnArr =  ars[0] 
	mtArr = ars[1]

	name.text = "m" + str(m_num)
	desc.text = "M_" + str(m_num) + " with "+ str(hi_num) + " as the greatest."
	card.text = str(card_num)

	join_arr = create_join(card_num, hi_num)
	meet_arr = create_meet(card_num, hi_num)
	
	for i in range(card_num):
		temp_el = xet.Element("row")
		temp_ol = xet.Element("row")
		wrk_2 = xet.SubElement(mtArr,"row",{"r":"["+str(i)+"]"}) 
		wrk = xet.SubElement(jnArr,"row",{"r":"["+str(i)+"]"})
		wrk.text = str(join_arr[i])[1:-1].replace(" ", "")
		wrk_2.text = str(meet_arr[i])[1:-1].replace(" ", "")

		wrk.tail = "\n\t\t\t"
		wrk_2.tail = "\n\t\t\t"
	tree.write("new_m"+str(m_num)+".ua", xml_declaration=True)
	print(ars)

def create_join(m_num, hi_num):
	temp_arr = [[hi_num for i in range(m_num)] for j in range(m_num)]
	for i in range(m_num):
		temp_arr[0][i] = i
		temp_arr[i][0] = i 
		temp_arr[i][i] = i
	return temp_arr
def create_meet(m_num, hi_num):
	temp_arr = [[hi_num for i in range(m_num)] for j in range(m_num)]
	for i in range(m_num):
		temp_arr[m_num-1][i] = i
		temp_arr[i][m_num-1] = i 
		temp_arr[i][i] = i
	return temp_arr

def getTree(fl_name):
	return xet.parse(fl_name)
	

def main():
	ARGS = (len(sys.argv) == 1)
	if ARGS:
		parseTree("mn.ua", 8, 3)
	else:
		inpn = int(input("Input n value for n in mn Universal Algebra:"))
		inphi = int(input("Input hi value:"))
		parseTree("mn.ua", inpn, inphi)
	

if __name__ == "__main__":
	main()