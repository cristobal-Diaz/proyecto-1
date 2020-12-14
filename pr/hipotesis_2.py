#Comparacion en los indices de obesidad entre LATAM - EEUU
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
    df_latam = df_clean.iloc[[5,17,20,29,31,33,36,43,45,60,65,100,111,118,119,120,42,162,165,161]]
    #los numeros corresponden a los paises de Latino America y Ustados Unidos
    df_latam["Obesitypp"] = df_latam.apply(obesitypp, axis = 1)
    df_latam.plot.bar(x = "Country", y = "Obesitypp", rot = 0)
    print("\n\n\nA la hora de comparar estos datos, la diferencia entre latino america y estados unidos es muy grande,")
    print("hasta el punto que ningun pais de latinoamerica puede hacer la mitad de las cifras de estados unidos\n")
    print(df_latam)
    plt.show() 


if __name__ == '__main__':
    main()
    