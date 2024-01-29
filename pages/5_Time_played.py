import streamlit as st 
Time = 'pages\Time.txt'
    
    #files_names
        #Pixsol----------------
AK33file ='pages/pixsol/AK33_stats.txt'
AK33solo='pages/pixsol/AK33-solo.txt'
AK33duo='pages/pixsol/AK33-duo.txt'
AK33squad='pages/pixsol/AK33-squad.txt'
AK33all='pages/pixsol/AK33-all.txt'
        #vector----------------
vectorfile ='pages/vector/vector_stats.txt'
vectorsolo='pages/vector/vector-solo.txt'
vectorduo='pages/vector/vector-duo.txt'
vectorsquad='pages/vector/vector-squad.txt'
vectorall='pages/vector/vector-all.txt'
        #lo-key----------------
lokeyfile ='pages/lokey/lokey_stats.txt'
lokeysolo='pages/lokey/lokey-solo.txt'
lokeyduo='pages/lokey/lokey-duo.txt'
lokeysquad='pages/lokey/lokey-squad.txt'
lokeyall='pages/lokey/lokey-all.txt'
        #LeFloor---------------
LeFloorfile ='pages/LeFloor/LeFloor_stats.txt'
LeFloorsolo='pages/LeFloor/LeFloor-solo.txt'
LeFloorduo='pages/LeFloor/LeFloor-duo.txt'
LeFloorsquad='pages/LeFloor/LeFloor-squad.txt'
LeFloorall='pages/LeFloor/LeFloor-all.txt'

        #ghirradeil----------------
ghirradeilfile ='pages/ghirradeil/ghirradeil_stats.txt'
ghirradeilsolo='pages/ghirradeil/ghirradeil-solo.txt'
ghirradeilduo='pages/ghirradeil/ghirradeil-duo.txt'
ghirradeilsquad='pages/ghirradeil/ghirradeil-squad.txt'
ghirradeilall='pages/ghirradeil/ghirradeil-all.txt'

        #phlash----------------
phlashfile ='pages/phlash/phlash.txt'
phlashsolo='pages/phlash/phlash-solo.txt'
phlashduo='pages/phlash/phlash-duo.txt'
phlashsquad='pages/phlash/phlash-squad.txt'
phlashall='pages/phlash/phlash-all.txt'

    #ryptyde----------------
ryptydefile ='pages/ryptyde/ryptyde_stats.txt'
ryptydesolo='pages/ryptyde/ryptyde-solo.txt'
ryptydeduo='pages/ryptyde/ryptyde-duo.txt'
ryptydesquad='pages/ryptyde/ryptyde-squad.txt'
ryptydeall='pages/ryptyde/ryptyde-all.txt'

    #sideKwinder----------------
sideKwinderfile ='pages/sideKwinder/sideKwinder_stats.txt'
sideKwindersolo='pages/sideKwinder/sideKwinder-solo.txt'
sideKwinderduo='pages/sideKwinder/sideKwinder-duo.txt'
sideKwindersquad='pages/sideKwinder/sideKwinder-squad.txt'
sideKwinderall='pages/sideKwinder/sideKwinder-all.txt'

    #Tandumm----------------
Tandummfile ='pages/Tandumm/Tandumm_stats.txt'
Tandummsolo='pages/Tandumm/Tandumm-solo.txt'
Tandummduo='pages/Tandumm/Tandumm-duo.txt'
Tandummsquad='pages/Tandumm/Tandumm-squad.txt'
Tandummall='pages/Tandumm/Tandumm-all.txt'

    #o3zone----------------
o3zonefile ='pages/o3zone/o3zone_stats.txt'
o3zonesolo='pages/o3zone/o3zone-solo.txt'
o3zoneduo='pages/o3zone/o3zone-duo.txt'
o3zonesquad='pages/o3zone/o3zone-squad.txt'
o3zoneall='pages/o3zone/o3zone-all.txt'

    #keauxda----------------
keauxdafile ='pages/keauxda/keauxda_stats.txt'
keauxdasolo='pages/keauxda/keauxda-solo.txt'
keauxdaduo='pages/keauxda/keauxda-duo.txt'
keauxdasquad='pages/keauxda/keauxda-squad.txt'
keauxdaall='pages/keauxda/keauxda-all.txt'

    #mulligan----------------
mulliganfile ='pages/mulligan/mulligan_stats.txt'
mulligansolo='pages/mulligan/mulligan-solo.txt'
mulliganduo='pages/mulligan/mulligan-duo.txt'
mulligansquad='pages/mulligan/mulligan-squad.txt'
mulliganall='pages/mulligan/mulligan-all.txt'

    #mcfly----------------
mcflyfile ='pages/mcfly/mcfly_stats.txt'
mcflysolo='pages/mcfly/mcfly-solo.txt'
mcflyduo='pages/mcfly/mcfly-duo.txt'
mcflysquad='pages/mcfly/mcfly-squad.txt'
mcflyall='pages/mcfly/mcfly-all.txt'

    #saitama----------------
saitamafile ='pages/saitama/saitama_stats.txt'
saitamasolo='pages/saitama/saitama-solo.txt'
saitamaduo='pages/saitama/saitama-duo.txt'
saitamasquad='pages/saitama/saitama-squad.txt'
saitamaall='pages/saitama/saitama-all.txt'

    #trubadoor----------------
trubadoorfile ='pages/trubadoor/trubadoor_stats.txt'
trubadoorsolo='pages/trubadoor/trubadoor-solo.txt'
trubadoorduo='pages/trubadoor/trubadoor-duo.txt'
trubadoorsquad='pages/trubadoor/trubadoor-squad.txt'
trubadoorall='pages/trubadoor/trubadoor-all.txt'

    #romKulus----------------
romKulusfile ='pages/romKulus/romKulus_stats.txt'
romKulussolo='pages/romKulus/romKulus-solo.txt'
romKulusduo='pages/romKulus/romKulus-duo.txt'
romKulussquad='pages/romKulus/romKulus-squad.txt'
romKulusall='pages/romKulus/romKulus-all.txt'
    #can_nun----------------
can_nunfile ='pages/can_nun/can_nun_stats.txt'
can_nunsolo='pages/can_nun/can_nun-solo.txt'
can_nunduo='pages/can_nun/can_nun-duo.txt'
can_nunsquad='pages/can_nun/can_nun-squad.txt'
can_nunall='pages/can_nun/can_nun-all.txt'




#Pixsol---------------------------------------------------------------------------    
   #getstime
AK33time = 0
with open(AK33all, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            AK33time = field.split(':')[1].strip()                 

#mcfly---------------------------------------------------------------------------   
   #gets time
mcflytime = 0
with open(mcflyall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            mcflytime = field.split(':')[1].strip()                 

#vector-----------------------------------------------------------------------------
# time
vectortime = 0
with open(vectorall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            vectortime = field.split(':')[1].strip()                 

#lokey-----------------------------------------------------------------------------
#     #gets time
lokeytime = 0
with open(lokeyall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            lokeytime = field.split(':')[1].strip()                 

#LeFloor-----------------------------------------------------------------------------
#     #gets time
LeFloortime = 0
with open(LeFloorall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            LeFloortime = field.split(':')[1].strip()                 

#ghirradeil-----------------------------------------------------------------------------
#     #gets time
ghirradeiltime = 0
with open(ghirradeilall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            ghirradeiltime = field.split(':')[1].strip()                 

#phlash---------------------------------------------------------------------------     
   #gets time
phlashtime = 0
with open(phlashall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            phlashtime = field.split(':')[1].strip()                 

#ryptyde---------------------------------------------------------------------------    
   #gets time
ryptydetime = 0
with open(ryptydeall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            ryptydetime = field.split(':')[1].strip()                 

#sideKwinder---------------------------------------------------------------------------    
   #gets time
sideKwindertime = 0
with open(sideKwinderall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            sideKwindertime = field.split(':')[1].strip()                 

#Tandumm---------------------------------------------------------------------------    
   #gets time
Tandummtime = 0
with open(Tandummall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            Tandummtime = field.split(':')[1].strip()                 


#o3zone---------------------------------------------------------------------------    
   #gets time
o3zonetime = 0
with open(o3zoneall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            o3zonetime = field.split(':')[1].strip()                 


#keauxda--------------------------------------------------------------------------- 
   #gets time
keauxdatime = 0
with open(keauxdaall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            keauxdatime = field.split(':')[1].strip()                 

#mulligan---------------------------------------------------------------------------     
   #gets time
mulligantime = 0
with open(mulliganall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            mulligantime = field.split(':')[1].strip()                 


#saitama---------------------------------------------------------------------------     
   #gets time
saitamatime = 0
with open(saitamaall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            saitamatime = field.split(':')[1].strip()                 


#trubadoor---------------------------------------------------------------------------
   #gets time
trubadoortime = 0
with open(trubadoorall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            trubadoortime = field.split(':')[1].strip()                 


#romKulus---------------------------------------------------------------------------     
   #gets time
romKulustime = 0
with open(romKulusall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            romKulustime = field.split(':')[1].strip()                 


#can_nun---------------------------------------------------------------------------    
   #getstime
can_nuntime = 0
with open(can_nunall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'minutesPlayed' in field:
            can_nuntime = field.split(':')[1].strip()                 



#Changes all time variables from strings to integers for calculations
AK33time = int(AK33time)
mcflytime = int(mcflytime)
vectortime = int(vectortime)
lokeytime = int(lokeytime)
LeFloortime = int(LeFloortime)
ghirradeiltime = int(ghirradeiltime)
phlashtime = int(phlashtime)
ryptydetime = int(ryptydetime)
sideKwindertime = int(sideKwindertime)
Tandummtime = int(Tandummtime)
o3zonetime = int(o3zonetime)
keauxdatime = int(keauxdatime)
mulligantime = int(mulligantime)
saitamatime = int(saitamatime)
trubadoortime = int(trubadoortime)
romKulustime = int(romKulustime)
can_nuntime = int(can_nuntime)

#divided by 60 for minutes to hours and rounds all time to 1 decimal 
# Pixsol---------------------------------------------------------------------------   

AK33time = AK33time /60
standardized_AK33time = ("{:.1f}".format(AK33time))

# mcflytime---------------------------------------------------------------------------   

mcflytime = mcflytime /60
standardized_mcflytime = ("{:.1f}".format(mcflytime))

# vectortime---------------------------------------------------------------------------   

vectortime = vectortime /60
standardized_vectortime = ("{:.1f}".format(vectortime))

# lokeytime---------------------------------------------------------------------------   
lokeytime = lokeytime /60
standardized_lokeytime = ("{:.1f}".format(lokeytime))

# LeFloortime---------------------------------------------------------------------------   

LeFloortime = LeFloortime /60
standardized_LeFloortime = ("{:.1f}".format(LeFloortime))

# ghirradeiltime---------------------------------------------------------------------------   

ghirradeiltime = ghirradeiltime /60
standardized_ghirradeiltime = ("{:.1f}".format(ghirradeiltime))

# phlashtime ---------------------------------------------------------------------------   

phlashtime  = phlashtime /60
standardized_phlashtime  = ("{:.1f}".format(phlashtime ))

# ryptydetime---------------------------------------------------------------------------   
ryptydetime = ryptydetime /60
standardized_ryptydetime = ("{:.1f}".format(ryptydetime))

# sideKwindertime---------------------------------------------------------------------------   

sideKwindertime = sideKwindertime /60
standardized_sideKwindertime = ("{:.1f}".format(sideKwindertime))

# Tandummtime---------------------------------------------------------------------------   

Tandummtime = Tandummtime /60
standardized_Tandummtime = ("{:.1f}".format(Tandummtime))

# o3zonetime---------------------------------------------------------------------------   
o3zonetime = o3zonetime /60
standardized_o3zonetime = ("{:.1f}".format(o3zonetime))

# keauxdatime---------------------------------------------------------------------------   

keauxdatime = keauxdatime /60
standardized_keauxdatime = ("{:.1f}".format(keauxdatime))

# mulligantime---------------------------------------------------------------------------   
mulligantime = mulligantime /60
standardized_mulligantime = ("{:.1f}".format(mulligantime))

# saitamatime---------------------------------------------------------------------------   
saitamatime = saitamatime /60
standardized_saitamatime = ("{:.1f}".format(saitamatime))

# trubadoortime---------------------------------------------------------------------------   
trubadoortime = trubadoortime /60
standardized_trubadoortime = ("{:.1f}".format(trubadoortime))

# romKulustime---------------------------------------------------------------------------   
romKulustime = romKulustime /60
standardized_romKulustime = ("{:.1f}".format(romKulustime))

# can_nuntime---------------------------------------------------------------------------   
can_nuntime = can_nuntime /60
standardized_can_nuntime = ("{:.1f}".format(can_nuntime))


player_stats = {
    'AK33': {
       'time':(standardized_AK33time), 
    },
    
     'mcfly': {
       'time':(standardized_mcflytime), 
       
    },
    
    'Vector': {
       'time':(standardized_vectortime), 
        
    },
    'lokey': {
       'time':(standardized_lokeytime), 
    },
    
    'LeFloor': {
       'time':(standardized_LeFloortime), 
    },
    
     'ghirradeil': {
       'time':(standardized_ghirradeiltime), 
    },
     
     'phlash': {
       'time':(standardized_phlashtime), 
    },
     
     'ryptyde': {
       'time':(standardized_ryptydetime),
    },
     
     'sideKwinder': {
       'time':(standardized_sideKwindertime), 
       
    },
     
     'Tandumm': {
       'time':(standardized_Tandummtime), 
       
    },
     
     'o3zone': {
       'time':(standardized_o3zonetime), 
       
    },
     
    'keauxda': {
       'time':(standardized_keauxdatime), 
       
    },
    'mulligan': {
       'time':(standardized_mulligantime), 
       
    },
   
    'saitama': {
       'time':(standardized_saitamatime), 
       
    },
    'trubadoor': {
       'time':(standardized_trubadoortime), 
       
    },
    'romKulus': {
       'time':(standardized_romKulustime), 
             
    },
    'can_nun': {
       'time':(standardized_can_nuntime),
       },

   }




# Define ranking function for kills in each category
def rank_players_by_category(category):
    category_stats = [(player, stats[category]) for player, stats in player_stats.items()]
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

# Generate rankings for each category
categories = ['time',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_time_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat}\n"
    rankings_data[category] = category_rankings
    print_time_rankings.append(category_rankings)
 
with open(Time, 'w') as f:
     f.write('\n'.join(print_time_rankings))

with open(Time, "r") as file:
   time_data_content = file.read()
   
#website - 

st.set_page_config(page_title='Time Played', layout= "centered")
st.title ('Time Played')
st.caption("Time played in hours - BR modes")
st.write(time_data_content)   



