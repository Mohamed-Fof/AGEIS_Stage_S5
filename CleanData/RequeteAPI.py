import requests
import csv
import time

# Utiliser une session HTTP pour réutiliser la connexion
session = requests.Session()

# Définition des indicateurs et pays
indicators = {
    "Espérance de vie à la naissance, hommes (années)": "SP.DYN.LE00.MA.IN",
    "Espérance de vie à la naissance, femmes (années)": "SP.DYN.LE00.FE.IN",    
    "Espérance de vie à la naissance à 60 ans, femmes (années)": "SP.DYN.LE60.FE.IN",
    "Espérance de vie à la naissance à 60 ans, hommes (années)": "SP.DYN.LE60.MA.IN",
    "Taux de mortalité infantile, filles (pour 1 000 naissances vivantes)": "SP.DYN.IMRT.FE.IN",
    "Taux de mortalité infantile, garçons (pour 1 000 naissances vivantes)": "SP.DYN.IMRT.MA.IN",
    "PIB par habitant ($ US courants)": "NY.GDP.PCAP.CD",
    "Gini index": "SI.POV.GINI",
    "Taux de mortalité, adultes, hommes (pour 1 000 hommes adultes)": "SP.DYN.AMRT.MA",
    "Taux de mortalité, adultes, femmes (pour 1 000 femmes adultes)": "SP.DYN.AMRT.FE",
    "Chômage, femmes (% de la population active féminine)": "SL.UEM.TOTL.FE.ZS",
    "Chômage, hommes (% de la population active masculine)": "SL.UEM.TOTL.MA.ZS",
    "Émissions de CO2 par habitant (tonnes)": "EN.GHG.CO2.PC.CE.AR5",
    "Taux de naissance, brut (pour 1 000 personnes)": "SP.DYN.CBRT.IN",
    "Population âgée de 15 à 64 ans, hommes": "SP.POP.1564.MA.IN",
    "Population âgée de 15 à 64 ans, femmes": "SP.POP.1564.FE.IN",
    "Dépenses de santé actuelles (% du PIB)": "SH.XPD.CHEX.GD.ZS",
    "Mortalité prématurée par maladies cardiovasculaires, cancer, diabète ou maladies respiratoires chroniques (femmes, 30-70 ans)": "SH.DYN.NCOM.FE.ZS",
    "Mortalité prématurée par maladies cardiovasculaires, cancer, diabète ou maladies respiratoires chroniques (hommes, 30-70 ans)": "SH.DYN.NCOM.MA.ZS",
    "Incidence du VIH (% de la population de 15 à 49 ans)": "SH.HIV.INCD.ZS",
    "Prévalence du VIH, total (% de la population âgée de 15 à 49 ans)": "SH.DYN.AIDS.ZS",
    "Population âgée de 0 à 4 ans, filles (% de la population féminine)": "SP.POP.0004.FE.5Y",
    "Population âgée de 0 à 4 ans, garçons (% de la population masculine)": "SP.POP.0004.MA.5Y",
    "Population âgée de 5 à 9 ans, filles (% de la population féminine)": "SP.POP.0509.FE.5Y",
    "Population âgée de 5 à 9 ans, garçons (% de la population masculine)": "SP.POP.0509.MA.5Y",
    "Population âgée de 10 à 14 ans, filles (% de la population féminine)": "SP.POP.1014.FE.5Y",
    "Population âgée de 10 à 14 ans, garçons (% de la population masculine)": "SP.POP.1014.MA.5Y",
    "Population âgée de 15 à 19 ans, filles (% de la population féminine)": "SP.POP.1519.FE.5Y",
    "Population âgée de 15 à 19 ans, garçons (% de la population masculine)": "SP.POP.1519.MA.5Y",
    "Population âgée de 20 à 24 ans, femmes (% de la population féminine)": "SP.POP.2024.FE.5Y",
    "Population âgée de 20 à 24 ans, hommes (% de la population masculine)": "SP.POP.2024.MA.5Y",
    "Population âgée de 25 à 29 ans, femmes (% de la population féminine)": "SP.POP.2529.FE.5Y",
    "Population âgée de 25 à 29 ans, hommes (% de la population masculine)": "SP.POP.2529.MA.5Y",
    "Population âgée de 30 à 34 ans, femmes (% de la population féminine)": "SP.POP.3034.FE.5Y",
    "Population âgée de 30 à 34 ans, hommes (% de la population masculine)": "SP.POP.3034.MA.5Y",
    "Population âgée de 35 à 39 ans, femmes (% de la population féminine)": "SP.POP.3539.FE.5Y",
    "Population âgée de 35 à 39 ans, hommes (% de la population masculine)": "SP.POP.3539.MA.5Y",
    "Population âgée de 40 à 44 ans, femmes (% de la population féminine)": "SP.POP.4044.FE.5Y",
    "Population âgée de 40 à 44 ans, hommes (% de la population masculine)": "SP.POP.4044.MA.5Y",
    "Population âgée de 45 à 49 ans, femmes (% de la population féminine)": "SP.POP.4549.FE.5Y",
    "Population âgée de 45 à 49 ans, hommes (% de la population masculine)": "SP.POP.4549.MA.5Y",
    "Population âgée de 50 à 54 ans, femmes (% de la population féminine)": "SP.POP.5054.FE.5Y",
    "Population âgée de 50 à 54 ans, hommes (% de la population masculine)": "SP.POP.5054.MA.5Y",
    "Population âgée de 55 à 59 ans, femmes (% de la population féminine)": "SP.POP.5559.FE.5Y",
    "Population âgée de 55 à 59 ans, hommes (% de la population masculine)": "SP.POP.5559.MA.5Y",
    "Population âgée de 60 à 64 ans, femmes (% de la population féminine)": "SP.POP.6064.FE.5Y",
    "Population âgée de 60 à 64 ans, hommes (% de la population masculine)": "SP.POP.6064.MA.5Y",
    "Population âgée de 65 à 69 ans, femmes (% de la population féminine)": "SP.POP.6569.FE.5Y",
    "Population âgée de 65 à 69 ans, hommes (% de la population masculine)": "SP.POP.6569.MA.5Y",
    "Population âgée de 70 à 74 ans, femmes (% de la population féminine)": "SP.POP.7074.FE.5Y",
    "Population âgée de 70 à 74 ans, hommes (% de la population masculine)": "SP.POP.7074.MA.5Y",
    "Population âgée de 75 à 79 ans, femmes (% de la population féminine)": "SP.POP.7579.FE.5Y",
    "Population âgée de 75 à 79 ans, hommes (% de la population masculine)": "SP.POP.7579.MA.5Y",
    "Population âgée de 80 ans et plus, femmes (% de la population féminine)": "SP.POP.80UP.FE.5Y",
    "Population âgée de 80 ans et plus, hommes (% de la population masculine)": "SP.POP.80UP.MA.5Y"
}

countries = {
    "Afrique du Sud": "ZAF",
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
    "États-Unis": "USA"
}

years = list(range(2000, 2024))

# Fonction pour récupérer les données avec gestion des erreurs et pause exponentielle
def fetch_indicator_data(country_code, indicator_code, max_retries=3):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?date=2000:2023&format=json&per_page=1000"
    for attempt in range(max_retries):
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()  # Lève une exception pour les erreurs HTTP
            data = response.json()
            if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list):
                return data[1]
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête (tentative {attempt+1}/{max_retries}) pour {country_code} - {indicator_code}: {e}")
            time.sleep(2 ** attempt)  # Pause exponentielle avant de réessayer
    print(f"Échec pour {country_code} - {indicator_code}")
    return []

# Nom du fichier CSV
output_file = "BdAPI.csv"

# Création des colonnes du fichier CSV
fieldnames = ["Année", "Pays", "Code Pays"] + list(indicators.keys())

# Initialiser la liste des données
data_rows = []

for year in years:
    for country_name, country_code in countries.items():
        row_data = {"Année": year, "Pays": country_name, "Code Pays": country_code}
        for indicator_name, indicator_code in indicators.items():
            print(f"Récupération des données {year} - {country_name} - {indicator_name}...")
            data = fetch_indicator_data(country_code, indicator_code)
            for entry in data:
                if isinstance(entry, dict) and entry.get("date") == str(year):
                    value = entry.get("value")
                    row_data[indicator_name] = value
        data_rows.append(row_data)

# Écriture des données dans un fichier CSV
#with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
#    writer.writeheader()
 #   writer.writerows(data_rows)

#print(f"Les données ont été enregistrées dans le fichier : {output_file}")
# Chemin vers le dossier "Bureau/L3MIASHS/Stage"
dossier = os.path.expanduser("~/Desktop/L3MIASHS/Stage")

# Écriture des données dans un fichier CSV
with open("BdAPI.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Année", "Pays", "Code Pays"] + list(indicators.keys()))
    writer.writeheader()
    writer.writerows(data_rows)

print(f"Les données ont été enregistrées dans le fichier : BdAPI.csv")
