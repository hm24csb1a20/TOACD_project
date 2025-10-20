from clang import cindex
import os
# Point this to where LLVM installed
cindex.Config.set_library_file(r"C:\Program Files\LLVM\bin\libclang.dll")

index = cindex.Index.create()

current = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current,"tests","test.cpp")
tu = index.parse(file_path)

# Recursive walker
def collect_kinds(node, kinds):
    kinds.append(node.kind.name)
    for child in node.get_children():
        collect_kinds(child, kinds)

# Gather all kinds
node_kinds = []
collect_kinds(tu.cursor, node_kinds)

print(node_kinds)
