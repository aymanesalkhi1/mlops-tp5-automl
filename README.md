# Register and promote an AutoML model

The FLAML search is exported to a scikit-learn estimator, registered in MLflow as `fraude-automl`, then promoted with the `production` alias.

MLflow runs locally at `http://127.0.0.1:5000`. `donnees.py` rebuilds `data/transactions.csv`, the same generator as in the previous lab.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install mlflow flaml scikit-learn pandas joblib
python donnees.py
python src/automl_deploy.py
python src/promouvoir.py fraude-automl
```

`src/modele_manuel.py` trains a comparison model. `src/client.py` calls the promoted model.
