import pyshorteners

# ANSI escape code for red color
RED = "\033[91m"
RESET = "\033[0m"  # Reset color

url = input('Enter the URL: ')

def shortenurl(url):
    s = pyshorteners.Shortener(timeout=10)
    try:
        shortened_url = s.tinyurl.short(url)
        print("\n" * 2)  # Adding some space between input and output
        print(f'{RED}The shortened url is: {shortened_url}{RESET}')
    except Exception as e:
        print(f"Error: {e}")

shortenurl(url)
