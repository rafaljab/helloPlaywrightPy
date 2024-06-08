# Hello Playwright (Python)
This is an example implementation of automated tests using Playwright with Python (and Pytest).

You can also check how this can be done using Playwright with Typescript here: [hello-playwright-ts](https://github.com/rafaljab/hello-playwright-ts).

## Features
* Page Object Model
* Pytest fixtures
* Parametrized tests
* Markers (tagged tests)
* CI Pipeline (GitHub Actions)
* HTML reports

## Application under tests
We'll be testing a web application written in React from this repository: [GUI Automation Playground](https://github.com/rafaljab/gui-automation-playground) (v1.2.0).

Install and run the application according to the instructions on the above page.

## Dependencies
* Python (I use version 3.10)

## Set up
Clone the repository:
```bash
git clone https://github.com/rafaljab/helloPlaywrightPy.git
```
If you want more freedom, you can fork the repository first instead of cloning it directly.

Then you need to create a virtual environment.
If you don't have virtualenv package installed on your machine, you need to run this command first:
```bash
pip install virtualenv
```
Now, you can create and activate a new virtual environment, but first, go to the main catalog:
```bash
cd helloPlaywrightPy
python -m venv env
.\env\Scripts\activate
```
The above instructions work for Windows (Powershell). If you have Unix/macOS or want to learn more about virtual environments, here's the official documentation: [Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Now, when you've activated the virtual environment, install all required packages in it:
```bash
pip install -r requirements.txt
```

Then install all required tools to run Playwright tests:
```bash
playwright install
```

Create an `.env` file in the root directory (`helloPlaywrightPy`).
This file is ignored by Git and should contain a variable for the domain:
```
DOMAIN=https://rafaljab.github.io
```

You're all set!

## Running tests

Just run the following command:
```bash
pytest
```

The tests will run without launching the browser.
If you want to see the progress of the tests, use the `headed` mode and the `slowmo` option.
`slowmo=1000` means that each action will be performed in 1s intervals.

```bash
pytest --headed --slowmo=1000
```

Generating tests report:
```bash
pytest --template=html1/index.html --report=report.html
```

Running tests for a given marker:
```bash
pytest -m e2e
```

You can also exclude tests with a given marker:
```bash
pytest -m "not e2e"
```

You can freely combine different commands.
Pytest is very flexible and allows you to specify which tests to run in different ways.
More details in the documentation - [Command-line Flags](https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags)
