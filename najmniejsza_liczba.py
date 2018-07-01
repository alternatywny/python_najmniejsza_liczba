# pobieranie danych od uzytkownika
while True:
    try:
        A, B, C = input("podaj 3 cyfry oddzielone spacjami: ").split(" ")

        A = int(A)
        B = int(B)
        C = int(C)
        break
    except ValueError:
        print("Błędne dane! Stosuj się do instrukcji")

rowne = False

if A == B or B == C or A == C:
    rowne = True
elif A > B < C:
    mini = B
elif B > C < A:
    mini = C
elif B > A < C:
    mini = A

if rowne == False:
    if mini == C and mini < A < B:
        medi = A
        maxi = B
    elif mini == A and mini < B < C:
        medi = B
        maxi = C
    elif mini == B and mini < C < A:
        medi = C
        maxi = A

    print("Najmniejsza liczba to: %s" % (mini))
    print("Średnia liczba to: %s" % (medi))
    print("Największa liczba to: %s" % (maxi))

if A == B == C:
    print("Wszystkie liczby sa takie same!")
    exit()

if rowne:
    if A == B:
        if A < C:
            mini = (A, B)
            maxi = C
        if A > C:
            mini = C
            maxi = (A, B)

    if A == C:
        if A < B:
            mini = (A, C)
            maxi = B
        if A > B:
            mini = B
            maxi = (A, C)

    else:
        mini = (B,C)
        maxi = A

    print("Najmniejsza liczba to: %s" % (str(mini)))
    print("Największa liczba to: %s" % (str(maxi)))