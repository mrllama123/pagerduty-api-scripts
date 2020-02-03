# PagerDuty-management-api
a POC for creating a management api for pagerduty tasks

# dev setup

## requirements 

- python 3.7 installed
- [pipenv](https://pipenv.readthedocs.io/en/latest/) installed via `pip install pipenv`

## vscode setup

just install the [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and open the folder from the gui or from the cli using `code .`
and it should setup everything (debugger, virtual env etc). If not set it up via cli.

## cli setup 

To do it via the cli its pretty simple, To setup the virtual env just run `pipenv` or 
`pipenv install` in the root directory. 

Then run `pipenv shell` to open a shell inside the virtual env or run `pipenv run <python script>.py` to run the python scripts outside of the shell