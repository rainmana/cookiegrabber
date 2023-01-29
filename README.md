# cookiegrabber

Simple Python3 script/CLI tool to grab and dump cookies from all browsers. Building further capabilities to make requests, sort, etc. as time goes on. This tool is focused around legal, ethical, and education penetration and security testing. Please read the [disclaimer](#disclaimer) before proceeding with installation and/or usage.

## Install and usage
1. `git clone https://github.com/rainmana/cookiegrabber`
2. `cd cookiegrabber`
3. `pip install -r requirements.txt`
4. `python3 cookiegrabber.py --help` for commandline based help
5. `python3 cookiebrabber.py function --help` for specific help on commandline arguments and options
6. `python3 cookiebrabber.py get-all-cookies` to dump all cookies from all browsers in pretty JSON (example functionality)

### Latest Update as of 1/29/2023:

- Get human-readable text from a site of your choosing to test whether extract cookies can load site content where they're typically required
- Implemented [Mozilla Bleach](https://github.com/mozilla/bleach) to strip new-line characters and other text artifacts from JSON-formatted cookiejars to ensure readability
- Get all cookies from all browsers for a domain of your choice
- Added [Textualize's Rich](https://github.com/Textualize/rich) library which integrates automagically with [Tiagalo's Typer](https://github.com/tiangolo/typer) for improved color-coding with Typer-provided command line arguments and output
- Cleaned up code and added actual comments and standardized function names


### TODO:

- [x] Add requirements.txt
- [ ] Add installation instructions
- [ ] Add a screenshot grabbing function
- [ ] Allow use as a module for additional functionality
- [ ] Add command line arguments to specify browser, domain, site/page, screenshots, etc.
- [ ] Structure more/add features making this more pentest/security auditing focused
- [ ] Add user-requested features and other 🦄's :)



## DISCLAIMER: 

This tool is provided for educational and responsible legal use only. I claim no responsbility for any end-users' usage in any way in whole or in part of usage of this tool. Using this tool without prior authorization is likely against the law in your locality/jurisdiction. It is the end-users' responsiblity to ensure they are in compliance with and adhere to any local laws regarding penetration testing, security testing, general usage, etc.
