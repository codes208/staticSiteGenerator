from typing import Text
import unittest
import node_delimiter
from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])

    def test_non_text_node_pass_through(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("already bold", TextType.BOLD)
            ])

    def test_mult_delimiters(self):
        node = TextNode("a `b` c `d` e", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.CODE),
            TextNode(" c ", TextType.TEXT),
            TextNode("d", TextType.CODE),
            TextNode(" e", TextType.TEXT)
            ])

    def test_unmatched_delimiter(self):
        node = TextNode("This is a `test", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_mult_nodes(self):
        nodes = [
            TextNode("first `code block` here", TextType.TEXT),
            TextNode("this is already bold", TextType.BOLD),
            TextNode("second `code block` here", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("first ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" here", TextType.TEXT),
            TextNode("this is already bold", TextType.BOLD),
            TextNode("second ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" here", TextType.TEXT)
            ])

