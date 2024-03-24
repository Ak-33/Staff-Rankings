import streamlit as st 
Duo_data = 'pages\duo_data.txt'
   
    #files_names
        #Pixsol----------------
AK33duo='pages/pixsol/AK33-duo.txt'
        #vector----------------
vectorduo='pages/vector/vector-duo.txt'
        #lo-key----------------
lokeyduo='pages/lokey/lokey-duo.txt'
        #LeFloor---------------
LeFloorduo='pages/LeFloor/LeFloor-duo.txt'
        #ghirradeil----------------
ghirradeilduo='pages/ghirradeil/ghirradeil-duo.txt'
        #phlash----------------
phlashduo='pages/phlash/phlash-duo.txt'
   #ryptyde----------------
ryptydeduo='pages/ryptyde/ryptyde-duo.txt'
    #sideKwinder----------------
sideKwinderduo='pages/sideKwinder/sideKwinder-duo.txt'
    #Tandumm----------------
Tandummduo='pages/Tandumm/Tandumm-duo.txt'
    #o3zone----------------
o3zoneduo='pages/o3zone/o3zone-duo.txt'
    #keauxda----------------
# keauxdaduo='pages/keauxda/keauxda-duo.txt'
   #mulligan----------------
mulliganduo='pages/mulligan/mulligan-duo.txt'
    #mcfly----------------
mcflyduo='pages/mcfly/mcfly-duo.txt'
    #saitama----------------
saitamaduo='pages/saitama/saitama-duo.txt'
    #trubadoor----------------
trubadoorduo='pages/trubadoor/trubadoor-duo.txt'
   #romKulus----------------
romKulusduo='pages/romKulus/romKulus-duo.txt'
    #can_nun----------------
can_nunduo='pages/can_nun/can_nun-duo.txt'
    #apolllo----------------
apollloduo='pages/apolllo/apolllo-duo.txt'
    #jaknkife----------------
jaknkifeduo='pages/jaknkife/jaknkife-duo.txt'


#Pixsol---------------------------------------------------------------------------
#duo stats
AK33duowins = 0
AK33duokills = 0
AK33duotop5 = 0
with open(AK33duo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            AK33duowins = field.split(':')[1].strip()
        if 'totalk' in field:
            AK33duokills = field.split(':')[1].strip()
        if "top5" in field:
            AK33duotop5 = field.split(':')[1].strip()        
    
            
#mcfly---------------------------------------------------------------------------

# #     #duo stats
mcflyduowins = 0
mcflyduokills = 0
mcflyduotop5 = 0
with open(mcflyduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            mcflyduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            mcflyduokills = field.split(':')[1].strip()
        if "top5" in field:
            mcflyduotop5 = field.split(':')[1].strip()        

#vector-----------------------------------------------------------------------------
# #     #duo stats
vectorduowins = 0
vectorduokills = 0
vectorduotop5 = 0
with open(vectorduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            vectorduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            vectorduokills = field.split(':')[1].strip()
        if "top5" in field:
            vectorduotop5 = field.split(':')[1].strip()        

#lokey-----------------------------------------------------------------------------

            
# #     #duo stats
lokeyduowins = 0
lokeyduokills = 0
lokeyduotop5 = 0
with open(lokeyduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            lokeyduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            lokeyduokills = field.split(':')[1].strip()
        if "top5" in field:
            lokeyduotop5 = field.split(':')[1].strip()        

#LeFloor-----------------------------------------------------------------------------

# #     #duo stats
LeFloorduowins = 0
LeFloorduokills = 0
LeFloorduotop5 = 0
with open(LeFloorduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            LeFloorduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            LeFloorduokills = field.split(':')[1].strip()
        if "top5" in field:
            LeFloorduotop5 = field.split(':')[1].strip()        
      

#ghirradeil-----------------------------------------------------------------------------

#duo stats
ghirradeilduowins = 0
ghirradeilduokills = 0
ghirradeilduotop5 = 0
with open(ghirradeilduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            ghirradeilduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            ghirradeilduokills = field.split(':')[1].strip()
        if "top5" in field:
            ghirradeilduotop5 = field.split(':')[1].strip()        
   

#phlash---------------------------------------------------------------------------

# #     #duo stats
phlashduowins = 0
phlashduokills = 0
phlashduotop5 = 0
with open(phlashduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            phlashduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            phlashduokills = field.split(':')[1].strip()
        if "top5" in field:
            phlashduotop5 = field.split(':')[1].strip()        

#ryptyde---------------------------------------------------------------------------
#     #duo stats
ryptydeduowins = 0
ryptydeduokills = 0
ryptydeduotop5 = 0
with open(ryptydeduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            ryptydeduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            ryptydeduokills = field.split(':')[1].strip()
        if "top5" in field:
            ryptydeduotop5 = field.split(':')[1].strip()        

#sideKwinder---------------------------------------------------------------------------

#duo stats
sideKwinderduowins = 0
sideKwinderduokills = 0
sideKwinderduotop5 = 0
with open(sideKwinderduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            sideKwinderduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            sideKwinderduokills = field.split(':')[1].strip()
        if "top5" in field:
            sideKwinderduotop5 = field.split(':')[1].strip()        

#Tandumm---------------------------------------------------------------------------

#duo stats
Tandummduowins = 0
Tandummduokills = 0
Tandummduotop5 = 0
with open(Tandummduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            Tandummduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            Tandummduokills = field.split(':')[1].strip()
        if "top5" in field:
            Tandummduotop5 = field.split(':')[1].strip()        

#o3zone---------------------------------------------------------------------------

#duo stats
o3zoneduowins = 0
o3zoneduokills = 0
o3zoneduotop5 = 0
with open(o3zoneduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            o3zoneduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            o3zoneduokills = field.split(':')[1].strip()
        if "top5" in field:
            o3zoneduotop5 = field.split(':')[1].strip()        

#keauxda---------------------------------------------------------------------------

#duo stats
# keauxdaduowins = 0
# keauxdaduokills = 0
# keauxdaduotop5 = 0
# with open(keauxdaduo, 'r') as file:
#     content = file.read()
#     fields = content.split(',')
 
#     for field in fields:
#         if "wins" in field: 
#             keauxdaduowins = field.split(':')[1].strip()
#         if 'totalk' in field:
#             keauxdaduokills = field.split(':')[1].strip()
#         if "top5" in field:
#             keauxdaduotop5 = field.split(':')[1].strip()        

#mulligan---------------------------------------------------------------------------
#duo stats
mulliganduowins = 0
mulliganduokills = 0
mulliganduotop5 = 0
with open(mulliganduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            mulliganduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            mulliganduokills = field.split(':')[1].strip()
        if "top5" in field:
            mulliganduotop5 = field.split(':')[1].strip()        

#saitama---------------------------------------------------------------------------

#duo stats
saitamaduowins = 0
saitamaduokills = 0
saitamaduotop5 = 0
with open(saitamaduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            saitamaduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            saitamaduokills = field.split(':')[1].strip()
        if "top5" in field:
            saitamaduotop5 = field.split(':')[1].strip()        

#trubadoor---------------------------------------------------------------------------

#duo stats
trubadoorduowins = 0
trubadoorduokills = 0
trubadoorduotop5 = 0
with open(trubadoorduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            trubadoorduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            trubadoorduokills = field.split(':')[1].strip()
        if "top5" in field:
            trubadoorduotop5 = field.split(':')[1].strip()        

#romKulus---------------------------------------------------------------------------
#duo stats
romKulusduowins = 0
romKulusduokills = 0
romKulusduotop5 = 0
with open(romKulusduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            romKulusduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            romKulusduokills = field.split(':')[1].strip()
        if "top5" in field:
            romKulusduotop5 = field.split(':')[1].strip()        
#can_nun---------------------------------------------------------------------------
#duo stats
can_nunduowins = 0
can_nunduokills = 0
can_nunduotop5 = 0
with open(can_nunduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            can_nunduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            can_nunduokills = field.split(':')[1].strip()
        if "top5" in field:
            can_nunduotop5 = field.split(':')[1].strip()        

#apolllo-----------------------------------------------------------------------------           
#duo stats
apollloduowins = 0
apollloduokills = 0
apollloduotop5 = 0
with open(apollloduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            apollloduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            apollloduokills = field.split(':')[1].strip()
        if "top5" in field:
            apollloduotop5 = field.split(':')[1].strip()
            
#jaknkife-----------------------------------------------------------------------------
#duo stats
jaknkifeduowins = 0
jaknkifeduokills = 0
jaknkifeduotop5 = 0
with open(jaknkifeduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            jaknkifeduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            jaknkifeduokills = field.split(':')[1].strip()
        if "top5" in field:
            jaknkifeduotop5 = field.split(':')[1].strip()        
         
   

#Solo print stats and add more users above-----------------------------------------------------------------------------------------

player_stats = {
    'AK33': {
      'Duo kills': int(AK33duokills), 'Duo Wins': int(AK33duowins), 'Duo Finished top 5': int(AK33duotop5)
              
    },
    
     'mcfly': {
       'Duo kills': int(mcflyduokills), 'Duo Wins': int(mcflyduowins), 'Duo Finished top 5': int(mcflyduotop5)
       
    },
    
    'Vector': {
        'Duo kills': int(vectorduokills),  'Duo Wins': int(vectorduowins), 'Duo Finished top 5': int(vectorduotop5)
        
    },
    'lokey': {
       'Duo kills': int(lokeyduokills),  'Duo Wins': int(lokeyduowins), 'Duo Finished top 5': int(lokeyduotop5)
    },
    
    'LeFloor': {
        'Duo kills': int(LeFloorduokills),  'Duo Wins': int(LeFloorduowins), 'Duo Finished top 5': int(LeFloorduotop5)
    },
    
     'ghirradeil': {
        'Duo kills': int(ghirradeilduokills),  'Duo Wins': int(ghirradeilduowins), 'Duo Finished top 5': int(ghirradeilduotop5)
    },
     
     'phlash': {
        'Duo kills': int(phlashduokills),  'Duo Wins': int(phlashduowins), 'Duo Finished top 5': int(phlashduotop5)
    },
     
     'ryptyde': {
        'Duo kills': int(ryptydeduokills),  'Duo Wins': int(ryptydeduowins), 'Duo Finished top 5': int(ryptydeduotop5)
    },
     
     'sideKwinder': {
        'Duo kills': int(sideKwinderduokills), 'Duo Wins': int(sideKwinderduowins), 'Duo Finished top 5': int(sideKwinderduotop5)
       
    },
     
     'Tandumm': {
        'Duo kills': int(Tandummduokills), 'Duo Wins': int(Tandummduowins), 'Duo Finished top 5': int(Tandummduotop5)
       
    },
     
     'o3zone': {
        'Duo kills': int(o3zoneduokills), 'Duo Wins': int(o3zoneduowins), 'Duo Finished top 5': int(o3zoneduotop5)
       
    },
     
    'keauxda': {
        # 'Duo kills': int(keauxdaduokills), 'Duo Wins': int(keauxdaduowins), 'Duo Finished top 5': int(keauxdaduotop5)
       
    },
    'mulligan': {
       'Duo kills': int(mulliganduokills), 'Duo Wins': int(mulliganduowins), 'Duo Finished top 5': int(mulliganduotop5)
       
    },
   
    'saitama': {
       'Duo kills': int(saitamaduokills), 'Duo Wins': int(saitamaduowins), 'Duo Finished top 5': int(saitamaduotop5)
       
    },
    'trubadoor': {
        'Duo kills': int(trubadoorduokills), 'Duo Wins': int(trubadoorduowins), 'Duo Finished top 5': int(trubadoorduotop5)
       
    },
    'romKulus': {
       'Duo kills': int(romKulusduokills), 'Duo Wins': int(romKulusduowins), 'Duo Finished top 5': int(romKulusduotop5)
             
    },
    'can_nun': {
        'Duo kills': int(can_nunduokills), 'Duo Wins': int(can_nunduowins), 'Duo Finished top 5': int(can_nunduotop5)
       },
     
     'apolllo': {
        'Duo kills': int(apollloduokills), 'Duo Wins': int(apollloduowins), 'Duo Finished top 5': int(apollloduotop5)
       },
     
     
      'jaknkife': {
        'Duo kills': int(jaknkifeduokills), 'Duo Wins': int(jaknkifeduowins), 'Duo Finished top 5': int(jaknkifeduotop5)
       },

   }


# Define ranking function for kills in each category
def rank_players_by_category(category):
    category_stats = [(player, stats[category]) for player, stats in player_stats.items()]
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

# Generate rankings for each category
categories = [ 'Duo kills', 'Duo Wins', 'Duo Finished top 5',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_duo_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat}\n"
    rankings_data[category] = category_rankings
    print_duo_rankings.append(category_rankings)
 
with open(Duo_data, 'w') as f:
     f.write('\n'.join(print_duo_rankings))

with open(Duo_data, "r") as file:
    Duo_data_content = file.read()
   
#website -

st.set_page_config(page_title='Duo Rankings', layout= "centered")
st.title ('Duo Rankings')
st.caption("Includes data from the duo BR mode")
st.write(Duo_data_content)   






