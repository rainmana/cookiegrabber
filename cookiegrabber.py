'''
This script takes input from the user to decide which of the following they'd like to do:
1. Get all cookies from the browser (Chrome)
2. Get all cookies from a particular domain
3. Get a particular cookie from a particular domain
'''

# Import required libraries
import browser_cookie3
import typer
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from rich import print
import bleach

# Initialize typer :)
app = typer.Typer()

# Create a function to get all cookies from all browsers
@app.command()
def get_all_cookies():
    # Load all cookies from all browsers as assign to the variable cookies
    cookies = browser_cookie3.load()

    # Create a dictionary to store the cookies from the cookies class
    domain_cookies = {}

    # Loop through the cookies and add them to the dictionary
    for cookie in cookies:
        domain_cookies[cookie.name] = cookie.value

    # Convert the dictionary to JSON and clean with bleach
    json_cookies = json.dumps(domain_cookies, indent=4)
    clean_json = bleach.clean(json_cookies, tags=[], attributes={}, strip=True)

    # Print the bleached JSON as pretty JSON
    print(clean_json)


# Create a function to get all cookies from a particular domain and dump them as pretty JSON
@app.command()
def get_cookies_from_domain(domain: str):
    # Load all cookies from all browsers
    cookies = browser_cookie3.load()

    # Create a dictionary to store the cookies from the cookie class
    domain_cookies = {}

    # Loop through the cookies and add them to the dictionary
    for cookie in cookies:
        if (domain in cookie.domain):
            domain_cookies[cookie.name] = cookie.value

    # Convert the dictionary to JSON and clean with bleach
    json_cookies = json.dumps(domain_cookies, indent=4)
    clean_json = bleach.clean(json_cookies, tags=[], attributes={}, strip=True)

    # Print the bleached JSON as pretty JSON
    print(clean_json)

# Create a function to request a website which requires a cookie to access and return the page content
@app.command()
def get_site_text(url: str = typer.Argument(..., help="The URL of the site you want to access")):

    page = url
    # Get all cookies from all browsers
    cookies = browser_cookie3.load()

    # Use the cookies to access the website with requests
    request = requests.get(page, cookies=cookies)

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(request.content, 'html.parser')

    # Get the text of the page
    text = soup.get_text()
    # Print the HTML
    print(text)

# Make typer run the app
if __name__ == "__main__":
    app()
