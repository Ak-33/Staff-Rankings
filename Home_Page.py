import streamlit as st
import fortnite_api 
from fortnite_api import TimeWindow
from fortnite_api import AccountType
import re
import string 

api = fortnite_api.FortniteAPI(api_key='8eeca9b5-14ca-4afd-91d6-aed25f55d5b7')
symbols_to_keep = ":," 
punctuation_to_remove =''.join(c for c in string.punctuation if c not in symbols_to_keep)

    #user_names
Ak33_name ='AK33_' 
vector_name ='VECtOR8547'
lokey_name='CoarseCat'
LeFloor_name ='TROLLSphincter'
ghirradeil_name ='FossilArcher'
phlash_name ='SlimJimothy2907'
ryptyde_name ='Ryptyde15'
sideKwinder_name ='calebjennings922'
Tandumm_name ='Tandumm24'
o3zone_name ='Samuel517'
keauxda_name ='KeauXDa'
mulligan_name = "ChristianKid18"
mcfly_name ='Admiral_pile'
saitama_name ='Kmoore123'
trubadoor_name ='Trub8door'
romKulus_name ='Cr1spyNugg3t'
can_nun_name ='can-nun'

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

st.set_page_config(
    page_title="McCall Staff Rankings",
    page_icon="🔫",
    layout= "wide"
)


with st.spinner("# Please wait - Do not select a category until done"):
    st.sidebar.success("Select a stat category from above")
    url = "https://www.scbaptist.org/campmccall/"
    Purl = 'https://pixsolsprops.com/'

    st.title("Welcome to the McCall Staff Fortnite Rankings")
    st.subheader("How Refreash data:")
    st.write("""After wainting on this initial loading screen all data will be loaded. Do not retern to the "Home Page" unless you want to refreash the data.""")
    st.write("This is a python script I wrote so me and my staff brothers can compare one another in fortnite. If you want to learn more about Camp McCall vist this [link](%s)." % url, """Also, the maker for this site (Pixsol) has a personal Webpage called "[PixsolsProps](%s)" feel free give it a visit""" % Purl)
    st.caption (""""McCall Staff Rankings" is not endorsed nor partnered with, Camp McCall or the SCBC in any offical capacity""")



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

        with open('pages/pixsol/Ak33-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/pixsol/AK33-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/pixsol/AK33-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")

    #mcfly---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=mcfly_name, time_window=TimeWindow.SEASON,account_type=AccountType.PSN )

    with open(mcflyfile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("mcflys's Data written successfully!------------")

    with open(mcflyfile, 'r') as file:
        content = file.read()

    #gets rid of unneeded punctuation
    with open(mcflyfile, 'r') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", punctuation_to_remove)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
    with open(mcflyfile, 'w') as f:
        f.write(assembled)

        
        #for splits changes solo duo and squad and battlepass level properly 
    with open(mcflyfile, 'r') as f:
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
    with open(mcflyfile, 'w') as f:
        f.write(updated_text)


        #spits to sepret txt files
    with open(mcflyfile, 'r') as original_file:
        content = original_file.read()

    # Splitting content using regular expressions to find sections
    sections = re.split(r'==\w+:', content)

    if len(sections) >= 4:
        solo_section = "==SOLO:" + sections[1]
        duo_section = "==DUO:" + sections[2]
        squad_section = "==SQUAD:" + sections[3]

        with open('pages/mcfly/mcfly-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/mcfly/mcfly-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/mcfly/mcfly-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/vector/vector-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/vector/vector-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/vector/vector-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")

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

        with open('pages/lokey/lokey-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/lokey/lokey-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/lokey/lokey-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/LeFloor/LeFloor-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/LeFloor/LeFloor-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/LeFloor/LeFloor-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/ghirradeil/ghirradeil-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/ghirradeil/ghirradeil-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/ghirradeil/ghirradeil-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
    #phlash---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=phlash_name, time_window=TimeWindow.SEASON)

    with open(phlashfile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("phlash's Data written successfully!------------")

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

        with open('pages/phlash/phlash-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/phlash/phlash-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/phlash/phlash-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/ryptyde/ryptyde-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/ryptyde/ryptyde-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/ryptyde/ryptyde-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/sideKwinder/sideKwinder-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/sideKwinder/sideKwinder-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/sideKwinder/sideKwinder-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")

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

        with open('pages/Tandumm/Tandumm-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/Tandumm/Tandumm-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/Tandumm/Tandumm-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/o3zone/o3zone-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/o3zone/o3zone-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/o3zone/o3zone-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
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

        with open('pages/keauxda/keauxda-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/keauxda/keauxda-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/keauxda/keauxda-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
    #mulligan---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=mulligan_name, time_window=TimeWindow.SEASON)

    with open(mulliganfile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("mulligans's Data written successfully!------------")

    with open(mulliganfile, 'r') as file:
        content = file.read()

    #gets rid of unneeded punctuation
    with open(mulliganfile, 'r') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", punctuation_to_remove)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
    with open(mulliganfile, 'w') as f:
        f.write(assembled)

        
        #for splits changes solo duo and squad and battlepass level properly 
    with open(mulliganfile, 'r') as f:
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
    with open(mulliganfile, 'w') as f:
        f.write(updated_text)


        #spits to sepret txt files
    with open(mulliganfile, 'r') as original_file:
        content = original_file.read()

    # Splitting content using regular expressions to find sections
    sections = re.split(r'==\w+:', content)

    if len(sections) >= 4:
        solo_section = "==SOLO:" + sections[1]
        duo_section = "==DUO:" + sections[2]
        squad_section = "==SQUAD:" + sections[3]

        with open('pages/mulligan/mulligan-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/mulligan/mulligan-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/mulligan/mulligan-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")

    #saitama---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=saitama_name, time_window=TimeWindow.SEASON, account_type=AccountType.XBL)

    with open(saitamafile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("saitamas's Data written successfully!------------")

    with open(saitamafile, 'r') as file:
        content = file.read()

    #gets rid of unneeded punctuation
    with open(saitamafile, 'r') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", punctuation_to_remove)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
    with open(saitamafile, 'w') as f:
        f.write(assembled)

        
        #for splits changes solo duo and squad and battlepass level properly 
    with open(saitamafile, 'r') as f:
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
    with open(saitamafile, 'w') as f:
        f.write(updated_text)


        #spits to sepret txt files
    with open(saitamafile, 'r') as original_file:
        content = original_file.read()

    # Splitting content using regular expressions to find sections
    sections = re.split(r'==\w+:', content)

    if len(sections) >= 4:
        solo_section = "==SOLO:" + sections[1]
        duo_section = "==DUO:" + sections[2]
        squad_section = "==SQUAD:" + sections[3]

        with open('pages/saitama/saitama-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/saitama/saitama-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/saitama/saitama-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
    #trubadoor---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=trubadoor_name, time_window=TimeWindow.SEASON, account_type=AccountType.XBL)

    with open(trubadoorfile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("trubadoors's Data written successfully!------------")

    with open(trubadoorfile, 'r') as file:
        content = file.read()

    #gets rid of unneeded punctuation
    with open(trubadoorfile, 'r') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", punctuation_to_remove)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
    with open(trubadoorfile, 'w') as f:
        f.write(assembled)

        
        #for splits changes solo duo and squad and battlepass level properly 
    with open(trubadoorfile, 'r') as f:
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
    with open(trubadoorfile, 'w') as f:
        f.write(updated_text)


        #spits to sepret txt files
    with open(trubadoorfile, 'r') as original_file:
        content = original_file.read()

    # Splitting content using regular expressions to find sections
    sections = re.split(r'==\w+:', content)

    if len(sections) >= 4:
        solo_section = "==SOLO:" + sections[1]
        duo_section = "==DUO:" + sections[2]
        squad_section = "==SQUAD:" + sections[3]

        with open('pages/trubadoor/trubadoor-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/trubadoor/trubadoor-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/trubadoor/trubadoor-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
    #romKulus---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=romKulus_name, time_window=TimeWindow.SEASON)

    with open(romKulusfile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("romKuluss's Data written successfully!------------")

    with open(romKulusfile, 'r') as file:
        content = file.read()

    #gets rid of unneeded punctuation
    with open(romKulusfile, 'r') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", punctuation_to_remove)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
    with open(romKulusfile, 'w') as f:
        f.write(assembled)

        
        #for splits changes solo duo and squad and battlepass level properly 
    with open(romKulusfile, 'r') as f:
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
    with open(romKulusfile, 'w') as f:
        f.write(updated_text)


        #spits to sepret txt files
    with open(romKulusfile, 'r') as original_file:
        content = original_file.read()

    # Splitting content using regular expressions to find sections
    sections = re.split(r'==\w+:', content)

    if len(sections) >= 4:
        solo_section = "==SOLO:" + sections[1]
        duo_section = "==DUO:" + sections[2]
        squad_section = "==SQUAD:" + sections[3]

        with open('pages/romKulus/romKulus-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/romKulus/romKulus-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/romKulus/romKulus-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")
        
    #can_nun---------------------------------------------------------------------------
    player_stats = api.stats.fetch_by_name(name=can_nun_name, time_window=TimeWindow.SEASON)

    with open(can_nunfile, 'w') as file:
            
            for attribute in dir(player_stats):
                if not attribute.startswith('__'):  # Skip special attributes
                    value = getattr(player_stats, attribute)
                    file.write(f"{attribute}: {str(value)}\n")  # Write attribute and value to file
    print("can_nuns's Data written successfully!------------")

    with open(can_nunfile, 'r') as file:
        content = file.read()

    #gets rid of unneeded punctuation
    with open(can_nunfile, 'r') as f:
        text = f.read()
        words = text.split()
        table = str.maketrans("", "", punctuation_to_remove)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
    with open(can_nunfile, 'w') as f:
        f.write(assembled)

        
        #for splits changes solo duo and squad and battlepass level properly 
    with open(can_nunfile, 'r') as f:
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
    with open(can_nunfile, 'w') as f:
        f.write(updated_text)


        #spits to sepret txt files
    with open(can_nunfile, 'r') as original_file:
        content = original_file.read()

    # Splitting content using regular expressions to find sections
    sections = re.split(r'==\w+:', content)

    if len(sections) >= 4:
        solo_section = "==SOLO:" + sections[1]
        duo_section = "==DUO:" + sections[2]
        squad_section = "==SQUAD:" + sections[3]

        with open('pages/can_nun/can_nun-solo.txt', 'w') as section1_file:
            section1_file.write(solo_section.strip())
        
        with open('pages/can_nun/can_nun-duo.txt', 'w') as section2_file:
            section2_file.write(duo_section.strip())
        
        with open('pages/can_nun/can_nun-squad.txt', 'w') as section3_file:
            section3_file.write(squad_section.strip())
    else:
        print("Sections not found in the expected format.")     
           
st.success('Thank you for waiting! You may now select a category! Only Retern to the "Home Page" if you want to refreash the data.')    
