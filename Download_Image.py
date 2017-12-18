# Download image

import random                # For File-Name
import urllib.request        # To retrieve image from url

def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"              # File name with extension
    urllib.request.urlretrieve(url, full_name)  # What the fuck?????????

url = "https://pbs.twimg.com/media/DQUT4kRX0AEPgVh.jpg"   # Specify URL
download_image(url)
