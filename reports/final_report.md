# Final Project Report: Mushroom Yield Forecast & Automation Pipeline

## 1. Executive Summary
The goal of this project was to design, develop, and deploy an end-to-end machine learning solution to optimize and predict crop yields within a controlled-environment mushroom cultivation facility. By leveraging real-time sensor streams tracking environmental indicators (Temperature, Humidity, and $CO_2$ levels), the system implements a predictive framework to assist growers in maintaining optimal cultivation conditions, maximizing output efficiency, and mitigating crop failure risks. The final pipeline is fully containerized, integrated into a continuous version-control workflow, and deployed to a public cloud environment with automated infrastructure monitoring.

---

## 2. Problem Statement & Objectives
Mushroom cultivation is highly sensitive to subtle fluctuations in microclimatic conditions. Traditional manually observed systems often fail to react quickly enough to rapid shifts in air matrix attributes, resulting in suboptimal yields or devastating crop diseases. 

### Key Project Objectives:
* **Predictive Performance:** Develop a robust regression pipeline to forecast real-time mushroom yield ($kg/m^2$).
* **Interactive UI Interface:** Construct a lightweight dashboard enabling growers to input sensor values manually and receive rapid yield estimations.
* **Production Deployment:** Host the system securely via a public cloud instance accessible to stakeholders.
* **MLOps Foundations:** Implement an architectural framework tracking data drifting, model decay, and logging to trigger structured retraining schedules.

---

## 3. Dataset & Feature Engineering
The model utilizes a comprehensive dataset containing continuous environmental parameters linked directly to final production metrics.

### Feature Matrix Overview:
* **Temperature (°C):** Regulates mycelium vegetative expansion and subsequent fruiting bodies.
* **Humidity (%):** Maintains the high-moisture environment crucial for cap development.
* **$CO_2$ Concentration (ppm):** Higher concentrations support mycelial run, while lower levels trigger pinning and growth.

### Preprocessing Pipeline:
1. **Missing Value Imputation:** Handled via forward-fill mechanisms matching sequential time-series trends.
2. **Feature Scaling:** Applied a standard `StandardScaler` transformation pipeline to stabilize distance-based coefficients and gradient optimization during training:
   
   $$z = \frac{x - \mu}{\sigma}$$

---

## 4. Model Exploration & Performance Evaluation
Multiple model candidates were tested during the prototyping phase, including Linear Regression, Decision Tree Regressors, and Random Forest Ensembles. 

### Final Model Selection:
The **Random Forest Regressor** (or chosen model architecture) was selected as the final production algorithm due to its robust ability to capture non-linear feature interactions without overfitting.

### Production Validation Metrics:
* **Mean Absolute Error (MAE):** Measures average magnitude of prediction errors.
* **Root Mean Squared Error (RMSE):** Penalizes extreme structural variance errors.
* **$R^2$ Score:** Indicates percentage of variance explained by environmental features.

---

## 5. System Architecture & Deployment Infrastructure
The system has been designed with a modular architecture to separate the raw modeling assets from the interactive presentation layer.### Production Infrastructure:
* **Interface Layer:** Developed via **Streamlit**, providing a clean, responsive UI with sliders mimicking physical environment sensors.
* **Hosting Platform:** Publicly hosted on **Streamlit Community Cloud**, connected via continuous integration to the GitHub repository branch.
* **Live Deployment URL:** [Mushroom Yield Predictor Dashboard](https://3vfdteee7bjgdqemjtu44k.streamlit.app)

---

## 6. MLOps, Logging & Monitoring Framework
To prevent production degradation due to seasonal variations or sensor degradation, an active monitoring pipeline is coupled with the live UI.

* **Telemetry Logs:** Every incoming user prediction, alongside its evaluated timestamp and input parameters, is routed directly to `logs/app_monitoring.log`.
* **Retraining Triggers:** Model degradation checks are scheduled to monitor cumulative error trends. Outlined in `monitoring.md`, performance drops below defined thresholds or extensive data drift triggers an automated pipeline to pull recent telemetry records and re-optimize weights.

---

## 7. Conclusions & Future Work
Task 9 has been successfully finalized. The model is fully integrated into a stable public web infrastructure, ensuring instant prediction deliveries. 

Future iterations will look to integrate automated IoT hardware webhooks to feed data straight into the inference endpoint without manual user slider inputs, closing the loop on a fully automated smart-farming facility.
## 10. Engineering Reflection
Building this end-to-end MLOps pipeline provided invaluable hands-on experience balancing model predictive power with operational deployment guardrails. Navigating data transformations without introducing future leakage during temporal cross-validation highlighted the nuances of production-grade time-series engineering. Transitioning the system from a localized development container to a live cloud architecture running on Streamlit Community Cloud made the abstract concepts of continuous integration and monitoring tangible, laying a rock-solid foundation for future edge IoT automation systems.

## 11. Live Application Preview
![Streamlit Production UI Dashboard](../app_demo.png)