import os

ext_file_path = os.environ["HOME"]
module_file_name = "module2.py"
file_abs_path = os.path.join(ext_file_path, module_file_name)

with open(file_abs_path, "w") as code:
    code.write("print('----- Running module2.py....')\n")
    code.write('x = "python"\n')
