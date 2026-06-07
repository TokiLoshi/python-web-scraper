import sys
import requests
from crawl import crawl_page

def main():
    print("Hello from python-web-scraper!")
    to_crawl = "https://learnwebscraping.dev/practice/ecommerce/products/ashenfang-longsword-fan-1001/"
    print("Echoing: ", sys.argv)
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    script_name = sys.argv[0]
    base_url = sys.argv[1]
    print(f"script name: {script_name}")
    print(f"starting crawl of {base_url}")
    page_data = crawl_page(base_url)
    print(f"Found {len(page_data)} pages:")
    for page in page_data.values():
        print(f"- {page['url']}: {len(page['outgoing_links'])} outgoing links")
    
    sys.exit(0)

    
if __name__ == "__main__":
    main()
