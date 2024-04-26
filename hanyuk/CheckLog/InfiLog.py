import requests
import time
import re
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree

session = requests.Session()


def login(email, password):
    print('')
    try:
        login_page = session.get("https://dash.infinityfree.com/login")
        login_soup = BeautifulSoup(login_page.text, 'html.parser')
        token = login_soup.find('input', {'name': '_token'}).get('value')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Referer': 'https://dash.infinityfree.com/login',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "_token": token,
            "username": email,
            "password": password,
            "captcha-type": "turnstile",
            "type": "submit"
        }

        response = session.post("https://dash.infinityfree.com/login", headers=headers, data=data)

        if 'Dashboard' in response.text:
            cookies = "; ".join([f"{name}={value}" for name, value in session.cookies.items()])
            success_tree = Tree(Panel.fit("[bold green]Log in Success"))
            success_tree.add(Panel.fit(f"[bold green]Username password lms : {email}|{password}"))
            success_tree.add(Panel.fit(f"[bold green]Cookies lms : {cookies}"))
            prints(success_tree)
            return True
        elif 'Invalid username or password' in response.text:
            prints(Panel.fit("[bold red]Invalid username or password"))
        else:
            prints(Panel.fit("[bold red]Login failed for unknown reason"))
    except Exception as e:
        prints(Panel.fit(f"[bold red]An error occurred: {str(e)}"))

    return False


email = input("+_ masukan email : ")
password = input("+_ masukan password : ")
if login(email, password):
    pass
else:
    pass
