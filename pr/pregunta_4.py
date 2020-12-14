#¿Cuáles son los 5 paı́ses que tienen más habitantes con obesidad y que además lo que más muertes
#tienen? Esta respuesta es distinta a la anterior, pues no necesariamente un paı́s que esté en el
#top5 de obesidad también tenga una mayor cantidad de muertes en cifras. Las cifras son en tipo
#entero, no porcentual.

import pandas as pd
import matplotlib.pyplot as plt


#Crea un Data Frame del archivo csv
def makeData():
    data = pd.read_csv('suministro_alimentos_kcal.csv')
    return data


def obesitypp(fila):
    perso = (fila["Obesity"]*fila["Population"])/100
    return perso


def deathpp(fila):
    death = (fila["Deaths"]*fila["Population"])/100
    return death


def main():
    df = makeData()
    df_salud_alim = df[["Country", "Obesity", "Population","Deaths"]]
    df_clean = df_salud_alim.fillna(0)
    df_clean["Obesitypp"] = df_clean.apply(obesitypp, axis = 1)
    df_clean["deathpp"] = df_clean.apply(deathpp, axis = 1)
    df_mayor = df_clean.sort_values("Obesitypp",ascending = False)
    df_mayor5_d= df_mayor
    df_mayor5_d.plot(x = "Country", y = "Obesitypp", rot = 0)
    df_mayor_o = df_mayor5_d.sort_values("deathpp",ascending = False)
    df_mayor5_o = df_mayor_o.head()
    df_mayor5_o.plot(x = "Country", y = "deathpp", rot = 0)
    print(df_mayor5_o)
    plt.show() 

if __name__ == '__main__':
    main()