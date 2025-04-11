import subprocess

def get_git_diff_gcpc(staged=False):
    cmd = ['git', 'diff', '--cached'] if staged else ['git', 'diff']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def get_git_diff_gcpull():
    cmd = ['git', 'diff', 'HEAD@{1}', 'HEAD']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def get_entire_file_gcpc(version, file_path, staged=False):
    if version == "original":
        # Committed version (HEAD)
        cmd = ['git', 'show', f'HEAD:{file_path}']
        result = subprocess.run(cmd, capture_output=True, text=True)

    elif version == "current":
        if staged:
            # Staged version (from index)
            cmd = ['git', 'show', f':{file_path}']
            result = subprocess.run(cmd, capture_output=True, text=True)
        else:
            # Seems to be no git command to get unchanged values
            # Unstaged version (read from disk)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                return f"[Error reading {file_path} from disk]\n{str(e)}"
    else:
        return f"Invalid version: {version}"

    if result.returncode != 0:
        return f"[Error retrieving {version} of {file_path}]\n{result.stderr.strip()}"

    return result.stdout


def get_entire_file_gcpull(version, file_path):
    if version == "original":
        cmd = ['git', 'show', f'HEAD@{{1}}:{file_path}']
    elif version == "current":
        cmd = ['git', 'show', f'HEAD:{file_path}']
    else:
        return f"Invalid version: {version}"
    
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return f"[Error retrieving {version} of {file_path}]\n{result.stderr.strip()}"

    return result.stdout


def get_changed_files_names_gcpc(staged=False):
    cmd = ['git', 'diff', '--name-only', '--cached'] if staged else ['git', 'diff', '--name-only']
    result = subprocess.run(cmd, capture_output=True, text=True)

    return result.stdout.strip().splitlines()
def get_changed_files_names_gcpull():
    cmd = ['git', 'diff', '--name-only', 'HEAD@{1}', 'HEAD']
    result = subprocess.run(cmd, capture_output=True, text=True)

    return result.stdout.strip().splitlines()