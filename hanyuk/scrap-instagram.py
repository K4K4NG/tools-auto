# // Please use this script specifically for learning.
# // If you misuse it, it is your right.
# // I am not responsible for your detrimental actionsimport requests
# // My code is not perfect, I am still learning.
# // I am not responsible for your actions.
# // My Website : https://github.com/K4K4NG
# // My Medsos : IG @ksyfmldkkk_  FB : Sory my facebook random
# // My Country : Indonesia
# // My Language : Python,Java,C++,C lang,C#,PHP,HTML,CSS,JS,SQL
# // My City : Bandung
# // My School : Private
# // Don't recode or copy my code in the name of the person who created it
# // Don't hope in falsehood because it will make you fall to the lowest point

# // [ ----------- MY QUOTES ----------- ]
# //  - STRUGGLING TO PURSUE HOPE, ENDING PAINFULLY :)
# //  - STILL STRUGGLING WAITING FOR HIM TO COME HOME, AND GOING TO LEAVE THE MEMORIES :)

# // [ -------------- Meledak X Cik Created -------------- ]

import os
import random
import json
import requests
import time
import datetime
import re
import youtube_dl
from pytube import YouTube
from datetime import datetime
from rich import print as prints
from bs4 import BeautifulSoup
from rich.panel import Panel as Panel
from rich.tree import Tree
from rich.table import Table as lipat
from rich.console import Console as solsapatu
from rich.columns import Columns as coli , Columns

console = solsapatu()
session = requests.Session()
ugen = []
Agus = []
xtr = []
# ------ [ warna dasar ] ------ #
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' # WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3


for x in range(1000):
    rr = random.randint
    rc = random.choice
    uacrack1 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX2101 Build/RKQ1.{str(rr(111111,211111))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack2 = f"Mozilla/5.0 (Linux; Android 11; Infinix X6512 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5000,5500))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; LG-H918 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.{str(rr(3200,3500))}.84 Mobile Safari/537.36"
    uacrack4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9,16))}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
    uacrack5 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    uacrack6 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; LEGEND MAX Build/RP1A.{str(rr(111111,210000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,4000))}.{str(rr(75,150))} UCBrowser/{str(rr(10,20))}.4.0.{str(rr(1300,1500))} Mobile Safari/537.36"
    uacrack7 = f"Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(4500,4900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uanyancek= random.choice([uacrack1, uacrack2, uacrack3, uacrack4, uacrack5, uacrack6, uacrack7])
    ugen.append(uanyancek)


def menu():
    os.system('cls')
    try:
        cek_data = requests.get("http://ip-api.com/json/").json
    except:
        cek_data = {'-'}
    try:
        Iplu = cek_data["query"]
    except:
        Iplu = {'-'}
    prints(
        Panel.fit(
            f"[bold red]Warning!!!!. [bold white]this script not give to people and Don't sell it illegally or legally",
            style="bold green"))
    Agus.append(
        Panel(
            f"[bold white]MENU SCRAPING INSTAGRAM   Created by : Meledak X Cik",
            style="bold green"))
    Agus.append(Panel(f"[bold white]ip adres : {Iplu}", style="bold green"))
    console.print(Columns(Agus))
    Meledak = f"[bold white]1\n2\n3\n4\n5\n6"
    Meledak2 = f"[bold white]Pencarian scraping melewati foto\nPencarian scraping melewati nama\nDownloader convert lagu video youtube\nDownloader post instagram from link\nDownload video highlist instagram (Login)\nUpdate Tools"
    Meledak3 = f"[bold green]ON[bold white]\n[bold green]ON[bold white]\n[bold green]ON[bold white]\n[bold green]ON[bold white]\n[bold red]OFF[bold white]\n[bold red]Up[bold white]"
    Cik = lipat()
    Cik.add_column(f"[bold white]NO", justify="center")
    Cik.add_column(f"[bold white]MENU", justify="center", width=55)
    Cik.add_column(f"[bold white]STATUS", justify="center")
    Cik.add_row(Meledak, Meledak2, Meledak3)
    console.print(Cik, justify="left", style=f"bold green")
    i = input("Masukan Pilihan : ")
    if i == '1':
        url = input(f'Masukan link foto : ')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        caption = soup.find('meta', property='og:description')['content']
        likes = soup.find('meta', property='og:see_also')
        comments = soup.find('meta', property='og:see_also')
        print(f"Caption: {caption}")
    elif i == '2':
        username = input("Masukkan nama pengguna (username) Instagram: ")
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        followers_tag = soup.find('meta',
                                  attrs={
                                      'property': 'og:description',
                                      'content': True
                                  })
        if followers_tag:
            followers_content = followers_tag['content']
            followers_count = followers_content.split(',')[0].split()[0]
        following_tag = soup.find('meta',
                                  attrs={
                                      'property': 'og:description',
                                      'content': True
                                  })
        if following_tag:
            following_content = following_tag['content']
            following_count = following_content.split(',')[1].split()[0]
        post_tag = soup.find('meta',
                             attrs={
                                 'property': 'og:description',
                                 'content': True
                             })
        if post_tag:
            post_content = post_tag['content']
            post_count = post_content.split(',')[2].split()[0]

        profile_photo_tag = soup.find('meta', property='og:image')
        if profile_photo_tag:
            profile_photo_url = profile_photo_tag['content']
            filename = f"{username}_profile_photo.jpg"
            save_path = os.path.join(os.getcwd(), "profile_photos")
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            with open(os.path.join(save_path, filename), 'wb') as handler:
                handler.write(requests.get(profile_photo_url).content)
            print(
                f"Foto profil @{username} berhasil diunduh sebagai {filename} di folder profile_photos."
            )
        else:
            print("Foto profil tidak ditemukan.")
        link_url = soup.find('meta',
                             attrs={
                                 'property': 'og:url',
                                 'content': True
                             })
        if link_url:
            link_content = link_url['content']
            link_count = link_content.split('/')[4]
        print(f"Nama Pengguna: {username}")
        print(f"Akun @{username}")
        print(f"Jumlah Pengikut: {followers_count}")
        print(f"Jumlah yang Diikuti: {following_count}")
        print(f"Jumlah Postingan: {post_count}")
        print(f"Link username: {link_url}")
    elif i == '3':
        video_url = input("Masukkan URL YouTube: ")
        yt = YouTube(video_url)
        print("Mendownload...")
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(f"Download selesai {new_file}")
    elif i == '4':
        url = input("Masukkan link post instagram: ")
        username = input("Masukkan nama orang yang ada dalam foto: ")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find('meta', property='og:image')
        if meta_tag:
            filename = f"{username}_post.jpg"
            save_path = os.path.join(os.getcwd(), "profile_photos")
            img_url = meta_tag['content']
            img_data = requests.get(img_url).content
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            with open(os.path.join(save_path, filename), 'wb') as handler:
                handler.write(img_data)
            print("Download gambar selesai!")
        else:
            print("Tidak dapat menemukan gambar.")
    elif i == '5':
        prints(
            Panel.fit(
                "[bold green]Masih dalam uji coba di karenakan harus ada akses login[bold white]",
                style=f"bold green"))
        url = input("Masukkan id highlights instagram : ")
        response = requests.get(
            'https://z-p42.www.instagram.com/stories/highlights/{}/'.format(
                url))
        soup = BeautifulSoup(response.text, 'html.parser')
        titel = soup.find('meta', attrs={'property': 'og:title', 'content': True})
        titel_content = titel['content'] if titel else None
        titel_count = titel_content.split('/')[0].split()[0] if titel_content else None
        typee = soup.find('meta', attrs={'property': 'og:type', 'content': True})
        typee_content = typee['content'] if typee else None
        typee_count = typee_content.split(',')[0].split()[0] if typee_content else None 
        url_tag = soup.find('meta', attrs={'property': 'og:url', 'content': True})
        url_content = url_tag['content'] if url_tag else None
        url_count = url_content.split(',')[0].split()[0] if url_content else None
        print(f"Title Hightligh : {titel_count}")
        print(f"Tipe : {typee_count}")
        print(f"Url link : {url_count}")
    elif i == '6':
        prints(
            Panel.fit(
                f"[bold red]Maaf Update Belum Tersedia Oleh owner nya[bold white]",
                style="bold green"))
        time.sleep(1)
        menu()
    else:
        print("Pilihan tidak ditemukan")

def check_license(license_url, expected_key):
    response = requests.get(license_url)
    if response.status_code == 200:
        license_key = response.text.strip()
        if license_key == expected_key:
            return True
    return False


if __name__ == "__main__":
    os.system("cls")
    prints(
        Panel.fit(
            "[bold green]Silahkan masukkan license key untuk menggunakan skrip ini.[bold white]"
        ))
    prints(
        Panel.fit(
            "[bold green]Untuk Key nya bisa cari di github saya dan jangan lupa folow: https://github.com/K4K4NG/ [bold white]"
        ))
    license_url = "https://raw.githubusercontent.com/K4K4NG/key-licence/master/scrape-ig.txt"
    try:
        lisensi = open("check/lisen.txt", "r").read()
        if lisensi:
            prints(
                Panel.fit(f"[bold green]Your Lisen : {lisensi}[bold white]",
                          style="bold white"))
        else:
            prints(
                Panel.fit(
                    f"print('[bold red]Anda tidak memiliki kunci lisensi[bold white]",
                    style="bold red"))
    except FileNotFoundError:
        prints(
            Panel.fit(
                f"print('[bold red]File lisensi anda tidak buat manual saja : folder check , file : lisen.txt[bold white]",
                style="bold green"))
    except Exception as e:
        prints(
            Panel.fit(f"[bold red]Terjadi kesalahan: {e}[bold white]",
                      style="bold green"))
    expected_license_key = input("Masukkan license key: ")
    if check_license(license_url, expected_license_key):
        prints(
            Panel.fit(
                "[bold green]Lisensi valid. Melanjutkan eksekusi skrip...[bold white]"
            ))
        time.sleep(1)
        lisensi = open("check/lisen.txt", "w").write(expected_license_key)
        menu()
    else:
        prints(
            Panel.fit(
                "[bold red]Lisensi tidak valid. Skrip tidak dijalankan.[bold white]"
            ))
        exit()
