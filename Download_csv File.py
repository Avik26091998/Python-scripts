# Download CSV File

from urllib import request          #import urllib.request

url = "https://www.youtube.com/redirect?event=comments&redir_token=ZbDm8xzKH_MM2DuQlUJs2j9p3Zd8MTUxMzk0ODIzOEAxNTEzODYxODM4&q=http%3A%2F%2Fwww.sample-videos.com%2Fdownload-sample-csv.php"

def download(csv_url):

    response = request.urlopen(csv_url)     # open the url and save contents in response
    csv = response.read()                   # read data into csv
    csv_str = str(csv)
    lines = csv_str.split("\\n")            # spli string at new line
    dest_url = r'finance.csv'               # specify the path of file
    fx = open(dest_url, "w")                
    for line in lines:                      # Read data int fx with new line
        fx.write(line + '\n')
    fx.close()

download(url)
