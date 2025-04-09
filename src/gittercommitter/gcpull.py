import click
from gittercommitter.llm_interface import summarize_diff_openai, summarize_diff_gemini
from gittercommitter.diff_utils import get_git_diff_from_pull

@click.command()
@click.option('--model', '-m', type=click.Choice(['openai', 'gemini']), default='gemini',
              help="Choose which model to use (openai or gemini)")
def main(model):
    """Generate a behavioral summary of the git diff using the selected LLM."""
    diff_text = get_git_diff_from_pull()
    if not diff_text.strip():
        click.secho("No diff found.", fg="yellow")
        return

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
