import fortnite_api

from fortnite_api import TimeWindow

import re

import string 

import streamlit as st 

api = fortnite_api.FortniteAPI(api_key='8eeca9b5-14ca-4afd-91d6-aed25f55d5b7')
symbols_to_keep = ":," 
punctuation_to_remove = ''.join(c for c in string.punctuation if c not in symbols_to_keep)

    #user_names
Ak33_name = 'AK33_' 
vector_name = 'VECtOR8547'
lokey_name= 'CoarseCat'
LeFloor_name = 'TROLLSphincter'
ghirradeil_name = 'FossilArcher'
phlash_name = 'SlimJimothy2907'
ryptyde_name = 'Ryptyde15'
sideKwinder_name = 'calebjennings922'
Tandumm_name = 'Tandumm24'
o3zone_name = 'Samuel517'
keauxda_name = 'KeauXDa'



    
    #files_names
        #Pixsol----------------
AK33file = 'pixsol/AK33_stats.txt'
AK33solo= 'pixsol/AK33-solo.txt'
AK33duo= 'pixsol/AK33-duo.txt'
AK33squad= 'pixsol/AK33-squad.txt'
        #vector----------------
vectorfile = 'vector/vector_stats.txt'
vectorsolo= 'vector/vector-solo.txt'
vectorduo= 'vector/vector-duo.txt'
vectorsquad= 'vector/vector-squad.txt'
        #lo-key----------------
lokeyfile = 'lokey/lokey_stats.txt'
lokeysolo= 'lokey/lokey-solo.txt'
lokeyduo= 'lokey/lokey-duo.txt'
lokeysquad= 'lokey/lokey-squad.txt'
        #LeFloor---------------
LeFloorfile = 'LeFloor/LeFloor_stats.txt'
LeFloorsolo= 'LeFloor/LeFloor-solo.txt'
LeFloorduo= 'LeFloor/LeFloor-duo.txt'
LeFloorsquad= 'LeFloor/LeFloor-squad.txt'
        #ghirradeil----------------
ghirradeilfile = 'ghirradeil/ghirradeil_stats.txt'
ghirradeilsolo= 'ghirradeil/ghirradeil-solo.txt'
ghirradeilduo= 'ghirradeil/ghirradeil-duo.txt'
ghirradeilsquad= 'ghirradeil/ghirradeil-squad.txt'
        #phlash----------------
phlashfile = 'phlash/phlash.txt'
phlashsolo= 'phlash/phlash-solo.txt'
phlashduo= 'phlash/phlash-duo.txt'
phlashsquad= 'phlash/phlash-squad.txt'
    #ryptyde----------------
ryptydefile = 'ryptyde/ryptyde_stats.txt'
ryptydesolo= 'ryptyde/ryptyde-solo.txt'
ryptydeduo= 'ryptyde/ryptyde-duo.txt'
ryptydesquad= 'ryptyde/ryptyde-squad.txt'
    #sideKwinder----------------
sideKwinderfile = 'sideKwinder/sideKwinder_stats.txt'
sideKwindersolo= 'sideKwinder/sideKwinder-solo.txt'
sideKwinderduo= 'sideKwinder/sideKwinder-duo.txt'
sideKwindersquad= 'sideKwinder/sideKwinder-squad.txt'
    #Tandumm----------------
Tandummfile = 'Tandumm/Tandumm_stats.txt'
Tandummsolo= 'Tandumm/Tandumm-solo.txt'
Tandummduo= 'Tandumm/Tandumm-duo.txt'
Tandummsquad= 'Tandumm/Tandumm-squad.txt'
 #o3zone----------------
o3zonefile = 'o3zone/o3zone_stats.txt'
o3zonesolo= 'o3zone/o3zone-solo.txt'
o3zoneduo= 'o3zone/o3zone-duo.txt'
o3zonesquad= 'o3zone/o3zone-squad.txt'
 #keauxda----------------
keauxdafile = 'keauxda/keauxda_stats.txt'
keauxdasolo= 'keauxda/keauxda-solo.txt'
keauxdaduo= 'keauxda/keauxda-duo.txt'
keauxdasquad= 'keauxda/keauxda-squad.txt'

#Pixsol---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=Ak33_name, time_window=TimeWindow.SEASON)

with open(AK33file, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("Pixsols's Data written successfully!------------")

with open(AK33file, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(AK33file, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(AK33file, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(AK33file, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(AK33file, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(AK33file, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('pixsol/Ak33-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('pixsol/AK33-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('pixsol/AK33-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
AK33level = 0
with open(AK33file, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            AK33level = field.split(':')[1].strip()                 
print(f"battlepass level: {AK33level}")

#     #solo stats
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
print(f"Solo- Wins:{AK33solowins},  Kills: {AK33solokills}, Finished top 10: {AK33solotop10}")   
    
    
    
    
# #     #duo stats
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
                    
print(f"Duo- Wins:{AK33duowins},  Kills: {AK33duokills}, Finished top 5: {AK33duotop5}")     
    
# #     #squads stats
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
print(f"Squad- Wins:{AK33squadwins},  Kills: {AK33squadkills}, Finished top 3: {AK33squadtop3}")    
    

#vector-----------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=vector_name, time_window=TimeWindow.SEASON)

with open(vectorfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("Vector's Data written successfully!--------")

with open(vectorfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(vectorfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(vectorfile, 'w') as f:
    f.write(assembled)

       
     #for splits changes solo duo and squad and battlepass level properly 
with open(vectorfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(vectorfile, 'w') as f:
    f.write(updated_text)


      #spits to sepret txt files
with open(vectorfile, 'r') as original_file:
    content = original_file.read()

sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('vector/vector-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('vector/vector-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('vector/vector-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")

#BP level
vectorlevel = 0
with open(vectorfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            vectorlevel = field.split(':')[1].strip()                 
print(f"battlepass level: {vectorlevel}")

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
print(f"Solo- Wins:{vectorsolowins},  Kills: {vectorsolokills}, Finished top 10: {vectorsolotop10}")   
    
    
    
    
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
                    
print(f"Duo- Wins:{vectorduowins},  Kills: {vectorduokills}, Finished top 5: {vectorduotop5}")     
    
# #     #squads stats
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
print(f"Squad- Wins:{vectorsquadwins},  Kills: {vectorsquadkills}, Finished top 3: {vectorsquadtop3}")    
    




#lokey-----------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=lokey_name, time_window=TimeWindow.SEASON)

with open(lokeyfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("lokey's Data written successfully!--------")

with open(lokeyfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(lokeyfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(lokeyfile, 'w') as f:
    f.write(assembled)

       
     #for splits changes solo duo and squad and battlepass level properly 
with open(lokeyfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(lokeyfile, 'w') as f:
    f.write(updated_text)


      #spits to sepret txt files
with open(lokeyfile, 'r') as original_file:
    content = original_file.read()

sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('lokey/lokey-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('lokey/lokey-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('lokey/lokey-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")

#     #gets BP level
lokeylevel = 0
with open(lokeyfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            lokeylevel = field.split(':')[1].strip()                 
print(f"battlepass level: {lokeylevel}")

#     #solo stats
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


print(f"Solo- Wins:{lokeysolowins},  Kills: {lokeysolokills}, Finished top 10: {lokeysolotop10}")


#LeFloor-----------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=LeFloor_name, time_window=TimeWindow.SEASON)

with open(LeFloorfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("LeFloor's Data written successfully!--------")

with open(LeFloorfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(LeFloorfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(LeFloorfile, 'w') as f:
    f.write(assembled)

       
     #for splits changes solo duo and squad and battlepass level properly 
with open(LeFloorfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(LeFloorfile, 'w') as f:
    f.write(updated_text)


      #spits to sepret txt files
with open(LeFloorfile, 'r') as original_file:
    content = original_file.read()

sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('LeFloor/LeFloor-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('LeFloor/LeFloor-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('LeFloor/LeFloor-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")

#     #gets BP level
LeFloorlevel = 0
with open(LeFloorfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            LeFloorlevel = field.split(':')[1].strip()                 
print(f"battlepass level: {LeFloorlevel}")

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


print(f"Solo- Wins:{LeFloorsolowins},  Kills: {LeFloorsolokills}, Finished top 10: {LeFloorsolotop10}")



       
#ghirradeil-----------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=ghirradeil_name, time_window=TimeWindow.SEASON)

with open(ghirradeilfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("ghirradeil's Data written successfully!--------")

with open(ghirradeilfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(ghirradeilfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(ghirradeilfile, 'w') as f:
    f.write(assembled)

       
     #for splits changes solo duo and squad and battlepass level properly 
with open(ghirradeilfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(ghirradeilfile, 'w') as f:
    f.write(updated_text)


      #spits to sepret txt files
with open(ghirradeilfile, 'r') as original_file:
    content = original_file.read()

sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('ghirradeil/ghirradeil-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('ghirradeil/ghirradeil-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('ghirradeil/ghirradeil-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")

#     #gets BP level
ghirradeillevel = 0
with open(ghirradeilfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            ghirradeillevel = field.split(':')[1].strip()                 
print(f"battlepass level: {ghirradeillevel}")

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


print(f"Solo- Wins:{ghirradeilsolowins},  Kills: {ghirradeilsolokills}, Finished top 10: {ghirradeilsolotop10}")   
    
    
# #     #duo stats
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
                    
print(f"Duo- Wins:{ghirradeilduowins},  Kills: {ghirradeilduokills}, Finished top 5: {ghirradeilduotop5}")     
    
# #     #squads stats
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
print(f"Squad- Wins:{ghirradeilsquadwins},  Kills: {ghirradeilsquadkills}, Finished top 3: {ghirradeilsquadtop3}")    

#phlash---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=phlash_name, time_window=TimeWindow.SEASON)

with open(phlashfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("Pixsols's Data written successfully!------------")

with open(phlashfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(phlashfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(phlashfile, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(phlashfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(phlashfile, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(phlashfile, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('phlash/phlash-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('phlash/phlash-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('phlash/phlash-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
phlashlevel = 0
with open(phlashfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            phlashlevel = field.split(':')[1].strip()                 
print(f"battlepass level: {phlashlevel}")

#     #solo stats
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
print(f"Solo- Wins:{phlashsolowins},  Kills: {phlashsolokills}, Finished top 10: {phlashsolotop10}")   
    
    
    
    
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
                    
print(f"Duo- Wins:{phlashduowins},  Kills: {phlashduokills}, Finished top 5: {phlashduotop5}")     
    
# #     #squads stats
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
print(f"Squad- Wins:{phlashsquadwins},  Kills: {phlashsquadkills}, Finished top 3: {phlashsquadtop3}")

#ryptyde---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=ryptyde_name, time_window=TimeWindow.SEASON)

with open(ryptydefile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("ryptydes's Data written successfully!------------")

with open(ryptydefile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(ryptydefile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(ryptydefile, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(ryptydefile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(ryptydefile, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(ryptydefile, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('ryptyde/ryptyde-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('ryptyde/ryptyde-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('ryptyde/ryptyde-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
ryptydelevel = 0
with open(ryptydefile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            ryptydelevel = field.split(':')[1].strip()                 
print(f"battlepass level: {ryptydelevel}")

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
print(f"Solo- Wins:{ryptydesolowins},  Kills: {ryptydesolokills}, Finished top 10: {ryptydesolotop10}")   
    
    
    
    
# #     #duo stats
ryptydeduowins = 0
ryptydeduokills = 0
ryptydeduotop10 = 0
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
                    
print(f"Duo- Wins:{ryptydeduowins},  Kills: {ryptydeduokills}, Finished top 5: {ryptydeduotop5}")     
    
# #     #squads stats
ryptydesquadwins = 0
ryptydesquadkills = 0
ryptydesquadtop10 = 0
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
print(f"Squad- Wins:{ryptydesquadwins},  Kills: {ryptydesquadkills}, Finished top 3: {ryptydesquadtop3}")



#sideKwinder---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=sideKwinder_name, time_window=TimeWindow.SEASON)

with open(sideKwinderfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("sideKwinders's Data written successfully!------------")

with open(sideKwinderfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(sideKwinderfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(sideKwinderfile, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(sideKwinderfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(sideKwinderfile, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(sideKwinderfile, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('sideKwinder/sideKwinder-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('sideKwinder/sideKwinder-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('sideKwinder/sideKwinder-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
sideKwinderlevel = 0
with open(sideKwinderfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            sideKwinderlevel = field.split(':')[1].strip()                 
print(f"battlepass level: {sideKwinderlevel}")

#     #solo stats
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
print(f"Solo- Wins:{sideKwindersolowins},  Kills: {sideKwindersolokills}, Finished top 10: {sideKwindersolotop10}")   
 
    #duo stats
sideKwinderduowins = 0
sideKwinderduokills = 0
sideKwinderduotop10 = 0
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
                    
print(f"Duo- Wins:{sideKwinderduowins},  Kills: {sideKwinderduokills}, Finished top 5: {sideKwinderduotop5}")     
    
# #     #squads stats
sideKwindersquadwins = 0
sideKwindersquadkills = 0
sideKwindersquadtop10 = 0
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
print(f"Squad- Wins:{sideKwindersquadwins},  Kills: {sideKwindersquadkills}, Finished top 3: {sideKwindersquadtop3}")

#Tandumm---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=Tandumm_name, time_window=TimeWindow.SEASON)

with open(Tandummfile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("Tandumms's Data written successfully!------------")

with open(Tandummfile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(Tandummfile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(Tandummfile, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(Tandummfile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(Tandummfile, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(Tandummfile, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('Tandumm/Tandumm-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('Tandumm/Tandumm-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('Tandumm/Tandumm-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
Tandummlevel = 0
with open(Tandummfile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            Tandummlevel = field.split(':')[1].strip()                 
print(f"battlepass level: {Tandummlevel}")

#     #solo stats
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
print(f"Solo- Wins:{Tandummsolowins},  Kills: {Tandummsolokills}, Finished top 10: {Tandummsolotop10}")   
    
    
    
    
# #     #duo stats
Tandummduowins = 0
Tandummduokills = 0
Tandummduotop10 = 0
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
                    
print(f"Duo- Wins:{Tandummduowins},  Kills: {Tandummduokills}, Finished top 5: {Tandummduotop5}")     
    
# #     #squads stats
Tandummsquadwins = 0
Tandummsquadkills = 0
Tandummsquadtop10 = 0
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
print(f"Squad- Wins:{Tandummsquadwins},  Kills: {Tandummsquadkills}, Finished top 3: {Tandummsquadtop3}")

#o3zone---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=o3zone_name, time_window=TimeWindow.SEASON)

with open(o3zonefile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("o3zones's Data written successfully!------------")

with open(o3zonefile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(o3zonefile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(o3zonefile, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(o3zonefile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(o3zonefile, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(o3zonefile, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('o3zone/o3zone-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('o3zone/o3zone-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('o3zone/o3zone-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
o3zonelevel = 0
with open(o3zonefile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            o3zonelevel = field.split(':')[1].strip()                 
print(f"battlepass level: {o3zonelevel}")

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
print(f"Solo- Wins:{o3zonesolowins},  Kills: {o3zonesolokills}, Finished top 10: {o3zonesolotop10}")   
    
    
    
    
# #     #duo stats
o3zoneduowins = 0
o3zoneduokills = 0
o3zoneduotop10 = 0
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
                    
print(f"Duo- Wins:{o3zoneduowins},  Kills: {o3zoneduokills}, Finished top 5: {o3zoneduotop5}")     
    
# #     #squads stats
o3zonesquadwins = 0
o3zonesquadkills = 0
o3zonesquadtop10 = 0
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
print(f"Squad- Wins:{o3zonesquadwins},  Kills: {o3zonesquadkills}, Finished top 3: {o3zonesquadtop3}")

#keauxda---------------------------------------------------------------------------
player_stats = api.stats.fetch_by_name(name=keauxda_name, time_window=TimeWindow.SEASON)

with open(keauxdafile, 'w') as file:
        
        for attribute in dir(player_stats):
            if not attribute.startswith('__'):  # Skip special attributes
                value = getattr(player_stats, attribute)
                file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
print("keauxdas's Data written successfully!------------")

with open(keauxdafile, 'r') as file:
    content = file.read()

#gets rid of unneeded punctuation
with open(keauxdafile, 'r') as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("", "", punctuation_to_remove)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
with open(keauxdafile, 'w') as f:
    f.write(assembled)

       
    #for splits changes solo duo and squad and battlepass level properly 
with open(keauxdafile, 'r') as f:
    text = f.read()
    replacements = {
    "solo": "==SOLO",
    "duo": "==DUO",
    "squad": "==SQUAD",
    "ltm": "==LTM",
    "battlePass:": "",
    "kills:": "totalk:"
}
        
def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text
updated_text = replace_words(text, replacements)
with open(keauxdafile, 'w') as f:
    f.write(updated_text)


    #spits to sepret txt files
with open(keauxdafile, 'r') as original_file:
    content = original_file.read()

# Splitting content using regular expressions to find sections
sections = re.split(r'==\w+:', content)

if len(sections) >= 4:
    solo_section = "==SOLO:" + sections[1]
    duo_section = "==DUO:" + sections[2]
    squad_section = "==SQUAD:" + sections[3]

    with open('keauxda/keauxda-solo.txt', 'w') as section1_file:
        section1_file.write(solo_section.strip())
    
    with open('keauxda/keauxda-duo.txt', 'w') as section2_file:
        section2_file.write(duo_section.strip())
    
    with open('keauxda/keauxda-squad.txt', 'w') as section3_file:
        section3_file.write(squad_section.strip())
else:
    print("Sections not found in the expected format.")
     
   #gets BP level
keauxdalevel = 0
with open(keauxdafile, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if 'level' in field:
            keauxdalevel = field.split(':')[1].strip()                 
print(f"battlepass level: {keauxdalevel}")

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
print(f"Solo- Wins:{keauxdasolowins},  Kills: {keauxdasolokills}, Finished top 10: {keauxdasolotop10}")   
    
    
    
    
# #     #duo stats
keauxdaduowins = 0
keauxdaduokills = 0
keauxdaduotop10 = 0
with open(keauxdaduo, 'r') as file:
    content = file.read()
    fields = content.split(',')
 
    for field in fields:
        if "wins" in field: 
            keauxdaduowins = field.split(':')[1].strip()
        if 'totalk' in field:
            keauxdaduokills = field.split(':')[1].strip()
        if "top5" in field:
            keauxdaduotop5 = field.split(':')[1].strip()        
                    
print(f"Duo- Wins:{keauxdaduowins},  Kills: {keauxdaduokills}, Finished top 5: {keauxdaduotop5}")     
    
# #     #squads stats
keauxdasquadwins = 0
keauxdasquadkills = 0
keauxdasquadtop10 = 0
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
print(f"Squad- Wins:{keauxdasquadwins},  Kills: {keauxdasquadkills}, Finished top 3: {keauxdasquadtop3}")



#Solo print stats-----------------------------------------------------------------------------------------

player_stats = {
    'AK33': {
       'Battlepass level':int(AK33level), 'Solo kills': int(AK33solokills), 'Solo Wins': int(AK33solowins), 'Solo Finished top 10': int(AK33solotop10)
       
    },
    'Vector': {
       'Battlepass level':int(vectorlevel), 'Solo kills': int(vectorsolokills),  'Solo Wins': int(vectorsolowins), 'Solo Finished top 10': int(vectorsolotop10)
        
    },
    'lokey': {
       'Battlepass level':int(lokeylevel), 'Solo kills': int(lokeysolokills),  'Solo Wins': int(lokeysolowins), 'Solo Finished top 10': int(lokeysolotop10)
    },
    
    'LeFloor': {
       'Battlepass level':int(LeFloorlevel), 'Solo kills': int(LeFloorsolokills),  'Solo Wins': int(LeFloorsolowins), 'Solo Finished top 10': int(LeFloorsolotop10)
    },
    
     'ghirradeil': {
       'Battlepass level':int(ghirradeillevel), 'Solo kills': int(ghirradeilsolokills),  'Solo Wins': int(ghirradeilsolowins), 'Solo Finished top 10': int(ghirradeilsolotop10)
    },
     
     'phlash': {
       'Battlepass level':int(phlashlevel), 'Solo kills': int(phlashsolokills),  'Solo Wins': int(phlashsolowins), 'Solo Finished top 10': int(phlashsolotop10)
    },
     
     'ryptyde': {
       'Battlepass level':int(ryptydelevel), 'Solo kills': int(ryptydesolokills),  'Solo Wins': int(ryptydesolowins), 'Solo Finished top 10': int(ryptydesolotop10)
    },
     
     'sideKwinder': {
       'Battlepass level':int(sideKwinderlevel), 'Solo kills': int(sideKwindersolokills), 'Solo Wins': int(sideKwindersolowins), 'Solo Finished top 10': int(sideKwindersolotop10)
       
    },
     
     'Tandumm': {
       'Battlepass level':int(Tandummlevel), 'Solo kills': int(Tandummsolokills), 'Solo Wins': int(Tandummsolowins), 'Solo Finished top 10': int(Tandummsolotop10)
       
    },
     
     'o3zone': {
       'Battlepass level':int(o3zonelevel), 'Solo kills': int(o3zonesolokills), 'Solo Wins': int(o3zonesolowins), 'Solo Finished top 10': int(o3zonesolotop10)
       
    },
     
'keauxda': {
       'Battlepass level':int(keauxdalevel), 'Solo kills': int(keauxdasolokills), 'Solo Wins': int(keauxdasolowins), 'Solo Finished top 10': int(keauxdasolotop10)
       
    },
   }

# Define ranking function for kills in each category
def rank_players_by_category(category):
    category_stats = [(player, stats[category]) for player, stats in player_stats.items()]
    sorted_stats = sorted(category_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats

print()
print('--- Solo Stats Plus Level ---')
print()
# Generate rankings for each category
categories = ['Battlepass level', 'Solo kills', 'Solo Wins', 'Solo Finished top 10',]
rankings_data = {}  # Assuming rankings_data contains formatted rankings for each category

print_rankings = []

for category in categories:
    rankings = rank_players_by_category(category)
    category_rankings = f"--- {category.upper()} ---\n"
    for idx, (player, stat) in enumerate(rankings, start=1):
        category_rankings += f"{idx}. {player}: {stat}\n"
    rankings_data[category] = category_rankings
    print_rankings.append(category_rankings)

print("\n".join(print_rankings))

    
    
   
#website - 
st.set_page_config(page_title='Staff Fornite Rankings', layout= "centered")

st.subheader("In development")
st.title("Mcall Staff Fortnite Solo Rank")
st.write(print_rankings)







