import requests

image_path = "https://www.c82.net/images/twining/large/ranunculaceae.jpg"
  
image = requests.get(image_url) 
  
with open("ranunculaceae.jpg",'wb') as fout:
    fout.write(r.content)
