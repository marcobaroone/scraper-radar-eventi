import requests
from bs4 import BeautifulSoup
import json

localita_target = [
    "Rionero", "Atella", "Melfi", "Rapolla", "Monticchio", "Lagopesole", "Filiano"
]

url = "https://www.eventiesagre.it/Eventi_Vari/21151774_Calendario+Mensile+Eventi+E+Sagre+Regione+Basilicata.html"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

eventi = []

for p in soup.find_all("p"):
    testo = p.get_text(strip=True)
    for luogo in localita_target:
        if luogo.lower() in testo.lower():
            parti = testo.split(" - ")
            if len(parti) >= 2:
                data = parti[0].strip()
                titolo = " - ".join(parti[1:]).strip()
                eventi.append({
                    "Nome Evento": titolo,
                    "Data Evento": data,
                    "Località": luogo,
                    "Categoria": "Sagra",
                    "Fonte": url
                })

with open("eventi_radar.json", "w") as f:
    json.dump(eventi, f, indent=2)

print(f"{len(eventi)} eventi salvati.")
