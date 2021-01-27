import os
import sys


SCRIPT_NAME = sys.argv[0].split(os.path.sep)[-1]
DESCRIPTION = """Neovim wrapper project to install as a script

Useful to being able to install neovim with something like pipx

Usage:
{SCRIPT_NAME} --python
{SCRIPT_NAME} --vim
""".format(
    **locals()
)


def main():
    if "--python" in sys.argv:
        print(sys.executable)
    elif "--vim" in sys.argv:
        suffix = "3" if sys.version_info.major == 3 else ""
        name = sys.executable
        print("let g:python{suffix}_host_prog = '{name}'".format(**locals()))
    else:
        print(DESCRIPTION)


if __name__ == "__main__":
    main()
