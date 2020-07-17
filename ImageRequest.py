import os
import requests  # to get image from the web
import shutil  # to save it locally


def simple_get(url):
    image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    filename = image_url.split("/")[-1]
    image_path = os.path.join(os.path.dirname(__file__), 'assets', filename)

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(image_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
