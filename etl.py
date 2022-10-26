from codecs import ignore_errors
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import extract_functions
import transform_functions

logfile = 'logfile.txt'
targetfile = 'transformed_data.csv'

extracted_data = extract_functions.extract()

transformed_data = transform_functions.transform(extracted_data)

print(transformed_data)
