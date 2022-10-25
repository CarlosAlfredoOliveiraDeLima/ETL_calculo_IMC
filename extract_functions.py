import pandas as pd
import xml.etree.ElementTree as ET
import glob


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['name', 'height', 'weight'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find('name').text
        height = float(person.find('height').text)
        weight = float(person.find('weight').text)
        dataframe = dataframe.concat({'name':name, 'height':height, 'weight':weight}, ignore_index=True)
    
    return dataframe


def extract():
    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

    #Processo para os arquivos CSV
    for cvsfile in glob.glob("sources/*csv"):
        extracted_data = extracted_data.concat(extract_from_csv(cvsfile), ignore_index=True)
    
    #Processo para os arquivos JSON
    for jsonfile in glob.glob("sources/*.json"):
        extracted_data = extracted_data.concat(extract_from_json(jsonfile), ignore_index=True)
    
    #Processo para os arquivos XML
    for xmlfile in glob.glob("sources/*.xml"):
        extracted_data = extracted_data.concat(extract_from_xml(xmlfile), ignore_index=True)