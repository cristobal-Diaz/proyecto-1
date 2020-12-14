#¿Cu ́ales son los 5 pa ́ıses que tienen m ́as habitantes con obesidad?
# esta pregunta no es una cifraporcentual, si no que real, por lo que se 
# debe realizar el calculo a partir de la columna poblacion(Population)
import pandas as pd
import matplotlib.pyplot as plt


#Crea un Data Frame del archivo csv
def makeData():
    data = pd.read_csv('suministro_alimentos_kcal.csv')
    return data


def obesitypp(fila):
    perso = (fila["Obesity"]*fila["Population"])/100
    return perso


def main():
    df = makeData()
    df_salud_alim = df[["Country", "Obesity", "Population"]]
    df_clean = df_salud_alim.fillna(0)
    df_clean["Obesitypp"] = df_clean.apply(obesitypp, axis = 1)
    df_mayor = df_clean.sort_values("Obesitypp",ascending=False)
    df_mayor5 = df_mayor.head()
    df_mayor5.plot.bar(x = "Country", y = "Obesitypp", rot = 0)
    print(df_mayor5)
    plt.show() 

if __name__ == '__main__':
    main()