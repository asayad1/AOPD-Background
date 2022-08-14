import requests
from ctypes import windll
import os

def setDesktopBackground(path):
    windll.user32.SystemParametersInfoW(20, 0, path, 0)

def getImage():
    # Call NASA APOD API to get image URL 
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

    # Extract image URL from JSON and API call to get image data from URL 
    if 'hdurl' in response.json():
        image_url = response.json()['hdurl']
        image_data = requests.get(image_url).content

        # Download image 
        with open('image.jpg', 'wb') as handler:
            handler.write(image_data)

        # Return the path of the image 
    return os.path.abspath('image.jpg')


if __name__ == '__main__':
    # Set desktop image background to AOPD when the script is called
    image_path = getImage()
    setDesktopBackground(image_path) 
    