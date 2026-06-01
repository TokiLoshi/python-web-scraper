import unittest
from extract import get_heading_from_html, get_first_paragraph_from_html

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