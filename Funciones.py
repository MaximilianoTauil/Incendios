import pandas as pd 

def analizar_datos(df):
    


    resumen_dict = {"Nombre": [], "Tipos de Datos Únicos": [], "% de Valores No Nulos": [], "% de Valores Nulos": [], "Cantidad de Valores Nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        resumen_dict["Nombre"].append(columna)
        resumen_dict["Tipos de Datos Únicos"].append(df[columna].apply(type).unique())
        resumen_dict["% de Valores No Nulos"].append(round(porcentaje_no_nulos, 2))
        resumen_dict["% de Valores Nulos"].append(round(100 - porcentaje_no_nulos, 2))
        resumen_dict["Cantidad de Valores Nulos"].append(df[columna].isnull().sum())

    resumen_dataframe = pd.DataFrame(resumen_dict)
        
    return resumen_dataframe

def cambiar_tipo(dataframe,columna,tipo):
    try:
        dataframe[columna] = dataframe[columna].astype(tipo)
        print(f"El tipo de dato de la columna '{columna}' se cambió correctamente a {tipo}.\n")
    except ValueError:
        print(f"Error: No se pudo cambiar el tipo de dato de la columna '{columna}'. Verifica que los datos sean compatibles con el tipo {tipo}.\n")
    except KeyError:
        print(f"Error: La columna '{columna}' no existe en el dataframe.\n")
    except Exception as e:
        print(f"Error inesperado: {e}\n")

def cantidad_porcentaje(dataframe, columna):
    
    cantidad = dataframe.shape[0]
    cantidad_columna = dataframe[columna].value_counts(dropna=False)
    porcentaje_columna = round((cantidad_columna / cantidad) * 100, 2)
    
    print(f'Los valores de {columna}:\n{cantidad_columna.to_string(header=False)}')
    print(f'\nEl porcentaje que representa cada valor:\n{porcentaje_columna.to_string(header=False)}')

def cantidad_porcentaje_sum(dataframe, columna_valores,columna_referencia):
    
    df_copy = dataframe.copy()

    suma = df_copy[columna_valores].sum()

    porcentaje_columna = round((df_copy[columna_valores]/ suma) * 100, 2)

    df_copy['Porcentaje'] = porcentaje_columna
    
    print(f'El valor total de la columna {columna_valores} es:\n\n{suma}')
    
    print(f'\nEl porcentaje que representa cada valor es:\n\n{df_copy[[columna_referencia,'Porcentaje']]}')

def tasas_año(dataframe,columna_valores,escala_multiplicacion):
    total = dataframe[columna_valores].sum()
    dataframe['Tasa'] = round((dataframe[columna_valores] / total)*escala_multiplicacion,2)
    dataframe['Tasa_anterior'] = dataframe['Tasa'].shift(periods=1,fill_value=0)
    dataframe['Diferencia'] = round(dataframe['Tasa'] - dataframe['Tasa_anterior'],2)
    dataframe.loc[dataframe.index[0], 'Diferencia'] = 0
    dataframe