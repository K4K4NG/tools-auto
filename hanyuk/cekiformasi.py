import os, sys, requests, bs4, re, time, datetime, urllib, random, json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs

P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau


def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.datetime.now()
def finish():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\nProgram Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\nProgram Selesai Dalam Waktu 0 Detik\n')

def waktu_kom():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.datetime.now().month - 1]
    _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
    hari_ini = ("%s %s %s"%(datetime.datetime.now().day,_bulan_,datetime.datetime.now().year))
    jam      = datetime.datetime.now().strftime("%X")
    tem      = ('\n\n%s, %s --> %s'%(_hari_,hari_ini,str(jam).replace(':','.')))
    return(tem)

class login:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
        menu()
    def cek_cookies(self):
        try:
            global nama_akun, id_akun
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            language(self.cookie)
            req       = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()
            nama_akun = req['name']
            id_akun   = req['id']
            clear()
            print('%sLogin Sebagai %s%s%s'%(P,H,nama_akun,P))
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        print('%sCookie Invalid!%s'%(M,P))
        time.sleep(2)
        clear()
        ciko = input('%sMasukkan Cookie : %s%s'%(P,H,P))
        try:self.token_eaag = self.generate_token_eaag(ciko)
        except Exception as e: self.insert_cookie()
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        self.cek_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)

#--> Main Menu
class menu:
    def __init__(self):
        self.main()
    def main(self):
        print('[1] Edit Foto Profil'%())
        print('[2] Edit Foto Sampul'%())
        print('[3] Edit Bio'%())
        print('[4] Edit Kota'%())
        print('[5] Edit Website'%())
        print('[6] Edit Name'%())
        print('[7] Edit Ttl'%())
        print('[8] Hapus Akun'%())
        print('[0] Logout'%())
        x = input('Pilih : ')
        print('')
        if   x in ['1','01','a']: edit_profile_pic(); menu()
        elif x in ['2','02','b']: edit_cover_pic(); menu()
        elif x in ['3','03','d']: update_bio(); menu()
        elif x in ['4','04','e']: edit_kota(); menu()
        elif x in ['5','05','f']: edit_website(); menu()
        elif x in ['6','06','f']: change_name(); menu()
        elif x in ['7','07','f']: ttl_facebook(); menu()
        elif x in ['8','08','f']: menu()
        elif x in ['0','00','z']:
            try:
                os.remove('login/cookie.json')
                os.remove('login/token_eaag.json')
                print('Good Bye...')
            except Exception :
                print('Good Bye...')
        else :
            print('%sIsi Yg Benar!%s'%(M,P))

class change_name:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        print('Harap perhatikan: Jika Anda mengubah nama di Facebook, maka Anda tidak dapat mengubahnya lagi selama 60 hari. Jangan menambahkan huruf besar, tanda baca, karakter, atau kata-kata acak yang tidak biasa.')
        self.change = input('Nama Baru : ')
        self.change1 = input('Nama Tengah : ')
        self.change2 = input('Nama Belakang : ')
        self.pw = input('Password : ')
        self.scrap1()
    def scrap1(self):
        try:
            url = 'https://mbasic.facebook.com//settings/name_change_preview/?entrypoint=unknown&amp;refid=70&amp;paipv=0&amp;eav=Afb4fy9YVkgozUW22I0RwGftLxASuwMa4gZUfJljiI1s8qIvQsXQ0FRgU3vjuuKAE4Y'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                 : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                 : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'primary_first_name'      : self.change,
                'primary_middle_name'     : self.change1,
                'primary_last_name'       : self.change2,
                'save'                    : 'Simpan perubahan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Nama%s'%(M,P))
            else:
                url = 'https://mbasic.facebook.com/a/settings/account/?confirm_new_name=1&amp;confirm_name&amp;page_type=none&amp;eav=AfaHJCfUusBL9YQpIT1koxHuyW_O1GMZGkFHmoIcobRhNFnmQCNT8HlZGQ_1hXJa50s&amp;paipv=0'
                req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
                raq = req.find('form',{'method':'post'})
                dat = {
                    'fb_dtsg'                 : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'jazoest'                 : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'primary_first_name'      : self.change,
                    'primary_middle_name'     : self.change1,
                    'primary_last_name'       : self.change2,
                    'alternate_name'          : '',
                    'show_alternate'          : '',
                    'save_password'           : self.pw,
                    'save'                    : 'Simpan perubahan'}
                pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
                cek = pos.find('title').text
                if '/settings/name_change_preview/?invalid_password=1' in cek:
                    print('\n%sPassword Salah%s'%(M,P))
                elif cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                    print('\n%sGagal Mengganti Nama%s'%(M,P))
                else:
                    print('\n%sBerhasil Mengganti Nama%s'%(H,P))
                print('\n%sBerhasil Mengganti Nama%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Nama%s'%(M,P))

class delete_akun:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.pw = input("masukan pas : ")
        self.mulai()
        def mulai(self):
            try:
                url = 'https://mbasic.facebook.com/account/delete/?back_uri=%2Fhome.php&account_screen&reason=NONE&hcb=0&eav=AfaRlJ4pLedUKEl9OyRJaZsHXWY05zHKhy2kokVgWArmz-uNasq35hxuiig3bS_QAR0&paipv=0&consent'
                req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
                raq = req.find('form',{'method':'post'})
                dat = {
                    'fb_dtsg'                 : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'jazoest'                 : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'password'                : self.pw,
                    'hcb'                     : re.search('name="hcb" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'account'                 : 'Lanjut'}
                pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
                cek = pos.find('title').text
                if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                    print('\n%sGagal menghapus akun%s'%(M,P))
                else:
                    url = 'https://mbasic.facebook.com/account/delete/?back_uri=%2Fhome.php&deletion_screen&reason=NONE&hcb=0&eav=AfaBxsa4X_bPNn1R40eEKRsH8CgkaoGMClmabs_mTwIM2n6Ff_C3Wxia2Zd-8VriVN0&paipv=0&_rdr'
                    req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
                    raq = req.find('form',{'method':'post'})
                    dat = {
                        'fb_dtsg'                 : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'jazoest'                 : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'hcb'                     : re.search('name="hcb" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'delete'                 : 'Hapus Akun'}
                    pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
                    cek = pos.find('title').text
                    if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                        print('\n%sGagal menghapus akun%s'%(M,P))
                    else:
                        print("berhasil delet akun")
            except Exception as e:
                print('\n%sGagal menghapus akun%s'%(M,P))

class ttl_facebook:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1970,20010))}
        self.mulai()
    def mulai(self):
        try:
            url = 'https://mbasic.facebook.com/editprofile.php?type=basic&edit=birthday&eav=Afbcml7kH4Wm0NB_3vHraz4WaOMhnyxdSV6-pbFHDjqqQkn-10Rr7lhmv_VRFjue0jw&paipv=0&refid=17#/'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                 : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                 : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'                    : 'birthday',
                'type'                    : 'basic',
                'day'                     : self.ttl['tgl'],
                'month'                   : self.ttl['bln'],
                'year'                    : self.ttl['thn'],
                'save'                    : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Ttl%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Ttl%s'%(H,P))
                print('TTL    : %s %s %s'%(self.ttl['tgl'],bulan[self.ttl['bln']],self.ttl['thn']))
        except Exception as e:
            print('\n%sGagal Mengganti Ttl%s'%(M,P))


class edit_profile_pic:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.tanya()
    def tanya(self):
        d = input('URL Foto : ')
        self.scrap1(d)
    def scrap1(self,i):
        try:
            fot = urllib.request.urlopen(i)
            url = 'https://mbasic.facebook.com/profile_picture/'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Simpan'}
            fil = {'pic' : fot}
            pos = bs(self.xyz.post(raq['action'],data=dat,files=fil,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Foto Profil%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Foto Profil%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Foto Profil%s'%(M,P))

class edit_cover_pic:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.tanya()
    def tanya(self):
        d = input('URL Foto : ')
        self.scrap1(d)
    def scrap1(self,i):
        try:
            fot = urllib.request.urlopen(i)
            url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Unggah'}
            fil = {'file1' : fot}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,files=fil,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Foto Sampul%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Foto Sampul%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Foto Sampul%s'%(M,P))

class update_bio:
    def __init__(self):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.bio    = input('Tulis Bio cth : aku sayang alya : ')
        self.scrap1()
    def scrap1(self):
        try:
            url = 'https://mbasic.facebook.com/profile/basic/intro/bio/'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : self.bio,
                'publish_to_feed' : True,
                'submit'          : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Bio%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Bio%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Bio%s'%(M,P))
class edit_kota:
    def __init__(self):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        kota = input('Nama Kota : ')
        self.scrap('https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown','hometown','hometown[]',kota)
        self.scrap('https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city','current_city','current_city[]',kota)
    def scrap(self,url,a,b,kota):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : a,
                'type'       : 'basic',
                b : kota,
                'save'       : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('%sGagal Mengganti Kota%s'%(M,P))
            else:
                print('%sBerhasil Mengganti Kota%s'%(H,P))
        except Exception as e:
            print('%sGagal Mengganti Kota%s'%(M,P))

class edit_website:
    def __init__(self):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.web = input('URL Web : ')
        self.scrap('https://mbasic.facebook.com/editprofile.php?type=contact&edit=website')
    def scrap(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'type'       : 'contact',
                'edit'       : 'website',
                'add_website': '1',
                'new_info'   : self.web,
                'save'       : 'Tambahkan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Website%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Website%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Website%s'%(M,P))


if __name__ == '__main__':
    clear()
    start()
    login()
    finish()
