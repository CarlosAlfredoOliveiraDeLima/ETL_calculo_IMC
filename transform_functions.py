import pandas as pd


#Remover dados duplicados
def data_cleaning(data):
    return data.drop_duplicates(subset=['name', 'height', 'weight'], ignore_index=True)


def measurement_converter(data):
    data = data.copy() #Procedimento para evitar o erro de 'SettingWithCopyWarning', 
                       #neste caso, fazemos uma cópia do DF, as alterações não são feitas no objeto original, mas em um novo objeto independente.
    
    #Converter polegadas para milímetros com duas casas decimais
    data['height'] = round(data['height'] * 0.0254,2) 
    #data.loc[:,'height'] = round(data.loc[:,'height'] * 0.0254,2)
    #data.height = round(data.height * 0.0254,2)

    #Converter libras para quilogramas
    data['weight'] = round(data['weight'] * 0.45359237,2)
    #data.loc[:,'weight'] = round(data.loc[:,'weight'] * 0.45359237,2)
    #data.weight = round(data.weight * 0.45359237,2)

    return data


def BMI_calculator(data):
    #data['BMI'] = round((data.weight / (data.height ** data.height)), 2)
    data['BMI'] = round((data['weight'] / (data['height'] ** 2)), 2)
    return data


def transform(data):
    data = data_cleaning(data)
    data = measurement_converter(data)
    #data = BMI_calculator(data)
    return data