import pandas as pd


def data_cleaning(data):
    return data.drop_duplicates(subset=['name', 'height', 'weight'], keep='last')
