'''
This script takes input from the user to decide which of the following they'd like to do:
1. Get all cookies from the browser (Chrome)
2. Get all cookies from a particular domain
3. Get a particular cookie from a particular domain
'''

# Import required libraries
import browser_cookie3
import typer

app = typer.Typer()

@app.command()
def get_all_cookies():
    cookies = list(browser_cookie3.load())
    print(cookies)

# Create a function to get the cookies from the browser
@app.command()
def getCookiesFromDomain(domain: str, cookieName: str):

    Cookies={}
    chromeCookies = list(browser_cookie3.chrome())

    for cookie in chromeCookies:

        if (domain in cookie.domain):
            #print (cookie.name, cookie.domain,cookie.value)
            Cookies[cookie.name]=cookie.value

    if(cookieName!=''):
        try:
            return Cookies[cookieName] #return specified cookie
        except:
            return {} #if exception raised return an empty dictionary
    else:
        return Cookies #return all cookies or nothing


# Test the function to see if it's working
## print(getCookiesFromDomain('google',''))

if __name__ == "__main__":
    app()
