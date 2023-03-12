# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        思考プロセスを記載
        inorder traversalとは
            深さ優先探索(DFS)の3種類の一つ。rootが探索順の中間に来る探索方法。
            【tips】
            深さ優先探索(DFS)の3種類
            1.行きかけ順(pre-order)
            2.通りかけ順(in-order) ←これが今回の方法
            3.帰りがけ順(post-order)
            
        binari treeってどんなことを考慮すればいいですか
            ・nodeは数字だけを含むのか
                一つのnodeに一つの数字が含まれている。
            ・枝は一つのnodeに必ず2本までなのか
                必ず2本ではない。子nodeの数は1-2本になる。                
                【tips】
                二分木の種類は以下の通り
                1.全二分木(full binary tree)
                    個を持つnodeの数がすべて2個ずつであるもの
                2.完全二分木(perfect binary tree)
                    全二分木のうち、葉nodeがすべて同じ深さに揃っているもの
                3.complete N-ary tree
                    最下層の葉nodeはすべて2個ではないが、葉nodeが可能な限り左に寄っているもの
                4.二分探索木 (binary search tree/バイナリサーチツリー)
                    左にいけばいくほど数字が大きくなるように作成されたデータ構造。
                5.平衡二分探索木 (self-balancing binary search tree)
                    二分探索木のうち、rootから葉nodeまでの深さがなるべく均等になるように作成されたもの
                    値の挿入や削除が行われれば、高さが均等になるように処理を行う。

            ・
        '''
        if root is None:
            return root
        
        self.ans = []
        self.dfs(root)
        
        return self.ans

    def dfs(self, node):
        if node:
            self.dfs(node.left)
            self.ans.append(node.val)
            self.dfs(node.right)

