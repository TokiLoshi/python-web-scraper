import sys
import requests

def main():
    print("Hello from python-web-scraper!")
    to_crawl = "https://learnwebscraping.dev/practice/ecommerce/products/ashenfang-longsword-fan-1001/"
    # print("Echoing: ", sys.argv)
    # if len(sys.argv) < 2:
    #     print("no website provided")
    #     sys.exit(1)
    # if len(sys.argv) > 2:
    #     print("too many arguments provided")
    #     sys.exit(1)
    # script_name = sys.argv[0]
    # base_url = sys.argv[1]
    # print(f"script name: {script_name}")
    # print(f"starting crawl of {base_url}")
    html = get_html(to_crawl)
    print(html)

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
    return response

def crawl_page(base_url, current_url=None, page_data=None): 
    # all the recursion things
    pass
    
if __name__ == "__main__":
    main()
