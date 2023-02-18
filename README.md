# Hello Playwright (Python)
This is an example implementation of automated tests using Playwright with Python (Pytest).

## Dependencies
* Python (I use version 3.10)

## Application under tests
We'll be testing a web application written in React from this repository: [GUI Automation Playground](https://github.com/rafaljab/gui-automation-playground).

Install and run the application according to the instructions on the above page.

## Set up
Download the repository:
```bash
git clone https://github.com/rafaljab/helloPlaywrightPy.git
```
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
