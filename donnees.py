import numpy as np
import pandas as pd
from pathlib import Path

Path('data').mkdir(exist_ok=True)
np.random.seed(42)
n_samples = 5000

montant = np.random.exponential(scale=100, size=n_samples) + 5
heure = np.random.randint(0, 24, size=n_samples)
age_compte = np.random.randint(1, 3650, size=n_samples)
nb_transactions_24h = np.random.poisson(lam=3, size=n_samples)
distance_domicile = np.random.exponential(scale=20, size=n_samples)

score = (
    (montant > 300).astype(int) * 1.5 +
    ((heure < 5) | (heure > 23)).astype(int) * 2.0 +
    (age_compte < 30).astype(int) * 1.5 +
    (nb_transactions_24h > 7).astype(int) * 1.8 +
    (distance_domicile > 80).astype(int) * 1.2 +
    np.random.normal(0, 1, size=n_samples)
)

fraude = (score > 3.5).astype(int)

df = pd.DataFrame({
    'montant': np.round(montant, 2),
    'heure': heure,
    'age_compte': age_compte,
    'nb_transactions_24h': nb_transactions_24h,
    'distance_domicile': np.round(distance_domicile, 2),
    'fraude': fraude
})

df.to_csv('data/transactions.csv', index=False)
print("Données générées dans data/transactions.csv avec", len(df), "lignes.")
