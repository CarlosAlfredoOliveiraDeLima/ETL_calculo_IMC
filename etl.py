import pandas as pd
import extract_functions
import transform_functions
import loading_functions
from logging_functions import log


targetfile = 'transformed_data.csv'
logfile = 'logfile.txt'

log('ETL iniciado')
print('ETL iniciado')

log('Fase de extração dos dados iniciada')
print('Fase de extração dos dados iniciada')
extracted_data = extract_functions.extract()
print(extracted_data)
log('Fase de extração de dados finalizada')
print('Fase de extração de dados finalizada')

log('Fase de transformação de dados iniciada')
print('Fase de transformação de dados iniciada')
transformed_data = transform_functions.transform(extracted_data)
print(transformed_data)
log('Fase de transformação de dados finalizada')
print('Fase de transformação de dados finalizada')

log('Fase de carregamento e persistência de dados iniciada')
print('Fase de carregamento e persistência de dados iniciada')
loading_functions.load(targetfile, transformed_data)
log('Fase de carregamento e persistência de dados finalizada')
print('Fase de carregamento e persistência de dados finalizada')

log('Processo de ETL finalizado')
print('Processo de ETL finalizado')