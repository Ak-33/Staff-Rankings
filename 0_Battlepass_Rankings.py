
import streamlit as st 
Battlepass_data = 'pages\Battlepass_data.txt'
    
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
   #gets BP level
AK33level = 0
with open(AK33file, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            AK33level = field.split(':')[1].strip()                 

#mcfly---------------------------------------------------------------------------   
   #gets BP level
mcflylevel = 0
with open(mcflyfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            mcflylevel = field.split(':')[1].strip()                 

#vector-----------------------------------------------------------------------------
#BP level
vectorlevel = 0
with open(vectorfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            vectorlevel = field.split(':')[1].strip()                 

#lokey-----------------------------------------------------------------------------
#     #gets BP level
lokeylevel = 0
with open(lokeyfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            lokeylevel = field.split(':')[1].strip()                 

#LeFloor-----------------------------------------------------------------------------
#     #gets BP level
LeFloorlevel = 0
with open(LeFloorfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            LeFloorlevel = field.split(':')[1].strip()                 

#ghirradeil-----------------------------------------------------------------------------
#     #gets BP level
ghirradeillevel = 0
with open(ghirradeilfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            ghirradeillevel = field.split(':')[1].strip()                 

#phlash---------------------------------------------------------------------------     
   #gets BP level
phlashlevel = 0
with open(phlashfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            phlashlevel = field.split(':')[1].strip()                 

#ryptyde---------------------------------------------------------------------------    
   #gets BP level
ryptydelevel = 0
with open(ryptydefile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            ryptydelevel = field.split(':')[1].strip()                 

#sideKwinder---------------------------------------------------------------------------    
   #gets BP level
sideKwinderlevel = 0
with open(sideKwinderfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            sideKwinderlevel = field.split(':')[1].strip()                 

#Tandumm---------------------------------------------------------------------------    
   #gets BP level
Tandummlevel = 0
with open(Tandummfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            Tandummlevel = field.split(':')[1].strip()                 


#o3zone---------------------------------------------------------------------------    
   #gets BP level
o3zonelevel = 0
with open(o3zonefile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            o3zonelevel = field.split(':')[1].strip()                 


#keauxda--------------------------------------------------------------------------- 
   #gets BP level
keauxdalevel = 0
with open(keauxdafile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            keauxdalevel = field.split(':')[1].strip()                 

#mulligan---------------------------------------------------------------------------     
   #gets BP level
mulliganlevel = 0
with open(mulliganfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            mulliganlevel = field.split(':')[1].strip()                 


#saitama---------------------------------------------------------------------------     
   #gets BP level
saitamalevel = 0
with open(saitamafile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            saitamalevel = field.split(':')[1].strip()                 


#trubadoor---------------------------------------------------------------------------
   #gets BP level
trubadoorlevel = 0
with open(trubadoorfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            trubadoorlevel = field.split(':')[1].strip()                 


#romKulus---------------------------------------------------------------------------     
   #gets BP level
romKuluslevel = 0
with open(romKulusfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            romKuluslevel = field.split(':')[1].strip()                 


#can_nun---------------------------------------------------------------------------    
   #gets BP level
can_nunlevel = 0
with open(can_nunfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            can_nunlevel = field.split(':')[1].strip()                 


#Solo print stats-----------------------------------------------------------------------------------------

player_stats = {
    'AK33': {
       'Battlepass level':int(AK33level), 
    },
    
     'mcfly': {
       'Battlepass level':int(mcflylevel), 
       
    },
    
    'Vector': {
       'Battlepass level':int(vectorlevel), 
        
    },
    'lokey': {
       'Battlepass level':int(lokeylevel), 
    },
    
    'LeFloor': {
       'Battlepass level':int(LeFloorlevel), 
    },
    
     'ghirradeil': {
       'Battlepass level':int(ghirradeillevel), 
    },
     
     'phlash': {
       'Battlepass level':int(phlashlevel), 
    },
     
     'ryptyde': {
       'Battlepass level':int(ryptydelevel),
    },
     
     'sideKwinder': {
       'Battlepass level':int(sideKwinderlevel), 
       
    },
     
     'Tandumm': {
       'Battlepass level':int(Tandummlevel), 
       
    },
     
     'o3zone': {
       'Battlepass level':int(o3zonelevel), 
       
    },
     
    'keauxda': {
       'Battlepass level':int(keauxdalevel), 
       
    },
    'mulligan': {
       'Battlepass level':int(mulliganlevel), 
       
    },
   
    'saitama': {
       'Battlepass level':int(saitamalevel), 
       
    },
    'trubadoor': {
       'Battlepass level':int(trubadoorlevel), 
       
    },
    'romKulus': {
       'Battlepass level':int(romKuluslevel), 
             
    },
    'can_nun': {
       'Battlepass level':int(can_nunlevel),
       },

   }


# Define ranking function for kills in each category
def rank_players_by_category(category):
    category_stats = [(player, stats[category]) for player, stats in player_stats.items()]
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

# Generate rankings for each category
categories = ['Battlepass level',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_Battlepass_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat}\n"
    rankings_data[category] = category_rankings
    print_Battlepass_rankings.append(category_rankings)
 
with open(Battlepass_data, 'w') as f:
     f.write('\n'.join(print_Battlepass_rankings))

with open(Battlepass_data, "r") as file:
   Battlepass_data_content = file.read()
   
#website - 

st.set_page_config(page_title='Battlepass Rankings', layout= "centered")
st.title ('Battlepass Rankings')
st.write(Battlepass_data_content)   






