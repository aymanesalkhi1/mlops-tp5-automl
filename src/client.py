import sys
import time
import statistics
import requests

port = sys.argv[1] if len(sys.argv) > 1 else '8100'
URL = f'http://127.0.0.1:{port}/invocations'

# Utilisation des colonnes exactes attendues par le schéma du modèle
CORPS = {'dataframe_records': [{'montant': 8500.0, 'heure': 14, 'age_compte': 3, 'nb_transactions_24h': 2, 'distance_domicile': 12.5}]}

r = requests.post(URL, json=CORPS, timeout=10)
print('Réponse :', r.status_code, r.json())

for _ in range(10):
    requests.post(URL, json=CORPS, timeout=10)

lat = []
for _ in range(200):
    t = time.perf_counter()
    requests.post(URL, json=CORPS, timeout=10)
    lat.append((time.perf_counter() - t) * 1000)

print(f'Port {port} | Médiane : {statistics.median(lat):.1f} ms | p95 : {statistics.quantiles(lat, n=20)[18]:.1f} ms')