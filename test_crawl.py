import unittest 
from crawl import normalize_url 

class TestCrawl(unittest.TestCase):
  def test_normalize_url(self) -> None:
    input_url = "https://www.boot.dev/blog/path"
    actual = normalize_url(input_url)
    expected = "www.boot.dev/blog/path"
    self.assertEqual(actual, expected)

  def trailing_slash(self) -> None:
    input_url_1 = "https://www.boot.dev/blog/path/"
    input_url_2 = "http://www.boot.dev/blog/path/"
    actual_1 = normalize_url(input_url_1)
    actual_2 = normalize_url(input_url_2)
    expected = "www.boot.dev/blog/path"
    self.assertEqual(actual_1, expected)
    self.assertEqual(actual_2, expected)

  def http_handled(self) -> None:
    input_url = "http://www.boot.dev/blog/path"
    actual = normalize_url(input_url)
    expected = "www.boot.dev/blog/path"
    self.assertEqual(actual, expected)


if __name__ == "__main__":
  unittest.main()