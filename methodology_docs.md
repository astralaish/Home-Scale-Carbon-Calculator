# Methodology & Emission Factors

The Home Scale Carbon Calculator uses scientifically grounded proxies to estimate an individual's carbon footprint. Because energy grids, transportation infrastructure, and cultural diets vary heavily by region, accurate emission factors are crucial.

## Baseline Factors (India)
Currently, the baseline values are optimized for **India**. In future iterations, specific factors for other nations will be populated. 

* **Transportation (0.14 kg CO2/km):** Based on the average emission of a typical passenger internal combustion engine (ICE) vehicle in India.
* **Electricity (0.68 kg CO2/kWh):** Mapped to the Central Electricity Authority (CEA) of India, accounting for the country's coal-heavy national grid.
* **Diet (1.25 kg CO2/meal):** Traditional Indian diets are largely plant-based. Plant-based meals have a significantly lower carbon footprint compared to Western, meat-heavy diets, leading to an estimated 2.5 kg CO2 per day (assuming 2 meals).
* **Waste (0.1 kg CO2/kg):** A solid baseline proxy for general municipal solid waste, accounting for the methane produced by organic matter decomposing in landfills.

## Limitations
* Computations do not yet dynamically alter for all 200+ countries. Temporary dictionary comprehension falls back to the India baseline for unmapped countries to prevent application crashes.
* Calculations do not factor in secondary household members or the efficiency ratings of specific appliances. 