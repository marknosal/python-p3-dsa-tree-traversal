class Tree:
  def __init__(self, root = None):
    self.root = root

  # def get_element_by_id(self, id):
  #   nodes_to_visit = [self.root]
  #   while nodes_to_visit:
  #     current = nodes_to_visit.pop()
  #     if current['id'] == id:
  #       return current
  #     nodes_to_visit = nodes_to_visit + current['children']
  #   return None

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      nodes_to_visit = nodes_to_visit + node['children']
    return None

  def breadth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      # Remove first node from the 'notdes_to_visit' list
      node = nodes_to_visit.pop()
      # Add it's value to the result list
      result.append(node['value'])
      # Add its children (if any) to the END of the 'nodes_to_visit' list
      nodes_to_visit = nodes_to_visit + node['children']
    return result

  # def depth_first_traversal(node):
  #   result = []
  #   nodes_to_visit = [node]
  #   while len(nodes_to_visit) > 0:
  #     result.append(node['value'])
  #     nodes_to_visit = node['children'] + nodes_to_visit
  #   return result

  def depth_first_traversal(node, result = []):
    # Visit each node (add it to the list of results)
    result.append(node['id'])
    for child in node['children']:
      # Visit each child node
      depth_first_traversal(child, result)
    return result