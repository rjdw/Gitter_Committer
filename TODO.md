# TODO

**Please keep this updated if you have issues or ideas for features**  
this is bootstrapped alternative to github ticketing / jira board

**Use until we set up ticketing for this project**

## TODO List

1. Retrieval of files for context in prompting template

   - currently only using `basic_PR_template.txt` for prompting
   - will need context from `git diff` output for entire files that were changed
   - meaning, we only pass into the LLM input the `git diff` output and the prompt template
     - `git diff` is not enough context for the input
     - need to retrieve info on the whole file for all files modified
   - Must figure out how to structure this retrieval

2. Optimize local LLM execution for different SoTA models

   - Downloading and connecting DeepSeek
     - https://www.youtube.com/watch?v=72Ef65B65JA
   - first attempted openAI API (did not want to pay), changed to llama.cpp
     - llama.cpp is not best model, but runs locally and is free
   - HuggingFace integration?

3. VSCode extension using `python src/gittercommitter.py (--staged)` CLI command

   - need to figure out how to write VSCode extension
     - this will be in Node.js probably
   - Two ways
     1. VSCode hosts CLI tool as subprocess (easy to code)
     2. VSCode POST for CLI local server (harder to code, but maybe migrate to because more room for future dev)

4. CLI tool command aesthetics

   - currently, command is a fake CLI command: `python src/gittercommitter.py (--staged)`
     - wrapper `click` interface over python script
   - want to beautify this as a real CLI command `gcpc` (gitter committer pre commit)
     - possibly make multiple CLI commands
       - `gcpc` for pre commit LLM call (feature 1 in README)
       - `gcpull` for merge notes (feature 2 in README)
       - etc

5. Figure out external installation format
   - how will users install this program? options include:
     - `pip install` : making this a pip package
       - python only
     - `git clone` to `Make` : installing from git repo
     - download from our website
     - installation of VSCode extension from VSCode store
   - Need to figure out installation on the VSCode extensions and on the CLI tools side
