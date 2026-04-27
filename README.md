# Climate Challenge Week 0

## Setup Instructions

1. Clone repository
2. Create virtual environment
3. Activate virtual environment
4. Install requirements

```bash
pip install -r requirements.txt


# 🌍 Cross-Country Climate Analysis (Africa)

## 📌 Project Overview

This project presents a comparative climate analysis of five African countries: **Sudan, Tanzania, Ethiopia, Kenya, and Nigeria**.  
The goal is to understand how key meteorological variables interact across different climate zones and how these relationships differ geographically.

We focus on:
- Temperature dynamics
- Humidity influence
- Rainfall behavior
- Wind patterns
- Surface pressure effects
- Seasonal variation

This is a foundational **exploratory data analysis (EDA)** project in climate data science.

---

## 📊 Dataset Description

The dataset includes daily or monthly aggregated climate variables:

- **T2M** → Average temperature (2 meters above ground)
- **T2M_MAX** → Maximum temperature
- **T2M_MIN** → Minimum temperature
- **RH2M** → Relative humidity
- **QV2M** → Specific humidity
- **PRECTOTCORR** → Precipitation (corrected total)
- **WS2M** → Wind speed (2 meters)
- **WS2M_MAX** → Maximum wind speed
- **PS** → Surface pressure
- **DOY** → Day of year
- **Month** → Month index

---

## 🌡️ 1. The Temperature “Trifecta”

Temperature variables show strong internal relationships across all countries.

### 🔥 General Pattern (All Countries)
- T2M ↔ T2M_MAX → Strong positive correlation (0.65 – 0.94)
- T2M ↔ T2M_MIN → Strong to moderate positive correlation (0.52 – 0.95)

✔ Average temperature is strongly driven by both daily maximum and minimum temperatures.

---

### 🌵 Sudan (Arid Climate)
- T2M ↔ T2M_MIN: **0.94**
- T2M ↔ T2M_MAX: **0.93**

✔ Very strong and balanced temperature influence  
✔ Strong day-night temperature cycle effect

---

### 🌧️ Tanzania (Tropical Climate)
- T2M ↔ T2M_MIN: **0.95**

✔ Nighttime temperatures dominate average climate behavior  
✔ High humidity stabilizes temperature variation

---

### 🌿 Ethiopia (Highland Climate)
- T2M ↔ T2M_MAX: **0.65**
- T2M ↔ T2M_MIN: **0.72**

✔ Moderate relationships due to elevation effects  
✔ Terrain reduces extreme temperature dependency

---

### 🌍 Kenya (Equatorial Mixed Climate)
- T2M ↔ T2M_MAX: **0.88**
- T2M ↔ T2M_MIN: **0.52**

✔ Daytime heating is more influential than nighttime cooling

---

### 🌦️ Nigeria (Tropical Climate)
✔ Strong temperature coupling  
✔ Stable warm climate with low variation

---

## 💧 2. Humidity and Cooling Effects

Humidity is the strongest regulator of temperature stability.

### 🔴 General Pattern
- RH2M ↔ QV2M → Strong positive correlation (0.71 – 0.94)

---

### Key Insight
- High humidity reduces temperature extremes
- Low humidity increases temperature variability

---

### 🌵 Sudan
- RH2M vs T2M_RANGE: **-0.81**

✔ Strong inverse relationship  
✔ Dry air leads to extreme temperature differences

---

### 🌧️ Tanzania
- RH2M vs T2M_RANGE: **-0.79**

✔ Rainfall reduces temperature variability

---

### 🌿 Ethiopia
- RH2M ↔ QV2M: **0.90**
- QV2M ↔ T2M_RANGE: **-0.89**

✔ Strong humidity control on temperature stability

---

### 🌍 Kenya & 🌦️ Nigeria
✔ Similar pattern: humidity stabilizes temperature extremes

---

## 🌧️ 3. Precipitation Patterns

Rainfall behaves consistently across all countries.

### 🔵 General Pattern
- Rainfall ↔ Humidity → Positive correlation (0.4 – 0.51)
- Rainfall ↔ Temperature Range → Negative correlation (-0.39 to -0.52)

### Key Insight
✔ More humidity → more rainfall  
✔ More rainfall → lower temperature variation  
✔ Rainfall is strongly seasonal

---

## 🌬️ 4. Wind Speed Behavior

### 🌪️ Universal Pattern
- WS2M ↔ WS2M_MAX → Very strong correlation (0.91 – 0.95)

✔ Wind patterns are highly consistent across Africa  
✔ Wind is relatively independent of other variables

---

## 🧭 5. Surface Pressure (PS)

### 🌍 General Observation
- Weak correlation with most variables in all countries

### 🔥 Exception: Sudan
- PS ↔ T2M: **-0.87**

✔ Strong thermal low-pressure behavior due to extreme heat

---

## 📅 6. Seasonal Patterns

### Universal Finding
- DOY ↔ Month ≈ 1.0 (perfect correlation)

✔ Strong seasonal cycle across all countries

### Regional Notes
- Ethiopia & Tanzania → strong seasonal climate shifts  
- Sudan → sharp dry vs wet contrast  
- Kenya & Nigeria → moderate seasonal rainfall variation  

---

## 📌 Final Insights

### 🌍 1. Climate Type Controls Behavior
- Sudan → desert (strong pressure-temperature effects)
- Tanzania & Nigeria → tropical humidity-driven systems
- Ethiopia → elevation-modified climate
- Kenya → balanced equatorial climate

---

### 🌡️ 2. Temperature Structure
- Strong T2M–T2M_MAX relationship everywhere
- Minimum temperature dominates humid climates
- Maximum temperature dominates dry climates

---

### 💧 3. Humidity is the Key Regulator
Humidity controls:
- Temperature range
- Rainfall probability
- Nighttime cooling

---

### 🌧️ 4. Rainfall is Consistent
- Driven by humidity
- Reduces temperature extremes
- Strong seasonal dependency

---

### 🌬️ 5. Wind is Stable
- Highly consistent across all countries
- Weak dependence on other variables

---

## 🧠 Final Conclusion

Across all five African countries:

✔ Temperature is the core climate driver  
✔ Humidity regulates stability and extremes  
✔ Seasonality organizes climate cycles  
✔ Wind is consistent and stable  
✔ Pressure matters mainly in extreme climates (like Sudan)

---

## 🚀 Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📈 Author Notes

This is my first full-scale data science climate analysis project.  
Through this work, I learned how powerful coding and data analysis can be in understanding real-world systems like climate behavior.

Future improvements:
- Add machine learning clustering of climate zones
- Build predictive rainfall models
- Add geospatial visualizations

---

