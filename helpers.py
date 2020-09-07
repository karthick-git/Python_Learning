from colorama import init,Fore,Back,Style

def display(message,is_Warning=False):
    if is_Warning:
        print(Fore.RED+message)
    print(Fore.BLUE+message)
    