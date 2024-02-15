import streamlit as st 
   
Squad_data = 'pages\squad_data.txt'   

 #files_names
        #Pixsol----------------
AK33squad='pages/pixsol/AK33-squad.txt'
        #vector----------------
vectorsquad='pages/vector/vector-squad.txt'
        #lo-key----------------
lokeysquad='pages/lokey/lokey-squad.txt'
        #LeFloor---------------
LeFloorsquad='pages/LeFloor/LeFloor-squad.txt'
        #ghirradeil----------------
ghirradeilsquad='pages/ghirradeil/ghirradeil-squad.txt'
        #phlash----------------
phlashsquad='pages/phlash/phlash-squad.txt'
    #ryptyde----------------
ryptydesquad='pages/ryptyde/ryptyde-squad.txt'
    #sideKwinder----------------
sideKwindersquad='pages/sideKwinder/sideKwinder-squad.txt'
    #Tandumm----------------
Tandummsquad='pages/Tandumm/Tandumm-squad.txt'
    #o3zone----------------
o3zonesquad='pages/o3zone/o3zone-squad.txt'
    #keauxda----------------
keauxdasquad='pages/keauxda/keauxda-squad.txt'
    #mulligan----------------
mulligansquad='pages/mulligan/mulligan-squad.txt'
    #mcfly----------------
mcflysquad='pages/mcfly/mcfly-squad.txt'
    #saitama----------------
saitamasquad='pages/saitama/saitama-squad.txt'
    #trubadoor----------------
trubadoorsquad='pages/trubadoor/trubadoor-squad.txt'
    #romKulus----------------
romKulussquad='pages/romKulus/romKulus-squad.txt'
    #can_nun----------------
can_nunsquad='pages/can_nun/can_nun-squad.txt'
    #apolllo----------------
apolllosquad='pages/apolllo/apolllo-squad.txt'
    #jaknkife----------------
jaknkifesquad='pages/jaknkife/jaknkife-squad.txt'


#Pixsol---------------------------------------------------------------------------
#squadssquads stats
AK33squadwins = 0
AK33squadkills = 0
AK33squadtop3 = 0
with open(AK33squad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            AK33squadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           AK33squadkills = field.split(':')[1].strip()
        if "top3" in field:
            AK33squadtop3 = field.split(':')[1].strip() 
                        
#vector-----------------------------------------------------------------------------
#squads stats
vectorsquadwins = 0
vectorsquadkills = 0
vectorsquadtop3 = 0
with open(vectorsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            vectorsquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           vectorsquadkills = field.split(':')[1].strip()
        if "top3" in field:
            vectorsquadtop3 = field.split(':')[1].strip()             
   
#lokey-----------------------------------------------------------------------------

#squad stats
lokeysquadwins = 0
lokeysquadkills = 0
lokeysquadtop3 = 0
with open(lokeysquad, 'r') as file:
    content = file.read()
    fields = content.split(',')

    for field in fields:
        if "wins" in field: 
            lokeysquadwins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            lokeysquadkills = field.split(':')[1].strip()
        
        if "top3" in field:
            lokeysquadtop3 = field.split(':')[1].strip()   

#LeFloor-----------------------------------------------------------------------------

#squad stats
LeFloorsquadwins = 0
LeFloorsquadkills = 0
LeFloorsquadtop3 = 0
with open(LeFloorsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')

    for field in fields:
        if "wins" in field: 
            LeFloorsquadwins = field.split(':')[1].strip()
        
        if 'totalk' in field:
            LeFloorsquadkills = field.split(':')[1].strip()
        
        if "top3" in field:
            LeFloorsquadtop3 = field.split(':')[1].strip()   

       
#ghirradeil-----------------------------------------------------------------------------

#squads stats
ghirradeilsquadwins = 0
ghirradeilsquadkills = 0
ghirradeilsquadtop3 = 0
with open(ghirradeilsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            ghirradeilsquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           ghirradeilsquadkills = field.split(':')[1].strip()
        if "top3" in field:
            ghirradeilsquadtop3 = field.split(':')[1].strip()             

#phlash---------------------------------------------------------------------------

 #squads stats
phlashsquadwins = 0
phlashsquadkills = 0
phlashsquadtop3 = 0
with open(phlashsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            phlashsquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           phlashsquadkills = field.split(':')[1].strip()
        if "top3" in field:
            phlashsquadtop3 = field.split(':')[1].strip()             

#ryptyde---------------------------------------------------------------------------

 #squads stats
ryptydesquadwins = 0
ryptydesquadkills = 0
ryptydesquadtop3 = 0
with open(ryptydesquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            ryptydesquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           ryptydesquadkills = field.split(':')[1].strip()
        if "top3" in field:
            ryptydesquadtop3 = field.split(':')[1].strip()             



#sideKwinder---------------------------------------------------------------------------

#squads stats
sideKwindersquadwins = 0
sideKwindersquadkills = 0
sideKwindersquadtop3 = 0
with open(sideKwindersquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            sideKwindersquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           sideKwindersquadkills = field.split(':')[1].strip()
        if "top3" in field:
            sideKwindersquadtop3 = field.split(':')[1].strip()             

#Tandumm---------------------------------------------------------------------------

#squads stats
Tandummsquadwins = 0
Tandummsquadkills = 0
Tandummsquadtop3 = 0
with open(Tandummsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            Tandummsquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           Tandummsquadkills = field.split(':')[1].strip()
        if "top3" in field:
            Tandummsquadtop3 = field.split(':')[1].strip()             

#o3zone---------------------------------------------------------------------------

#squads stats
o3zonesquadwins = 0
o3zonesquadkills = 0
o3zonesquadtop3 = 0
with open(o3zonesquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            o3zonesquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           o3zonesquadkills = field.split(':')[1].strip()
        if "top3" in field:
            o3zonesquadtop3 = field.split(':')[1].strip()             

#keauxda---------------------------------------------------------------------------

#squads stats
keauxdasquadwins = 0
keauxdasquadkills = 0
keauxdasquadtop3 = 0
with open(keauxdasquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            keauxdasquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           keauxdasquadkills = field.split(':')[1].strip()
        if "top3" in field:
            keauxdasquadtop3 = field.split(':')[1].strip()             

#mulligan---------------------------------------------------------------------------
 #squads stats
mulligansquadwins = 0
mulligansquadkills = 0
mulligansquadtop3 = 0
with open(mulligansquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            mulligansquaddwins = field.split(':')[1].strip()
        if 'totalk' in field:
           mulligansquadkills = field.split(':')[1].strip()
        if "top3" in field:
            mulligansquadtop3 = field.split(':')[1].strip()             

#mcfly---------------------------------------------------------------------------
 #squads stats
mcflysquadwins = 0
mcflysquadkills = 0
mcflysquadtop3 = 0
with open(mcflysquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            mcflysquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           mcflysquadkills = field.split(':')[1].strip()
        if "top3" in field:
            mcflysquadtop3 = field.split(':')[1].strip()
            
#saitama---------------------------------------------------------------------------

#squads stats
saitamasquadwins = 0
saitamasquadkills = 0
saitamasquadtop3 = 0
with open(saitamasquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            saitamasquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           saitamasquadkills = field.split(':')[1].strip()
        if "top3" in field:
            saitamasquadtop3 = field.split(':')[1].strip() 

#trubadoor---------------------------------------------------------------------------

 #squads stats
trubadoorsquadwins = 0
trubadoorsquadkills = 0
trubadoorsquadtop3 = 0
with open(trubadoorsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            trubadoorsquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           trubadoorsquadkills = field.split(':')[1].strip()
        if "top3" in field:
            trubadoorsquadtop3 = field.split(':')[1].strip()

#romKulus---------------------------------------------------------------------------
 #squads stats
romKulussquadwins = 0
romKulussquadkills = 0
romKulussquadtop3 = 0
with open(romKulussquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            romKulussquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           romKulussquadkills = field.split(':')[1].strip()
        if "top3" in field:
            romKulussquadtop3 = field.split(':')[1].strip()          

#can_nun---------------------------------------------------------------------------
 #squads stats
can_nunsquadwins = 0
can_nunsquadkills = 0
can_nunsquadtop3 = 0
with open(can_nunsquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            can_nunsquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           can_nunsquadkills = field.split(':')[1].strip()
        if "top3" in field:
            can_nunsquadtop3 = field.split(':')[1].strip()     
            
#apolllo---------------------------------------------------------------------------

 #squads stats
apolllosquadwins = 0
apolllosquadkills = 0
apolllosquadtop3 = 0
with open(apolllosquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            apolllosquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           apolllosquadkills = field.split(':')[1].strip()
        if "top3" in field:
            apolllosquadtop3 = field.split(':')[1].strip()
            
#jaknkife---------------------------------------------------------------------------

 #squads stats
jaknkifesquadwins = 0
jaknkifesquadkills = 0
jaknkifesquadtop3 = 0
with open(jaknkifesquad, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            jaknkifesquadwins = field.split(':')[1].strip()
        if 'totalk' in field:
           jaknkifesquadkills = field.split(':')[1].strip()
        if "top3" in field:
            jaknkifesquadtop3 = field.split(':')[1].strip()            
                                         

#Squad print stats and add more users above-----------------------------------------------------------------------------------------

player_stats = {
    'AK33': {
       'Squad kills': int(AK33squadkills), 'Squad Wins': int(AK33squadwins), 'Squad Finished top 3': int(AK33squadtop3)
       
    },
    'Vector': {
        'Squad kills': int(vectorsquadkills),  'Squad Wins': int(vectorsquadwins), 'Squad Finished top 3': int(vectorsquadtop3)
        
    },
    'lokey': {
        'Squad kills': int(lokeysquadkills),  'Squad Wins': int(lokeysquadwins), 'Squad Finished top 3': int(lokeysquadtop3)
    },
    
    'LeFloor': {
       'Squad kills': int(LeFloorsquadkills),  'Squad Wins': int(LeFloorsquadwins), 'Squad Finished top 3': int(LeFloorsquadtop3)
    },
    
     'ghirradeil': {
       'Squad kills': int(ghirradeilsquadkills),  'Squad Wins': int(ghirradeilsquadwins), 'Squad Finished top 3': int(ghirradeilsquadtop3)
    },
     
     'phlash': {
        'Squad kills': int(phlashsquadkills),  'Squad Wins': int(phlashsquadwins), 'Squad Finished top 3': int(phlashsquadtop3)
    },
     
     'ryptyde': {
        'Squad kills': int(ryptydesquadkills),  'Squad Wins': int(ryptydesquadwins), 'Squad Finished top 3': int(ryptydesquadtop3)
    },
     
     'sideKwinder': {
        'Squad kills': int(sideKwindersquadkills), 'Squad Wins': int(sideKwindersquadwins), 'Squad Finished top 3': int(sideKwindersquadtop3)
       
    },
     
     'Tandumm': {
       'Squad kills': int(Tandummsquadkills), 'Squad Wins': int(Tandummsquadwins), 'Squad Finished top 3': int(Tandummsquadtop3)
       
    },
     
     'o3zone': {
       'Squad kills': int(o3zonesquadkills), 'Squad Wins': int(o3zonesquadwins), 'Squad Finished top 3': int(o3zonesquadtop3)
       
    },
     
    'keauxda': {
        'Squad kills': int(keauxdasquadkills), 'Squad Wins': int(keauxdasquadwins), 'Squad Finished top 3': int(keauxdasquadtop3)
       
    },
    'mulligan': {
        'Squad kills': int(mulligansquadkills), 'Squad Wins': int(mulligansquadwins), 'Squad Finished top 3': int(mulligansquadtop3)
       
    },
    
    'mcfly': {
        'Squad kills': int(mcflysquadkills), 'Squad Wins': int(mcflysquadwins), 'Squad Finished top 3': int(mcflysquadtop3)
       
    },
    'saitama': {
        'Squad kills': int(saitamasquadkills), 'Squad Wins': int(saitamasquadwins), 'Squad Finished top 3': int(saitamasquadtop3)
       
    },
    'trubadoor': {
       'Squad kills': int(trubadoorsquadkills), 'Squad Wins': int(trubadoorsquadwins), 'Squad Finished top 3': int(trubadoorsquadtop3)
       
    },
    'romKulus': {
       'Squad kills': int(romKulussquadkills), 'Squad kills': int(romKulussquadkills), 'Squad Wins': int(romKulussquadwins), 'Squad Finished top 3': int(romKulussquadtop3)
             
    },
    'can_nun': {
       'Squad kills': int(can_nunsquadkills), 'Squad Wins': int(can_nunsquadwins), 'Squad Finished top 3': int(can_nunsquadtop3)
       },
     
     'apolllo': {
       'Squad kills': int(apolllosquadkills), 'Squad Wins': int(apolllosquadwins), 'Squad Finished top 3': int(apolllosquadtop3)
       },
     
      'jaknkife': {
       'Squad kills': int(jaknkifesquadkills), 'Squad Wins': int(jaknkifesquadwins), 'Squad Finished top 3': int(jaknkifesquadtop3)
       },

   }


# Define ranking function for kills in each category
def rank_players_by_category(category):
    category_stats = [(player, stats[category]) for player, stats in player_stats.items()]
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

# Generate rankings for each category
categories = ['Squad kills', 'Squad Wins', 'Squad Finished top 3',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_squad_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat}\n"
    rankings_data[category] = category_rankings
    print_squad_rankings.append(category_rankings)
 
with open(Squad_data, 'w') as f:
     f.write('\n'.join(print_squad_rankings))

with open(Squad_data, "r") as file:
    squad_data_content = file.read()
   
#website - 

st.set_page_config(page_title='Squad Rankings', layout= "centered")
st.title ('Squads Rankings')
st.caption("Includes data from Trio and Squad BR modes (limitation of the API)")
st.write(squad_data_content)   







