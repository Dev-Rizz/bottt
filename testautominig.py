#This program run all the other programs in a serial manner
import colorama
import sys
from colorama import Fore, Back, Style
from datetime import datetime
colorama.init(autoreset=True)
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
from pyfiglet import Figlet
import os
import time

red = '\x1b[1;37;41m'
green = '\x1b[0;30;42m'
tijo = '\033[92m'
tabang = '\033[1;91m'
reset = '\033[0;0m'

os.system("clear")
# Banner
#custom_fig = Figlet(font='basic')
#print(red+str(custom_fig.renderText('Rizz Store')))

# Body Program

print(red+str("Prepare Material Mining GPU"))
time.sleep(0.5)
os.system("sudo apt-key adv -q --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub")
os.system("wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin")
os.system("sudo add-apt-repository -q 'deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /' ")
print(green+str("Successfully Update Component"))
time.sleep(2)

print(red+str("UPDATE SYSTEM"))
time.sleep(0.5)
os.system("sudo apt update -qq")
time.sleep(0.5)
print(green+str("Successfully Update Systems"))

print(red+str("Installing Component GPU"))
time.sleep(0.5)
os.system("sudo apt install -qq cmake cuda -y")
os.system("echo 'export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc")
os.system("source ~/.bashrc")
time.sleep(0.5)
print(green+str("Successfully Installing Component GPU"))

print(red+str("Building Worker Mining"))
time.sleep(0.5)
os.system("git clone https://github.com/xmrig/xmrig-cuda.git")
os.system("mkdir xmrig-cuda/build")
os.chdir("xmrig-cuda/build")
os.system("cmake .. -DCUDA_LIB=/usr/local/cuda/lib64/stubs/libcuda.so -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda")
os.system("make -j$(nproc)")
time.sleep(0.5)
print(green+str("Successfully Building Worker"))

print(red+str("Downloading Component Worker"))
time.sleep(0.5)
os.system("wget -q https://github.com/Dev-Rizz/mine/blob/main/xmrig?raw=true")
os.system("mv xmrig?raw=true xmrig")
time.sleep(0.5)
print(green+str("Successfully Downloading Component Worker"))

print(red+str("Optimalisasi Component Worker"))
time.sleep(0.5)
os.system("sudo sysctl -w vm.nr_hugepages=10240")
time.sleep(0.5)
print(green+str("Successfully Optimalisasi Component Worker"))


print(red+str("Starting Mining"))
print(red+str("Good Luck"))
time.sleep(1.5)
os.system("chmod +x xmrig")
os.system("sudo ./xmrig --no-cpu --cuda -a cn-heavy/xhv -o br.haven.herominers.com:1110 -u hvxy97D6ovr2KAC9k3JWWb3i7ZmrMa5iJCQVqA6kLefiTc4pu1qLTWSSxWWU3fGjpGA9quiDsriDZGfXXJiGF96R6NfT9PRfFZ -k --tls -p T4-BotRizz")
