import xml.etree.ElementTree as ET

tree = ET.parse('catalog.xml')
root = tree.getroot()

# for book in root.findall('book'):
#     author = book.find('author').text
#     title = book.find('title').text
#     price = book.find('price').text
#     print(author,'-', title, '-', price)

for book in root.iter('author'):
    print(book.text)