import click
import collections
from gittercommitter.llm_interface import summarize_diff_openai, summarize_diff_gemini
from gittercommitter.diff_utils import get_git_diff_gcpc, get_changed_files_names_gcpc, get_entire_file

@click.command()
@click.option('--staged', '-s', is_flag=True, help="Use staged changes (git diff --cached)")
@click.option('--model', '-m', type=click.Choice(['openai', 'gemini']), default='gemini',
              help="Choose which model to use (openai or gemini)")
def main(staged, model):
    """Generate a behavioral summary of the git diff using the selected LLM."""
    diff_text = get_git_diff_gcpc(staged=staged)
    if not diff_text.strip():
        click.secho("No diff found.", fg="yellow")
        return
    
    # this all inprogress, will finish later 
    # Need to edit summarize_diff to take in all these changed files and have it attach to the prompt
    changed_files = collections.defautdict(list)
    changed_files_names = get_changed_files_names_gcpc()
    for file_name in changed_files_names:
        entire_file_original = get_entire_file("original", file_name)
        entire_file_current = get_entire_file("current", file_name)
        changed_files["original"].append(entire_file_original)
        changed_files["current"].append(entire_file_current)

    click.secho(f"Generating summary using {model}...\n", fg="cyan")

    if model == 'openai':
        click.secho("Don't have openai functionality for paid API yet.", fg="red")
        # summary = summarize_diff_openai(diff_text)
    elif model == 'gemini':
        # print('gemini')
        summary = summarize_diff_gemini(diff_text)
        click.secho(summary, fg="green")

    # click.secho(summary, fg="green")

if __name__ == '__main__':
    main()
