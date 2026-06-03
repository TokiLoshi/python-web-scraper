from bs4 import BeautifulSoup, Tag 
from urllib.parse import urljoin
from typing import TypedDict

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
 images = []
 for image in soup.find_all("img"):
  img_link = image.get("src")
  if img_link is not None:
   images.append(urljoin(base_url, img_link))
 return images

class PageData(TypedDict):
 url: str
 heading: str
 first_paragraph: str
 outgoing_links: list[str]
 image_urls: list[str]

def extract_page_data(html: str, page_url: str) -> PageData: 
  soup = BeautifulSoup(html, "html.parser")
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