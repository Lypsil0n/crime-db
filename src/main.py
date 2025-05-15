from db.dao import DAO
from tabulate import tabulate

def main():
    dao = DAO()
    conn = dao.connect()

    headers = ["malnummer", "tilltalad", "personnummer", "brottsrubricering", "lank"]
    running = True


    print("Välkommen till CrimeDB")
    print("Skriv 'help' för en lista över kommandon. Skriv 'exit' för att avsluta")

    while running:
        command = input("> ")
        args = command.split(' ')

        if args[0].lower() == 'exit':
            print("Avslutar CrimeDB...")
            running = False

        elif args[0].lower() == 'help':
            print("help - Lista alla kommandon")
            print("access <sökord> - Sök efter ett mål baserat på målnummer, namn på tilltalad, personnummer eller brottsrubricering")
            print("access all - Lista alla tillgängliga domar")
            print("exit - Avsluta CrimeDB")

        elif args[0].lower() == 'access':
            if args[1] == 'all':
                res = dao.get_all(conn)
                print(tabulate(res, headers=headers, tablefmt="pretty"))

            else:
                query = ' '.join(args[1:]).capitalize()
                res = dao.get_by_query(conn, query)
                print(tabulate(res, headers=headers, tablefmt="pretty"))

        else:
            print("Okänt kommando")
    
main()
