import sys

if __name__ == "__main__":
    # The python that is executes is in the venv, that is what pre fix does
    print(sys.prefix)
    print(sys.exec_prefix)
    # Where python looks fir imports
    print(sys.path)
    #Hwta python does when try to import a module
