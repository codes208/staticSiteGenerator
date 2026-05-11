from re import L
import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "click me",
            None,
            {"href": "https://boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://boot.dev" target="_blank"',
        )

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "hello", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_values(self):
        node = HTMLNode("p", "hello world")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello world")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode("p", "hello world", None, {"class": "greeting"})
        self.assertEqual(
                repr(node),
                "HTMLNode(p, hello world, None, {'class': 'greeting'})",
                )

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):
    def test_to_html_basic(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "click me!", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "just some text")
        self.assertEqual(node.to_html(), "just some text")

    def test_repr(self):
        node = LeafNode("p", "hello", {"class": "greeting"})
        self.assertEqual(repr(node), "LeafNode(p, hello, {'class': 'greeting'})",)


if __name__ == "__main__":
    unittest.main()


