import requests
import time
import re
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree

session = requests.Session()


def namapw():
    print('')
    idf = input(f"+_ masukan username : ")
    pas = input(f"+_ masukan password : ")
    time.sleep(1)
    p = session.get("https://lms.smkn4padalarang.sch.id/login/index.php", verify=False)
    heade = {
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Host': 'lms.smkn4padalarang.sch.id',
        'Referer': 'https://lms.smkn4padalarang.sch.id/',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    data = {
        "logintoken": re.search('name="logintoken" value="(.*?)"', str(p.text)).group(1),
        "username": idf,
        "password": pas
    }
    response = session.post(
        "https://lms.smkn4padalarang.sch.id/login/index.php",
        headers=heade,
        data=data,
        allow_redirects=True,
        verify=False
    )

    if 'Dashboard' in response.text:
        koki = (";").join([
            kamu + "=" + asu
            for kamu, asu in session.cookies.get_dict().items()
        ])
        Meledak = Tree(Panel.fit(f"[bold green]Log in Success"))
        Meledak.add(Panel.fit(f"[bold green]Username password lms : {pas}|{idf}"))
        Meledak.add(Panel.fit(f"[bold green]Cookies lms : {koki}"))
        prints(Meledak)
        time.sleep(2)
    else:
        prints(Panel.fit(f"[bold red]username dan password anda salah"))



namapw()
