import os.path
import sys
from types import ModuleType

print("running importer")


def import_(module_name, module_file, module_path):
    if module_name in sys.modules:
        return sys.modules[module_name]

    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    # print(module_rel_file_path)
    # print(f"Is {module_file} exist? {os.path.exists(module_abs_file_path)}")

    # Need to read the text source code from module1_source.py
    with open(module_rel_file_path, "r") as code_file:
        source_code = code_file.read()

    # create a module
    mod = ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    # set a ref in the sys.modules
    sys.modules[module_name] = mod

    # compile
    code = compile(source_code, filename=module_abs_file_path, mode="exec")

    # Let's execute
    exec(code, mod.__dict__)

    return sys.modules[module_name]
