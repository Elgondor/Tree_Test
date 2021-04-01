from TreeNode import TreeNode
import urllib.request, json
def insert(root, parent, node):
    if root is None:
        root = node
    else:
        if int(root.data['ID']) == parent:
            root.add_child(node)
        else:
            l = len(root.children)
                
            for i in range(l):
                if int(root.children[i].data['ID']) == parent:
                    insert(root.children[i], parent, node)
                else:
                    insert(root.children[i], parent, node)

def make_tree():
    root_dict = {'ID': '0', 'Name': 'Data', 'Parent': 0}
    root = TreeNode(root_dict)
    
    with urllib.request.urlopen("https://test.defontana.com/") as url:
        data = json.loads(url.read().decode())
        data_list = data['data']
        for i in range(0, len(data_list)):
            node = data_list[i]
            if node['Parent'] != 0:
                insert(root, node['Parent'], TreeNode(node))
            if data_list[i]['Parent'] == 0:
                root.add_child(TreeNode(node))
            
    
    root.print_tree()
    return root


make_tree()