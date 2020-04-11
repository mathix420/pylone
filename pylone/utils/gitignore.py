from os import path


def add_to_gitignore(filenames):
    if isinstance(filenames, str):
        filenames = [filenames]
    if not path.isfile('.gitignore'):
        return
    with open('.gitignore') as fp:
        file = fp.read().strip() + '\n\n# Pylone\n'
    for name in filenames:
        if name in file: continue
        file = file + f'{name}\n'
    with open('.gitignore', 'w') as fp:
        fp.write(file.strip() + '\n')
