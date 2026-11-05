import streamlit as st
import pycountry

all_countries = [country.name for country in pycountry.countries]

#The baseline factors are adjusted as per India for now
baseline_factor = {
    "Transport" : 0.14, #kgCO2/km
    "Electricity" : 0.68, #kgCO2/KWt
    "Diet" : 1.25, #kgCO2/meal i.e. 2.5 kgCO2/kg
    "Waste" : 0.1 #kgCO2/kg
}

emission_factor = {country: baseline_factor for country in all_countries}

st.set_page_config(layout = "wide", page_title = "Home Scale carbon Calculator")
st.title("Home Scale carbon Calculator 🫪")

st.subheader("🧐 Your Country")

# This automatically creates a dropdown option for every country in library
country = st.selectbox("Select", all_countries, all_countries.index("India"))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily commute distance (in km)🥵")
    distance = st.slider("Distance", 0.0, 1000.0, key = "distance_input")

    st.subheader("Monthly electricity consumption (in kwh)⚡️")
    electricity = st.slider("Electricity", 0.0, 1000.0, key = "electricity_input")

with col2:
    st.subheader("Waste generated per week (in kg)💩")
    waste = st.slider("Waste", 0.0, 100.0, key = "waste_input")

    st.subheader("Number of meals per day🤤")
    meals = st.number_input("Meals", 0, key = "meals_input")

#distance per day
if distance > 0 :
    distance = distance * 365

#Electricity per month
if electricity > 0 :
    electricity = electricity * 12

#Waste per week
if waste > 0 :
    waste = waste * 52

#Meals per day
if meals > 0 :
    meals = meals * 365

#Emmisisons
transportation_emissions = emission_factor[country]['Transport'] * distance
electricity_emissions = emission_factor[country]['Electricity'] * electricity
waste_emissions = emission_factor[country]['Waste'] * waste
meals_emissions = emission_factor[country]['Diet'] * meals

#Round off in Tonnes
transportation_emissions = round (transportation_emissions / 1000, 2)
electricity_emissions = round (electricity_emissions / 1000, 2)
waste_emissions = round (waste_emissions / 1000, 2)
meals_emissions = round (meals_emissions / 1000, 2)

total_emissions = round (
    transportation_emissions + electricity_emissions + waste_emissions + meals_emissions
)

if st.button("Calculate CO2 Emissions"):
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emission by Categories")
        st.info(f"🛷Transport : {transportation_emissions} tonnes CO2 per year")
        st.info(f"🦄Electricity : {electricity_emissions} tonnes CO2 per year")
        st.info(f"🐷Waste : {waste_emissions} tonnes CO2 per year")
        st.info(f"🍔Diet : {meals_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Carbon Footprint")
        st.info(f"🛷Your total carbon footprint is : {total_emissions} tonnes CO2 per year")
        # Custom warnings for specific countries
        country_warnings = {
            "India": "India’s per capita CO2 emissions in 2025 are approximately 2.18 to 2.2 tonnes. Total emissions are projected to reach 3.22 billion tonnes in 2025, making India the third-largest emitter globally after China and the US...",
            "United States": "The US has one of the highest per capita CO2 emissions globally. Rapid transition to renewable energy is critical.",
            "United Kingdom": "The UK has made significant progress in reducing emissions, but continued efforts in home energy efficiency are needed."
        }
        
        # Create a generic fallback message for the 200+ other countries
        default_message = f"Every nation must reduce emissions to stay within the global carbon budget. Track your footprint in {country} to help limit warming to 1.5°C."
        
        # Fetch the specific warning, or use the default if the country isn't listed
        warning_message = country_warnings.get(country, default_message)
        
        st.warning(warning_message)

 
    
