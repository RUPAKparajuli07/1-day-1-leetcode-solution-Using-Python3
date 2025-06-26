class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # If either is a leaf
        if quadTree1.isLeaf:
            if quadTree1.val:  # True OR anything = True
                return Node(True, True, None, None, None, None)
            else:
                return quadTree2  # False OR X = X
        if quadTree2.isLeaf:
            return self.intersect(quadTree2, quadTree1)  # Swap for same logic

        # Recurse on all 4 children
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # If all 4 children are leaves with same value, merge into one leaf
        if (topLeft.isLeaf and topRight.isLeaf and
            bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True, None, None, None, None)
        
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
