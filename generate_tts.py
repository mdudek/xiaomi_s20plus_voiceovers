import os
from google.cloud import texttospeech
from pathlib import Path


#Vytvoření klíče služebního účtu
#Vytvořte služební účet:

#Otevřete IAM & Admin > Service Accounts.
#Klikněte na Create Service Account, zadejte název (např. tts-account), přejděte k dalšímu kroku a vyberte roli Text-to-Speech User.
#Stáhněte JSON klíč:

#Po vytvoření klikněte na Manage Keys > Add Key > Create New Key.
#Zvolte JSON a uložte soubor na svůj počítač (např. key.json).

# Nastavení cesty ke klíči
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"  # Nahraďte názvem vašeho klíče

# Inicializace klienta
client = texttospeech.TextToSpeechClient()

# Nastavení hlasu a výstupu
voice = texttospeech.VoiceSelectionParams(
    language_code="cs-CZ",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    sample_rate_hertz=16000
)

# Hlášky
hlaseni = {
    # 01 & 02 files are melodies
    "10": "Zapínám",
    "20": "Vypínám",
    "30": "Před vypnutím odpojte robotický vysavač z nabíjecí stanice",
    "40": "Spouštím obnovení továrního nastavení",
    "50": "Systémová nastavení byla obnovena",
    "60": "Čekání na konfiguraci sítě",
    "61": "Pro další funkce si stáhněte aplikaci Xiaomi Home a připojte se k ní",
    "70": "Nelze navázat připojení k síti, zkontrolujte a zkuste znovu",
    "80": "Nelze navázat připojení k serveru, zkontrolujte a zkuste znovu",
    "90": "Připojeno k síti",
    "100": "Připojení k síti bylo úspěšně navázáno",
    "110": "Začínám plánovaný úklid",
    "130": "Začínám úklid",
    "140": "Začínám úklid ve vlastním režimu",
    "150": "Začínám vlastní úklid",
    "151": "Spouštím úlohu úklidu ve vlastním režimu",
    "160": "Začínám rychlé vytvoření mapy",
    "170": "Úklid pozastaven",
    "180": "Pokračuji v úklidu",
    "190": "Úklid pokračuje",
    "200": "Vytváření mapy pokračuje",
    "201": "Ukončuji úklid",
    "202": "Vytváření mapy dokončeno",
    "210": "Úklid dokončen. Vracím se na nabíjecí stanici",
    "220": "Tvorba mapy dokončena. Vracím se na nabíjecí stanici",
    "230": "Začínám návrat na nabíjecí stanici",
    "240": "Nízký stav baterie, robotický vysavač se vrátí na nabíjecí stanici a po úplném nabití bude pokračovat v úkolu",
    "250": "Nízký stav baterie, vracím se na nabíjecí stanici",
    "260": "Nízký stav baterie, vyčkejte, dokud se zařízení nenabije",
    "270": "Přesuňte robotický vysavač zpět na nabíjecí stanici",
    "280": "Robotický vysavač je již na nabíjecí stanici",
    "290": "Nízký stav baterie, robotický vysavač je třeba nabít",
    "300": "Nízký stav baterie, robotický vysavač se brzy vypne",
    "301": "Pro dosažení optimálních výsledků používejte zařízení po úplném nabití",
    "310": "Začínám se nabíjet",
    "320": "Zastavení návratu na nabíjecí stanici",
    "350": "Nainstalujte sběrnou nádobu na prach",
    "370": "Odnímatelný mop odpojen, před použitím jej znovu připojte",
    "380": "Odnímatelný mop nainstalován",
    "390": "Odnímatelný mop odpojen",
    "400": "Úkol dokončen, je třeba vyjmout a vyčistit mopovací podložku",
    "410": "Sběrná nádoba na prach byla vyjmuta",
    "420": "Sběrná nádoba na prach byla nainstalována",
    "430": "Probíhá aktualizace. Nevypínejte robotický vysavač a nespouštějte úklid",
    "431": "Aktualizace se nezdařila, přesuňte robotický vysavač na nabíjecí stanici a zkuste to znovu, až bude baterie alespoň na 30 %",
    "440": "Aktualizace proběhla úspěšně",
    "450": "Aktualizace se nezdařila, zkuste to znovu",
    "460": "Aktualizuji systém, zkuste to později",
    "470": "Robotický vysavač se přesouvá, prosím, ustupte",
    "480": "Detekována nová oblast, robotický vysavač zahájí nový úklid",
    "490": "Přesun byl dokončen, pokračuji v úklidu",
    "491": "Detekována nová oblast, robotický vysavač zahájí nový proces mapování",
    "492": "Umístění bylo úspěšně určeno, pokračujte v tvorbě mapy",
    "500": "Přesun byl úspěšně dokončen, robotický vysavač se vrátí na nabíjecí stanici",
    "510": "Detekována nová oblast, robotický vysavač se vrátí na nabíjecí stanici",
    "520": "Robotický vysavač je zde! Robotický vysavač je zde! Robotický vysavač je zde!",
    "530": "Spouštím režim dálkového ovládání",
    "540": "Ukončuji režim dálkového ovládání",
    "550": "Dětská pojistka byla zapnuta, všechna tlačítka jsou zablokována",
    "560": "Dětská pojistka byla vypnuta, všechna tlačítka jsou odblokována",
    "570": "Všechna tlačítka jsou zablokována, pro odblokování podržte tlačítko návratu na dokovací stanici",
    "580": "Chyba kvůli teplotě baterie, počkejte, dokud se teplota nevrátí do normálu",
    "590": "Chyba kartáče, zkontrolujte a vyčistěte jej",
    "600": "Chyba bočního kartáče, zkontrolujte a vyčistěte jej",
    "610": "Chyba hnacího kola, zkontrolujte a vyčistěte jej",
    "630": "Očistěte senzory proti pádu a přemístěte robotický vysavač na nové místo a spusťte",
    "640": "Chyba ventilátoru, zkontrolujte a vyčistěte filtr prachového zásobníku a vzduchovod",
    "650": "Chyba nárazníku, zkontrolujte, zda nárazník správně pruží",
    "660": "Chyba nabíjení, zkuste vyčistit nabíjecí kontakty",
    "670": "Chyba laserového senzoru, zkontrolujte a vyčistěte jej",
    "680": "Zkontrolujte, zda nedošlo k zaseknutí ochranného krytu laserového senzoru",
    "690": "Chyba hraničního senzoru, zkontrolujte a vyčistěte jej",
    "700": "Zkuste vyčistit laserový senzor pro sledování směru",
    "710": "Chyba zásobníku vody mopovací podložky, zkontrolujte a vyčistěte jej",
    "720": "Robotický vysavač je zaseknutý, přemístěte jej na jiné místo a spusťte",
    "730": "Robotický vysavač uvázl ve vzduchu, přemístěte jej na jiné místo a spusťte",
    "740": "Robotický vysavač je nakloněný, přemístěte jej na jiné místo a spusťte",
    "750": "Na trase úklidu je překážka, odstraňte ji",
    "760": "Nelze se dostat do cílové oblasti, úklid nebyl dokončen, vracím se na nabíjecí stanici",
    "771": "Nelze najít cílovou oblast, úklid nebyl dokončen, vracím se na nabíjecí stanici",
    "780": "Robotický vysavač se nachází v zakázané zóně, přemístěte jej na mimo tuto oblast a spusťte",
    "910": "Odstraňte robotický vysavač z koberce"
    # Přidejte další hlášky zde
}

# Generování MP3 souborů
for cislo, text in hlaseni.items():
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    output_file = Path(f"mp3/{cislo}.mp3")
    output_file.parent.mkdir(exist_ok=True, parents=True)
    # Uložení MP3 souboru
    with open(output_file, "wb") as audio_file:
        audio_file.write(response.audio_content)
        print(f"Soubor {cislo}.mp3 vytvořen.")
