import unittest
from extract import get_heading_from_html, get_first_paragraph_from_html, get_urls_from_html, get_images_from_html

class TestExtract(unittest.TestCase):
  def test_heading(self) -> None:
    input_body = '<html><body><h1>Test Title</h1></body></html>'
    actual = get_heading_from_html(input_body)
    expected = "Test Title"
    self.assertEqual(actual, expected)

  def test_get_first_paragraph_from_html_main_priority(self):
    input_body = '''<html><body>
        <p>Outside paragraph.</p>
        <main>
            <p>Main paragraph.</p>
        </main>
    </body></html>'''
    actual = get_first_paragraph_from_html(input_body)
    expected = "Main paragraph."
    self.assertEqual(actual, expected)

  def test_get_first_paragraph_from_html_main_not_priority(self):
    input_body = '''<html><body>
        <p>Outside paragraph.</p>
        <main>
            <p>Main paragraph.</p>
        </main>
        <p>Another paragraph</p>
    </body></html>'''
    actual = get_first_paragraph_from_html(input_body)
    expected = "Main paragraph."
    self.assertEqual(actual, expected)

  def test_get_first_paragraph_from_html_no_paragraphs(self):
    input_body = '''<html><body>
       
    </body></html>'''
    actual = get_first_paragraph_from_html(input_body)
    expected = ""
    self.assertEqual(actual, expected)
  
  def test_get_heading_from_html_h2_fallback(self) -> None:
    input_body = "<html><body><h2>This is an h2 title</h2></body></html>"
    actual = get_heading_from_html(input_body)
    expected = "This is an h2 title"
    self.assertEqual(actual, expected)
  
  def test_get_heading_from_html_whitespace(self) -> None:
    input_body = "<html><body><h1>   Whitespace Title   </h1></body></html>"
    actual = get_heading_from_html(input_body)
    expected = "Whitespace Title"
    self.assertEqual(actual, expected)

  def test_get_first_paragraph_empty(self) -> None:
    input_body = "<html><body><h1>No paragraphs here</h1></body></html>"
    actual = get_first_paragraph_from_html(input_body)
    expected =""
    self.assertEqual(actual, expected)

  def test_get_urls_from_html_absolute(self) -> None: 
    input_url = "https://crawler-test.com"
    input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a></body></html>'
    actual = get_urls_from_html(input_body, input_url)
    expected = ["https://crawler-test.com"]
    self.assertEqual(actual, expected)

  def test_get_urls_from_html_multiple(self) -> None:
     input_url = "https://crawler-test.com"
     input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a><a href="https://another-test.com"another">another link</a></body></html>'
     actual = get_urls_from_html(input_body, input_url)
     expected = ["https://crawler-test.com", "https://another-test.com"]
     self.assertEqual(actual, expected)

  def test_get_urls_from_html_empty(self) -> None:
     input_url = "https://crawler-test.com"
     input_body = '<html><body><span>Boot.dev</span></body></html>'
     actual = get_urls_from_html(input_body, input_url)
     expected = []
     self.assertEqual(actual, expected)

  def test_get_images_from_html_realtive(self) -> None: 
    input_url = "https://crawler-test.com"
    input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
    actual = get_images_from_html(input_body, input_url)
    expected = ["https://crawler-test.com/logo.png"]
    self.assertEqual(actual, expected)

  def test_get_images_from_html_multiple(self) -> None: 
    input_url = "https://crawler-test.com"
    input_body = '<html><body><img src="/logo.png" alt="Logo"><img src="/hello.png" alt="Hello"></body></html>'
    actual = get_images_from_html(input_body, input_url)
    expected = ["https://crawler-test.com/logo.png", "https://crawler-test.com/hello.png"]
    self.assertEqual(actual, expected)

  def test_get_images_from_html_empty(self) -> None: 
    input_url = "https://crawler-test.com"
    input_body = '<html><body>No logos for you!</body></html>'
    actual = get_images_from_html(input_body, input_url)
    expected = []
    self.assertEqual(actual, expected)