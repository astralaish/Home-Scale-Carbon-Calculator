# Home Scale Carbon Calculator 🫪

A dynamic, interactive web application built with Python and Streamlit that allows users to calculate their personal carbon footprint based on daily habits. This project was developed to explore environmental sustainability metrics, specifically focusing on the carbon emission factors associated with transportation, electricity, diet, and waste management.

## Features
* **Interactive UI:** Users can input their daily commute, monthly electricity usage, weekly waste generation, and daily meals using intuitive sliders and input fields.
* **Dynamic Country Selection:** Incorporates the `pycountry` library to support global country selection.
* **Custom Emission Factors:** Calculates yearly CO2 emissions using baseline factors mapping to national grid and cultural data (e.g., India's electricity grid is mapped to 0.68 kg CO2/kWh based on CEA data).
* **Contextual Insights:** Provides specific environmental warnings and context based on the selected region to contextualize individual emissions against national averages.

## Technologies Used
* Python 3.15
* Streamlit (Web Framework)
* pycountry (Geographic Data)
* Pandas & OpenPyXL (Data processing dependencies)

## Installation and Setup (macOS/Linux)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
   cd YOUR-REPOSITORY-NAME
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage
Once the local server starts, the application will open automatically in your default web browser (typically at `http://localhost:8501`). Adjust the inputs to see your total carbon footprint update dynamically.