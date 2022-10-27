import pandas as pd
import extract_functions
import transform_functions
import loading_functions
from logging_functions import log


targetfile = 'transformed_data.csv'
logfile = 'logfile.txt'

extracted_data = extract_functions.extract()
#print(extracted_data)

#print('---')

transformed_data = transform_functions.transform(extracted_data)
#print(transformed_data)

#print('---')

BMI = transform_functions.BMI_calculator(transformed_data)
print(BMI)

loading_functions.load(targetfile, transformed_data)
