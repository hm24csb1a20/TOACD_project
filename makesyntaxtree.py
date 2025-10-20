from clang import cindex
import os
import subprocess
cindex.Config.set_library_file(r"C:\Program Files\LLVM\bin\libclang.dll")

# get all the libraries to be have to be imported from the cpp file 
def get_clang_includes():
    try:
        output = subprocess.check_output(
            ["clang", "-E", "-x", "c++", "-", "-v"],
            input=b"",
            stderr=subprocess.STDOUT
        ).decode(errors="ignore")

        paths = []
        capture = False
        for line in output.splitlines():
            if "#include <...> search starts here:" in line:
                capture = True
                continue
            if "End of search list." in line:
                break
            if capture:
                paths.append(line.strip())
        return paths

    except subprocess.CalledProcessError as e:
        print("Error getting clang includes:", e)
        return []

# parsing the given file to return list of Node types 
def parse_cpp_file(file_path):
    index = cindex.Index.create()

    include_paths = get_clang_includes()

    args = ["-std=c++17"]
    for path in include_paths:
        args.extend(["-I", path])

    # Parse the translation unit
    tu = index.parse(file_path, args=args)
    if not tu:
        raise RuntimeError("Unable to parse file!")

    node_kinds = []
    collect_kinds(tu.cursor, node_kinds)
    return node_kinds

# helper function to make the list
def collect_kinds(node, kinds):
    kinds.append(node.kind.name)
    for child in node.get_children():
        collect_kinds(child, kinds)

# if __name__ == "__main__":
#     current = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(current, "tests", "test.cpp")

#     node_kinds = parse_cpp_file(file_path)
#     print("Collected node kinds:")
#     for k in node_kinds:
#         print("-", k)