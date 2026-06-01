from bs4 import BeautifulSoup, Tag 

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
