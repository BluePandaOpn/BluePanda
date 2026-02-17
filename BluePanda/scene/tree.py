"""
BluePanda Metadata
- Version: v0.5
- Node Type: Core SceneTree Module
- Location: BluePanda/SceneTree.py
- Purpose: Manages node hierarchy, path lookup, and global events.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""


class _RootNode:
    """Internal root holder for the scene graph."""

    def __init__(self):
        self.name = "root"
        self.parent = None
        self.children = []


class SceneTree:
    """
    Scene tree service:
    - Hierarchy management (`add_child`, `remove_child`)
    - Path lookup (`get_node`)
    - Global event bus (`connect`, `emit`, `disconnect`)
    """

    def __init__(self, engine):
        self.engine = engine
        self.root = _RootNode()
        self._events = {}
        self._groups = {}

    def _unique_sibling_name(self, parent, desired):
        existing = {getattr(child, "name", None) for child in parent.children}
        base = str(desired).strip() if desired else "Node"
        if base not in existing:
            return base
        i = 2
        while f"{base}_{i}" in existing:
            i += 1
        return f"{base}_{i}"

    def add_child(self, child, parent=None):
        """Attach `child` to `parent` (or root if parent is None)."""
        target_parent = parent if parent is not None else self.root
        if target_parent is child:
            return child

        if getattr(child, "parent", None) is not None:
            self.remove_child(child)

        if not hasattr(target_parent, "children"):
            target_parent.children = []

        if not getattr(child, "name", None):
            child.name = child.__class__.__name__
        child.name = self._unique_sibling_name(target_parent, child.name)

        child.parent = target_parent
        target_parent.children.append(child)
        for group_name in list(getattr(child, "_groups", set())):
            self.add_to_group(child, group_name)
        return child

    def remove_child(self, child):
        """Detach a child from current parent/root."""
        parent = getattr(child, "parent", None)
        if parent is None:
            return
        if hasattr(parent, "children") and child in parent.children:
            parent.children.remove(child)
        for group_name in list(getattr(child, "_groups", set())):
            self.remove_from_group(child, group_name)
        child.parent = None

    def get_node(self, path, start=None):
        """
        Resolve a node by path.

        Supported path formats:
        - Absolute: `/Player/Weapon`
        - Relative: `Weapon`
        - Parent traversal: `../Sibling`
        - Current node marker: `./Child`
        """
        if path is None:
            return None
        raw = str(path).strip()
        if not raw:
            return None
        if raw in ("/", "root"):
            return self.root

        absolute = raw.startswith("/")
        parts = [p for p in raw.split("/") if p]
        current = self.root if absolute else (start if start is not None else self.root)

        for part in parts:
            if part == ".":
                continue
            if part == "..":
                current = getattr(current, "parent", None)
                if current is None:
                    return None
                continue
            next_node = None
            for child in getattr(current, "children", []):
                if getattr(child, "name", None) == part:
                    next_node = child
                    break
            if next_node is None:
                return None
            current = next_node
        return current

    def connect(self, event_name, callback):
        """Connect a callback to a global scene event."""
        listeners = self._events.setdefault(str(event_name), [])
        listeners.append(callback)

    def disconnect(self, event_name, callback):
        listeners = self._events.get(str(event_name), [])
        if callback in listeners:
            listeners.remove(callback)

    def emit(self, event_name, *args, **kwargs):
        """Emit a global scene event."""
        for callback in list(self._events.get(str(event_name), [])):
            callback(*args, **kwargs)

    def add_to_group(self, node, group_name):
        group = str(group_name).strip()
        if not group:
            return node
        members = self._groups.setdefault(group, set())
        members.add(node)
        if hasattr(node, "_groups"):
            node._groups.add(group)
        return node

    def remove_from_group(self, node, group_name):
        group = str(group_name).strip()
        members = self._groups.get(group)
        if members is not None:
            members.discard(node)
            if not members:
                self._groups.pop(group, None)
        if hasattr(node, "_groups"):
            node._groups.discard(group)
        return node

    def is_in_group(self, node, group_name):
        group = str(group_name).strip()
        return node in self._groups.get(group, set())

    def get_nodes_in_group(self, group_name):
        group = str(group_name).strip()
        return list(self._groups.get(group, set()))

    def call_group(self, group_name, method_name, *args, **kwargs):
        for node in list(self.get_nodes_in_group(group_name)):
            method = getattr(node, method_name, None)
            if callable(method):
                method(*args, **kwargs)

