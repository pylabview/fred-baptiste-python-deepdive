import os


def create_module_file(module_name, **kwargs):
    """Create a module file named <module_name>.py
    Module has a single function (print_values) that
    will print out the supplied (stringified) kwargs.
    """
    module_fine_name = f"{module_name}.py"
    module_rel_file_path = module_fine_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, "w") as f:
        f.write(f"# {module_name}.py\n")
        f.write(f"print('--- running {module_name}.py ....')\n\n")
        f.write("def print_values():\n")

        for k, v in kwargs.items():
            f.write(f"\tprint('{str(k)}', '{str(v)}')\n")
