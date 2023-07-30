import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
# import logging, requests, timeit
# logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Define the User-Agent header
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'
}

session = requests.Session()
url_file = open('urls.txt', 'a')

def download_xml_files(url):
    # Get the base URL's hostname
    base_hostname = urlparse(url).hostname

    # Send a request to the URL and get the HTML content
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links on the current page
    links = soup.find_all('a', href=True)

    hrefs = list(map(lambda x: x.get('href'), links))
    for href in hrefs:
        absolute_url = urljoin(url, href)

        # Check if the link is on the same hostname and not ending in '.pdf'
        if urlparse(absolute_url).hostname == base_hostname and not absolute_url.endswith('.pdf') and not absolute_url.endswith('.svg'):
            if absolute_url.endswith('.xml'):
                # If it's an XML file, download it
                download_file(absolute_url)
            else:
                # If it's another page, recursively visit the link
                download_xml_files(absolute_url)


def download_file(url):
    dirname = os.path.dirname(url.replace('https://legislation.govt.nz/subscribe/', ''))
    print(url)

    url_file.write(url + "\n")
    url_file.write(" dir=" + dirname + "\n")

if __name__ == "__main__":
    for i in range(1950, 2023):
        starting_url = "https://legislation.govt.nz/subscribe/act/public/" + str(i)  # Replace with the starting URL of the website
        output_folder = "xml_files"  # Replace with the folder where you want to save the downloaded XML files

        download_xml_files(starting_url)

    url_file.close()
