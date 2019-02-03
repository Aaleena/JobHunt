
#imports
from models import Road
from bs4 import BeautifulSoup
import pandas as pd
import requests

settings.configure()
url='http://camden.gov.uk/ccm/navigation/transport-and-streets/parking/parking-bay-suspensions/search-for-parking-bay-suspensions/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc,"html.parser")
table = soup.find('table')
rows = table.find_all('tr')
pd.set_option('display.max_colwidth', -1)
df = pd.read_html(str(table))[0]
df['href'] = [tag['href'] for tag in table.find_all('a')]

#Delete objects in Django 
Road.objects.all().delete()

for zone_index, zone_row in df.iterrows():
    print(zone_row[0],zone_row[1],zone_row[2])
    url=zone_row[2]
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc,"html.parser")
    table = soup.find('table')
    df2 = pd.read_html(str(table),header=0)[0]
    df2['href'] = [tag['href'] for tag in table.find_all('a')]
    road_list = [[zone_row[0],zone_row[1],road_row[0],'Camden','http://registers.camden.gov.uk/SuspendedBays/'+road_row['href'].replace(' ','%20')] 
                 for road_index,road_row in df2.iterrows() if pd.notnull(road_row[1]) == False ]
    road_df = pd.DataFrame(road_list,columns=['zone_code','zone','road','borough','suspension_href'])
    Roads = road_df.to_dict('roads')
    model_instances = [Road(
        road=record['road'],
        zone_code=record['zone_code'],
        borough=record['borough'],
        zone=record['zone'],
        suspension_href=record['suspension_href'],
        
        
    ) for record in Roads]
   
    Road.objects.bulk_create(model_instances)
    
