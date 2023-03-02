import requests
from datetime import datetime

def getURL():
    return input("Enter a URL: ")

def performRequest(url: str):
    print("Performing GET request...")
    return requests.get(url)

def printResponseHeaders(response: requests.Response):
    print("Response headers:")
    for i, header in enumerate(response.headers):
        print(f"{i+1:2d}.\t{header} -> {response.headers[header]}")

def printURLInfo(response: requests.Response):
    if 'Server' in response.headers:
        print(f"Web server: {response.headers['Server']}")
    else:
        print("The website does not specify a web server.")
    if 'Set-Cookie' in response.headers:
        print("Cookies info:")
        cookies = response.raw.headers.getlist("Set-Cookie")
        for i, cookie in enumerate(cookies):
            cookieData = cookie.split(';')
            print(f"{i+1:2d}.\tName: {cookieData[0].split('=')[0]}")
            try:
                print(f"\tExpires: {next(datum.split('=')[1] for datum in cookieData if 'Expires' in datum or 'expires' in datum)}")
            except StopIteration:
                print("\tUndefined expiration date.")
    else:
        print("The website did not send any cookies.")

    # This method does not find cookies without value.

    # if len(response.cookies) == 0:
    #     print("The website did not send any cookies.")
    # else:
    #     print("Cookies info:")
    #     for i, cookie in enumerate(response.cookies):
    #         print(f"{i+1:2d}.\tName: {cookie.name}\tExpires: {datetime.fromtimestamp(cookie.expires) if cookie.expires is not None else 'Undefined expiration date'}")

def main():
    url = getURL()
    with performRequest(url) as response:
        printResponseHeaders(response)
        print("---------------------")
        printURLInfo(response)

if __name__ == "__main__":
    main()