import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("This is an example text node", TextType.LINK, "http://boots.dev")
        node2 = TextNode("This is an example text node", TextType.LINK, "http://boots.dev")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node not equal to the first", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_link_uneq(self):
        node = TextNode("This is an example text node", TextType.LINK, "http://boots.dev")
        node2 = TextNode("This is an example text node", TextType.LINK, "http://google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
