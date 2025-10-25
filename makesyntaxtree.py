from clang import cindex
import os
import subprocess

# point to clang in the computer not to use MSY2
cindex.Config.set_library_file(r"C:\Program Files\LLVM\bin\libclang.dll")


# def get_clang_includes():
#     """Return system include paths for C files."""
#     try:
#         output = subprocess.check_output(
#             ["clang", "-E", "-x", "c", "-", "-v"],
#             input=b"",
#             stderr=subprocess.STDOUT
#         ).decode(errors="ignore")

#         paths = []
#         capture = False
#         for line in output.splitlines():
#             if "#include <...> search starts here:" in line:
#                 capture = True
#                 continue
#             if "End of search list." in line:
#                 break
#             if capture:
#                 paths.append(line.strip())
#         return paths

#     except subprocess.CalledProcessError as e:
#         print("Error getting clang includes:", e)
#         return []


def parse_c_file(file_path):
    index = cindex.Index.create()
    try:
        tu = index.parse(file_path, args=["-x", "c", "-std=c11"])
    except Exception as e:
        raise RuntimeError(f"Unable to parse {file_path}: {e}")

    node_kinds = []
    collect_kinds(tu.cursor, node_kinds)
    return node_kinds
# need to make recursive as teh tree if not will only visit the immediate children of node
def collect_kinds(node, kinds):
    kinds.append(node.kind.name)
    for child in node.get_children():
        collect_kinds(child, kinds)



if __name__ == "__main__":
    current = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current, "cpp_tests", "benign","__cos.c")
    node_kinds = parse_c_file(file_path=file_path)
    print("Collected node kinds:")
    for k in node_kinds:
        print("-", k)
    print("new malicius code")
    file_path = os.path.join(current, "cpp_tests", "malicious","CWE506_Embedded_Malicious_Code__file_transfer_connect_socket_01.c")
    node_kinds = parse_c_file(file_path=file_path)
    print("Collected node kinds:")
    for k in node_kinds:
        print("-", k)