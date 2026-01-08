import requests
import csv
import time
import os
# ===========================
# Configuration générale
# ===========================

# Années souhaitées
years = list(range(2000, 2022))

# Indicateurs
indicators = {
    "Espérance de vie à la naissance, hommes (années)": "SP.DYN.LE00.MA.IN",
    "Dépenses publiques générales de santé (% des dépenses courantes de santé)": "SH.XPD.GHED.CH.ZS",
}

# Pays 
countries = { "Afrique du Sud": "ZAF", 
             "Allemagne": "DEU", 
             "Brésil": "BRA", 
             "Canada": "CAN", 
             "Chine": "CHN", 
             "Chili": "CHL", 
             "Corée du Sud": "KOR", 
             "Côte d'Ivoire": "CIV", 
             "Espagne": "ESP", 
             "France": "FRA", 
             "Inde": "IND", 
             "Indonésie": "IDN", 
             "Iran": "IRN", 
             "Japon": "JPN", 
             "Maroc": "MAR", 
             "Mexique": "MEX", 
             "Nigeria": "NGA", 
             "Pérou": "PER", 
             "Royaume-Uni": "GBR", 
             "Russie": "RUS", 
             "Sénégal": "SEN", 
             "Suède": "SWE", 
             "Suisse": "CHE", 
             "Togo": "TGO", 
             "Turquie": "TUR",
             "États-Unis": "USA" }

# Nom du fichier de sortie
output_file = os.path.join(os.getcwd(), "BdAPI.csv")

# ===========================
# Fonction de récupération
# ===========================

def fetch_indicator_data(country_code, indicator_code, max_retries=5):
    """
    Récupère les données d'un indicateur pour un pays donné.
    """
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?date=2000:2022&format=json&per_page=2000"
    session = requests.Session()

    for attempt in range(max_retries):
        try:
            print(f"Tentative {attempt+1}/{max_retries} pour {country_code} - {indicator_code}")
            response = session.get(url, timeout=60)  # Timeout augmenté à 30s
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list):
                return data[1]
            else:
                print(f"Aucune donnée pour {country_code} - {indicator_code}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Erreur API ({attempt+1}/{max_retries}) : {e}")
            time.sleep(2**attempt + 1)  # Attente progressive
    print(f"ÉCHEC API : {country_code} - {indicator_code}")
    return []

# ===========================
# Collecte des données
# ===========================

print(">>> Le script Data.py a bien démarré")

fieldnames = ["Année", "Pays", "Code Pays"] + list(indicators.keys())
data_rows = []

for year in years:
    for country_name, country_code in countries.items():
        row_data = {"Année": year, "Pays": country_name, "Code Pays": country_code}
        for indicator_name, indicator_code in indicators.items():
            print(f"Récupération {year} - {country_name} - {indicator_name} ...")
            data = fetch_indicator_data(country_code, indicator_code)
            if data:
                for entry in data:
                    if isinstance(entry, dict) and entry.get("date") == str(year):
                        row_data[indicator_name] = entry.get("value")
        data_rows.append(row_data)

# ===========================
# Sauvegarde CSV
# ===========================

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_rows)

print(f">>> Fin du script Data.py. Les données ont été enregistrées dans le fichier : {output_file}")
