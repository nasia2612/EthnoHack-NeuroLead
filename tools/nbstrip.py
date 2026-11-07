"""Remove cell outputs and environment metadata from a notebook on stdin.

Used as the `nbstrip` clean filter, so notebooks are committed without their
outputs. Outputs can embed local file paths and are large in diffs.
"""

import sys

import nbformat

KERNELSPEC = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}


def main():
    nb = nbformat.reads(sys.stdin.buffer.read().decode('utf-8'), as_version=4)
    for cell in nb.cells:
        cell.metadata = {}
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
    nb.metadata = {'kernelspec': KERNELSPEC, 'language_info': {'name': 'python'}}
    sys.stdout.buffer.write((nbformat.writes(nb) + '\n').encode('utf-8'))


if __name__ == '__main__':
    main()
