import requests
import html2text

print("\033[31mSTART of execution\033[0m\n")

print("\033[1m1 - Read Github TXT file\033[0m")
url = "https://raw.githubusercontent.com/Orangestack-com/Orangestack-com/main/orangestack.txt"
print("Url:", url)
try:
    req = requests.get(url)
    req = req.text
    print("\033[33mContent:\033[0m", req)
except OSError as err:
    print("ERROR: {0}".format(err), "\n")

print("\n\033[1m2 - Read Github PAGES file\033[0m")
url = "https://Orangestack-com.github.io"
print("Url:", url)
try:
    req = requests.get(url)
    req = req.text
    print("\033[33mContent:\033[0m\n", html2text.html2text(req))
except OSError as err:
    print("ERROR: {0}".format(err), "\n")

print("\033[1m3 - Download Github RELEASE (Zip file)\033[0m")
url2 = "https://github.com/GuillaumeFalourd/git-commit-push/zipball/main"
print("Url:", url2)
try:
    r = requests.get(url2)
    if r.status_code == 200:
        print('\033[33mFile size:\033[0m', len(r.content))
        with open(f'output.zip', 'wb') as fh:
            fh.write(r.content)
            print("\033[33mDownloaded file:\033[0m output.zip")
    else:
        print(r.text)
except OSError as err:
    print("ERROR: {0}".format(err), "\n")

print("\n\033[31mEND of execution\033[0m")
