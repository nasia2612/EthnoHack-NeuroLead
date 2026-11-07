"""Configure the repository's notebook filter and hooks in this clone.

Git does not apply a repository's own filter or hook settings automatically, so
run this once after cloning:

    python tools/setup-git-filters.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args):
    subprocess.run(['git', '-C', str(ROOT), *args], check=True)


def main():
    try:
        import nbformat  # noqa: F401
    except ImportError:
        sys.exit('nbformat is missing. Run: pip install -r requirements.txt')

    clean = '"{}" tools/nbstrip.py'.format(Path(sys.executable).as_posix())
    git('config', 'filter.nbstrip.clean', clean)
    git('config', 'filter.nbstrip.smudge', 'cat')
    git('config', 'filter.nbstrip.required', 'true')
    git('config', 'core.hooksPath', 'tools/githooks')

    print('nbstrip filter and hooks configured for', ROOT)
    print('Notebook outputs are now stripped when files are staged.')


if __name__ == '__main__':
    main()
