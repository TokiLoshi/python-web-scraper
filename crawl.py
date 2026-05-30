from urllib.parse import urlparse 
def normalize_url(url):
 parsed_url = urlparse(url)
 full_path = f"{parsed_url.netloc}{parsed_url.path}"
 full_path = full_path.rstrip("/").lower()
 return full_path