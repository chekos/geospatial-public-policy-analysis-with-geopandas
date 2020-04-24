from pathlib import Path

def tree(directory):
    """
    Displays a directory's tree.
    """
    directory = Path(directory)
    print(f'+ {directory}')
    for path in sorted(directory.rglob('[!.]*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')