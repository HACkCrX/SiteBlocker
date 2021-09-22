
from colorama import init
init()
from colorama import Fore, Back, Style   
from os import system as cmd
import platform
import random
  

def Banner():
    B1 = Fore.LIGHTMAGENTA_EX+"""
Sit   lo k r
   X x  . X 
   X .  . X 
   X .  . X 
   X .  . X 
   X .  . X 
   . .  . . 
            
Site Blocker
"""+Style.RESET_ALL

    B2 = Fore.LIGHTYELLOW_EX+ """
 +-+-+-+-+ +-+-+-+-+-+-+-+
 |S|i|t|e| |B|l|o|c|k|e|r|
 +-+-+-+-+ +-+-+-+-+-+-+-+
    """+Style.RESET_ALL




    B3= Fore.LIGHTRED_EX+ '''
 __.  ,      .__ .      .        
(__ *-+- _   [__)| _  _.;_/ _ ._.
.__)| | (/,  [__)|(_)(_.| \(/,[ 
..................................
        Allowe <-> Deny 
..................................
    
'''+Style.RESET_ALL
    Banners = [B1,B2,B3]
    print(random.choice(Banners))



def clear():
    System = platform.platform().split("-")[0]
    if System=='Windows':
        cmd('cls')
    

    elif System=='Linux':
        cmd('clear')




def Take_Effect():
    cmd('ipconfig /flushdns >nul')
    print()
    print('['+Fore.GREEN+'+'+Style.RESET_ALL+']'+' Flush Dns   ..... ['+Fore.GREEN+'DONE'+Style.RESET_ALL+']')
    print('['+Fore.GREEN+'+'+Style.RESET_ALL+']'+' Take Effect ..... ['+Fore.GREEN+'DONE'+Style.RESET_ALL+']')


def BlockWebsites():
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    hosts_temp = "hosts"
    redirect = "127.0.0.1"
    clear()
    Banner()
    print('┌─'+Style.RESET_ALL+'['+Fore.LIGHTCYAN_EX+':BlockWebsites'+Style.RESET_ALL+'[──['+Fore.RED+'BlacklistFile'+Style.RESET_ALL+']:',end="")
    Blacklist = input()
    print()
    web_sites_list = open(Blacklist,'r').readlines()
    Blacklist_File = open('blacklist.txt','w+')
    for w in web_sites_list:
        w=w.strip('\n')
        Blacklist_File.write(redirect+' '+w+'\n')
    Blacklist_File.close()



    clear()
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in web_sites_list:
            website = website.strip('\n')
            if website in content:
                Code = False
                pass
                print('['+Fore.CYAN+'*'+Style.RESET_ALL+'] {} already in hosts file '.format(website))
                
            else:
                Code = True
                file.write(redirect+" "+website+"\n")
                print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] Deny {} '.format(website))
                

        if Code ==True:
            print()
            print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] Blacklist')
            for website in web_sites_list:
                website=website.strip('\n')
                print(website)
            Take_Effect()
    
        
    print()
    print(Fore.YELLOW+'[!] PRESS ENTER TO CONTINUE .....',end=""+Style.RESET_ALL);input()




def BLACKLIST():
    try:
        Blacklistread = open('blacklist.txt','r').readlines() 
    except FileNotFoundError:
        clear()
        print()
        print('['+Fore.CYAN+'*'+Style.RESET_ALL+'] Blacklist Not Found ')
        print()
        print(Fore.YELLOW+'[!] PRESS ENTER TO CONTINUE .....',end=""+Style.RESET_ALL);input()

        main()


    Blacklist = []
    for b in Blacklistread:
        b=b.strip('\n')
        Blacklist.append(b)
  
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, "r") as f:
        lines = f.readlines()
        print()
        clear()
        if not Blacklist :
            print()
            print('['+Fore.CYAN+'*'+Style.RESET_ALL+'] Blacklist Not Found ')
            print()
             
        else:
            print('['+Fore.CYAN+'*'+Style.RESET_ALL+'] Blacklist ')
            print()
           

            
        for i in lines:
            i=i.strip('\n')
            if i in Blacklist:
                print('['+Fore.CYAN+'+'+Style.RESET_ALL+']',i)
        
            
                
    print()
    print(Fore.YELLOW+'[!] PRESS ENTER TO CONTINUE .....',end=""+Style.RESET_ALL);input()


def UnblockWebsite():
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    hosts_temp = "hosts"
    redirect = "127.0.0.1"
    clear()
    Banner()
    print('┌─'+Style.RESET_ALL+'['+Fore.LIGHTCYAN_EX+':UnblockWebsites'+Style.RESET_ALL+'[──['+Fore.RED+'WhitelistFile'+Style.RESET_ALL+']:',end="")
    whitelist = input()
    web_sites_list = open(whitelist,'r').readlines()
    print()
    clear()
    with open(hosts_path, 'r+') as file: 
        content=file.readlines() 
        file.seek(0) 
        for line in content: 
            if not any(website in line for website in web_sites_list): 
                file.write(line) 
                
         # removing hostnmes from host file 
        file.truncate() 
        for website in web_sites_list:
            website=website.strip('\n')
            print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] Allowe {}'.format(website))

        print()
        print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] Whitelist')
        print()
        for website in web_sites_list:
            website=website.strip('\n')
            print(website)

    Take_Effect()
    cmd('del blacklist.txt')
    print()
    print(Fore.YELLOW+'[!] PRESS ENTER TO CONTINUE .....',end=""+Style.RESET_ALL);input()







def main():
    while True:
        clear()
        Banner()
        print()
        print('[1]'+Fore.RED+'-'+Style.RESET_ALL+'['+Fore.LIGHTCYAN_EX+'Block Sites'+Style.RESET_ALL+'] ')
        print('[2]'+Fore.RED+'-'+Style.RESET_ALL+'['+Fore.LIGHTCYAN_EX+'Unblock Sites'+Style.RESET_ALL+'] ')
        print('[3]'+Fore.RED+'-'+Style.RESET_ALL+'['+Fore.LIGHTCYAN_EX+'Show Blacklist'+Style.RESET_ALL+'] ')
        print()
        print('┌─'+Style.RESET_ALL+'['+Fore.LIGHTCYAN_EX+':BlockWebsites'+Style.RESET_ALL+'[──['+Fore.RED+'Choice'+Style.RESET_ALL+']:',end="")
        ch = input()

        if ch=='1':
            BlockWebsites()
        elif ch=='2':
            UnblockWebsite()
        elif ch=='3':
            BLACKLIST()





if __name__ == '__main__':
    main()





