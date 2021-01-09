# program oblicza bmi i z dostepnych w pliku aktywnosci losuje aktywnosci, których łaczny czas trwania nie moze przekroczyc podanego przez uzytkownika

print('Podaj wzrost w metrach')
while True:
    height = input()  # wyczyscic przyjac tylko int jak jest z zakresu 1,5-2,3
    try:
        height = float(height)
        if height < 1.5 or height > 2.3:
            print('Podaj poprawny wzrost')
            continue
        else:
            break
    except ValueError:
        print('Podaj poprawny wzrost2')
        continue

print('Podaj wagę')
while True:
    weight = input()
    try:
        weight = float(weight)
        break
    except ValueError:
        print('Podaj prawdilowa wage')
        continue



bmi_factor = weight / (height*height)

print(bmi_factor)


bmi_thresholds = {0: "wygłodzenie",  #dictionary
                 15: "wychudzenie",
                 16: "niedowaga",
                 18.5: "pożądana masa ciałą",
                 25: "nadwaga",
                 30: "otyłość 1 stopnia",
                 35: "otyłość 2 stopnia",
                 40: "otyłość 3 stopnia"}

for threshold, description in bmi_thresholds.items():  # bierze najwieksza pasujaca wartosc
    if bmi_factor >= threshold:
        bmi_description = description
    else:
        break

print("Twoje bmi: "+str(bmi_description))

# losowanie innej aktywnosci na kazdy dzien tygodnia
activities = open("activities.txt").read().split()

activities_list = []

for x in activities:
    if x not in activities_list:
        activities_list.append(x)
    if len(activities_list) == 7:
        break
print('Aktywnosci na ten tydzien:')
print(activities_list)