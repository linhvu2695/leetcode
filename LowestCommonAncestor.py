'''
    Given a binary tree, 
    find the lowest common ancestor (LCA) of two given nodes in the tree.
'''

#findPath to p & to q - then compare the 2 paths
def lowestCommonAncestor_1(root, p, q):
    def findPath(root, item):
        path =[]
        
        if root == None:
            return path
        if root == item:
            path.append(root)
                        
        if root.left:
            left_path = findPath(root.left, item)
            if len(left_path) > 0:
                path = left_path + [root]
                
        if root.right:
            right_path = findPath(root.right, item)
            if len(right_path) > 0:
                path = right_path + [root]
                            
        return path
    
    path_p = findPath(root, p)[::-1]
    path_q = findPath(root, q)[::-1]
    i = 0
    
    while i < min(len(path_p), len(path_q)):
        if path_p[i] != path_q[i]:
            break
        i += 1
    return path_p[i-1]


#recursion method    
def lowestCommonAncestor_2(root, p, q):    
    if root == None or root == p or root == q:
        return root
    
    left_LCA = lowestCommonAncestor(root.left, p, q)
    right_LCA = lowestCommonAncestor(root.right, p, q)
    
    #LCA at right sub-tree if left sub-tree found no LCA
    if left_LCA == None:
        return right_LCA
     
    #LCA at left sub-tree if right sub-tree found no LCA    
    if right_LCA == None:
        return left_LCA
        
    return root