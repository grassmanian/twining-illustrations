import requests
from bs4 import BeautifulSoup
import unicodedata

# Parse out list of plant names
table_page = requests.get('https://www.c82.net/twining/plants/?view=illustrated')
soup = BeautifulSoup(table_page.content, 'html.parser')

indices = [x for x in range(321) if x % 2 == 1]
pre_formatted_names = [soup.ol.contents[x].span.contents[0] for x in indices]
names = [''.join(filter(str.isalpha, x)) for x in pre_formatted_names]
ascii_names = [x.replace('æ', 'ae').lower() for x in names]

# Write download and write image
for item in ascii_names:
    image_url = 'https://www.c82.net/images/twining/large/{}.jpg'.format(item)
    image = requests.get(image_url) 
    try: 
        image.raise_for_status()
    except:
        print('Error downloading {}, status {}'.format(item, image))
        continue
    else:
        with open("{}.jpg".format(item),'wb') as fout:
            fout.write(image.content)
