# TODO

**Please keep this updated if you have issues or ideas for features**  
this is bootstrapped alternative to github ticketing / jira board

**Use until we set up ticketing for this project**

## TODO List

### High Priority

1. High Priority Tickets Here
   1. Just update the checkers if you work on something.

### General

- [ ] 1. Add functionality for pull update summary.

  - [x] `git diff HEAD@{1} HEAD` functionality
  - [x] integrate functionality with `gcpull` CLI
  - [x] create `prompts/pull_summary.txt` template prompt for `gcpull` LLM call.
  - [] Add git status, git diff doesnt account for untracked files

- [ ] 2. Retrieval of files for context in prompting template

  - [ ] currently only using `basic_PR_template.txt` for prompting
  - [-] will need context from `git diff` output for entire files that were changed
  - [ ] meaning, we only pass into the LLM input the `git diff` output and the prompt template
    - [ ] `git diff` is not enough context for the input
    - [-] need to retrieve info on the whole file for all files modified
  - [ ] Must figure out how to structure this retrieval
    

- [ ] 3. Optimize local LLM execution for different SoTA models

  - [x] Gemini API online eval
  - [ ] Downloading and connecting DeepSeek
    - [ ] https://www.youtube.com/watch?v=72Ef65B65JA
  - [ ] first attempted openAI API (did not want to pay), changed to llama.cpp
    - [ ] llama.cpp is not best model, but runs locally and is free
  - [ ] HuggingFace integration?
  - [ ] LangChain integration
  - [ ] Groq free online inference API

- [-] 4. VSCode extension using `python src/gittercommitter.py (--staged)` CLI command

  - [x] need to figure out how to write VSCode extension
    - [x] this will be in Node.js probably
  - [1] Two ways
    1.  VSCode hosts CLI tool as subprocess (easy to code)
    2.  VSCode POST for CLI local server (harder to code, but maybe migrate to because more room for future dev)
  - [] polish this out to take user input from terminal 
  - [] publish extension

- [x] 5. CLI tool command aesthetics
  - UPDATE: Made `pyproject.toml` file for prettier CLI tool commands
  - install with `pip install -e .`
  - check manual `gcpc --help`
  - [ ] Figure out `man gcpc` page.
  - [ ] Add `.md` browser page that opens with `gcpc --man` or `man gcpc`.
  - [x] currently, command is a fake CLI command: `python src/gittercommitter.py (--staged)`
    - [x] wrapper `click` interface over python script
  - [x] want to beautify this as a real CLI command `gcpc` (gitter committer pre commit)
    - [x] possibly make multiple CLI commands
      - [x] `gcpc` for pre commit LLM call (feature 1 in README)
      - [x] `gcpull` for merge notes (feature 2 in README)
      - [ ] etc

1. [ ] 6. Figure out external installation format

   - [ ] how will users install this program? options include:
     - [ ] `pip install` : making this a pip package
       - [ ] python only
     - [ ] `git clone` to `Make` : installing from git repo
     - [ ] download from our website
     - [ ] installation of VSCode extension from VSCode store
   - [ ] Need to figure out installation on the VSCode extensions and on the CLI tools side

2. [ ] 7. LLM evaluation
   - [ ] Need metrics for LLMs output evaluation
   - [ ] If we are actually doing good job with the output or not.
     - [ ] need metrics + feedback / debugging / monitoring for models

### Backlog
- [ ] If diff too long, add file-by-file summaries
