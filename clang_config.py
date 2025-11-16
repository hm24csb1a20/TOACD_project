import clang.cindex as cindex

_lib_loaded = False

def config():
    global _lib_loaded

    if _lib_loaded:
        return

    try:
        cindex.Config.set_library_file(r"C:\Program Files\LLVM\bin\libclang.dll")
    except Exception:
        pass

    _lib_loaded = True
