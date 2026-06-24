# Applied ML — Industrial & Tabular

> The papers that matter for the 80% of enterprise ML that isn't generative. Tabular fraud models, sensor anomaly detection, churn — this is where most production value still lives.

## Why this category exists

The conversation in 2026 is dominated by GenAI, but most ML revenue at most companies still comes from tabular and sensor data. XGBoost remains the default and still beats deep learning on most well-curated tabular problems. The ECNN paper is on the other end of the spectrum — an industrial use case (pump monitoring) where the constraint is *low-complexity inference on edge hardware*, which a 2B-parameter model is never going to satisfy.

## Papers

| Paper | Year | What it gave us | Folder |
|---|---|---|---|
| XGBoost: A Scalable Tree Boosting System | 2016 | Regularized gradient boosting + sparsity-aware splits + cache-aware system design. Still the tabular default. | [xgboost](xgboost/) |
| ECNN: A Low-Complex, Adjustable CNN for Pump Monitoring | 2024 | Right-sized CNN architecture for industrial sensor data on constrained hardware. | [ecnn-pump-monitoring](ecnn-pump-monitoring/) |

## Demo notebook

`applied-ml-industrial.ipynb` — picks a small classification problem on tabular data (UCI adult-income or similar), fits a tuned XGBoost model end-to-end with proper cross-validation, computes SHAP values for explainability, and ends with a "what would I monitor in production" cell (calibration drift, feature distribution drift, top-N feature importance stability over time). The point is to show the *full* production loop, not just the training cell.

## My take

The most undervalued skill on an applied ML team is the ability to look at a tabular problem and recognize that it doesn't need a neural network. XGBoost, a clean feature pipeline, a calibration step, and a drift monitor will outperform a poorly-instrumented deep learning system in production every time. The frontier of "applied ML" in regulated industries is usually not better models — it's better evaluation, better monitoring, and better explainability. ECNN belongs here as a reminder that *constraint shapes architecture* — when you're targeting a vibration sensor on a pump, you don't reach for a transformer.
