The `find` and `insert` methods of the `Trie` class take O(n) since we simply
iterate through the input characters. 

We can achieve this by representing the Trie by a hierarchial collection of TrieNode 
objects, each of which has one parent node and eventually multiple child nodes. Therefore, 
there will be always one unique path for an input string. 

The time complexity of the `suffixes` method of the `TrieNode` class depends on the nature 
of the subtree that lies under the specific node. In the worst case scenario the node has `m` 
completely seperated sub-branches of length `l`. For this specific problem, for large `m` 
we can assume that `m >> l`. Therefore, the `suffixes` method will also be of linear time.

The space complexity of the methods is O(1) since for each traversal we only need to keep 
track of the current node.