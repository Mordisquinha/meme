import requests 
from PIL import Image
from io import BytesIO

url = 'https://api.memegen.link/images/automatic'

search = str(input('Generate a random meme with: '))

data = {
      "text": search,
      "safe": True,
      "redirect": True
       }

response = requests.post(url, data=data)

image_data = BytesIO(response.content)
img = Image.open(image_data)
img.show()
