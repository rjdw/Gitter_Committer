import subprocess

def get_git_diff(staged=False):
    cmd = ['git', 'diff', '--cached'] if staged else ['git', 'diff']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout