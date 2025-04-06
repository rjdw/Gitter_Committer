import click
import subprocess
from llm_interface import summarize_diff
from diff_utils import get_git_diff

@click.command()
@click.option('--staged', is_flag=True, help="Use staged changes (git diff --cached)")
def main(staged):
    diff_text = get_git_diff(staged=staged)
    # print(diff_text)
    if not diff_text.strip():
        print("No diff found.")
        return
    print("Generating behavioral summary...\n")
    summary = summarize_diff(diff_text)
    print(summary)

if __name__ == '__main__':
    main()