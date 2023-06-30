# Selenium Examples
[![Python application](https://github.com/RISE-UNIBAS/selenium-examples/actions/workflows/python-app.yml/badge.svg)](https://github.com/RISE-UNIBAS/selenium-examples/actions/workflows/python-app.yml)

*This is a RISE example script. It should work in itself. You can clone or download the repository. If you have additions to an example which you would like to share, you are welcome to create a Pull Request.*


## Contents
Examples how to use selenium for web scraping. There are currently two examples:

- e-manuscripta.ch (Simple search and download of preview images)
- NZZ Newspaper archive (Example with login and Mouse simulation, NZZ-Login and permission required)

## Using the examples

- Install the requirements from requirements.txt:

```
pip install -f requirements.txt
```

- Edit the example (change search terms or login credentials) [Optional]

- Execute the example:

```
python e_manuscripta.py
```

## Writing your own example
There is extensive documentation on how to use selenium for python: https://selenium-python.readthedocs.io/ 

In general, follow these steps/tips when building your example:
- Go to the website in question. Find the search field (or whatever element you are trying to interact with) and right-click it. Choose "Inspect". 
- Inspect the element in the source and find out what makes it "findable" (ideally an "id" parameter but often class values are also unique for search fields).
- Find the element with the selenium driver and send keys to it. Send the "enter" key.
- On the result page, find the structure surrounding your result elements and iterate over its children with selenium
- For each result, find the information you are looking for and save it.

## Disclaimer
These are examples on how to use selenium for getting information from the internet. Be aware that some sites may prohibit automatic scraping of information. Always make sure that there is no better way to get the information (for example over an API) when scraping data. Be aware that website structures often change and your scraper may not work anymore very soon.
