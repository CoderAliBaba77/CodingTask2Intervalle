#############################
# Python-Datei "Intervalle" #
#############################

# Kommentare: Erstellt mit PyCharm CE 2019.3
# Die Liste input kann selbst gewählte Intervalle enthalten oder zufällig generierte
#
# Was noch nicht gefixt wurde: wenn der Anfang oder Ende eines Intervalls direkt neben einem bestehenden Intervall ist
# z.B. (20, 30), (31, 34), (35,40)
#
# Gesamte benötigte Bearbeitungsdauer: ca. 14 Stunden, diese wurden auf 5 Tage verteilt
#
# Erste Idee war, zunächst einfach alle Integer-Werte jedes Eingabe-Intervalls in den Output schreiben,
# den Output sortieren und die doppelten Werte eliminieren. Zur Anzeige die Intervalle neu bilden, etwa so:
# Input [23, 25], [30, 32], [35, 37], [31, 36]
# Output dann zunächst: [23, 24, 25, 30, 32, 35, 37, 31, 32, 33, 34, 35, 36]
# nach Sortieren und Entfernen der Dubletten: [23, 24, 25, 30, 31, 32, 33, 34, 35, 36, 37]
# für den Output dann Intervalle neu bilden: [23, 25], [30, 37]
# Die Überlegung war dann aber: wahrscheinlich zu hoher Speicherverbrauch bei sehr vielen und großen Intervallen.
# Daher wurde die aktuelle Lösung programmiert.

import random as rndm

print("program started")

input = []

input = [(20,30), (31,34), (35,40)]
# input = [(25,30), (2,19), (14,23), (4,8)]  # Liste der Aufgabenstellung

'''
# Oder zufällige Intervalle generieren:
a = 0
while a < 1000000:  # Empfehlung: Zahl der Durchläufe zwischen 100 und 1.000.000 wählen, sonst sehr lange Laufzeit
    interval = (rndm.randint(a, a + 10), rndm.randint(a + 20, a + 30))
    input.append(interval)
    a = a + 10  # [sic]
'''

print("Input: " + str(input))


# print("Unsortierter Input: " + str(input))
input.sort()  # Sortieren der Intervalle, anhand deren linken Ränder, in aufsteigender Reihenfolge
print("Sortierter Input: " + str(input))

def MERGE(input):  # Die MERGE-Funktion

    output = []
    gaplist = []

    # durch alle Intervalle des Inputs iterieren
    i = 0  # Zähler für die weiteren Intervalle des Inputs

    while i < len(input):  # Alle Intervalle des Inputs durchiterieren:

        lRi = rRi = 0  # linker / rechter Rand liegt innerhalb eines Intervalls
        lRiL = rRiL = 0  # linker / rechter Rand liegt innerhalb einer Lücke zwischen den Intervallen
        lRTiI = rRTiI = -1  # linker / rechter Rand Treffer im Intervall mit der Nummer des Integers
        lRTiL = rRTiL = -1  # linker / rechter Rand Treffer in Lücke mit der nummer des Integers

        ivl = input[i]  # Input-Intervall an der Stelle i in ivl ablegen
        print("Input-Intervall Nummer " + str(i) + " = " + str(ivl))

        # Output-Intervalle durchiterieren, Ränder des Input-Intervalls gegen die im Output liegenden Intervalle prüfen

        j = 0  # Zähler für die Output-Intervalle, muss bei jedem Schleifen-Durchlauf hier wieder auf Null gesetzt werden
        while j < len(output):  # Für jedes Intervall im Output:
            oivl = output[j]  # Das Intervall an der Stelle j im Output herausnehmen und in oivl ablegen
            print("Output-Intervall Nummer " + str(j) + " = " + str(oivl))
            # Ist der linke Rand des Input-Intervalls Teil des Output-Intervalls?
            if testObRandTeilDesIntervalls(oivl, ivl[0]) == 1:  # 1 bedeutet Treffer
                lRi = 1
                lRTiI = j  # Position des Treffer-Intervalls ablegen
                print("der linke Rand des Input-Intervalls ist Teil des Output-Intervalls Nummer " + str(j))
            j = j + 1  # Zähler inkrementieren

        k = 0  # Zähler für die Output-Intervalle, muss bei jedem Schleifen-Durchlauf hier wieder auf Null gesetzt werden
        while k < len(output):  # Für jedes Intervall im Output:
            oivl = output[k]
            print("Output-Intervall Nummer " + str(k) + " = " + str(oivl))
            # Ist der rechte Rand des Input-Intervalls Teil des Output-Intervalls?
            if testObRandTeilDesIntervalls(oivl, ivl[1]) == 1:
                rRi = 1
                rRTiI = k  # Position des Treffer-Intervalls ablegen
                print("der rechte Rand des Input-Intervalls ist Teil des Output-Intervalls Nummer " + str(k))
            k = k + 1  # Zähler inkrementieren

        # Durch alle Lücken zwischen den Intervallen iterieren

        l = 0  # Zähler für die Lücken
        while l < len(gaplist):
            livl = gaplist[l]  # Lücke an Position l der Gaplist herausnehmen und in livl ablegen
            # print("Intervall-Lücke: " + str(livl))
            # Ist der linke Rand des Input-Intervalls Teil einer Lücke zwischen den Output-Intervallen?
            if testObRandTeilDesIntervalls(livl, ivl[0]) == 1:
                lRiL = 1
                lRTiL = l  # Position der Treffer-Lücke ablegen
                print("der linke Rand des Input-Intervalls ist in der Lücke " + str(l))
            l = l + 1

        m = 0  # Zähler für die Lücken
        while m < len(gaplist):
            livl = gaplist[m]  # Lücke an Position m der Gaplist herausnehmen und in livl ablegen
            # print("Intervall-Lücke: " + str(livl))
            # Ist der rechte Rand des Input-Intervalls Teil einer Lücke zwischen den Output-Intervallen?
            if testObRandTeilDesIntervalls(livl, ivl[1]) == 1:
                rRiL = 1
                rRTiL = m  # Position der Treffer-Lücke ablegen
                print("der rechte Rand des Input-Intervalls ist in der Lücke " + str(m))
            m = m + 1

        # Jetzt entscheiden, ob das Input-Intervall zu den Output-Intervallen hinzugefügt werden soll
        print("---------------------------------------------------------------------------------------------")
        print("Prüf-Ergebnis für die Ränder des Input-Intervalls " + str(ivl))

        if lRi == 1:
            print("linker Rand innerhalb eines Output-Intervalls: ja")
            print("linker Rand im Intervall Nummer " + str(lRTiI))
        else:
            print("linker Rand liegt außerhalb aller Output-Intervalle")
        if rRi == 1:
            print("rechter Rand innerhalb des Output-Intervalls: ja")
            print("rechter Rand im Intervall Nummer " + str(rRTiI))
        else:
            print("rechter Rand liegt außerhalb aller Output-Intervalle")
        if lRiL == 1:
            print("linker Rand innerhalb einer Lücke: ja")
            print("linker Rand innerhalb der Lücke " + str(gaplist[lRTiL]))
        else:
            print("linker Rand liegt nicht innerhalb einer Lücke.")
        if rRiL == 1:
            print("rechter Rand innerhalb einer Lücke: ja")
            print("rechter Rand innerhalb der Lücke " + str(gaplist[rRTiL]))
        else:
            print("rechter Rand liegt nicht innerhalb einer Lücke.")
        print("----------------------------------------------------------------------------------------------")

        # Feststellen der Fälle:
        # Beispiel-Output: [(20, 30), (35, 40), (45, 50)]
        print("Fall Nummer ")
        if lRi == rRi == 1 and lRTiI == rRTiI:  # Linker und rechter Rand innerhalb desselben Intervalls
            # Beispiel-Input: (25, 28)
            print("1: Input-Intervall liegt vollständig innerhalb desselben Output-Intervalls")
            print("Aktion: keine, da Intervall bereits abgedeckt")
        if lRi == rRi == 1 and lRTiI != rRTiI:  # Linker und rechter Rand innerhalb von zwei verschiedenen Intervallen
            # Beispiel-Input: (25, 47)  -> Zwischenintervall(e) möglich
            print("2: Input-Intervall liegt mit beiden Rändern innerhalb zweier verschiedenen Output-Intervalle")
            print("Zwei Intervalle mergen, potenzielle Zwischen-Intervalle löschen, Lücken-Liste neu aufbauen")

            # Merge-Vorgang:
            # Intervall im Output erzeugen, dessen linker Rand der des Intervalls mit dem linken Treffer ist und
            # dessen rechter Rand der des Intervalls mit dem rechten Treffer ist

            newLeftEdge = output[lRTiI][0]  # linker Rand des neu zu erstellenden Intervalls
            newRightEdge = output[rRTiI][1]  # rechter Rand des neu zu erstellenden Intervalls
            output.append(
                (newLeftEdge, newRightEdge))  # Intervall mit den entsprechenden Rändern neu erzeugen und anhängen
            # Frage: liegt eines oder mehrere Intervalle dazwischen? falls nicht: die beiden benachbarten löschen
            # falls doch: zusätzlich das oder die inneren Intervalle löschen
            AnzahlIntervalle = rRTiI - lRTiI + 1  # Anzahl der Intervalle, die gelöscht werden müssen
            c = 0  # Zähler für die Löschung der Intervalle
            while c < AnzahlIntervalle:
                output.remove((output[lRTiI]))
                c = c + 1

            output.sort()  # Output sortieren
            gaplist = erstelleGapList(output)  # Lücken-Liste neu erstellen

        if lRi == rRi == 0 and lRiL == rRiL == 0:  # Beide Ränder außerhalb und nicht innerhalb einer Lücke
            print("3: Ränder des Input-Intervalls nicht Teil eines Output-Intervalls oder einer Lücke")
            # Es können beide Ränder links, beide rechts oder einer links und einer rechts von allen Intervallen liegen

            # Falls noch keine Intervalle im Output liegen:
            if len(output) == 0:
                output = [(ivl)]

            # linker Rand links des Intervalls das am weitesten links liegt, rechter Rand rechts des Intervalls,
            # welches am weitesten Rechts liegt
            if ivl[0] < output[0][0] and ivl[1] > output[len(output)][1]:
                print("Output- und Lücken-Liste leeren, Input-Intervall in Output-Liste anlegen")
                output = [(ivl)]
                gaplist = []

            # Falls beide Ränder links oder rechts liegen: Intervall neu anlegen, Output sortieren, Lückenliste erneuern
            # beide Ränder links des am weitesten links liegenden Intervalls
            if ivl[0] < output[0][0] and ivl[1] < output[0][0]:
                output.append((ivl))
                output.sort()
                gaplist = erstelleGapList(output)
            # beide Ränder rechts des am weitesten rechts liegenden Intervalls
            if  ivl[0] > output[len(output) - 1][0] and ivl[1] > output[len(output) - 1][0]:
                output.append((ivl))
                output.sort()
                gaplist = erstelleGapList(output)



        if lRiL == rRiL == 1 and lRTiL == rRTiL:  # Beide Ränder innerhalb derselben Lücke
            # Beispiel-Input: (42, 44)
            print(
                "4a: Ränder des Input-Intervalls nicht innerhalb eines Output-Intervalls, aber innerhalb derselben Lücke")
            print("Input-Intervall neu anlegen, Liste sortieren, Lücken-Liste erneuern")
            output.append(ivl)
            output.sort()
            gaplist = erstelleGapList(output)
        if lRiL == rRiL == 1 and lRTiL != rRTiL:  # Beide Ränder innerhalb unterschiedlicher Lücken
            # Beispiel-Input: (33, 44)
            print("4b: Beide Ränder außerhalb eines Outputintervalls, aber innerhalb von zwei verschiedenen Lücken")
            print("Input-Intervall neu anlegen, Zwischenintervall(e) löschen, Liste sortieren, Lückenliste neu anlegen")
            print("Output vor append " + str(output))

            output.append(ivl)
            print("Output nach append " + str(output))
            # Anzahl der zu löschenden Zwischenintervalle bestimmen:
            AnzahlIntervalle = rRTiL - lRTiL
            d = 0  # Zähler für die Anzahl der zu löschenden Zwischenintervalle
            while d < AnzahlIntervalle:
                output.remove(output[rRTiL])
                print("Output nach Löschvorgang: " + str(output))
                d = d + 1

            output.sort()
            gaplist = erstelleGapList(output)

        if lRi == 1 and rRi == 0 and rRiL == 0:  # Linker Rand innerhalb, rechter Rand außerhalb aber nicht innerhalb Lücke
            # Beispiel-Input: (25, 55)  -> Zwischenintervalle (möglich)
            print("5: Linker Rand innerhalb, rechter Rand außerhalb aber nicht Teil einer Lücke")
            print(
                "Ergo: Rechter Rand des Inputintervalls liegt rechts des am weitesten rechts liegenden Output-Intervalls")
            print(
                "Aktion: Rechten Rand des Output-Intervalls auf den Wert des rechten Rands des Input-Intervalls abändern")
            print("Ggfs. Zwischenintervalle löschen, Lückenliste neu erstellen")

            AnzahlIntervalle = len(output) - lRTiI  # Anzahl der zu löschenden Intervalle bestimmen
            output.append((output[lRTiI][0], ivl[1]))
            e = 0  # Zähler für die Anzahl der zu löschenden Intervalle
            while e < AnzahlIntervalle:
                output.remove(output[lRTiI])
                e = e + 1

            output.sort()
            gaplist = erstelleGapList(output)

        if lRi == 1 and rRiL == 1:  # Linker Rand innerhalb, rechter Rand in Lücke
            # Beispiel-Input: (25, 44)  -> Zwischenintervall(e) (möglich)
            print(
                "6: Linker Rand innerhalb, rechter Rand außerhalb und innerhalb einer Lücke -> pot. Zwischenintervalle")
            print(
                "Rechten Rand des Output-Intervalls abändern, ggfs. Zwischenintervalle löschen und Lücken-Liste erneuern")

            AnzahlIntervalle = rRTiL - lRTiI + 1  # Anzahl der zu löschenden Intervalle bestimmen
            output.append((output[lRTiI][0], ivl[1]))
            f = 0  # Zähler für die Anzahl der zu löschenden Intervalle
            while f < AnzahlIntervalle:
                output.remove(output[lRTiI])
                f = f + 1

            output.sort()
            gaplist = erstelleGapList(output)

        if lRi == 0 and rRi == 1 and lRiL == 0:  # wie Fall 5, nur seitenverkehrt
            # Beispiel-Input: (16, 47)  -> Zwischenintervall(e) (möglich)
            print("7: Linker Rand außerhalb aber nicht innerhalb einer Lücke, rechter Rand innerhalb")
            print(
                "Ergo: Linker Rand des Input-Intervalls liegt links des am weitesten links liegenden Output-Intervalls")
            print("Rechter Rand des Input-Intervalls liegt innerhalb eines Output-Intervalls")
            print(
                "Linken Rand des ersten Output-Intervalls auf den Wert des linken Randes des Input-Intervalls abändern")
            print("Ggfs. Zwischenintervalle löschen, Lückenliste neu erstellen")

            AnzahlIntervalle = rRTiI + 1  # Anzahl der zu löschenden Intervalle bestimmen
            output.append((ivl[0], output[rRTiI][1]))
            g = 0  # Zähler für die Anzahl der zu löschenden Intervalle
            while g < AnzahlIntervalle:
                output.remove(output[0])
                g = g + 1

            output.sort()
            gaplist = erstelleGapList(output)

        if rRi == 1 and lRiL == 1:  # wie Fall 6, nur seitenverkehrt
            # Beispiel-Input: (33, 47)
            print(
                "8: Linker Rand außerhalb aber innerhalb einer Lücke, rechter Rand innerhalb -> pot. Zwischenintervalle")
            print(
                "Linken Rand des Output-Intervalls abändern, ggfs. Zwischenintervalle löschen und Lücken-Liste erneuern")

            AnzahlIntervalle = rRTiI - lRTiL  # Anzahl der zu löschenden Intervalle bestimmen
            output.append((ivl[0], output[rRTiI][1]))
            h = 0  # Zähler für die Anzahl der zu löschenden Intervalle
            while h < AnzahlIntervalle:
                output.remove(output[lRTiL + 1])
                h = h + 1

            output.sort()
            gaplist = erstelleGapList(output)
        print("Output nach Durchlauf " + str(i) + ": " + str(output))
        i = i + 1

    return output

def testObRandTeilDesIntervalls(ivl, Rand):
    print("Rand : " + str(Rand))
    print("Intervall: " + str(ivl))
    if Rand >= ivl[0] and Rand <= ivl[1]:
        print("Rand liegt innerhalb des Intervalls")
        return 1
    print("Rand liegt außerhalb des Intervalls")
    return 0

def erstelleGapList(outputList):
    h = 0  # Zähler für die Lücken

    gaplist = []  # Lücken-Liste anlegen

    while h < len(outputList) - 1:
        ivl0 = outputList[h]  # das linke von zwei Intervallen in ivl0 ablegen
        ivl1 = outputList[h + 1] # das rechte von zwei Intervallen in ivl1 ablegen
        liRaGap = ivl0[1] + 1  # linker Rand der Lücke ist rechter Rand des linken Intervalls plus eins
        reRaGap = ivl1[0] - 1  # rechter Rand der Lücke ist linker Rand des rechten Intervalls minus eins
        gap = (liRaGap, reRaGap)
        gaplist.append(gap)
        h = h + 1

    return gaplist

output = MERGE(input)

print("Ergebnis-Output: " + str(output))
