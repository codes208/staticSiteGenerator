from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = list()
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_values = node.text.split(delimiter)
        if len(split_values) % 2 == 0:
            raise Exception(f"Invalid markdown: no closing delimiter for {delimiter}")
        
        for i, value in enumerate(split_values):
            if i % 2 == 0:
                new_nodes.append(TextNode(value, TextType.TEXT))
            else:
                new_nodes.append(TextNode(value, text_type))

    return new_nodes

