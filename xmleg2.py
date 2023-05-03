import xml.dom.minidom

domtree = xml.dom.minidom.parse('catalog.xml')
group = domtree.documentElement
books = group.getElementsByTagName('book')

# List books in Catalog
for book in books:
    if book.hasAttribute('id'):
        print(f"Book Id {book.getAttribute('id')}")
        

    print(f"Author {book.getElementsByTagName('author')[0].childNodes[0].data}")
    print(f"Title {book.getElementsByTagName('title')[0].childNodes[0].data}")
    print(f"Genre {book.getElementsByTagName('genre')[0].childNodes[0].data}")
    print(f"Price {book.getElementsByTagName('price')[0].childNodes[0].data}")
    print(f"Publish {book.getElementsByTagName('publish_date')[0].childNodes[0].data}")
    print(f"Description {book.getElementsByTagName('description')[0].childNodes[0].data}")

# Add Book to Catalog
newbook = domtree.createElement('book')
newbook.setAttribute('id','bk113')
author = domtree.createElement('author')
author.appendChild(domtree.createTextNode('Ian Davies'))
title = domtree.createElement('title')
title.appendChild(domtree.createTextNode('How to Cure Depression'))
genre = domtree.createElement('genre')
genre.appendChild(domtree.createTextNode('Self Help'))
price = domtree.createElement('price')
price.appendChild(domtree.createTextNode('0'))
publish = domtree.createElement('publish_date')
publish.appendChild(domtree.createTextNode('2024-01-01'))
description = domtree.createElement('description')
description.appendChild(domtree.createTextNode('All that I know so far'))

newbook.appendChild(author)
newbook.appendChild(title)
newbook.appendChild(genre)
newbook.appendChild(price)
newbook.appendChild(publish)
newbook.appendChild(description)

group.appendChild(newbook)

domtree.writexml(open('catalog2.xml','w'))