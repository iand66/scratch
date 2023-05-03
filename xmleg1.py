# SAX approach - Read Only
import xml.sax

class Catalog(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if self.current == "book":
            print(f"Book Id {attrs['id']}")

    def characters(self, content):
        match self.current:
            case 'author':
                self.author = content
            case 'title':
                self.title = content
            case 'genre':
                self.genre = content
            case 'price':
                self.price = content
            case 'publish_date':
                self.publish_date = content
            case 'description':
                self.description = content

    def endElement(self, book):
        match book:
            case 'author':
                print(f"Author {self.author}")
            case 'title':
                print(f"Title {self.title}")
            case 'genre':
                print(f"Genre {self.genre}")
            case 'price':
                print(f"Price {self.price}")
            case 'publish_date':
                print(f"Publish {self.publish_date}")
            case 'description':
                print(f"Description {self.description}")
        self.current = ""
            
handler = Catalog()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('catalog.xml')