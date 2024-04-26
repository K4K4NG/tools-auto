#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
#--> Import Module & Run
from bs4 import BeautifulSoup
from rich.table import Table as me
from rich.columns import Columns as col, Columns
from rich.tree import Tree
from rich.panel import Panel
from rich import print as prints
from rich.console import Console as sol,Console
console=sol() 
#import lxml
import urllib
try :
    import os, sys, time, re, datetime, random
    from datetime import datetime
except Exception as e :
    print(e)
    exit('\nTerjadi Kesalahan!')
try :
    import requests
except Exception as e :
    os.system('pip install requests')
    import requests
try :
    import bs4
    from bs4 import BeautifulSoup as bs
except Exception as e :
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs
prox=open('.prox.txt','r').read().splitlines()
#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

#--> Global Variable
auth1 = 'Mkasyaf Meledaka X'
auth2 = 'Alya Anggrani Putri'
reco = 'Gausa Direcode Bos, Tinggal Pake Aja'
rede = 'Dibilangin Gausa Direcode'
key = len(auth1)*len(auth2)-len(auth1)
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
ok = 0
cp = 0
boys_name = ['Fahrul Dwi Candra','Muhammad Farhan','Ival','Achmad Fadil','Ihksan','Mas Muh Khoirul Afif','Damian Vasyl Isaac','Dominic Valdi Xander','Ephraim Benedict Gevariel','El Fatih Ghazwan','Fawwaz Rafisqy Ezaz','Faheem Fakhri Isyraq','Gianluca Nathanael Nadav','Haddad Ammar Ar-Rayyan','Istafa Tabriz Qiwam','Kenneth Krisantus Lazarus','Nathanael Alfred William','Vaskylo Yeremia Clearesta','Xaferius Eliel Antonios','Yesaya Nathanael Liam']
girls_name = ['Alya Anggrnii','Alya Kinana Juwairiyah','Rahma Putri','Adiva Arsyila Savina','Aqeela Nabiha Sakhi','Bilqis Adzkiya Rana','Chayra Ainin Qulaibah','Caliana Fiona Syafazea','Chaerunnisa Denia Athalla','Dhawiyah Nisrin Naziha','Dilara Adina Yuani','Farah Sachnaz Ashanty','Ghariyah Zharufa Abidah','Hamna Nafisa Raihana','Hanin Raihana Syahira','Izza Hilyah Nafisah','Kayla Zhara Qamela','Mahreen Shafana Almahyra','Rasahana Shafwa Ruqayah','Shakayla Aretha Shaima']

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))
#--> Penjeda Waktu
def jeda(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)
def tunggu_kode(t):
    for x in range(t+1):
        print('\r%sTunggu Kode %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> User Agent Vivo
def random_ua_vivo():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Samsung
def random_ua_samsung():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-75505","GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-g900f","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160","GT-I8258","GT-I8262D","GT-I8268","GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-i8700","GT-I8750", "GT-I900","GT-I9008L","GT-i9040","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-m190","GT-M5650","GT-mini","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5200","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","GT-P7500R","GT-P7500V","GT-P7501","GT-P7511","GT-S3330","GT-S3332","GT-S3333","GT-S3370","GT-S3518","GT-S3570","GT-S3600i","GT-S3650","GT-S3653W","GT-S3770K","GT-S3770M","GT-S3800W","GT-S3802","GT-S3850","GT-S5220","GT-S5220R","GT-S5222","GT-S5230","GT-S5230W","GT-S5233T","GT-s5233w","GT-S5250","GT-S5253","GT-s5260","GT-S5280","GT-S5282","GT-S5283B","GT-S5292","GT-S5300","GT-S5300L","GT-S5301","GT-S5301B","GT-S5301L","GT-S5302","GT-S5302B","GT-S5303","GT-S5303B","GT-S5310","GT-S5310B","GT-S5310C","GT-S5310E","GT-S5310G","GT-S5310I","GT-S5310L","GT-S5310M","GT-S5310N","GT-S5312","GT-S5312B","GT-S5312C","GT-S5312L","GT-S5330","GT-S5360","GT-S5360B","GT-S5360L","GT-S5360T","GT-S5363","GT-S5367","GT-S5369","GT-S5380","GT-S5380D","GT-S5500","GT-S5560","GT-S5560i","GT-S5570B","GT-S5570I","GT-S5570L","GT-S5578","GT-S5600","GT-S5603","GT-S5610","GT-S5610K","GT-S5611","GT-S5620","GT-S5670","GT-S5670B","GT-S5670HKB","GT-S5690","GT-S5690R","GT-S5830","GT-S5830D","GT-S5830G","GT-S5830i","GT-S5830L","GT-S5830M","GT-S5830T","GT-S5830V","GT-S5831i","GT-S5838","GT-S5839i","GT-S6010","GT-S6010BBABTU","GT-S6012","GT-S6012B","GT-S6102","GT-S6102B","GT-S6293T","GT-S6310B","GT-S6310","GT-S6312","GT-S6313T","GT-S6352","GT-S6500","GT-S6500D","GT-S6500L","GT-S6790","GT-S6790L","GT-S6790N","GT-S6792L","GT-S6800","GT-S6800HKAXFA","GT-S6802","GT-S6810","GT-S6810B","GT-S6810E","GT-S6810L","GT-S6810M","GT-S6810MBASER","GT-S6810P","GT-S6812","GT-S6812B","GT-S6812C","GT-S6812i","GT-S6818","GT-S6818V","GT-S7230E","GT-S7233E","GT-S7250D","GT-S7262","GT-S7270","GT-S7270L","GT-S7272","GT-S7272C","GT-S7273T","GT-S7278","GT-S7278U","GT-S7390","GT-S7390G","GT-S7390L","GT-S7392","GT-S7392L","GT-S7500","GT-S7500ABABTU","GT-S7500ABADBT","GT-S7500ABTTLP","GT-S7500CWADBT","GT-S7500L","GT-S7500T","GT-S7560","GT-S7560M","GT-S7562","GT-S7562C","GT-S7562i","GT-S7562L","GT-S7566","GT-S7568","GT-S7568I","GT-S7572","GT-S7580E","GT-S7583T","GT-S758X","GT-S7592","GT-S7710","GT-S7710L","GT-S7898","GT-S7898I","GT-S8500","GT-S8530","GT-S8600","GT-STB919","GT-T140","GT-T150","GT-V8a","GT-V8i","GT-VC818","GT-VM919S","GT-W131","GT-W153","GT-X831","GT-X853","GT-X870","GT-X890","GT-Y8750i","SAMSUNG SM-G780G"]) 
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Realme
def random_ua_realme():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                        #--> OS Version
    dv_typ = random.choice(["RMX3261","RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]) 
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                     #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                #--> Device Version
    sd_ver = random.randrange(1,10)                                                         #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                               #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Custom
def random_ua_custom():
    try:
        _file_ = uman
        if 'Android' in str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(10,13))
            ua1 = _file_.replace(ad_ver,os_ver)
        else: ua1 = _file_
        if 'Build' in str(_file_):
            od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A','PKQ1'])
            dv_ver = random.randrange(100000,250000)
            sd_ver = random.randrange(1,10)
            nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.replace(od_ver,nw_str)
        else: ua2 = ua1
        if 'Chrome' in str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            a = random.randrange(112,115)
            b = random.randrange(1000,10000)
            c = random.randrange(10,100)
            ch_ver = f'{a}.0.{b}.{c}'
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.replace(ch_old,ch_new)
        else: ua3 = ua2
        return(ua3)
    except Exception as e:
        return('Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36')

#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s;'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.1 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,M,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      ─────────────── %s• %sMeledak rikod %s• %s───────────────\n%s'%(A,M,P,M,A,P))

#--> Main Menu
class menu:
    def __init__(self):
        logo()
        self.main_menu()
    def main_menu(self):
        Kawancik = f"{H2}01\n02\n03"
        Kawancik2 = f"{P2}Create Account\nCheck Result\nBot"
        Kawancik3 = f"{H2}ON\nON\nON"
        Kawanhir = me()
        Kawanhir.add_column(f"{P2}NO", style=f"bold blue", justify='center')
        Kawanhir.add_column(f"{P2}PILIHAN", style=f"bold blue", justify='center',width=70)
        Kawanhir.add_column(f"{P2}STATUS", style=f"bold blue", justify='center')
        Kawanhir.add_row(Kawancik,Kawancik2, Kawancik3)
        console.print(Kawanhir, style=f"bold green")
        x = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).lower()
        print('')
        if   x in ['1','01','001','a']: menu_create()
        elif x in ['2','02','002','b']: menu_check()
        elif x in ['3','03','003','c']: belum_tersedia()
        elif x in ['4','04','004','d']: belum_tersedia()
        else: exit('%sIsi Yang Benar!%s'%(M,P))

#--> Menu Create
class menu_create:
    def __init__(self):
        global kelamin, namstat, nameme, web_email, tampil, useragent, uman, passtat, password, lanjutken
        try:os.mkdir('Akun_New')
        except Exception as e :pass
        prints(Panel.fit(f"[bold green]◉ [bold white]Rekomendasi   [bold red]◉ [bold white]Tidak Rekomendasi   ◉ Netral", style="bold green")) 
        print('')
        kelamin   = input('%s[%s•%s] %sAkun Laki/Perempuan/Random [%sl%s/%sp%s/%sr%s] : '%(M,P,M,P,H,P,H,P,M,P)).lower()
        namanama  = input('%s[%s•%s] %sGunakan Nama Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,M,P,H,P)).lower()
        if namanama in ['m','manual','0','00']:
            namstat = 'Manual'
            nameme = input(' %s└─ %sNama : %s'%(M,P,M)).split(',')
        else:
            namstat = 'Random'
        prints(Panel.fit(f"[bold white] Email [bold red]CryptoGmail/TempMail[bold yellow]SecMail/[bold green]MinuteMail",style="bold green"))
        web_email = input(' %s└─ %s[c/s/m/t] [skip=MinuteMail] : '%(M,P)).lower()
        tampil    = input('%s[%s•%s] %sTampilkan Akun CP [%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        prints(Panel.fit(f"[bold white] Metode [bold green]Dap",style="bold green"))
        lanjutken = input(' %s└─ %s[d] [skip=dap] : '%(M,P)).lower()
        prints(Panel.fit(f"[bold red]User Agent Vivo/[bold yellow]Samsung/[bold yellow]Realme/[bold green]Manual",style="bold green"))
        useragent = input(' %s└─ %s[v/s/r/m] [skip=statis] : '%(M,P)).lower()
        if useragent in ['m','manual','0','00']:
            uman = input(' %s└─ %sUser Agent : %s'%(M,P,M))
            if uman == '' or uman == ' ':
                exit('%sIsi Yang Benar!%s'%(M,P))
        else:
            uman = 'Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X688C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36'
        passtat   = input('%s[%s•%s] %sGunakan Password Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,H,P,M,P)).lower()
        if passtat in ['m','manual','b','2','02']:
            password = input(' %s└─ %sPassword : %s'%(M,P,M))
            if len(password) < 6:
                exit('%sPassword Minimal 6 Digit!%s'%(M,P))
            if password in ['akusayangkamu','123456','iloveyou','password','qwerty','sayang','anjing','bismillah']:
                exit('%sGunakan Password Yang Kuat!%s'%(M,P))
        else:
            password = 'kasyafcintaalyareal'
        d = input('%s[%s•%s] %sBeri Delay (%sDalam Menit%s) : '%(M,P,M,P,M,P))
        if d == '' or d == ' ':
            d = 1
        print('')
        l = int(d)*60
        for y in range(10000):
            if key/len(auth1) == len(reco)/2: create_fb(); self.hitung(l)
            else: create_fb(); self.hitung(l)
    def hitung(self,a):
        for x in range(a+1):
            print('\r[%sOK:%s%s] [%sCP:%s%s] Tunggu %s Detik         '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Create Facebook Account
class create_fb:
    #--> Tampung Kabeh
    def __init__(self):
        self.file  = 'Akun_New/%s.txt'%(waktu())
        self.abc = requests.Session() #--> Sesi Email
        self.xyz = requests.Session() #--> Sesi Facebook
        self.abc.cookies.clear()
        self.xyz.cookies.clear()
        self.bio    = "aku cinta alya"
        if   useragent in ['v','vivo','1','01','a']:    self.ua = random_ua_vivo()
        elif useragent in ['s','samsung','2','02','b']: self.ua = random_ua_samsung()
        elif useragent in ['r','realme','3','03','c']:  self.ua = random_ua_realme()
        elif useragent in ['m','manual','0','00','z']:  self.ua = random_ua_custom()
        else : self.ua = 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 AppContainer/10.5.10 AppContainer PhoenixContainer/1.0.0-beta-8.16.2-CA-82415-RC3'
        self.head_email = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'}
        self.ua_wind = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.headers_get = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '?1','upgrade-insecure-requests':'1','user-agent' : self.ua}
        self.generate_data()
        if lanjutken in ['1','dap','d']: self.scrap1()
        else : self.scrap1()
    
    #--> Generate Data
    def generate_data(self):
        self.name, soex = self.get_name().split('|')
        self.nope  = self.get_nope()
        if   web_email in ['c','cryptogmail','1','01','a']: self.email = self.get_email_cryptogmail()
        elif web_email in ['s','secmail','2','02','b']:     self.email = self.get_email_onesecmail()
        elif web_email in ['m','minutemail','4','04','d']:  self.email = self.get_email_10minutemail()
        elif web_email in ['t','teml','5','05','e']:  self.email = self.get_email_mailtem()
        else : self.email = self.get_email_10minutemail()
        if soex == 'male' : self.sex = '2'
        else : self.sex = '1'
        if passtat in ['m','manual','b','2','02']: self.pw = password
        else: self.pw = self.get_pass()
        self.ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1970,2001))}
        self.perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'
        
    
    #--> Generate Random Name
    def get_name(self):
        if kelamin in ['l','laki','1','01','a']: gder = 'male'
        elif kelamin in ['p','perempuan','2','02','b']: gder = 'female'
        else: gder = random.choice(['male','female'])
        try:
            if gder == 'male':
                if namstat == 'Manual': name = random.choice(nameme)
                else: name = random.choice(boys_name)
            else:
                if namstat == 'Manual': name = random.choice(nameme)
                else: name = random.choice(girls_name)
        except Exception as e:
            nam1 = random.choice(['Eka','Dwi','Tri','Budi','Indah','Dewi'])
            nam2 = random.choice(['Nurhayati','Handoko','Setiyani','Susanto','Permata'])
            nam3 = random.choice(['Triatmaja','Siagian','Manopo','Jayaningrat','Widodo'])
            name = f'{nam1} {nam2} {nam3}'
        klop = f'{name}|{gder}'
        return(klop)

    #--> Generate Random Phone Number
    def get_nope(self):
        na   = random.choice(['77','78','59','13','58','96', '88'])
        ni   = str(random.randrange(1000,10000))
        nu   = str(random.randrange(10000,100000))
        nope = '08%s%s%s'%(na,ni,nu)
        return(nope)

    #--> Generate Random Password
    def get_pass(self):
        up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lw = up.lower()
        nb = '0123456789'
        ch = up + lw + nb
        pw = ''.join(random.choice(ch) for _ in range(12))
        return(pw.lower())
        
    def get_email_mailtem(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['gixenmixen.com','happy2023year.com','superblohey.com','dishcatfish.com','drowblock.com','pirolsnet.com','skygazerhub.com','myinfoinc.com','zipcatfish.com','bloheyz.com'])
        email = f'{nam}{ran}@{dom}'
        return(email)
    def get_code_mailtem(self):
        name, domain = self.email.split('@')
        url = f'https://api.internal.temp-mail.io/api/v3/message/150068a8-c75e-4287-bcf3-c6a32ce2144e&login={name}&domain={domain}'
        req = self.abc.get(url,headers=self.head_email).json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)
        
    #--> Generate Email & Code From Cryptogmail
    
    def get_email_cryptogmail(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['fexbox.org','mailto.plus','rover.info','chitthi.in','fextemp.com','any.pink','merepost.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        return(email)
    def get_code_cryptogmail(self):
        url = f'https://tempmail.plus/api/mails?email={self.email}'
        req = self.abc.get(url,headers=self.head_email).json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From 1SecMail
    def get_email_onesecmail(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['1secmail.com','1secmail.org','1secmail.net','kzccv.com','qiott.com','wuuvo.com','icznn.com','wwjmp.com','esiix.com','xojxe.com','yoggm.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        return(email)
    def get_code_onesecmail(self):
        name, domain = self.email.split('@')
        req = self.abc.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}').json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From 10minutemail
    def get_email_10minutemail(self):
        req = bs(self.abc.get('https://10minutemail.net/m/?lang=id',headers=self.head_email,allow_redirects=True).content,'html.parser')
        self.ses_email = re.search('sessionid="(.*?)"',str(req)).group(1)
        self.tim_email = str(time.time()).replace('.','')[:13]
        dat = {'new':'1','sessionid':self.ses_email,'_':self.tim_email}
        pos = self.abc.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,allow_redirects=True).json()
        email = pos['mail_get_mail']
        self.cookie_email = '; '.join([str(x)+"="+str(y) for x,y in self.abc.cookies.get_dict().items()])
        return(email)
    def get_code_10minutemail(self):
        dat = {'new':'0','sessionid':self.ses_email,'_':self.tim_email}
        pos = self.abc.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,cookies={'cookie':self.cookie_email},allow_redirects=True).json()
        kode = re.search(r'FB-([^ ]+)',str(pos)).group(1)
        return(kode) 
    def scrap1(self): #--> Post Login Awal
        req = bs(self.xyz.get('https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk',headers=self.headers_get).content,'html.parser')
        fom = req.find('form',{'method':'post'})
        data = {
            'lsd'                        : re.search('name="lsd" type="hidden" value="(.*?)"',               str(fom)).group(1),
            'jazoest'                    : re.search('name="jazoest" type="hidden" value="(.*?)"',           str(fom)).group(1),
            'fb_dtsg'                    : re.search('{"dtsg":{"token":"(.*?)",',                            str(req)).group(1),
            'ccp'                        : re.search('name="ccp" type="hidden" value="(.*?)"',               str(fom)).group(1),
            'reg_instance'               : re.search('name="reg_instance" type="hidden" value="(.*?)"',      str(fom)).group(1),
            'reg_impression_id'          : re.search('name="reg_impression_id" type="hidden" value="(.*?)"', str(fom)).group(1),
            'ns'                         : re.search('name="ns" type="hidden" value="(.*?)"',                str(fom)).group(1),
            'app_id'                     : re.search('name="app_id" type="hidden" value="(.*?)"',            str(fom)).group(1),
            'logger_id'                  : re.search('name="logger_id" type="hidden" value="(.*?)"',         str(fom)).group(1),
            'suma_create_event'          : 'suma_redirection_click_create_account',
            'field_names[0]'             : 'firstname',
            'field_names[1]'             : 'birthday_wrapper',
            'field_names[2]'             : 'reg_email__',
            'field_names[3]'             : 'sex',
            'field_names[4]'             : 'reg_passwd__',
            'is_birthday_confirmed'      : 'confirmed',
            'multi_step_form'            : '1',
            'skip_suma'                  : '0',
            'shouldForceMTouch'          : '1',
            'ref'                        : 'dbl',
            'firstname'                  : self.name,
            'reg_email__'                : self.nope,
            'sex'                        : self.sex,
            'reg_passwd__'               : self.pw,
            'birthday_day'               : self.ttl['tgl'],
            'birthday_month'             : self.ttl['bln'],
            'birthday_year'              : self.ttl['thn'],
            'welcome_step_completed'     : True,
            'submission_request'         : True,
            'age_step_input'             : False,
            'did_use_age'                : False,
            'custom_gender'              : False,
            'name_suggest_elig'          : False,
            'was_shown_name_suggestions' : False,
            'did_use_suggested_name'     : False,
            'use_custom_gender'          : False,
            'zero_header_af_client'      : '',
            'helper'                     : '',
            'guid'                       : '',
            'pre_form_step'              : '',
            'korean_tos_is_present'      : '',
            'checkbox_privacy_policy'    : '',
            'checkbox_tos'               : '',
            'checkbox_location_policy'   : ''}
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        next = 'https://m.facebook.com' + fom['action']
        pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        if key/len(auth1) != len(auth1): print(rede)
        else:
            if pos.find('title').text == 'Konfirmasikan Akun Anda': #--> Jika Akun Sudah Dibuat
                self.scrap4()
            else:
                rog = pos.find('form',{'method':'post'})
                if 'login/device-based/update-nonce' in str(rog['action']): #--> Jika Masuk Menu Save Device
                    self.scrap2(rog)
                elif 'conf/notifmedium/send_code' in str(rog['action']): #--> Jika Langsung Masuk Menu Minta Kode Nope
                    self.scrap3(rog)
                elif 'checkpoint' in str(rog['action']): #--> Jika Checkpoint
                    self.printing('CP')
                else:
                    print('\rTerjadi Kesalahan                    ',end='');sys.stdout.flush()
     
    def scrap2(self,fom): #--> Save Device OK
        print('\rLolos Tahap 1                    ',end='');sys.stdout.flush()
        data = {
            'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
            'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
            'flow'       : 'interstitial_nux',
            'next'       : '',
            'nux_source' : 'dbl_nux_after_reg',
            'submit'     : 'OK'}
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        next = 'https://m.facebook.com' + fom['action']
        pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        rog = pos.find('form',{'method':'post'})
        self.scrap3(rog)
    def scrap3(self,fom): #--> Minta Kode Nope
        print('\rLolos Tahap 2                    ',end='');sys.stdout.flush()
        try:
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'medium'  : 'sms',
                'submit'  : 'Kirim kode'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
            cok += self.perangkat
            next = 'https://m.facebook.com' + fom['action']
            pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            self.scrap4()
        except Exception as e:
            self.printing('CP')
    def scrap4(self): #--> Add Email
        print('\rLolos Tahap 3                    ',end='');sys.stdout.flush()
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        try:
            req = bs(self.xyz.get('https://m.facebook.com/changeemail',headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            data = {
                'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'old_email'    : re.search('name="old_email" type="hidden" value="(.*?)"',str(fom)).group(1),
                'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"',str(fom)).group(1),
                'new'          : self.email,
                'next'         : '',
                'submit'       : 'Tambahkan'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
            cok += self.perangkat
            next = 'https://m.facebook.com' + fom['action']
            pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            tunggu_kode(30)
            self.scrap5(pos)
        except Exception as e:
            self.printing('CP')
    def scrap5(self,req): #--> Confirm Code
        print('\rLolos Tahap 4                    ',end='');sys.stdout.flush()
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        try:
            if   web_email in ['c','cryptogmail','1','01','a']: code = self.get_code_cryptogmail()
            elif web_email in ['s','secmail','2','02','b']:     code = self.get_code_onesecmail()
            elif web_email in ['m','minutemail','4','04','d']:  code = self.get_code_10minutemail()
            elif web_email in ['t','temp','5','05','e']:  code = self.get_code_mailtem()
            else : code = self.get_code_10minutemail()
            id = re.search('c_user=(.*?);',cok).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            dtsg = re.search('"dtsg":{"token":"(.*?)",',str(req)).group(1)
            jazoest = re.search('"jazoest", "(.*?)",',str(req)).group(1)
            data = {
                'contact': self.email,
                'type': 'submit',
                'is_soft_cliff': False,
                'medium': 'email',
                'code': code,
                'fb_dtsg': dtsg,
                'jazoest': jazoest,
                'lsd': lsd,
                '__user': id}
            pos = bs(self.xyz.post('https://m.facebook.com/confirmation_cliff/',data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            self.semi_final()
        except Exception as e:
            self.printing('CP')
    def zero_optin(self): #--> Khusus Mode Data (No Wifi)
        try:
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req1 = bs(self.xyz.get('https://mbasic.facebook.com',headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            nek = ['https://mbasic.facebook.com'+x['href'] for x in req1.find_all('a',href=True) if 'dialtone_optin_page' in str(x['href'])][0]
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req2 = bs(self.xyz.get(nek,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            fom  = req2.find('form',{'method':'post'})
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'submit'  : 'OK, Gunakan Data'}
            nuk  = 'https://mbasic.facebook.com' + fom['action']
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            pos7 = self.xyz.post(nuk,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True)
            print('\rBerhasil Skip Free Mode                ',end='');sys.stdout.flush()
        except Exception as e: pass
    def semi_final(self): #--> Sortir
        print('\rLolos Tahap 5                    ',end='');sys.stdout.flush()
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        try:
            if len(reco)/2 != len(auth1): clear(); exit('Ini Orang Dibilangin Gausah Direcode, Ngeyel Amat')
            else:
                id = re.search('c_user=(.*?);',cok).group(1)
                self.zero_optin()
                jeda(10)
                final = check_account(id)
                if final == 'OK': self.printing('OK')
                else: self.printing('CP')
        except Exception as e:
            self.printing('CP')
    def printing(self,stat): #--> Print Hasil
        global ok, cp
        if stat == 'OK':
            cookie = cvt('ok',self.xyz.cookies.get_dict())
            id = self.xyz.cookies.get_dict()['c_user']
            print('\r%sStatus : %sSuccess%s                         '%(P,H,P))
            print('Nama   : %s'%(str(self.name)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(self.pw)))
            print('Email  : %s'%(str(self.email)))
            print('TTL    : %s %s %s'%(self.ttl['tgl'],bulan[self.ttl['bln']],self.ttl['thn']))
            print('Cookie : %s\n'%(str(cookie)))
            open(self.file,'a+').write('%s|%s|%s|%s\n'%(self.name,id,self.email,self.pw))
            ok += 1
        else:
            if tampil in ['t','2','02','b']: pass
            else:
                print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
                print('Nama   : %s'%(str(self.name)))
                print('Nope   : %s'%(str(self.nope)))
                print('Pass   : %s\n'%(str(self.pw)))
            cp += 1
#--> Menu Checker Account
class menu_check:
    def __init__(self): #--> Mengecek Ketersediaan Folder
        self.xyz = requests.Session()
        self.file = {}
        self.isi = 0
        self.ok  = 0
        self.cp  = 0
        self.sortir()
    def sortir(self): #--> Memilih File
        f = 'Akun_New'
        if os.path.isdir(f):
            p = 0
            l = os.listdir(f)
            for y in l:
                p += 1
                self.file.update({str(p):y})
                c = '%s• %s%s'%(M,P,y)
                print(c)
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
        try:
            d = input('\n%s[%s•%s] %sMasukkan File : '%(M,P,M,P))
            if d in list(self.file.keys()): l = 'Akun_New/%s'%(self.file[d])
            else: l = 'Akun_New/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g:
                try:
                    nama, id, email, pw = a.split('|')
                    stat = check_account(id)
                    if stat == 'OK': self.printing('OK',nama,id,email,pw)
                    else: self.printing('CP',nama,id,email,pw) 
                except Exception as e: pass
            if self.isi == 0: print('%sTidak Ada Hasil :(\n%s'%(M,P))
            else: print('%sDari %s Akun, Terdapat %s%s Akun CP %sdan %s%s Akun OK\n%s'%(P,str(self.isi),M,str(self.cp),P,H,str(self.ok),P))
        except Exception as e:
            print('%sError : %s'%(P,e))
            print('%sTerjadi Kesalahan!\n%s'%(M,P))
    def printing(self,stat,nama,id,email,pw): #--> Print Hasil Cek
        if stat == 'OK':
            cookie = cvt('ok',self.xyz.cookies.get_dict())
            print('\r%sStatus : %sSuccess%s                         '%(P,H,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s\n'%(str(email)))
            print('cookie  : %s\n'%(str(cookie)))
            self.ok += 1
        else:
            print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
            print('Nama   : %s'%(str(nama)))
            print('ID     : %s'%(str(id)))
            print('Pass   : %s'%(str(pw)))
            print('Email  : %s\n'%(str(email)))
            self.cp += 1
        self.isi += 1
            
#--> Check Account
def check_account(id):
    url = f'https://www.facebook.com/p/{id}'
    r = requests.Session()
    head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    req = bs(r.get(url,headers=head,allow_redirects=True).content,'html.parser')
    title = req.find('title').text
    if title == 'Facebook': return('CP')
    else: return('OK')
   
#--> Notice
class belum_tersedia:
    def __init__(self):
        self.main()
    def main(self):
        print('\n%s[%sMenu Sedang Di Perbaiki%s] %s '%(M,P,M,P))
        print('%s[%sUntuk Waktu Perbaikan Agak lama%s] %s Edit Foto Profil'%(M,P,M,P))
        print('%s[%sTerimakasih Sudah Memakai Script Dapunta%s] %s Logout'%(M,P,M,P))
   
#--> Trigger
if __name__ == '__main__':
    clear()
    menu()