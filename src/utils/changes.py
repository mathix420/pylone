import subprocess


def detect_changes(path=None, ref_commit=None, cwd='.'):
    """
    This function return True if changes are detected in the `path` location
    """
    command = ['git', 'diff']
    if ref_commit:
        command.append(ref_commit)
    if path:
        command.append(path)
    process = subprocess.run(command, capture_output=True, cwd=cwd)
    return bool(process.stdout)


def get_last_commit(branch='HEAD', cwd='.'):
    """
    This function return the last commit hash
    """
    process = subprocess.run(
        ['git', 'rev-parse', branch],
        capture_output=True,
        cwd=cwd
    )
    # Removing the '\n'
    return process.stdout.decode('utf-8')[:-1]