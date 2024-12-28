class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level  
    
    def add_child(self, child):
        child.parent = self
        # self.children[child.name] = child.designation
        self.children.append(child)

        
        
    def print_tree(self, data):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if data == 'name':
            print(prefix + self.name)
        elif data == 'designation':
            print(prefix + self.designation)
        elif data == 'both':
            print(f"{prefix}{self.name} ({self.designation})")
        
        # Recursively print children
        for child in self.children:
            child.print_tree(data)
            
            
            
def build_management_tree():
    root = TreeNode('Nilupul', 'CEO')
    cto = TreeNode('Chinmay', 'CTO')
    infra_head = TreeNode('Vishwa', 'Infrastructure Head')
    cloud_manager = TreeNode('Dhaval', 'Cloud Manager')
    app_manager = TreeNode('Abhijit', 'App Manager')
    app_head = TreeNode('Aamir', 'Application Head')
    hr_head = TreeNode('Gels', 'HR Head')
    recruit_manager = TreeNode('Peter', 'Recruitment Manager')
    policy_manager = TreeNode('Waqas', 'Policy Manager')
    
    # declaring children
    root.add_child(cto)
    root.add_child(hr_head)
    cto.add_child(infra_head)
    cto.add_child(app_head)
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)
    hr_head.add_child(recruit_manager)
    hr_head.add_child(policy_manager)    
    
    return root
    
if __name__ == '__main__':
    root_node = build_management_tree()
    # root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    # root_node.print_tree("both") # prints both (name and designation) hierarchy