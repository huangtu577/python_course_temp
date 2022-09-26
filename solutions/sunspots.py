import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Konstanten werden gewöhnlich in CAPS am Anfang des Programms definiert. Sie sollen
# Für die gesamte Laufzeit des Programms nicht geändert werden.
# Es bietet sich an Dateinamen als eigene Variable zu speichern, damit man den Code 
# einfach für eine andere Datei verwenden kann, ohne überall den Dateinamen zu ändern.
FILENAME = "sunspot_data.csv"

# Lies die Dateien ein
df = pd.read_csv(FILENAME)

# Um sich den DataFrame genauer anzuschauen, bietet sich entweder der Variable Explorer
# an, wenn du Spyder Verwendest (Was ich dir empfehlen würde),
# ansonten kannst du dir mit folgendem Befehl die ersten Zeilen anzeigen lassen

# print(df.head())


# Es fällt auf, dass es eine Zeile gibt, in der keine Sinnvolle Information steht
# (die erste). Deshalb entfernen wir diese:
    
# Wir müssen das label der Zeile angeben, ohne die Spezifizierte Achse kommt ein
# KeyError, da Pandas Versucht das Label in den Zeilenlabeln zu finden. Wir wollen
# aber eine Spalte löschen. Wir müssen das Ergebnis einer neuen Variable zuweisen, 
# da das Spalte löschen ein neues Objekt erstellt. Man könnte auch eine inplace Änderung
# Vornehmen, dann müsste man die flag inplace=True in den Funktionsaufruf einfügen
df = df.drop(labels = "Unnamed: 0", axis = 1)


# Es ist möglich, DataFrames zu filtern nach einem Boolschen Ausdruck:
# vgl dazu https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression
df = df.drop(labels = df[df["Number of Sunspots"] == -1].index)



# Erstelle einen Neuen DataFrame. Man könnte das auch alles in einer Zeile machen, 
# Aber dann wird der Code sehr unleserlich, und wenn man den Code nach einer Weile
# nochmal anschaut, versteht man nicht mehr was da passiert.

# Man kann DataFrames auch nach Verketteten Boolschen Aussagen filtern (verknüpft 
# durch 'und' oder 'oder')
df_new = df.drop(labels = df[(df.Year < 1900) | (df.Year > 1999)].index)


# Man muss bei der Beizeichung der Variablen aufpassen, dass man variablen nicht 
# wie Python Built-Ins nennt. sum (anstatt summe), wäre zB ein Built-In
# selben gilt für lambda (das erkennst du auch immer daran, dass deine IDE
# die Variable anders einfärbt)

# Es gibt sehr viele Standardoperationen auf Dataframes schon implementiert in Pandas
# zb Max/Min/Mean/Std etc. Schau dir dazu mal die Docs an:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
summe = df_new["Number of Sunspots"].sum()
mean = df_new["Number of Sunspots"].mean()


# f-Strings sind ein eleganter Weg, Variablen in Strings einzubauen. Dabei
# gibt es viele Formatierungsmöglichkeiten. 
# vgl. dazu https://www.youtube.com/watch?v=BxUxX1Ku1EQ
print("Von 1.1.1900 - 31.12.1999 gab es insgesamt:")
print(f"Summe: {summe:_} Sonnenflecken")
print(f"im Mittel: {mean:.2f} Sonnenflecken pro Tag")


#%% 

# .cumsum() gibt eine pd.Series objekt zurück, also keinen Einzelnen Wert. Das 
# heißt, die y-Werte haben wir schon
cum_sum = df_new["Number of Sunspots"].cumsum()
number_of_days = list(range(len(cum_sum)))

# =============================================================================
# # Alternativer Code wäre dafür:
# number_of_days = []
# for i in range(len(cum_sum)):
#     number.append(i)
# 
# =============================================================================

fig = plt.Figure(figsize=(15, 10))
plt.plot(number_of_days, cum_sum, label="Messdaten")
plt.xlabel("Anzahl der Tage")
plt.ylabel("Kummulierte Summe der Sonnenflecken")
plt.yscale("log")
plt.title("Kummulierte Sonnenflecken")
plt.legend()










