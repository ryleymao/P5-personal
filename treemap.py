from __future__ import annotations
from typing import Any, Optional, List, Tuple


class TreeNode:
    def __init__(self, key: int, val: Any):
        self.key: int = key
        self.val: Any = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

    def __repr__(self) -> str:
        return f"TreeNode(key={self.key}, val={self.val})"


class TreeMap:
    """
    Minimal BST-backed map with:
      - insert(key, val): insert or update (size only grows on new key)
      - get(key, default=None)
      - __contains__(key)  -> 'key in tm'
      - __len__()          -> size
      - keys()/values()/items() in sorted (in-order) key order
    """

    def __init__(self):
        self.root: Optional[TreeNode] = None
        self._size: int = 0

    # ---------- public API ----------
    def insert(self, key: int, val: Any) -> None:
        """Insert or update key->val. Size increases only on new key."""
        if self.root is None:
            self.root = TreeNode(key, val)
            self._size = 1
            return

        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = TreeNode(key, val)
                    self._size += 1
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = TreeNode(key, val)
                    self._size += 1
                    return
                curr = curr.right
            else:
                # Key exists: update value, do not change size
                curr.val = val
                return

    def get(self, key: int, default: Any = None) -> Any:
        """Return value for key if present; else default."""
        node = self._find_node(key)
        return node.val if node else default

    def __contains__(self, key: int) -> bool:
        return self._find_node(key) is not None

    def __len__(self) -> int:
        return self._size

    def keys(self) -> List[int]:
        return [k for k, _ in self.items()]

    def values(self) -> List[Any]:
        return [v for _, v in self.items()]

    def items(self) -> List[Tuple[int, Any]]:
        out: List[Tuple[int, Any]] = []
        self._inorder(self.root, out)
        return out

    # ---------- internal helpers ----------
    def _find_node(self, key: int) -> Optional[TreeNode]:
        curr = self.root
        while curr is not None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr
        return None

    def _inorder(self, node: Optional[TreeNode], out: List[Tuple[int, Any]]) -> None:
        if node is None:
            return
        self._inorder(node.left, out)
        out.append((node.key, node.val))
        self._inorder(node.right, out)
