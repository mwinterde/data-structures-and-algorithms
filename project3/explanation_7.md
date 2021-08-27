As suggested, I implemented the HTTP request handler using a Trie data structure.
The additional requirements are that we need to implement handlers for each Trie Node
and that we need to translate multi-level URLs into consecutive components. Moreover, 
I choose to implement an additional handling of edge cases (e.g. URL starts with `/` vs. 
starts not with `/`) in the `split_path` method.

The time complexity of insertions and lookups is O(n) since there will be a unique linear
path for each URL. The space complexity is O(1) since for each traversal it is only necessary
to keep track of the current node.