# Gitter Commiter

## Table of Contents

[TODO List](TODO.md)  
please update with ideas / tickets

- [Gitter Commiter](#gitter-commiter)
  - [Table of Contents](#table-of-contents)
  - [Idea](#idea)
  - [Features](#features)
  - [Description](#description)
    - [Feature 1](#feature-1)
    - [Feature 2](#feature-2)
    - [Feature 3](#feature-3)
  - [Setup](#setup)
  - [Trying to beat](#trying-to-beat)

## Idea

CLI tool and VSCode extension for AI precommit hook and pull code update changelogs.

## Features

1. CLI precommit pipeline that circumvents the time spent in PR browser screen
2. VSCode (jetbrains, eclipse) extension that shows behavior change from summaries from the precommit.

   - as well as changes from a pull
   - in future, chat bot with this knowledge

3. All local LLM inference - No data saved in inference, no security risks.

## Description

### Feature 1

Before you push a change, the CLI hooks into your diff and says: "Your changes update the password hashing function from SHA-1 to bcrypt. This improves security but may break backward compatibility."

Or: “You created a new file called xyz which is React code for the interface. Seems like you removed all the html code from the php file and migrated into the xyz file.”

CLI / git hook on local commits:  
we ai generate commit messages, + PR summary + changelog.  
this is precommit - and this means we circumvent the codeium forge use in browser.

We generate detailed changlog with behavior change - for the local commit

### Feature 2

when we pull from git,
we also have in IDE changelog from the pull.

so we give breakdown of what the new pull has done with behavior, performance, security, etc.

so when a dev pulls, he doesn’t need to go to SCM to see what the changes in the new pull were.
this can also be chatbot bc of LLM
“what does the new pull do to latency” or whatever

### Feature 3

Codeium forge is all on chrome extension -> cloud inference.

ours is CLI so its local -> local inference
this means we are private - no company security risk. We can run on no internet. So we don’t need to save any of the code input to the LLM. Whereas, most companies probably will not allow for devs to use codeium forge bc its online.

## Setup

1. Clone git repo
2. Ensure you're using `Python 3.13.1` locally for venv.
   - can use something like `pyenv` to make sure you are on this version.
3. `python -m venv venv` make virtual dev environment for Python.
4. `pip install -r requirements.txt`
5. Add llama.cpp installation guide here
   - need installation for LLMs
6. If using OpenAI API, go make an API key online
   - set the API key, `export OPENAI_API_KEY=your-key-here`
   - or use an .env file
7. Run code with `python src/gittercommitter.py (--staged)`
8. `pip install -e .` for editable mode installation of `gcpc` and other CLI tools for dev.

## Trying to beat

https://windsurf.com/forge
Chrome extension for PR
https://www.reddit.com/r/Jetbrains/comments/1c6dfi4/git_assistant_is_a_plugin_that_utilizes_git_diff/
Uses git diff / openai to autogenerate commit messages
https://github.com/Nutlope/aicommits  
https://marketplace.visualstudio.com/items?itemName=ArielPollack.gitsmart
