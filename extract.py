from bs4 import BeautifulSoup, Tag 
from urllib.parse import urljoin
from typing import TypedDict
import requests

def get_heading_from_html(html: str) -> str:
 soup = BeautifulSoup(html, "html.parser")
 heading = soup.find("h1") or soup.find("h2")
 return heading.get_text(strip=True) if isinstance(heading, Tag) else ""

def get_first_paragraph_from_html(html: str) -> str:
 soup = BeautifulSoup(html, "html.parser")
 main = soup.find("main")
 if isinstance(main, Tag):
  first_paragraph = main.find("p")
 else:
  first_paragraph = soup.find("p")
 return first_paragraph.get_text(strip=True) if isinstance(first_paragraph, Tag) else ""

def get_urls_from_html(html, base_url): 
 soup = BeautifulSoup(html, "html.parser")
 all_links = []
 for link in soup.find_all("a"): 
  href = link.get("href")
  if href is not None:
    all_links.append(urljoin(base_url, href))
 return all_links

def get_images_from_html(html, base_url):
 soup = BeautifulSoup(html, "html.parser")
 image_urls = []
 images = soup.find_all("img")
 for image in images:
  if not isinstance(image, Tag):
    continue
  src = image.get("src")
  if isinstance(src, str) and src:
    try:
      absolute_url = urljoin(base_url, src)
      image_urls.append(absolute_url)
    except Exception as e:
      print(f"{str(e)}: {src}")
 return image_urls


def get_html(url):
    response = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
    print(f"response {response}")
    if response.status_code >= 400:
        print(f"BAd response: {response.status_code}")
        raise Exception(f"Exception code: {response.status_code}")
    content_type = response.headers.get('Content-Type', "")
    print(f"Content type: {content_type}")
    if "text/html" not in content_type:
        raise Exception(f"incorrect content type: {content_type} it should be text/html")
    if response.status_code == 200: 
        return response.text 
    return response.text

class PageData(TypedDict):
 url: str
 heading: str
 first_paragraph: str
 outgoing_links: list[str]
 image_urls: list[str]

def extract_page_data(html: str, page_url: str) -> PageData: 
  heading = get_heading_from_html(html)
  first_paragraph = get_first_paragraph_from_html(html)
  links = get_urls_from_html(html, page_url)
  images = get_images_from_html(html, page_url)
  layout = {
   "url" : page_url, 
   "heading" : heading,
   "first_paragraph" : first_paragraph,
   "outgoing_links" : links, 
   "image_urls" : images
  }
  return layout

def get_safe_html(url: str) -> str | None:
  try:
    return get_html(url)
  except Exception as e:
    print(f"{e}")
    return None