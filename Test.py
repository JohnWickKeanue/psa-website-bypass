import time
import requests 
import re
import cloudscraper 
import concurrent.futures
from bs4  import BeautifulSoup

psa_url = "https://htpmovies.xyz/tees-maar-khan-2022-movie-download-in-telugu-hd-480p-720p-1080p/"


def psa_bypasser(psa_url):
	client = cloudscraper.create_scraper(allow_brotli=False)
	r = client.get(psa_url)
	soup = BeautifulSoup(r.text, "html.parser").find_all(class_="dropshadowboxes-drop-shadow dropshadowboxes-rounded-corners dropshadowboxes-inside-and-outside-shadow dropshadowboxes-lifted-both dropshadowboxes-effect-default")
	
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for link in soup:
			try:
				exit_gate = link.a.get("href")
				executor.submit(htp, exit_gate)
			except: pass

def htp(url):
    download = rget(url, stream=True, allow_redirects=False) 
    url = download.headers["location"]
    print(gt(url) 

def gt(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    DOMAIN = "https://go.bloggertheme.xyz"
    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}?quelle="

    resp = client.get(final_url)
    
    soup = BeautifulSoup(resp.content, "html.parser")
    try:
        inputs = soup.find(id="go-link").find_all(name="input")
    except:
        return "Incorrect Link"
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(6)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    return r.json()['url']


    
print(psa_bypasser(psa_url)) 
 
