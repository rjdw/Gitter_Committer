import subprocess

def get_git_diff(staged=False):
    cmd = ['git', 'diff', '--cached'] if staged else ['git', 'diff']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def get_git_diff_from_pull():
    cmd = ['git', 'diff', 'HEAD@{1}', 'HEAD']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def get_entire_file(version, file_path):
    if version == "before":
        cmd = ['git', 'show', f'HEAD@{{1}}:{file_path}']
    elif version == "after":
        cmd = ['git', 'show', f'HEAD:{file_path}']
    else:
        return "Invalid version specified."

    result = subprocess.run(cmd, capture_output=True, text=True)
    
    return result.stdout

def get_changed_files_names():
    cmd = ['git', 'diff', '--name-only', 'HEAD@{1}', 'HEAD']
    result = subprocess.run(cmd, capture_output=True, text=True)

    return result.stdout.strip().splitlines()