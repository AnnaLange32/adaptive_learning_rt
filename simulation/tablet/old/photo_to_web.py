

import urllib
import urllib.request as urllibr
import base64
import json

def uploadPhotoToWeb(photo):
    """Upload a photo to the web (Imgur). This script has to be run in Python3.
     I could not resolve dependencies in urllibr in Python2.7"""
    with open(photo, "rb") as f:
        image_data = f.read()
        b64_image = base64.standard_b64encode(image_data).decode("utf-8")

    client_id = "88df624fe066938"  # Replace with your actual Imgur client ID
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': b64_image, 'title': 'test'}
    data = urllib.parse.urlencode(data).encode('utf-8')  # Encode data as bytes

    url = "https://api.imgur.com/3/upload.json"
    request = urllibr.Request(url, data=data, headers=headers)

    try:
        response = urllibr.urlopen(request).read()
        parse = json.loads(response)
        return parse['data']['link']  # Return the URL of the uploaded photo
    except Exception as e:
        print("Error:", e)
        return None

# Replace 'enjoyment.png' with the path to your image file
image_url = uploadPhotoToWeb('enjoyment.png')
if image_url:
    print("Image uploaded to:", image_url)
else:
    print("Failed to upload the image.")

def uploadPhotoToWeb1(photo):
    """we need to upload photo to web as we (me) are not able to open it from local folder"""
    f = open(photo, "rb")  # open our image file as read only in binary mode
    image_data = f.read()  # read in our image file
    b64_image = base64.standard_b64encode(image_data)
    client_id = "88df624fe066938"  # this the id which we've got after registrating the app on imgur 677c5a8b1f463b62c5560a7ac8a1d212aa6215af
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': b64_image, 'title': 'test'}
    request = urllibr.Request(url="https://api.imgur.com/3/upload.json", data=urllib.parse.urlencode(data),
                              headers=headers)
    response = urllibr.urlopen(request).read()
    parse = json.loads(response)
    return parse['data']['link'] #returns a url of the photo

#uploadPhotoToWeb('enjoyment.png')




def uploadPhotoToWebv(photo):
    """Upload a photo to the web (Imgur)."""
    # Open the image file
    with open(photo, "rb") as f:
        image_data = f.read()
        b64_image = base64.standard_b64encode(image_data).decode("utf-8")

    client_id = "88df624fe066938"  # Replace with your actual Imgur client ID
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': b64_image, 'title': 'test'}
    data = urllib.urlencode(data)  # Encode data as a URL-encoded string

    url = "https://api.imgur.com/3/upload.json"
    request = request.Request(url, data=data, headers=headers)

    try:
        response = request.urlopen(request).read()
        parse = json.loads(response)
        return parse['data']['link']  # Return the URL of the uploaded photo
    except Exception as e:
        print("Error:", e)
        return None

# Replace 'enjoyment.png' with the path to your image file
#image_url = uploadPhotoToWeb('enjoyment.png')
if image_url:
    print("Image uploaded to:", image_url)
else:
    print("Failed to upload the image.")