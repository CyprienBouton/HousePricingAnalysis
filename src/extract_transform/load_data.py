import pandas as pd

def load_data(year):
   """
   Load data corresponding to a given year
   """
   # rename columns with english name
   col_names = ['id_mutation', 'Transaction date', 'numero_disposition', 'Transaction type',
      'Transaction cost', 'adresse_numero', 'adresse_suffixe',
      'adresse_nom_voie', 'adresse_code_voie', 'Postcode', 'code_commune',
      'Town', 'Department', 'ancien_code_commune',
      'ancien_nom_commune', 'id_parcelle', 'ancien_id_parcelle',
      'numero_volume', 'lot1_numero', 'lot1_surface_carrez', 'lot2_numero',
      'lot2_surface_carrez', 'lot3_numero', 'lot3_surface_carrez',
      'lot4_numero', 'lot4_surface_carrez', 'lot5_numero',
      'lot5_surface_carrez', 'nombre_lots', 'code_type_local', 'Type of property',
      'Built surface', 'Number of rooms',
      'code_nature_culture', 'nature_culture', 'code_nature_culture_speciale',
      'nature_culture_speciale', 'Ground surface', 'Longitude', 'Latitude']

   # keep the most relevant cols
   col2use = ['Transaction cost', 'Transaction date', 'Transaction type', 'Type of property',
    'Built surface', 'Number of rooms', 'Ground surface', 'Longitude',
      'Latitude', 'Town']
   typecols = {'Transaction cost':float,
      'Transaction type':str,                
      'Built surface':float,
      'Number of rooms':float,
      'Ground surface':float,
      'Longitude':float,
      'Latitude':float,
      'Town':str}
   return pd.read_csv('dset/full_'+str(year)+".csv.gz", header=0,
     names=col_names, usecols=col2use, dtype=typecols, compression='gzip')
     