import streamlit as st 
kd_data = 'pages\kd_data.txt'
    
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
   #getskd
AK33kd = 0
with open(AK33all, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            AK33kd = field.split(':')[1].strip()                 

#mcfly---------------------------------------------------------------------------   
   #gets kd
mcflykd = 0
with open(mcflyall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            mcflykd = field.split(':')[1].strip()                 

#vector-----------------------------------------------------------------------------
# kd
vectorkd = 0
with open(vectorall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            vectorkd = field.split(':')[1].strip()                 

#lokey-----------------------------------------------------------------------------
#     #gets kd
lokeykd = 0
with open(lokeyall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            lokeykd = field.split(':')[1].strip()                 

#LeFloor-----------------------------------------------------------------------------
#     #gets kd
LeFloorkd = 0
with open(LeFloorall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            LeFloorkd = field.split(':')[1].strip()                 

#ghirradeil-----------------------------------------------------------------------------
#     #gets kd
ghirradeilkd = 0
with open(ghirradeilall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            ghirradeilkd = field.split(':')[1].strip()                 

#phlash---------------------------------------------------------------------------     
   #gets kd
phlashkd = 0
with open(phlashall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            phlashkd = field.split(':')[1].strip()                 

#ryptyde---------------------------------------------------------------------------    
   #gets kd
ryptydekd = 0
with open(ryptydeall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            ryptydekd = field.split(':')[1].strip()                 

#sideKwinder---------------------------------------------------------------------------    
   #gets kd
sideKwinderkd = 0
with open(sideKwinderall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            sideKwinderkd = field.split(':')[1].strip()                 

#Tandumm---------------------------------------------------------------------------    
   #gets kd
Tandummkd = 0
with open(Tandummall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            Tandummkd = field.split(':')[1].strip()                 


#o3zone---------------------------------------------------------------------------    
   #gets kd
o3zonekd = 0
with open(o3zoneall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            o3zonekd = field.split(':')[1].strip()                 


#keauxda--------------------------------------------------------------------------- 
   #gets kd
keauxdakd = 0
with open(keauxdaall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            keauxdakd = field.split(':')[1].strip()                 

#mulligan---------------------------------------------------------------------------     
   #gets kd
mulligankd = 0
with open(mulliganall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            mulligankd = field.split(':')[1].strip()                 


#saitama---------------------------------------------------------------------------     
   #gets kd
saitamakd = 0
with open(saitamaall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            saitamakd = field.split(':')[1].strip()                 


#trubadoor---------------------------------------------------------------------------
   #gets kd
trubadoorkd = 0
with open(trubadoorall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            trubadoorkd = field.split(':')[1].strip()                 


#romKulus---------------------------------------------------------------------------     
   #gets kd
romKuluskd = 0
with open(romKulusall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            romKuluskd = field.split(':')[1].strip()                 


#can_nun---------------------------------------------------------------------------    
   #getskd
can_nunkd = 0
with open(can_nunall, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'kd' in field:
            can_nunkd = field.split(':')[1].strip()                 



#Changes all KD variables from strings to integers for calculations
AK33kd = int(AK33kd)
mcflykd = int(mcflykd)
vectorkd = int(vectorkd)
lokeykd = int(lokeykd)
LeFloorkd = int(LeFloorkd)
ghirradeilkd = int(ghirradeilkd)
phlashkd = int(phlashkd)
ryptydekd = int(ryptydekd)
sideKwinderkd = int(sideKwinderkd)
Tandummkd = int(Tandummkd)
o3zonekd = int(o3zonekd)
keauxdakd = int(keauxdakd)
mulligankd = int(mulligankd)
saitamakd = int(saitamakd)
trubadoorkd = int(trubadoorkd)
romKuluskd = int(romKuluskd)
can_nunkd = int(can_nunkd)

#Def to couint how many digits are in the kd stat
def countDigits(n):
   ans = 0
   while (n):
      ans = ans + 1
      n = n // 10
   return ans

#sets the varibule count_Xkd. Counts the Xkd stat for every user 
count_AK33kd = countDigits(AK33kd)
count_mcflykd = countDigits(mcflykd)
count_vectorkd = countDigits(vectorkd)
count_lokeykd = countDigits(lokeykd)
count_LeFloorkd = countDigits(LeFloorkd)
count_ghirradeilkd = countDigits(ghirradeilkd)
count_phlashkd = countDigits(phlashkd)
count_ryptydekd = countDigits(ryptydekd)
count_sideKwinderkd = countDigits(sideKwinderkd)
count_Tandummkd = countDigits(Tandummkd)
count_o3zonekd = countDigits(o3zonekd)
count_keauxdakd = countDigits(keauxdakd)
count_mulligankd = countDigits(mulligankd)
count_saitamakd = countDigits(saitamakd)
count_trubadoorkd = countDigits(trubadoorkd)
count_romKuluskd = countDigits(romKuluskd)
count_can_nunkd = countDigits(can_nunkd)


#rounds all KD stats to 2 decimal places
# Pixsol---------------------------------------------------------------------------   
if count_AK33kd == 2:
    AK33kd = AK33kd * 0.10

elif count_AK33kd == 3:
    AK33kd = AK33kd * 0.01

elif count_AK33kd == 4 or 5:
    AK33kd = AK33kd * 0.001
  
standardized_AK33kd = ("{:.2f}".format(AK33kd))

# mcflykd---------------------------------------------------------------------------   
if count_mcflykd == 2:
    mcflykd = mcflykd * 0.10

elif count_mcflykd == 3:
    mcflykd = mcflykd * 0.01

elif count_mcflykd == 4 or 5:
    mcflykd = mcflykd * 0.001
  
standardized_mcflykd = ("{:.2f}".format(mcflykd))

# NULL---------------------------------------------------------------------------   
if count_vectorkd == 2:
    NULL_ = vectorkd * 0.10

elif count_vectorkd == 3:
    vectorkd = vectorkd * 0.01

elif count_vectorkd == 4 or 5:
    vectorkd = vectorkd * 0.001
  
standardized_vectorkd = ("{:.2f}".format(vectorkd))

# lokeykd---------------------------------------------------------------------------   
if count_lokeykd == 2:
    lokeykd = lokeykd * 0.10

elif count_lokeykd == 3:
    lokeykd = lokeykd * 0.01

elif count_lokeykd == 4 or 5:
    lokeykd = lokeykd * 0.001
  
standardized_lokeykd = ("{:.2f}".format(lokeykd))

# LeFloorkd---------------------------------------------------------------------------   
if count_LeFloorkd == 2:
    LeFloorkd = LeFloorkd * 0.10

elif count_LeFloorkd == 3:
    LeFloorkd = LeFloorkd * 0.01

elif count_LeFloorkd == 4 or 5:
    LeFloorkd = LeFloorkd * 0.001
  
standardized_LeFloorkd = ("{:.2f}".format(LeFloorkd))

# ghirradeilkd---------------------------------------------------------------------------   
if count_ghirradeilkd == 2:
    ghirradeilkd = ghirradeilkd * 0.10

elif count_ghirradeilkd == 3:
    ghirradeilkd = ghirradeilkd * 0.01

elif count_ghirradeilkd == 4 or 5:
    ghirradeilkd = ghirradeilkd * 0.001
  
standardized_ghirradeilkd = ("{:.2f}".format(ghirradeilkd))

# phlashkd ---------------------------------------------------------------------------   
if count_phlashkd == 2:
    phlashkd  = phlashkd  * 0.10

elif count_phlashkd == 3:
    phlashkd  = phlashkd  * 0.01

elif count_phlashkd == 4 or 5:
    phlashkd  = phlashkd  * 0.001
  
standardized_phlashkd  = ("{:.2f}".format(phlashkd ))

# ryptydekd---------------------------------------------------------------------------   
if count_ryptydekd  == 2:
    ryptydekd = ryptydekd * 0.10

elif count_ryptydekd  == 3:
    ryptydekd = ryptydekd * 0.01

elif count_ryptydekd  == 4 or 5:
    ryptydekd = ryptydekd * 0.001
  
standardized_ryptydekd = ("{:.2f}".format(ryptydekd))

# sideKwinderkd---------------------------------------------------------------------------   
if count_sideKwinderkd == 2:
    sideKwinderkd = sideKwinderkd * 0.10

elif count_sideKwinderkd == 3:
    sideKwinderkd = sideKwinderkd * 0.01

elif count_sideKwinderkd == 4 or 5:
    sideKwinderkd = sideKwinderkd * 0.001
  
standardized_sideKwinderkd = ("{:.2f}".format(sideKwinderkd))

# Tandummkd---------------------------------------------------------------------------   
if count_Tandummkd == 2:
    Tandummkd = Tandummkd * 0.10

elif count_Tandummkd == 3:
    Tandummkd = Tandummkd * 0.01

elif count_Tandummkd == 4 or 5:
    Tandummkd = Tandummkd * 0.001
  
standardized_Tandummkd = ("{:.2f}".format(Tandummkd))

# o3zonekd---------------------------------------------------------------------------   
if count_o3zonekd == 2:
    o3zonekd = o3zonekd * 0.10

elif count_o3zonekd == 3:
    o3zonekd = o3zonekd * 0.01

elif count_o3zonekd == 4 or 5:
    o3zonekd = o3zonekd * 0.001
  
standardized_o3zonekd = ("{:.2f}".format(o3zonekd))

# keauxdakd---------------------------------------------------------------------------   
if count_keauxdakd == 2:
    keauxdakd = keauxdakd * 0.10

elif count_keauxdakd == 3:
    keauxdakd = keauxdakd * 0.01

elif count_keauxdakd == 4 or 5:
    keauxdakd = keauxdakd * 0.001
  
standardized_keauxdakd = ("{:.2f}".format(keauxdakd))

# mulligankd---------------------------------------------------------------------------   
if count_mulligankd == 2:
    mulligankd = mulligankd * 0.10

elif count_mulligankd == 3:
    mulligankd = mulligankd * 0.01

elif count_mulligankd == 4 or 5:
    mulligankd = mulligankd * 0.001
  
standardized_mulligankd = ("{:.2f}".format(mulligankd))

# saitamakd---------------------------------------------------------------------------   
if count_saitamakd == 2:
    saitamakd = saitamakd * 0.10

elif count_saitamakd == 3:
    saitamakd = saitamakd * 0.01

elif count_saitamakd == 4 or 5:
    saitamakd = saitamakd * 0.001
  
standardized_saitamakd = ("{:.2f}".format(saitamakd))

# NULL---------------------------------------------------------------------------   
if count_trubadoorkd == 2:
    trubadoorkd = trubadoorkd * 0.10

elif count_trubadoorkd == 3:
    trubadoorkd = trubadoorkd * 0.01

elif count_trubadoorkd == 4 or 5:
    trubadoorkd = trubadoorkd * 0.001
  
standardized_trubadoorkd = ("{:.2f}".format(trubadoorkd))

# romKuluskd---------------------------------------------------------------------------   
if count_romKuluskd == 2:
    romKuluskd = romKuluskd * 0.10

elif count_romKuluskd == 3:
    romKuluskd = romKuluskd * 0.01

elif count_romKuluskd == 4 or 5:
    romKuluskd = romKuluskd * 0.001
  
standardized_romKuluskd = ("{:.2f}".format(romKuluskd))

# can_nunkd---------------------------------------------------------------------------   
if count_can_nunkd == 2:
    can_nunkd = can_nunkd * 0.10

elif count_can_nunkd == 3:
    can_nunkd = can_nunkd * 0.01

elif count_can_nunkd == 4 or 5:
    can_nunkd = can_nunkd * 0.001
  
standardized_can_nunkd = ("{:.2f}".format(can_nunkd))



player_stats = {
    'AK33': {
       'KD':(standardized_AK33kd), 
    },
    
     'mcfly': {
       'KD':(standardized_mcflykd), 
       
    },
    
    'Vector': {
       'KD':(standardized_vectorkd), 
        
    },
    'lokey': {
       'KD':(standardized_lokeykd), 
    },
    
    'LeFloor': {
       'KD':(standardized_LeFloorkd), 
    },
    
     'ghirradeil': {
       'KD':(standardized_ghirradeilkd), 
    },
     
     'phlash': {
       'KD':(standardized_phlashkd), 
    },
     
     'ryptyde': {
       'KD':(standardized_ryptydekd),
    },
     
     'sideKwinder': {
       'KD':(standardized_sideKwinderkd), 
       
    },
     
     'Tandumm': {
       'KD':(standardized_Tandummkd), 
       
    },
     
     'o3zone': {
       'KD':(standardized_o3zonekd), 
       
    },
     
    'keauxda': {
       'KD':(standardized_keauxdakd), 
       
    },
    'mulligan': {
       'KD':(standardized_mulligankd), 
       
    },
   
    'saitama': {
       'KD':(standardized_saitamakd), 
       
    },
    'trubadoor': {
       'KD':(standardized_trubadoorkd), 
       
    },
    'romKulus': {
       'KD':(standardized_romKuluskd), 
             
    },
    'Can_nun': {
       'KD':(standardized_can_nunkd),
       },

   }


# Define ranking function for ranking in each category
def rank_players_by_category(category):
    category_stats = [(player, float(stats[category])) for player, stats in player_stats.items()] #different from other pages- this turns everything to a float
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

# Generate rankings for each category
categories = ['KD',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_kd_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat:.2f}\n" #different from other pages- Keep a "0" after one deccmial palce example 1.1 shows up at 1.0
    rankings_data[category] = category_rankings
    print_kd_rankings.append(category_rankings)

with open(kd_data, 'w') as f:
     f.write('\n'.join(print_kd_rankings))

with open(kd_data, "r") as file:
   kd_data_content = file.read()
     

#website - 

st.set_page_config(page_title='K/D Rankings', layout= "centered")
st.title ('K/D Rankings')
st.caption("Included data: Solos, Duos, Trios, Squads and LTM(s) BR modes")
st.write(print_kd_rankings)
st.write(kd_data_content)   


