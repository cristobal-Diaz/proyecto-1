#Según las cifras mundiales del COVID-19 (SARS-Cov-2), ¿El numero de muertos es mayor al número de recuperados?

import pandas as pd
import matplotlib.pyplot as plt


#Crea un Data Frame del archivo csv
def makeData():
    data = pd.read_csv('suministro_alimentos_kcal.csv')
    return data


def main():
    fullFile = makeData()

    
    #Creación del sub DataFrame
    data = fullFile[['Country',
                     'Confirmed',
                     'Deaths',
                     'Recovered',
                     'Active',
                     'Population']]


    worldPop = round(data['Population'].sum())
    worldRec = 0
    worldDed = 0
    worldCon = 0
    worldAct = 0


    #Conversiones de datos y cálculos de totales (La idea es conseguir una cifra mundial)
    for indice , fila in data.iterrows():
        deaths = fila['Deaths'] * fila['Population'] / 100
        recovered = fila['Recovered'] * fila['Population'] / 100
        confirmed = fila['Confirmed'] * fila['Population'] / 100
        active = fila['Active'] * fila['Population'] / 100

        if (deaths + 1) > 1: 
            worldDed = worldDed + round(deaths)

        if (recovered + 1) > 1:
            worldRec = worldRec + round(recovered)

        if (confirmed + 1) > 1:
            worldCon = worldCon + round(confirmed)

        if (active + 1) > 1:
            worldAct = worldAct + round(active)

        


    onePercent = worldCon / 100
    worldRec_percent = round((worldRec / onePercent), 3)
    worldDed_percent = round((worldDed / onePercent), 3)
    worldAct_percent = round((worldAct / onePercent), 3)
    other = worldCon - (worldDed + worldRec + worldAct)
    other_percent = round((100 - (worldRec_percent + worldDed_percent + worldAct_percent)) , 3)


    #porcentajes de muertos, recuperados, activos, recuperados y sanos.
    muertosporc = (worldDed * 100) / worldPop
    recuperadosporc = (worldRec * 100) / worldPop
    confirmadosporc = (worldCon * 100) / worldPop
    activosporc = (worldAct * 100) / worldPop
    sanosporc = 100 - (muertosporc - recuperadosporc - confirmadosporc - activosporc)
    casos = ("muertos", "recuperados", "confirmados", "activos", "sanos")
    porc = (muertosporc, recuperadosporc, confirmadosporc, activosporc, sanosporc)
    plt.pie(porc, labels = casos)


    #Los espacios son así de largos para que al momento de imprimir los valores estén alineados y sea más fácil comparar
    print('Población:   ', worldPop)
    print('Confirmados:   ', worldCon)
    print('Recuperados:   ', worldRec, worldRec_percent, '%')
    print('Muertos:        ', worldDed,'', worldDed_percent, '%')
    print('Activos:        ', worldAct, worldAct_percent, '%')
    print('Otros:          ', other, other_percent, '%',)
    print('')
    plt.show()


    #Comprobación de la Hipotesis
    if worldRec_percent > worldDed_percent:
        print('Según las cifras, hay más recuperados que muertos por ', end='')
        print('COVID-19 (SARS-CoV-2)\nLa hipotesis se confirma')
    else:
        print('Según las cifras, hay más muertos que recuperados por ', end='')
        print('COVID-19 (SARS-CoV-2).\nLa hipotesis se descarta')


if __name__ == "__main__":
    main()    