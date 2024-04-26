import random,os,requests,re
from bs4 import BeautifulSoup
from rich.panel import Panel as nel, Panel
from rich import print as prints

def get_random_user_agent():
	user_agent_components = {
	'browser': ['Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android',],
	'build': ['Build/MMB29M; wv)','Build/TP1A.220624.014; wv)','Build/PPR1.180610.011; wv)','Build/TP1A.220624.014; wv)','Build/SP1A.210812.016; wv)','Build/RP1A.200720.012; wv)','Build/LMY48B; wv)','Build/QP1A.190711.020; wv)',],
	'version': ['SM-M146B','SM-M326B','SM-N971N','SM-N971U','SM-N986N','SM-N9860','SM-N986W','SM-N986U1','SM-N986U', 'SM-N986B','SM-M625F','SM-N7506V','SM-N7500Q', 'SM-N750L', 'SM-N7507', 'SM-N750S', 'SM-N750K', 'SM-N7505', 'SM-N750', 'SM-N7502', 'SM-N910C', 'SM-N910S', 'SM-N910H', 'SM-N910F', 'SM-N910G', 'SM-N910U', 'SM-N910K', 'SM-N916S', 'SM-N910L', 'SM-N916L', 'SM-N916K', 'SM-N910T3', 'SM-M3070', 'SM-M307FN', 'SM-M307F', 'SM-N9150', 'SM-N915A', 'SM-N915D', 'SM-N915D', 'SM-N915F', 'SM-N915FY', 'SM-N915G', 'SM-N915K', 'SM-N915S', 'SM-N915X', 'SM-M205M', 'SC-02K', 'SM-G960U', 'SM-N920CD', 'SHV-E250L', 'SM-N9208', 'GT-N7100', 'SM-G110B', 'SM-N915L', 'SM-N915T', 'SC-01G', 'SM-M205F', 'SM-G960X', 'SM-G960', 'SM-N920C', 'SGH-I317M', 'SM-N920', 'GT-N7105', 'SM-G730A', 'SM-N915P', 'SM-N915V', 'SM-M205G', 'SM-G960N', 'SM-G960U1', 'SM-G960W', 'SM-M135F', 'SGH-T889', 'SHV-E250S', 'SM-G110M', 'GT-I8190L', 'SM-N915R4,', 'SM-N915W8', 'SM-M205FN', 'SCV38', 'SM-G9600', 'SM-G960F', 'SM-M127F', 'SHV-E250K', 'SM-G110H', 'SM-G110B', 'GT-I8190N', 'SM-S918U', 'SM-S918U1', 'SM-S918W', 'SM-S918N', 'SM-S9180', 'SM-S918E', 'SM-G990F', 'GT-I8200', 'GT-I8200N', 'GT-I8200L', 'GT-I8190', 'SM-S918B', 'SM-G550T2', 'SM-S550TL', 'SM-G550T', 'SM-G550T1', 'SM-G5510', 'SM-G5528', 'SM-G550F', 'SM-G5500', 'SM-M136B', 'GT-I9515L', 'SM-M115M', 'SM-R855', 'SM-G860', 'SM-G860P', 'GT-I9505', 'GT-I9515', 'SGH-I337', 'SC-04E', 'SM-R845F', 'SM-R855U', 'SM-R845U', 'SM-G530FZ', 'SM-G530H', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530W', 'SM-M115F', 'GT-P6200', 'GT-S5360', 'SM-R850', 'SM-R840', '600GN', 'SM-G530Y', 'SM-G5308W', 'SM-G530AZ', 'SM-G5309W', 'SM-G530BT', 'SM-G530FZ', 'SM-G530A', 'SM-G530M', 'SM-G531BT', 'SM-G530MU', 'M2004J19C', 'M2006C3LG', 'SM-G5306W', 'SM-G531Y', 'SM-G530T1', 'SM-G531M', 'SM-G530FQ', 'SM-G530F', ],
	'os': ['AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2. Chrome/',' AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/', ],
	'mobile': ['Mobile Safari/537.36', ], 
	'fb_waf': ['[FB_IAB/Orca-Android;FBAV/354.0.0.10.113;]','[FB_IAB/FB4A;FBAV/406.0.0.26.90;]','[FB_IAB/FB4A;FBAV/404.0.0.35.70;]','[FBAN/EMA;FBLC/en_US;FBAV/331.0.0.9.105;]','[FB_IAB/FB4A;FBAV/406.0.0.17.90;]','[FB_IAB/FB4A;FBAV/405.0.0.23.72;]','[FB_IAB/FB4A;FBAV/405.1.0.28.72;]','[FB_IAB/FB4A;FBAV/396.0.0.21.104;]','[FB_IAB/FB4A;FBAV/385.0.0.32.114;]','[FB_IAB/FB4A;FBAV/387.0.0.24.102;]'],}
	browser = random.choice(user_agent_components['browser'])
	app = random.randint(2,13)
	build = random.choice(user_agent_components['build'])
	version = random.choice(user_agent_components['version'])
	os = random.choice(user_agent_components['os'])
	language = str(random.randint(50,199)) + ".0." + str(random.randint(2999,5999)) + "." + str(random.randint(50,150))
	mobile = random.choice(user_agent_components['mobile'])
	fb = random.choice(user_agent_components['fb_waf'])
	ua_oppo = f'{browser} {app}; {version} {build} {os}{language} {mobile} {fb}'
	return ua_oppo

def sistem_dalvik_ua():
	user_componen = {
		'mes': ['MessengerLite','Orca-Android','FB4A',],
		'com' : ['com.facebook.mlite','com.facebook.orca','com.facebook.katana',],
		'loc' : ['en_US','th_TH','vi_VN','id-ID','jp-JP',],
		'fbcr' : ['Airtel','TNT','TRUE-H','AIS','null','T-Mobile',],
		'model' : ['LGE','INFINIX MOBILITY LIMITED','OPPO','samsung','oppo','vivo','infinix','redmi','realmi','lg','asus',],
		'mod' : ['lge','Infinix','OPPO','samsung','Redmi','Realmi','lg','Asus','POCO','XIOMI',],
		'jenis' : ['L-03K','Infinix X688B','CPH1909','SM-A720F','SM-G532G','SM-G3518',],
	}
	messeger = random.choice(user_componen['mes'])
	ip = str(random.randint(100,299)) + '.0.0.' + str(random.randint(1,99)) + '.' + str(random.randint(99,299))
	com_facebook = random.choice(user_componen['com'])
	lokasi = random.choice(user_componen['loc'])
	fbv = str(random.randint(1999999,59999999))
	face = random.choice(user_componen['fbcr'])
	model = random.choice(user_componen['model'])
	mod = random.choice(user_componen['mod'])
	jenis = random.choice(user_componen['jenis'])
	fbs = str(random.randint(1,10))
	fbs1 = str(random.randint(1,10)) + '.' + str(random.randint(0,5)) + '.' + str(random.randint(0,3))
	FBSV = random.choice([fbs,fbs1])
	densi = "{density=" + str(random.randint(1,3)) + ".0,width=" + str(random.randint(720,1920)) + ",height=" + str(random.randint(720,1920)) + "};FB_FW/1;FBRV/" + str(random.randint(19999999,499999999)) + ";]"
	ua = f"[FBAN/{messeger};FBAV/{ip};FBPN/{com_facebook};FBLC/{lokasi};FBBV/{fbv};FBCR/{face};FBMF/{model};FBBD/{mod};FBDV/{jenis};FBSV/{FBSV};FBCA/x86:armeabi-v7a;FBDM/{densi}"
	return ua

ua = get_random_user_agent()
ua2 = sistem_dalvik_ua()
os.system('cls')
prints(Panel.fit(f'[#00C8FF]' + ua))
print("\n--------------------------------------\n")
prints(Panel.fit(f'[#00C8FF]' + ua2))