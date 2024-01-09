
import streamlit as st 
Solo_data = 'pages\solo_data.txt'
    
    #files_names
        #Pixsol----------------
AK33file ='pages/pixsol/AK33_stats.txt'
AK33solo='pages/pixsol/AK33-solo.txt'
AK33duo='pages/pixsol/AK33-duo.txt'
AK33squad='pages/pixsol/AK33-squad.txt'
        #vector----------------
vectorfile ='pages/vector/vector_stats.txt'
vectorsolo='pages/vector/vector-solo.txt'
vectorduo='pages/vector/vector-duo.txt'
vectorsquad='pages/vector/vector-squad.txt'
        #lo-key----------------
lokeyfile ='pages/lokey/lokey_stats.txt'
lokeysolo='pages/lokey/lokey-solo.txt'
lokeyduo='pages/lokey/lokey-duo.txt'
lokeysquad='pages/lokey/lokey-squad.txt'
        #LeFloor---------------
LeFloorfile ='pages/LeFloor/LeFloor_stats.txt'
LeFloorsolo='pages/LeFloor/LeFloor-solo.txt'
LeFloorduo='pages/LeFloor/LeFloor-duo.txt'
LeFloorsquad='pages/LeFloor/LeFloor-squad.txt'
        #ghirradeil----------------
ghirradeilfile ='pages/ghirradeil/ghirradeil_stats.txt'
ghirradeilsolo='pages/ghirradeil/ghirradeil-solo.txt'
ghirradeilduo='pages/ghirradeil/ghirradeil-duo.txt'
ghirradeilsquad='pages/ghirradeil/ghirradeil-squad.txt'
        #phlash----------------
phlashfile ='pages/phlash/phlash.txt'
phlashsolo='pages/phlash/phlash-solo.txt'
phlashduo='pages/phlash/phlash-duo.txt'
phlashsquad='pages/phlash/phlash-squad.txt'
    #ryptyde----------------
ryptydefile ='pages/ryptyde/ryptyde_stats.txt'
ryptydesolo='pages/ryptyde/ryptyde-solo.txt'
ryptydeduo='pages/ryptyde/ryptyde-duo.txt'
ryptydesquad='pages/ryptyde/ryptyde-squad.txt'
    #sideKwinder----------------
sideKwinderfile ='pages/sideKwinder/sideKwinder_stats.txt'
sideKwindersolo='pages/sideKwinder/sideKwinder-solo.txt'
sideKwinderduo='pages/sideKwinder/sideKwinder-duo.txt'
sideKwindersquad='pages/sideKwinder/sideKwinder-squad.txt'
    #Tandumm----------------
Tandummfile ='pages/Tandumm/Tandumm_stats.txt'
Tandummsolo='pages/Tandumm/Tandumm-solo.txt'
Tandummduo='pages/Tandumm/Tandumm-duo.txt'
Tandummsquad='pages/Tandumm/Tandumm-squad.txt'
    #o3zone----------------
o3zonefile ='pages/o3zone/o3zone_stats.txt'
o3zonesolo='pages/o3zone/o3zone-solo.txt'
o3zoneduo='pages/o3zone/o3zone-duo.txt'
o3zonesquad='pages/o3zone/o3zone-squad.txt'
    #keauxda----------------
keauxdafile ='pages/keauxda/keauxda_stats.txt'
keauxdasolo='pages/keauxda/keauxda-solo.txt'
keauxdaduo='pages/keauxda/keauxda-duo.txt'
keauxdasquad='pages/keauxda/keauxda-squad.txt'
    #mulligan----------------
mulliganfile ='pages/mulligan/mulligan_stats.txt'
mulligansolo='pages/mulligan/mulligan-solo.txt'
mulliganduo='pages/mulligan/mulligan-duo.txt'
mulligansquad='pages/mulligan/mulligan-squad.txt'
    #mcfly----------------
mcflyfile ='pages/mcfly/mcfly_stats.txt'
mcflysolo='pages/mcfly/mcfly-solo.txt'
mcflyduo='pages/mcfly/mcfly-duo.txt'
mcflysquad='pages/mcfly/mcfly-squad.txt'
    #saitama----------------
saitamafile ='pages/saitama/saitama_stats.txt'
saitamasolo='pages/saitama/saitama-solo.txt'
saitamaduo='pages/saitama/saitama-duo.txt'
saitamasquad='pages/saitama/saitama-squad.txt'
    #trubadoor----------------
trubadoorfile ='pages/trubadoor/trubadoor_stats.txt'
trubadoorsolo='pages/trubadoor/trubadoor-solo.txt'
trubadoorduo='pages/trubadoor/trubadoor-duo.txt'
trubadoorsquad='pages/trubadoor/trubadoor-squad.txt'
    #romKulus----------------
romKulusfile ='pages/romKulus/romKulus_stats.txt'
romKulussolo='pages/romKulus/romKulus-solo.txt'
romKulusduo='pages/romKulus/romKulus-duo.txt'
romKulussquad='pages/romKulus/romKulus-squad.txt'
    #can_nun----------------
can_nunfile ='pages/can_nun/can_nun_stats.txt'
can_nunsolo='pages/can_nun/can_nun-solo.txt'
can_nunduo='pages/can_nun/can_nun-duo.txt'
can_nunsquad='pages/can_nun/can_nun-squad.txt'




#Pixsol---------------------------------------------------------------------------    
  #solo stats
AK33solowins = 0
AK33solokills = 0
AK33solotop10 = 0
with open(AK33solo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            AK33solowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            AK33solokills = field.split(':')[1].strip()
        
        if "top10" in field:
            AK33solotop10 = field.split(':')[1].strip()   
        

#mcfly---------------------------------------------------------------------------   
#     #solo stats
mcflysolowins = 0
mcflysolokills = 0
mcflysolotop10 = 0
with open(mcflysolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            mcflysolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            mcflysolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            mcflysolotop10 = field.split(':')[1].strip()   
              
#vector-----------------------------------------------------------------------------
#     #solo stats
vectorsolowins = 0
vectorsolokills = 0
vectorsolotop10 = 0
with open(vectorsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            vectorsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            vectorsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            vectorsolotop10 = field.split(':')[1].strip()   

#lokey-----------------------------------------------------------------------------
#solo stats
lokeysolowins = 0
lokeysolokills = 0
lokeysolotop10 = 0
with open(lokeysolo, 'r') as file:
    content = file.read()
    fields = content.split(',')

    for field in fields:
        if "wins" in field: 
            lokeysolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            lokeysolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            lokeysolotop10 = field.split(':')[1].strip()   

#LeFloor-----------------------------------------------------------------------------
#     #solo stats
LeFloorsolowins = 0
LeFloorsolokills = 0
LeFloorsolotop10 = 0
with open(LeFloorsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')

    for field in fields:
        if "wins" in field: 
            LeFloorsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            LeFloorsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            LeFloorsolotop10 = field.split(':')[1].strip()   

#ghirradeil-----------------------------------------------------------------------------
#     #solo stats
ghirradeilsolowins = 0
ghirradeilsolokills = 0
ghirradeilsolotop10 = 0
with open(ghirradeilsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')

    for field in fields:
        if "wins" in field: 
            ghirradeilsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            ghirradeilsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            ghirradeilsolotop10 = field.split(':')[1].strip()   
            
#phlash---------------------------------------------------------------------------     
#solo stats
phlashsolowins = 0
phlashsolokills = 0
phlashsolotop10 = 0
with open(phlashsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            phlashsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            phlashsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            phlashsolotop10 = field.split(':')[1].strip()   
   
#ryptyde---------------------------------------------------------------------------    
#     #solo stats
ryptydesolowins = 0
ryptydesolokills = 0
ryptydesolotop10 = 0
with open(ryptydesolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            ryptydesolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            ryptydesolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            ryptydesolotop10 = field.split(':')[1].strip()   

#sideKwinder---------------------------------------------------------------------------    
    #solo stats
sideKwindersolowins = 0
sideKwindersolokills = 0
sideKwindersolotop10 = 0
with open(sideKwindersolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            sideKwindersolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            sideKwindersolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            sideKwindersolotop10 = field.split(':')[1].strip()   

#Tandumm---------------------------------------------------------------------------    
#solo stats
Tandummsolowins = 0
Tandummsolokills = 0
Tandummsolotop10 = 0
with open(Tandummsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            Tandummsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            Tandummsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            Tandummsolotop10 = field.split(':')[1].strip()   

#o3zone---------------------------------------------------------------------------    
#     #solo stats
o3zonesolowins = 0
o3zonesolokills = 0
o3zonesolotop10 = 0
with open(o3zonesolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            o3zonesolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            o3zonesolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            o3zonesolotop10 = field.split(':')[1].strip()   

#keauxda--------------------------------------------------------------------------- 

#     #solo stats
keauxdasolowins = 0
keauxdasolokills = 0
keauxdasolotop10 = 0
with open(keauxdasolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            keauxdasolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            keauxdasolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            keauxdasolotop10 = field.split(':')[1].strip()   

#mulligan---------------------------------------------------------------------------     
 #     #solo stats
mulligansolowins = 0
mulligansolokills = 0
mulligansolotop10 = 0
with open(mulligansolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            mulligansolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            mulligansolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            mulligansolotop10 = field.split(':')[1].strip()   

#saitama---------------------------------------------------------------------------     
#solo stats
saitamasolowins = 0
saitamasolokills = 0
saitamasolotop10 = 0
with open(saitamasolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            saitamasolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            saitamasolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            saitamasolotop10 = field.split(':')[1].strip()   

#trubadoor---------------------------------------------------------------------------
#     #solo stats
trubadoorsolowins = 0
trubadoorsolokills = 0
trubadoorsolotop10 = 0
with open(trubadoorsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            trubadoorsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            trubadoorsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            trubadoorsolotop10 = field.split(':')[1].strip()   

#romKulus---------------------------------------------------------------------------     
#     #solo stats
romKulussolowins = 0
romKulussolokills = 0
romKulussolotop10 = 0
with open(romKulussolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            romKulussolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            romKulussolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            romKulussolotop10 = field.split(':')[1].strip()   

#can_nun---------------------------------------------------------------------------    
#     #solo stats
can_nunsolowins = 0
can_nunsolokills = 0
can_nunsolotop10 = 0
with open(can_nunsolo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            can_nunsolowins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            can_nunsolokills = field.split(':')[1].strip()
        
        if "top10" in field:
            can_nunsolotop10 = field.split(':')[1].strip()   

#Solo print stats-----------------------------------------------------------------------------------------

player_stats = {
    'AK33': {
        'Solo kills': int(AK33solokills), 'Solo Wins': int(AK33solowins), 'Solo Finished top 10': int(AK33solotop10)
              
    },
    
     'mcfly': {
        'Solo kills': int(mcflysolokills), 'Solo Wins': int(mcflysolowins), 'Solo Finished top 10': int(mcflysolotop10)
       
    },
    
    'Vector': {
        'Solo kills': int(vectorsolokills),  'Solo Wins': int(vectorsolowins), 'Solo Finished top 10': int(vectorsolotop10)
        
    },
    'lokey': {
        'Solo kills': int(lokeysolokills),  'Solo Wins': int(lokeysolowins), 'Solo Finished top 10': int(lokeysolotop10)
    },
    
    'LeFloor': {
       'Solo kills': int(LeFloorsolokills),  'Solo Wins': int(LeFloorsolowins), 'Solo Finished top 10': int(LeFloorsolotop10)
    },
    
     'ghirradeil': {
        'Solo kills': int(ghirradeilsolokills),  'Solo Wins': int(ghirradeilsolowins), 'Solo Finished top 10': int(ghirradeilsolotop10)
    },
     
     'phlash': {
        'Solo kills': int(phlashsolokills),  'Solo Wins': int(phlashsolowins), 'Solo Finished top 10': int(phlashsolotop10)
    },
     
     'ryptyde': {
        'Solo kills': int(ryptydesolokills),  'Solo Wins': int(ryptydesolowins), 'Solo Finished top 10': int(ryptydesolotop10)
    },
     
     'sideKwinder': {
        'Solo kills': int(sideKwindersolokills), 'Solo Wins': int(sideKwindersolowins), 'Solo Finished top 10': int(sideKwindersolotop10)
       
    },
     
     'Tandumm': {
        'Solo kills': int(Tandummsolokills), 'Solo Wins': int(Tandummsolowins), 'Solo Finished top 10': int(Tandummsolotop10)
       
    },
     
     'o3zone': {
       'Solo kills': int(o3zonesolokills), 'Solo Wins': int(o3zonesolowins), 'Solo Finished top 10': int(o3zonesolotop10)
       
    },
     
    'keauxda': {
     'Solo kills': int(keauxdasolokills), 'Solo Wins': int(keauxdasolowins), 'Solo Finished top 10': int(keauxdasolotop10)
       
    },
    'mulligan': {
       'Solo kills': int(mulligansolokills), 'Solo Wins': int(mulligansolowins), 'Solo Finished top 10': int(mulligansolotop10)
       
    },
   
    'saitama': {
        'Solo kills': int(saitamasolokills), 'Solo Wins': int(saitamasolowins), 'Solo Finished top 10': int(saitamasolotop10)
       
    },
    'trubadoor': {
        'Solo kills': int(trubadoorsolokills), 'Solo Wins': int(trubadoorsolowins), 'Solo Finished top 10': int(trubadoorsolotop10)
       
    },
    'romKulus': {
        'Solo kills': int(romKulussolokills), 'Solo Wins': int(romKulussolowins), 'Solo Finished top 10': int(romKulussolotop10)
             
    },
    'can_nun': {
      'Solo kills': int(can_nunsolokills), 'Solo Wins': int(can_nunsolowins), 'Solo Finished top 10': int(can_nunsolotop10)
       },

   }


# Define ranking function for kills in each category
def rank_players_by_category(category):
    category_stats = [(player, stats[category]) for player, stats in player_stats.items()]
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

# Generate rankings for each category
categories = ['Solo kills', 'Solo Wins', 'Solo Finished top 10',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_solo_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat}\n"
    rankings_data[category] = category_rankings
    print_solo_rankings.append(category_rankings)
 
with open(Solo_data, 'w') as f:
     f.write('\n'.join(print_solo_rankings))

with open(Solo_data, "r") as file:
    Solo_data_content = file.read()
   
#website - 

st.set_page_config(page_title='Solo Rankings', layout= "centered")
st.title ('Solo Rankings')
st.write(Solo_data_content)   






