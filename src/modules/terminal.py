"""Module to provide colored terminals """
# Terminal

from colorama import init, Fore, Style
init()

# Styled text on terminal.
BOLD = f"{Style.BRIGHT}"

# Colored status on terminal.
ALERT = f"{Style.BRIGHT}{Fore.YELLOW}[{
    Fore.WHITE}*{Fore.YELLOW}] ALERT {Fore.RESET}- "

ERROR = f"{Style.BRIGHT}{Fore.RED}[{
    Fore.WHITE}*{Fore.RED}] ERROR {Fore.RESET}- "

INFORMATION = f"{Style.BRIGHT}{Fore.BLUE}[{
    Fore.WHITE}*{Fore.BLUE}] INFORMATION {Fore.RESET}- "

SUCCESS = f"{Style.BRIGHT}{Fore.GREEN}[{
    Fore.WHITE}*{Fore.GREEN}] SUCCESS {Fore.RESET}- "

SAVED_IN = f"{Style.BRIGHT}{Fore.GREEN}[{
    Fore.WHITE}*{Fore.GREEN}] SAVED IN {Fore.RESET}- "
