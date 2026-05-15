from re import L
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class testParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag_raises(self):
        parent = ParentNode(None, [LeafNode("p", "hi")])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_no_children_raises(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_multiple_children(self):
        parent = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic"),
            LeafNode(None, " text"),
            ])
        self.assertEqual(parent.to_html(),
        "<p><b>Bold</b> and <i>italic</i> text</p>",
        )

    def test_to_html_mixed_children(self):
        parent = ParentNode("div", [
            LeafNode("h1", "Title"),
            ParentNode("p", [
                LeafNode(None, "Some "),
                LeafNode("b", "bold"),
                LeafNode(None, " text."),
                ]),
            LeafNode("hr", ""),
            ])
        expected = "<div><h1>Title</h1><p>Some <b>bold</b> text.</p><hr></hr></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_to_html_deeply_nested(self):
        deepest = LeafNode("em", "deep")
        level3 = ParentNode("b", [deepest])
        level2 = ParentNode("i", [level3])
        level1 = ParentNode("p", [level2])
        root = ParentNode("div", [level1])
        self.assertEqual(
                root.to_html(),
                "<div><p><i><b><em>deep</em></b></i></p></div>",
                )

    def test_to_html_with_props(self):
        parent = ParentNode(
                "a",
                [LeafNode(None, "click me")],
                {"href": "https://boot.dev", "target": "_blank"},
                )
        self.assertEqual(
                parent.to_html(), '<a href="https://boot.dev" target="_blank">click me</a>',
                )

    def test_to_html_with_nested_props(self):
        parent = ParentNode(
                "section", 
                [
                    LeafNode("a", "boot.dev", {"href": "https://boot.dev"}),
                    LeafNode(None, " is awesome"),
                    ],
                    {"class": "intro"},
                )
        self.assertEqual(
                parent.to_html(),
                '<section class="intro"><a href="https://boot.dev">boot.dev</a> is awesome</section>',
                )

    def test_to_html_empty_children(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_repr(self):
        child = LeafNode("p", "hi")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertIn("ParentNode", repr(parent))
        self.assertIn("div", repr(parent))

if __name__ == "__main__":
    unittest.main()


