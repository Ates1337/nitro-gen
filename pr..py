import random, string
import webbrowser
import time
import requests
from colorama import Fore, init
init()

print(Fore.RED + """\n\n
 █████╗ ████████╗ ██████╗ ██╗     ██╗    
██╔══██╗╚══██╔══╝██╔═══██╗██║     ██║    
███████║   ██║   ██║   ██║██║     ██║    
██╔══██║   ██║   ██║   ██║██║     ██║    
██║  ██║   ██║   ╚██████╔╝███████╗██║    
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝    
                                         \n\n""")

yarbeline = int(input('     Kaç tane nitro oluşturulsun: ')) # toolummu neden çalıyon ibiş
value = 1
while value <= yarbeline:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('kodlar.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[Üretilen] {code}')
    value += 1

print(Fore.GREEN + """Şimdi nitro kodlarını kontrol edicem aslan parçası""")    # Kodları kontrol ediyo

with open("Kodlar.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Nitro Çıktı lan | {} ".format(line.strip("\n")))
            break
        else:
            print(" Geçersiz | {}".format(line.strip("\n")))
input("Sona geldik aslan parçası  Programı kapatmak için 5 kez Enter tuşuna basın.") # Ve Toolumuz bitti
input("4")
input("3")
input("2")
input("1")    
