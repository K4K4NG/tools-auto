lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI = Exception, __name__, str, input, open, print

import os as lIIllIIIIlIIIl, sys as lIIlllIllllIIl, requests as IIllIlIllIIIll, bs4 as IIlllIIIlllIII, re as llIllllIlIIlll, time as lIllIIIIlIIIlI, datetime as lllIlIlllIIlII, urllib as IIlllIlIIlIlII, random as IIlIllIIIIIlIl, json as IIlllIIIIlllll
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs
IIlllIlIlIlIllIIlI = '\x1b[38;5;231m'
llIlllIIlIllIIIlll = '\x1b[38;5;196m'
lIIIIIlIlIlllIIlIl = '\x1b[38;5;46m'

def lllIIlIIIllIllllll():
    if 'linux' in lIIlllIllllIIl.platform.lower():
        lIIllIIIIlIIIl.system('clear')
    elif 'win' in lIIlllIllllIIl.platform.lower():
        lIIllIIIIlIIIl.system('cls')

def lIllIIlIIlIllIlIIl(IlllIIIllllIlIIlIl):
    try:
        with IIllIlIllIIIll.Session() as lIIIIIlIIIIIlIlIll:
            lllIlIllIlIlllllll = lIIIIIlIIIIIlIlIll.get('https://mbasic.facebook.com/language/', cookies=IlllIIIllllIlIIlIl)
            lllIllIlIllIlllIII = bs(lllIlIllIlIlllllll.content, 'html.parser')
            for IIIlIllIIIIlIllIlI in lllIllIlIllIlllIII.find_all('form', {'method': 'post'}):
                if 'Bahasa Indonesia' in lllllllllllllIl(IIIlIllIIIIlIllIlI):
                    llIIIIIlllllllIlIl = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" value="(.*?)"', lllllllllllllIl(lllIlIllIlIlllllll.text)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" value="(.*?)"', lllllllllllllIl(lllIlIllIlIlllllll.text)).group(1), 'submit': 'Bahasa Indonesia'}
                    IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com' + IIIlIllIIIIlIllIlI['action']
                    exec = lIIIIIlIIIIIlIlIll.post(IIlIIlllIlIIllIIIl, data=llIIIIIlllllllIlIl, cookies=IlllIIIllllIlIIlIl)
    except lllllllllllllll as IIIlllllllIlllIIlI:
        pass

def IllllllllIIlIIllll():
    global IlIIIlIllllIIIIIll
    IlIIIlIllllIIIIIll = lllIlIlllIIlII.datetime.now()

def IIlIIllllIIllIIlll():
    global llIIIlIlIIIllllIIl, IlllllIlIIlIIIlIIl
    llIIIlIlIIIllllIIl = lllIlIlllIIlII.datetime.now()
    IlllllIlIIlIIIlIIl = llIIIlIlIIIllllIIl - IlIIIlIllllIIIIIll
    try:
        llIlllIIIIIlIllIII = lllllllllllllIl(IlllllIlIIlIIIlIIl).split(':')[1]
        lIIIIlIIIlllIlIlll = lllllllllllllIl(IlllllIlIIlIIIlIIl).split(':')[2].replace('.', ',').split(',')[0] + ',' + lllllllllllllIl(IlllllIlIIlIIIlIIl).split(':')[2].replace('.', ',').split(',')[1][:1]
        llllllllllllIlI('\nProgram Selesai Dalam Waktu %s Menit %s Detik\n' % (llIlllIIIIIlIllIII, lIIIIlIIIlllIlIlll))
    except lllllllllllllll as IIIlllllllIlllIIlI:
        llllllllllllIlI('\nProgram Selesai Dalam Waktu 0 Detik\n')

def IIllIlIIIlllIIIIll():
    IIIIlIllIIIIlIllIl = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'][lllIlIlllIIlII.datetime.now().month - 1]
    lIIIIIllIIIIIlIIIl = {'Sunday': 'Minggu', 'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu', 'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu'}[lllllllllllllIl(lllIlIlllIIlII.lllIlIlllIIlII.now().strftime('%A'))]
    IIIlIIlIIIlIIIIIIl = '%s %s %s' % (lllIlIlllIIlII.datetime.now().day, IIIIlIllIIIIlIllIl, lllIlIlllIIlII.datetime.now().year)
    lllIlIIIlIlllllIIl = lllIlIlllIIlII.datetime.now().strftime('%X')
    IIIlIlIIIIllllIIll = '\n\n%s, %s --> %s' % (lIIIIIllIIIIIlIIIl, IIIlIIlIIIlIIIIIIl, lllllllllllllIl(lllIlIIIlIlllllIIl).replace(':', '.'))
    return IIIlIlIIIIllllIIll

class IIIllIlllIIIIIIlIl:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.lIlIlIIIlIlIIlIlll()
        lIllllIllIIlIlIIll()

    def lIlIlIIIlIlIIlIlll(IlllIllllIllIlIllI):
        try:
            global IlIlIIIIlIlIllIIIl, IlIlllIlllIlIllIlI
            IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
            IlllIllllIllIlIllI.IIlIlllIIIIIIlllll = llllllllllllIll('login/token_eaag.json', 'r').read()
            lIllIIlIIlIllIlIIl(IlllIllllIllIlIllI.IlllIIIllllIlIIlIl)
            lllIlIllIlIlllllll = IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get('https://graph.facebook.com/me?fields=name,id&access_token=%s' % IlllIllllIllIlIllI.IIlIlllIIIIIIlllll, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).IIlllIIIIlllll()
            IlIlIIIIlIlIllIIIl = lllIlIllIlIlllllll['name']
            IlIlllIlllIlIllIlI = lllIlIllIlIlllllll['id']
            lllIIlIIIllIllllll()
            llllllllllllIlI('%sLogin Sebagai %s%s%s' % (IIlllIlIlIlIllIIlI, lIIIIIlIlIlllIIlIl, IlIlIIIIlIlIllIIIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            IlllIllllIllIlIllI.lIIIlllIlIlIlIllIl()

    def lIIIlllIlIlIlIllIl(IlllIllllIllIlIllI):
        llllllllllllIlI('%sCookie Invalid!%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
        lIllIIIIlIIIlI.sleep(2)
        lllIIlIIIllIllllll()
        IIllIIIlIIIIIIlIlI = lllllllllllllII('%sMasukkan Cookie : %s%s' % (IIlllIlIlIlIllIIlI, lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        try:
            IlllIllllIllIlIllI.IIlIlllIIIIIIlllll = IlllIllllIllIlIllI.lIlIlIllllIIlIIlIl(IIllIIIlIIIIIIlIlI)
        except lllllllllllllll as IIIlllllllIlllIIlI:
            IlllIllllIllIlIllI.lIIIlllIlIlIlIllIl()
        try:
            lIIllIIIIlIIIl.mkdir('login')
        except:
            pass
        llllllllllllIll('login/cookie.json', 'w').write(IIllIIIlIIIIIIlIlI)
        llllllllllllIll('login/token_eaag.json', 'w').write(IlllIllllIllIlIllI.IIlIlllIIIIIIlllll)
        IlllIllllIllIlIllI.lIlIlIIIlIlIIlIlll()

    def lIlIlIllllIIlIIlIl(IlllIllllIllIlIllI, lIIIlIlIIIlIllIIlI):
        IIlIIlllIlIIllIIIl = 'https://business.facebook.com/business_locations'
        lllIlIllIlIlllllll = IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies={'cookie': lIIIlIlIIIlIllIIlI})
        lIIIIllIIIIIllllll = llIllllIlIIlll.search('(\\["EAAG\\w+)', lllIlIllIlIlllllll.text).group(1).replace('["', '')
        return lIIIIllIIIIIllllll

class lIllllIllIIlIlIIll:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lllIlIlIIllIlIllIl()

    def lllIlIlIIllIlIllIl(IlllIllllIllIlIllI):
        llllllllllllIlI('[1] Edit Foto Profil' % ())
        llllllllllllIlI('[2] Edit Foto Sampul' % ())
        llllllllllllIlI('[3] Edit Bio' % ())
        llllllllllllIlI('[4] Edit Kota' % ())
        llllllllllllIlI('[5] Edit Website' % ())
        llllllllllllIlI('[6] Edit Name' % ())
        llllllllllllIlI('[7] Edit Ttl' % ())
        llllllllllllIlI('[8] Hapus Akun' % ())
        llllllllllllIlI('[0] Logout' % ())
        IIIlIllIIIIlIllIlI = lllllllllllllII('Pilih : ')
        llllllllllllIlI('')
        if IIIlIllIIIIlIllIlI in ['1', '01', 'a']:
            IIllIIllllIlIlIlIl()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['2', '02', 'b']:
            IIlllIlIIIlIIlIIII()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['3', '03', 'd']:
            lIIlIIlllIllllllII()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['4', '04', 'e']:
            IlIlIIIIIIlIlIlllI()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['5', '05', 'f']:
            IIllIlIIlllIlIIIII()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['6', '06', 'f']:
            IIIlllIIIIIIIIllII()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['7', '07', 'f']:
            IIIlllllIllllIllIl()
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['8', '08', 'f']:
            lIllllIllIIlIlIIll()
        elif IIIlIllIIIIlIllIlI in ['0', '00', 'z']:
            try:
                lIIllIIIIlIIIl.remove('login/cookie.json')
                lIIllIIIIlIIIl.remove('login/token_eaag.json')
                llllllllllllIlI('Good Bye...')
            except lllllllllllllll:
                llllllllllllIlI('Good Bye...')
        else:
            llllllllllllIlI('%sIsi Yg Benar!%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class IIIlllIIIIIIIIllII:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        llllllllllllIlI('Harap perhatikan: Jika Anda mengubah nama di Facebook, maka Anda tidak dapat mengubahnya lagi selama 60 hari. Jangan menambahkan huruf besar, tanda baca, karakter, atau kata-kata acak yang tidak biasa.')
        IlllIllllIllIlIllI.IllIIlIlllllIIIIII = lllllllllllllII('Nama Baru : ')
        IlllIllllIllIlIllI.IIlllllIlllllIIIIl = lllllllllllllII('Nama Tengah : ')
        IlllIllllIllIlIllI.IlIIIlIIlIllIIlIII = lllllllllllllII('Nama Belakang : ')
        IlllIllllIllIlIllI.lIIIIlIlIIIlIIIlII = lllllllllllllII('Password : ')
        IlllIllllIllIlIllI.llIlIllIIlIIlIllII()

    def llIlIllIIlIIlIllII(IlllIllllIllIlIllI):
        try:
            IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com//settings/name_change_preview/?entrypoint=unknown&amp;refid=70&amp;paipv=0&amp;eav=Afb4fy9YVkgozUW22I0RwGftLxASuwMa4gZUfJljiI1s8qIvQsXQ0FRgU3vjuuKAE4Y'
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'primary_first_name': IlllIllllIllIlIllI.IllIIlIlllllIIIIII, 'primary_middle_name': IlllIllllIllIlIllI.IIlllllIlllllIIIIl, 'primary_last_name': IlllIllllIllIlIllI.IlIIIlIIlIllIIlIII, 'save': 'Simpan perubahan'}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('\n%sGagal Mengganti Nama%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/a/settings/account/?confirm_new_name=1&amp;confirm_name&amp;page_type=none&amp;eav=AfaHJCfUusBL9YQpIT1koxHuyW_O1GMZGkFHmoIcobRhNFnmQCNT8HlZGQ_1hXJa50s&amp;paipv=0'
                lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
                lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
                IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'primary_first_name': IlllIllllIllIlIllI.IllIIlIlllllIIIIII, 'primary_middle_name': IlllIllllIllIlIllI.IIlllllIlllllIIIIl, 'primary_last_name': IlllIllllIllIlIllI.IlIIIlIIlIllIIlIII, 'alternate_name': '', 'show_alternate': '', 'save_password': IlllIllllIllIlIllI.lIIIIlIlIIIlIIIlII, 'save': 'Simpan perubahan'}
                IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
                lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
                if '/settings/name_change_preview/?invalid_password=1' in lIlIlIlIIIIIllllIl:
                    llllllllllllIlI('\n%sPassword Salah%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
                elif lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                    llllllllllllIlI('\n%sGagal Mengganti Nama%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
                else:
                    llllllllllllIlI('\n%sBerhasil Mengganti Nama%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
                llllllllllllIlI('\n%sBerhasil Mengganti Nama%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('\n%sGagal Mengganti Nama%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class lIIIlIIllllIIlIIIl:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IlllIllllIllIlIllI.lIIIIlIlIIIlIIIlII = lllllllllllllII('masukan pas : ')
        IlllIllllIllIlIllI.llllllIlllIllIllII()

        def llllllIlllIllIllII(IlllIllllIllIlIllI):
            try:
                IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/account/delete/?back_uri=%2Fhome.php&account_screen&reason=NONE&hcb=0&eav=AfaRlJ4pLedUKEl9OyRJaZsHXWY05zHKhy2kokVgWArmz-uNasq35hxuiig3bS_QAR0&paipv=0&consent'
                lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
                lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
                IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'password': IlllIllllIllIlIllI.lIIIIlIlIIIlIIIlII, 'hcb': llIllllIlIIlll.search('name="hcb" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'account': 'Lanjut'}
                IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
                lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
                if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                    llllllllllllIlI('\n%sGagal menghapus akun%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
                else:
                    IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/account/delete/?back_uri=%2Fhome.php&deletion_screen&reason=NONE&hcb=0&eav=AfaBxsa4X_bPNn1R40eEKRsH8CgkaoGMClmabs_mTwIM2n6Ff_C3Wxia2Zd-8VriVN0&paipv=0&_rdr'
                    lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
                    lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
                    IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'hcb': llIllllIlIIlll.search('name="hcb" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'delete': 'Hapus Akun'}
                    IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
                    lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
                    if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                        llllllllllllIlI('\n%sGagal menghapus akun%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
                    else:
                        llllllllllllIlI('berhasil delet akun')
            except lllllllllllllll as IIIlllllllIlllIIlI:
                llllllllllllIlI('\n%sGagal menghapus akun%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class IIIlllllIllllIllIl:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IlllIllllIllIlIllI.IIlllIIIllIIIIllIl = {'tgl': lllllllllllllIl(IIlIllIIIIIlIl.randrange(1, 29)), 'bln': lllllllllllllIl(IIlIllIIIIIlIl.randrange(1, 13)), 'thn': lllllllllllllIl(IIlIllIIIIIlIl.randrange(1970, 20010))}
        IlllIllllIllIlIllI.llllllIlllIllIllII()

    def llllllIlllIllIllII(IlllIllllIllIlIllI):
        try:
            IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/editprofile.php?type=basic&edit=birthday&eav=Afbcml7kH4Wm0NB_3vHraz4WaOMhnyxdSV6-pbFHDjqqQkn-10Rr7lhmv_VRFjue0jw&paipv=0&refid=17#/'
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'edit': 'birthday', 'type': 'basic', 'day': IlllIllllIllIlIllI.IIlllIIIllIIIIllIl['tgl'], 'month': IlllIllllIllIlIllI.IIlllIIIllIIIIllIl['bln'], 'year': IlllIllllIllIlIllI.IIlllIIIllIIIIllIl['thn'], 'save': 'Simpan'}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('\n%sGagal Mengganti Ttl%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                llllllllllllIlI('\n%sBerhasil Mengganti Ttl%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
                llllllllllllIlI('TTL    : %s %s %s' % (IlllIllllIllIlIllI.IIlllIIIllIIIIllIl['tgl'], bulan[IlllIllllIllIlIllI.IIlllIIIllIIIIllIl['bln']], IlllIllllIllIlIllI.IIlllIIIllIIIIllIl['thn']))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('\n%sGagal Mengganti Ttl%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class IIllIIllllIlIlIlIl:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IlllIllllIllIlIllI.lIlllIIIlIllllIllI()

    def lIlllIIIlIllllIllI(IlllIllllIllIlIllI):
        IIlIllIllllllllllI = lllllllllllllII('URL Foto : ')
        IlllIllllIllIlIllI.llIlIllIIlIIlIllII(IIlIllIllllllllllI)

    def llIlIllIIlIIlIllII(IlllIllllIllIlIllI, IIIllIlIllllIlllll):
        try:
            IlIlIlIIlIlIllllII = IIlllIlIIlIlII.request.urlopen(IIIllIlIllllIlllll)
            IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/profile_picture/'
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'submit': 'Simpan'}
            lIlllllIIlIIIlIlII = {'pic': IlIlIlIIlIlIllllII}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post(lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, files=lIlllllIIlIIIlIlII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('\n%sGagal Mengganti Foto Profil%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                llllllllllllIlI('\n%sBerhasil Mengganti Foto Profil%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('\n%sGagal Mengganti Foto Profil%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class IIlllIlIIIlIIlIIII:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IlllIllllIllIlIllI.lIlllIIIlIllllIllI()

    def lIlllIIIlIllllIllI(IlllIllllIllIlIllI):
        IIlIllIllllllllllI = lllllllllllllII('URL Foto : ')
        IlllIllllIllIlIllI.llIlIllIIlIIlIllII(IIlIllIllllllllllI)

    def llIlIllIIlIIlIllII(IlllIllllIllIlIllI, IIIllIlIllllIlllll):
        try:
            IlIlIlIIlIlIllllII = IIlllIlIIlIlII.request.urlopen(IIIllIlIllllIlllll)
            IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'return_uri': llIllllIlIIlll.search('name="return_uri" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'return_uri_error': llIllllIlIIlll.search('name="return_uri_error" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'ref': llIllllIlIIlll.search('name="ref" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'csid': llIllllIlIIlll.search('name="csid" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'ctype': llIllllIlIIlll.search('name="ctype" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'profile_edit_logging_ref': llIllllIlIIlll.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'submit': 'Unggah'}
            lIlllllIIlIIIlIlII = {'file1': IlIlIlIIlIlIllllII}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, files=lIlllllIIlIIIlIlII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('\n%sGagal Mengganti Foto Sampul%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                llllllllllllIlI('\n%sBerhasil Mengganti Foto Sampul%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('\n%sGagal Mengganti Foto Sampul%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class lIIlIIlllIllllllII:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IlllIllllIllIlIllI.IlllIllllllllIIlIl = lllllllllllllII('Tulis Bio cth : aku sayang alya : ')
        IlllIllllIllIlIllI.llIlIllIIlIIlIllII()

    def llIlIllIIlIIlIllII(IlllIllllIllIlIllI):
        try:
            IIlIIlllIlIIllIIIl = 'https://mbasic.facebook.com/profile/basic/intro/bio/'
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'bio': IlllIllllIllIlIllI.IlllIllllllllIIlIl, 'publish_to_feed': True, 'submit': 'Simpan'}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('\n%sGagal Mengganti Bio%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                llllllllllllIlI('\n%sBerhasil Mengganti Bio%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('\n%sGagal Mengganti Bio%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class IlIlIIIIIIlIlIlllI:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IllIlIIlllllIIlIII = lllllllllllllII('Nama Kota : ')
        IlllIllllIllIlIllI.lIlIIIlIIIlllllIlI('https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown', 'hometown', 'hometown[]', IllIlIIlllllIIlIII)
        IlllIllllIllIlIllI.lIlIIIlIIIlllllIlI('https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city', 'current_city', 'current_city[]', IllIlIIlllllIIlIII)

    def lIlIIIlIIIlllllIlI(IlllIllllIllIlIllI, IIlIIlllIlIIllIIIl, llllllllIIIlIIIlIl, lIlIlIllIlIlllIlIl, IllIlIIlllllIIlIII):
        try:
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'edit': llllllllIIIlIIIlIl, 'type': 'basic', lIlIlIllIlIlllIlIl: IllIlIIlllllIIlIII, 'save': 'Simpan'}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('%sGagal Mengganti Kota%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                llllllllllllIlI('%sBerhasil Mengganti Kota%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('%sGagal Mengganti Kota%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))

class IIllIlIIlllIlIIIII:

    def __init__(IlllIllllIllIlIllI):
        IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll = IIllIlIllIIIll.Session()
        IlllIllllIllIlIllI.IlllIIIllllIlIIlIl = {'cookie': llllllllllllIll('login/cookie.json', 'r').read()}
        IlllIllllIllIlIllI.IlIIlllIlllIlIIlIl = lllllllllllllII('URL Web : ')
        IlllIllllIllIlIllI.lIlIIIlIIIlllllIlI('https://mbasic.facebook.com/editprofile.php?type=contact&edit=website')

    def lIlIIIlIIIlllllIlI(IlllIllllIllIlIllI, IIlIIlllIlIIllIIIl):
        try:
            lllIlIllIlIlllllll = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.get(IIlIIlllIlIIllIIIl, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIIIlllIIIllIIIlII = lllIlIllIlIlllllll.find('form', {'method': 'post'})
            IlllllIlIlIllllIII = {'fb_dtsg': llIllllIlIIlll.search('name="fb_dtsg" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'jazoest': llIllllIlIIlll.search('name="jazoest" type="hidden" value="(.*?)"', lllllllllllllIl(lIIIlllIIIllIIIlII)).group(1), 'type': 'contact', 'edit': 'website', 'add_website': '1', 'new_info': IlllIllllIllIlIllI.IlIIlllIlllIlIIlIl, 'save': 'Tambahkan'}
            IllIIIlIIlIIlIIIIl = bs(IlllIllllIllIlIllI.lIIIIIlIIIIIlIlIll.post('https://mbasic.facebook.com' + lIIIlllIIIllIIIlII['action'], data=IlllllIlIlIllllIII, cookies=IlllIllllIllIlIllI.IlllIIIllllIlIIlIl).content, 'html.parser')
            lIlIlIlIIIIIllllIl = IllIIIlIIlIIlIIIIl.find('title').text
            if lIlIlIlIIIIIllllIl == 'Akun Anda dibatasi saat ini' or lIlIlIlIIIIIllllIl == 'Anda Diblokir Sementara' or lIlIlIlIIIIIllllIl == 'Kesalahan':
                llllllllllllIlI('\n%sGagal Mengganti Website%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
            else:
                llllllllllllIlI('\n%sBerhasil Mengganti Website%s' % (lIIIIIlIlIlllIIlIl, IIlllIlIlIlIllIIlI))
        except lllllllllllllll as IIIlllllllIlllIIlI:
            llllllllllllIlI('\n%sGagal Mengganti Website%s' % (llIlllIIlIllIIIlll, IIlllIlIlIlIllIIlI))
if llllllllllllllI == '__main__':
    lllIIlIIIllIllllll()
    IllllllllIIlIIllll()
    IIIllIlllIIIIIIlIl()
    IIlIIllllIIllIIlll()