# Hello Playwright (Python)
This is an example implementation of automated tests using Playwright with Python (Pytest).

## Dependencies
* Python (I use version 3.10)

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
