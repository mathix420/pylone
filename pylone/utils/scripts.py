from subprocess import check_output


def run(script):
    check_output(['/bin/bash', '-c', script])
