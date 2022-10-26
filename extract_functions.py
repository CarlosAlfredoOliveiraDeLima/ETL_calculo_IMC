import pandas as pd
import xml.etree.ElementTree as ET
import glob


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        data_dict = {"name":[name], "height":[height], "weight":[weight]} #PRECISA ESTAR EM COLCHETES!!!
        DataFrameFromDict = pd.DataFrame(data_dict)
        #dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
        dataframe = pd.concat([dataframe, DataFrameFromDict], ignore_index=True)
        #print(dataframe)
        #print('----')
    return dataframe


def extract():
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"])

    #Processo para os arquivos CSV
    for cvsfile in glob.glob("sources/*csv"):
        #extracted_data = extracted_data.append(extract_from_csv(cvsfile), ignore_index=True)
        extracted_data = pd.concat([extracted_data, extract_from_csv(cvsfile)], ignore_index=True)
        #print("CSV", extracted_data)
    
    #Processo para os arquivos JSON
    for jsonfile in glob.glob("sources/*.json"):
        #extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
        extracted_data = pd.concat([extracted_data, extract_from_json(jsonfile)], ignore_index=True)
        #print("JSON", extracted_data)
    
    #Processo para os arquivos XML
    for xmlfile in glob.glob("sources/*.xml"):
        #extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        extracted_data = pd.concat([extracted_data, extract_from_xml(xmlfile)], ignore_index=True)
        #print("XML", extracted_data)
    
    return extracted_data