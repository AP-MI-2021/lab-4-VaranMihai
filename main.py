def citire_lista():
    l = []
    givenString = input("dati lista, cu sirurile de caractere separate prin vigula: ")
    stringChar = givenString.split(",")
    for x in stringChar:
        l.append(str(x))
    return l


def sirul_se_afla_in_lista(l,s):
    '''
    Verifica daca un sir se gaseste in lista
    :param l: lista de siruri
    :param s: sirul ce trebuie aflat
    :return: DA daca se afla sau NU daca nu se afla in lista
    '''
    ok = 0
    for x in l:
        if x == s:
            ok = 1
    if ok == 1:
        return "DA"
    else:
        return "NU"


def test_sirul_se_afla_in_lista():
    assert sirul_se_afla_in_lista(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'], 'drd') == "DA"


def siruri_care_se_repeta(l):
    '''
    Afiseaza o lista cu toate sirurile de caractere care se repeta in lista principala
    :param l: lista de siruri
    :return: lsita de siruri care se repeta
    '''
    rezultat = []
    ok = 0
    for x in l:
        for i in l:
            if i == x and ok == 1:
                rezultat.append(x)
            else:
                ok = 1
    return rezultat


def test_siruri_care_se_repeta():
    assert siruri_care_se_repeta(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa']


def palindrom(s):
    '''
    Verifica daca un sir este palindrom
    :param s: sirul
    :return: True daca este sau False daca nu
    '''
    palindrom_s = s[::-1]
    if s == palindrom_s:
        return True
    else:
        return False


def test_palindrom():
    assert palindrom(['asa']) is True


def siruri_palindroame(l):
    '''
    Afiseaza lista cu siruri palindroame dintr-o lista
    :param l: lista de siruri
    :return: lista de siruri palindroame
    '''
    rezultat = []
    for x in l:
        if palindrom(x):
            rezultat.append(x)
    return rezultat


def test_siruri_palindroame():
    assert siruri_palindroame([]) == []
    assert siruri_palindroame(['ada', 'abc', 'cmtc', 'drd', 'aaa']) == ['ada', 'drd', 'aaa']



def main():
    test_sirul_se_afla_in_lista()
    test_palindrom()
    test_siruri_palindroame()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afisati daca un sir de caractere se gaseste in lista.")
        print("3. Afisati o lista cu toate sirurile care se repeta.")
        print("4. Afiseaza toate sirurile palindroame din lista")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            s = str(input("Dati sirul de caractere: "))
            print(sirul_se_afla_in_lista(l,s))
        elif optiune == "3":
            print(siruri_care_se_repeta(l))
        elif optiune == "4":
            print(siruri_palindroame(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati.")

main()