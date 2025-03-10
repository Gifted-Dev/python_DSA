#### Data structures exercise: General Tree

1. Below is the management hierarchy of a company.

    ![alt text](image.png)

Extent [tree class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree.py) built in our
main tutorial so that it takes **name** and **designation** in data part of TreeNode class.
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,

   ![alt text](image-1.png)

Here is how your main function should will look like,
```
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
```

[Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/Exercise/management_hierarchy.py)

1. Build below location tree using **TreeNode** class

    ![alt text](image-2.png)

Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below,

   ![alt text](image-3.png)

[Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/Exercise/location_hierarchy.py)

