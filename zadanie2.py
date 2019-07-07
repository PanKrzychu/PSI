import re
import sys

tab = []
ile_wszystkich = sum(1 for line in open('learning.txt', 'r'))
ile_wczytanych = 0
koniec_ladowania = 0


def read():
    global ile_wczytanych
    global ile_wszystkich
    global koniec_ladowania
    global tab

    if(ile_wczytanych >= ile_wszystkich):
        ile_wczytanych = ile_wszystkich
        koniec_ladowania = 1

    regex = re.compile(r"[0-9]+\,[0-9]*|[0-9]+|[\w]")
    with open('learning.txt', 'r') as f:
        for i in range(ile_wczytanych, ile_wczytanych+10):
            tab.append(re.findall(regex, f.readline()))


    print(tab, "\n")

    ile_wczytanych += 10

    print("Wczytanych: ",ile_wczytanych,"\nWszystkich: ", ile_wszystkich,"\n")

    menu()


def check():

    print("\nPamiętaj o schemacie wprowadzanych danych. Pierwsza liczba zawsze jest calkowita, druga jest od niej większa o jeden, trzecia skacze co pól, a czwarta jest od trzeciej o pól większa. \nJeśli wyjdziesz poza ten schemat, wyniki będą zakladame bądź ich nie będzie. Także zakres liczb wplywa na wyniki. Pierwsza z nich powinna być w przedziale od 1 do 6, a druga od 0 do 2,5.\nZasady te okeślone zostaly na podstawie pliku learning.txt\n")

    x = input("Podaj dolną granicę x: ")
    y = input("Podaj dolną granicę y: ")
    y = y.replace(',', '.')
    x = x.replace(',', '.')

    wynikA = 0
    wynikB = 0
    wynikC = 0

    ileX = 0
    ileY = 0

    ileA = 0
    ileB = 0
    ileC = 0

    p_ze_A = 0
    p_ze_B = 0
    p_ze_C = 0

    maxWartosc = 0.0
    maxLitera = 'BRAK WYNIKU'


    print("Twój zakres to: [", x, "; ", (int(x) + 1), ") | [", y, "; ", (float(y) + 0.5), ")")


    for i in tab:
        if i[4] == 'A':
            ileA =+ 1

            if i[0] == x:
                ileX =+ 1;
            if i[2] == y:
                ileY =+ 1;

    p_ze_A = (ileX*ileX * ileY*ileY) / (ileA**4)
    wynikA = p_ze_A*ileA/ile_wczytanych

    ileX = 0
    ileY = 0

    for i in tab:
        if i[4] == 'B':
            ileB =+ 1

            if i[0] == x:
                ileX =+ 1;
            if i[2] == y:
                ileY =+ 1;

    p_ze_B = (ileX*ileX * ileY*ileY) / (ileB**4)
    wynikB = p_ze_B*ileB/ile_wczytanych

    ileX = 0
    ileY = 0

    for i in tab:
        if i[4] == 'C':
            ileC =+ 1

            if i[0] == x:
                ileX =+ 1;
            if i[2] == y:
                ileY =+ 1;

    p_ze_C = (ileX*ileX * ileY*ileY) / (ileC**4)
    wynikC = p_ze_C*ileC/ile_wczytanych

    if wynikA > maxWartosc:
        maxWartosc = wynikA
        maxLitera = 'A'
    if wynikB > maxWartosc:
        maxWartosc = wynikB
        maxLitera = 'B'
    if wynikC > maxWartosc:
        maxWartosc = wynikC
        maxLitera = 'C'

    print("Po analizie naiwnym klasyfikatorem bayesowskim otrzymano: ",maxLitera,"\n")
    menu()


#main:
def menu():

    print("# Opcje:\n"
          "# 1. Wczytaj pakiet 10 rekordów\n"
          "# 2. Sprawdź, do jakiej klasy należy zakres\n"
          "# inne - wyjście\n")
    choice = input("\nWybieram opcję: ")

    if choice == "1":
        if koniec_ladowania == 0:
            read()
        else:
            print("Wybrano wszytko z pliku\n")
            menu()
    elif choice == "2":
        check()
    else:
        sys.exit()


menu()