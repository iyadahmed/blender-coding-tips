def abs_node_loc(node):
    loc = node.location
    if node.parent is None:
        return loc
    return loc + abs_node_loc(node.parent)
