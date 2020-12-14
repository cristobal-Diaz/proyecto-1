#¿Los paı́ses que tienen mayor consumo de alcohol son los paı́ses que más contagios confirmados
#tienen? graficar el top10 de paı́ses más consumo de alcohol tienen vs más contagios activos tienen(scatter plot)
import pandas as pd
import matplotlib.pyplot as plt


#Crea un Data Frame del archivo csv
def makeData():
    data = pd.read_csv('suministro_alimentos_kcal.csv')
    return data


def confirmedp(fila):
    perso = (fila["Confirmed"]*fila["Population"])/100
    return perso


def main():
    df = makeData()
    df_confirmados = df[["Country","Confirmed", "Population","Alcoholic Beverages"]]
    df_confirmados["confirmedp"] = df_confirmados.apply(confirmedp, axis = 1)
    df_confirmados_alcoholic = df_confirmados[df_confirmados["Alcoholic Beverages"] > 3.0]
    df_mayor = df_confirmados_alcoholic.sort_values("confirmedp",ascending = False)
    df_mayor10 = df_mayor.head(10)
    df_mayor10.plot.bar(x = "Country", y = "confirmedp", rot = 0)
    df_mayor10.plot.bar(x = "Country", y = "Alcoholic Beverages", rot = 0)
    print(df_mayor10)
    plt.show() 


if __name__ == "__main__":
    main()    