from tkinter import Tk, Label, Button
from random import shuffle

baza = [
    ["Z jakim numerem na początku kariery w NBA grał Kobe Bryant?", ["23", "4", "8", "24"], 2],
    ["W którym roku Robert Kubica wygrał wyścig w F1?", ["2010", "2008", "2007", "2019"], 1],
    ["Zaokrąglenie liczby Pi do części setnych to?", ["2,71", "3,14", "2,72", "3,64"], 1],
    ["W którym roku Polska dołączyła do NATO?", ["2015", "1990", "2004", "1999"], 3],
    ["Jaka jest temperatura w Celsjuszach zera absolutnego w zaokrągleniu do liczb całkowitych?", ["-273", "0", "-1335", "-121"], 0],
    ["Kto był pierwszym Prezydentem w 3RP?",
     ["Wojciech Jaruzelski", "Lech Wałęsa", "Gabriel Narutowicz", "Aleksander Kwaśniewski"], 0],
    ["Jaką Planetę nazywamy błękitną?", ["Ziemia", "Mars", "Jowisz", "Wenus"], 0],
    ["Nikola Tesla był pochodzenia?", ["Polskiego", "Amerykańskiego", "Niemieckiego", "Serbskiego"], 3],
    ["Jak nazywał się główny bohater filmu Blade Runner?",
     ["Rick Deckard", "Geralt z Rivii", "Dick Grayson", "Paul Atreides"], 0],
    ["Zwycięzca Ligi mistrzów w piłce nożnej z 2010 roku?",
     ["Real Madryt", "Inter Mediolan", "Barcelona", "Manchester United"], 1],
    ["Mona Lisa to dzielo?", ["Picassa", "Da Vinci", "Van Gogha", "Dali"], 1],
    ["Jakie jest miejsce zerowe funkcji f(x) = (x-3)?", ["-3", "3", "0", "nie posiada miejsc zerowych"], 1]
]

kasa = ["1 000 zł", "2 000 zł", "5 000 zł", "10 000 zł", "15 000 zł", "25 000 zł", "50 000 zł", "75 000 zł",
        "125 000 zł", "250 000 zł", "500 000 zł", "1 MILION zł"]

p = 0
guziki = []
obecne_pytania = []


def mieszaj():
    global obecne_pytania
    obecne_pytania = baza.copy()
    shuffle(obecne_pytania)


def graj():
    global p
    for g in guziki:
        g.config(state="normal")

    txt = obecne_pytania[p][0]
    odp = obecne_pytania[p][1]
    pieniadze = kasa[p]
    l1.config(text="Pytanie nr " + str(p + 1) + " | Grasz o: " + pieniadze)
    l2.config(text=txt, fg="black")

    for i in range(4):
        guziki[i].config(text=odp[i])


def klik(co):
    global p
    ok = obecne_pytania[p][2]
    if co == ok:
        win = kasa[p]
        p += 1
        if p == 12:
            l_grat.config(text="KONIEC! WYGRAŁEŚ " + win + "!", fg="green")
            l2.config(text="JESTEŚ MILIONEREM!", fg="gold")
            koniec()
        else:
            l_grat.config(text="BRAWO! Masz już " + win, fg="green")
            graj()
    else:
        dobry_tekst = obecne_pytania[p][1][ok]
        l_grat.config(text="Niestety, zła odpowiedź...", fg="red")
        l2.config(text="Przegrałeś! Poprawna odpowiedź to: " + dobry_tekst, fg="red")
        koniec()


def koniec():
    for g in guziki:
        g.config(state="disabled")
    reset_btn.pack(pady=10)


def restart():
    global p
    mieszaj()
    p = 0
    l_grat.config(text="Powodzenia!", fg="blue")
    reset_btn.pack_forget()
    graj()


okno = Tk()
okno.title("Milionerzy")
okno.geometry("650x600")

l_grat = Label(okno, text="Witaj w grze!", font=("Arial", 18, "bold"), fg="blue")
l_grat.pack(pady=10)

l1 = Label(okno, text="", font=("Arial", 14))
l1.pack(pady=5)

l2 = Label(okno, text="", font=("Arial", 22, "bold"), wraplength=600, height=4)
l2.pack(pady=10)

for i in range(4):
    btn = Button(okno, text="", width=40, font=("Arial", 12), command=lambda x=i: klik(x))
    btn.pack(pady=5)
    guziki.append(btn)

reset_btn = Button(okno, text="ZAGRAJ JESZCZE RAZ", bg="lightgreen", font=("Arial", 14, "bold"), command=restart)

restart()
okno.mainloop()
