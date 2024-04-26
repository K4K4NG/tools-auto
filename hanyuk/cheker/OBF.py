import os
import re
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

try:
    import requests
    from fake_useragent import UserAgent
except ImportError:
    os.system('pip install requests fake-useragent')
    import requests
    from fake_useragent import UserAgent

GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
RESET = '\033[0m'
UNGU = '\033[35m'
LIME = '\033[38;5;154m'
MERAH = '\033[31m'

s = requests.Session()

ua = {
    'User-Agent': UserAgent().random
}

names = []


def process_site(site, token, output_file):
    try:
        if site.startswith("http://"):
            site = site.replace("http://", "")
        if site.startswith("https://"):
            site = site.replace("https://", "")
        response = s.get(f"https://priv8.xrxaxm.com/api/revip.php?ip={site}&token={token}", headers=ua).content.decode("utf-8")
        pattern = r"<br>(.*?)<br>"
        results = re.findall(pattern, response)
        print(GREEN + "[✓]" + UNGU + site + YELLOW + " Total:" + LIME + str(len(results)) + MERAH + " Domain" + GREEN + " diambil")

        for line in results:
            line = line.strip()  # delete ' '
            if line.startswith("www."):
                line = "" + line[4:]
            if line not in names:
                names.append(line)
                with open(output_file, 'a+') as f:
                    f.write(line + "\n")  # write output

        time.sleep(1)  # Penundaan selama 1 detik setelah setiap permintaan

    except:
        pass


def reverse():
    try:
        output_file = input('Enter output file name: ')
        site = input('[]Masukkan file List IP: ')
        token = input('[]Masukkan token: ')
        line = open(site, 'r').read().splitlines()
        print("")

        with ProcessPoolExecutor() as executor:
            for site in line:
                executor.submit(process_site, site, token, output_file)

        executor.shutdown(wait=True)  # Menunggu semua tugas selesai sebelum script berakhir

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    reverse()
