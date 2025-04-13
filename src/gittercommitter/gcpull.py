import click
import collections
from gittercommitter.llm_interface import summarize_diff_openai, summarize_diff_gemini
from gittercommitter.diff_utils import get_git_diff_gcpull, get_changed_files_names_gcpull, get_entire_file_gcpull

@click.command()
@click.option('--model', '-m', type=click.Choice(['openai', 'gemini']), default='gemini',
              help="Choose which model to use (openai or gemini)")
def main(model):
    """Generate a behavioral summary of the git diff using the selected LLM."""
    diff_text = get_git_diff_gcpull()
    if not diff_text.strip():
        click.secho("No pull diff found.", fg="yellow")
        return

    changed_files = collections.defaultdict(list)
    changed_files_names = get_changed_files_names_gcpull()
    for file_path in changed_files_names:
        entire_file_original = get_entire_file_gcpull("original", file_path)
        entire_file_current = get_entire_file_gcpull("current", file_path)
        changed_files["original"].append((file_path, entire_file_original))
        changed_files["current"].append((file_path, entire_file_current))


    file_data_formatted = ""
    for (name, original), (_, current) in zip(changed_files["original"], changed_files["current"]):
        file_data_formatted += f"[{name}] BEFORE:\n{original}\n\n"
        file_data_formatted += f"[{name}] AFTER:\n{current}\n\n"
        
    click.secho(f"Generating summary using {model}...\n", fg="cyan")

    if model == 'openai':
        click.secho("Don't have openai functionality for paid API yet.", fg="red")
        # summary = summarize_diff_openai(diff_text)
    elif model == 'gemini':
        # print('gemini')
        summary = summarize_diff_gemini(diff_text, file_data_formatted=file_data_formatted)
        click.secho(summary, fg="green")

    # click.secho(summary, fg="green")

if __name__ == '__main__':
    main()
