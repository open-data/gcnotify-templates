[![Sync GC Notify Templates](https://github.com/open-data/gcnotify-templates/actions/workflows/pull-commit.yaml/badge.svg?branch=main&event=schedule)](https://github.com/open-data/gcnotify-templates/actions/workflows/pull-commit.yaml)

# GC Notify Templates

Python script to pull and version controll GC Notfiy template objects

## Requirements

* Python 3.6+

## Installation

1. Pull the repository: `git clone https://github.com/open-data/gcnotify-templates.git`
1. Navigate to new repo: `cd gcnotify-templates`
1. Create a python virtual environment: `python3 -m venv ./venv`
1. Activate the venv: `. venv/bin/activate`
1. Install the requirements into the venv: `pip install -r requirements.txt`
1. Run the python script: `python3 notify.py`

## GitHub Actions

The action is run at midnight and noon. It will build the python3 environment, and run the notify.py script.

This will fetch the templates from the GC Notify API and parse them into yaml files. It will commit any template changes, including deletions.