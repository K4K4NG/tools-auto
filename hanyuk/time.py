import os
import marshal
import logging
from rich.panel import Panel as Panel
from rich.tree import Tree
from rich.table import Table as lipat
from rich.console import Console as solsapatu
from rich.columns import Columns as coli, Columns
from rich import print as prints

console = solsapatu()


def main():
    os.system('cls')
    prints(Panel.fit(f"[bold green]___________ _______  _________          _______________ ___ ________ \n \_   _____/ \      \ \_   ___ \         \______   \__  |   |\_____  \ \n |    __)_  /   |   \/    \  \/   ______ |     ___//   |   |  _(__  < \n |        \/    |    \     \____ /_____/ |    |    \____   | /       \ \n/_______  /\____|__  /\______  /         |____|    / ______|/______  /\n        \/         \/        \/                    \/              \/ [bold white]"))
    tree = Tree(
        Panel.fit(
            f"[bold green] Selamat datang di script encripsi by : Meledak cik[bold white]"
        ))
    tree.add(Panel.fit(f"[bold blue]Encripsi Version 0.01\nCoded Python[bold white]"))
    prints(tree)
    prints(Panel.fit(f"[bold red]Peringatan!!![bold green] Jika terjadi eror saat proses biasanya salah memasukan alamat tempat atau typo tulisan file[bold white]"))
    file = input("+_ Masukan nama file : ")
    string = input("+_ Masukan number variable minimmal (1000) max (5000) : ")
    mode2(file,string)


def mode2(file, string):
    x = open(file).read()
    m = compile(x, '', 'exec')
    k = marshal.dumps(m)
    l = open('encoded-' + file, 'w')
    l.write(
        '# // Please use this script specifically for learning.\n# // If you misuse it, it is your right.\n# // I am not responsible for your detrimental actionsimport requests\n# // My code is not perfect, I am still learning.\n# // I am not responsible for your actions.\n# // My Website : https://github.com/K4K4NG\n# // My Medsos : IG @ksyfmldkkk_  FB : Sory my facebook random\n# // My Country : Indonesia\n# // My Language : Python,Java,C++,C lang,C#,PHP,HTML,CSS,JS,SQL\n# // My City : Bandung\n# // My School : Private\n# // Dont recode or copy my code in the name of the person who created it\n# // Dont hope in falsehood because it will make you fall to the lowest point\n# // [ -------------- Meledak X Cik Created X Owner Hacker Cyber Nalar -------------- ]\n# # Enc By : Meledak Cik\n# Github : https://github.com/K4K4NG/\n# Instagram : @ksyfmldkkk_\n\n# Terimakasih sudah menggunakan script ini\n'
    )
    for i in range(string):
        l.write(
            "Meledak__ = ('https://github.com/K4K4NG/');_Agus_ = ['from','import','as','marshal','crypto','RSA','econic','base64','zlib','((','))','exec',]\n"
        )
    l.write('import marshal\n')
    l.write('eval(marshal.loads(' + repr(k) + "))\n")
    for i in range(string):
        l.write(
            "Meledak__ = ('https://github.com/K4K4NG/');_Agus_ = ['from','import','as','marshal','crypto','RSA','econic','base64','zlib','((','))','exec',]\n"
        )
    l.close()
    prints(Panel.fit('[bold green]Dont forget follow instagram me : ksyfmldkkkk_[bold white]\nEncripsi file sudah sukses as \'encoded-{}\''.format(file)))



if __name__ == "__main__":
    main()