import click
import collections
from gittercommitter.llm_interface import summarize_diff_openai, generate_commit_message_gemini
from gittercommitter.diff_utils import get_git_diff_gcpc, get_changed_files_names_gcpc, get_entire_file_gcpc

@click.command()
@click.option('--staged', '-s', is_flag=True, help="Use staged changes (git diff --cached)")
@click.option('--model', '-m', type=click.Choice(['openai', 'gemini']), default='gemini',
              help="Choose which model to use (openai or gemini)")
def main(staged, model):
    """Generate commit message using the selected LLM."""
    diff_text = get_git_diff_gcpc(staged=staged)
    if not diff_text.strip():
        if staged:
            click.secho("No staged changes found.", fg="yellow")
        else:
            click.secho("No diff found.", fg="yellow")
        return
    
    changed_files = collections.defaultdict(list)
    changed_files_names = get_changed_files_names_gcpc()
    for file_path in changed_files_names:
        entire_file_original = get_entire_file_gcpc("original", file_path, staged)
        entire_file_current = get_entire_file_gcpc("current", file_path, staged)
        changed_files["original"].append((file_path, entire_file_original))
        changed_files["current"].append((file_path, entire_file_current))


    file_data_formatted = ""
    for (name, original), (_, current) in zip(changed_files["original"], changed_files["current"]):
        file_data_formatted += f"[{name}] BEFORE:\n{original}\n\n"
        file_data_formatted += f"[{name}] AFTER:\n{current}\n\n"

    click.secho(f"Generating commit message using {model}...\n", fg="cyan")

    if model == 'openai':
        click.secho("Don't have openai functionality for paid API yet.", fg="red")
        # summary = summarize_diff_openai(diff_text)
    elif model == 'gemini':
        # print('gemini')
        summary = generate_commit_message_gemini(diff_text, file_data_formatted)
        click.secho(summary, fg="green")

    # click.secho(summary, fg="green")

if __name__ == '__main__':
    main()
