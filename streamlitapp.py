import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# trained models
with open('xgb_regressor.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Rank Dictionaries
rank_state = {
    'AS_NEW': 6,
    'JUST_RENOVATED': 5,
    'GOOD': 4,
    'TO_RESTORE': 3,
    'TO_RENOVATE': 2,
    'TO_BE_DONE_UP': 1
}

rank_PEB = {
    'A++': 9,'A+': 8,'A': 7,'B': 6,
    'C': 5,'D': 4,'E': 3,'F': 2,'G': 1
}

rank_kitchen = {
    'NOT INSTALLED': 1, 'SEMI EQUIPPED': 2,
    'INSTALLED': 3, 'HYPER EQUIPPED': 4,
}

rank_district = {
    'Brussels': 5.0,'Aalst': 3.5,'Antwerp': 4.5,'Arlon': 3.5,'Ath':2.5,
    'Bastogne': 3.5,'Brugge': 4.0,'Charleroi': 2.0,'Dendermonde': 4.0,'Dinant': 2.5,
    'Diksmuide': 3.0,'Eeklo': 3.5,'Gent': 4.0,'Halle-Vilvoorde': 4.5,'Hasselt': 3.5,
    'Huy': 3.0,'Ieper': 3.0,'Kortrijk': 3.5,'Leuven': 4.5,'Liège': 2.5,
    'Marche-en-Famenne':3.0,'Maaseik': 3.5,'Mechelen': 4.0,'Mons': 2.0,
    'Mouscron': 2.5,'Namur': 3.0,'Nivelles': 5.0,'Neufchâteau': 3.0,
    'Oudenaarde': 3.5,'Oostend': 3.0,'Philippeville':2.0,'Roeselare': 3.0,
    'Soignies': 2.5,'Sint-Niklaas': 3.5,'Thuin': 2.5,'Tielt' : 3.5,
    'Tongeren': 3.0,'Tournai': 3.0,'Turnhout': 3.5,'Verviers': 3.0,'Veurne': 3.5,'Virton': 3.0,
    'Waremme': 3.0,
}

rank_province = {
    'Brussels': 5.0,
    'Flemish Brabant': 4.7,
    'Antwerp': 4.3,
    'East Flanders': 4.0,
    'West Flanders': 3.6,
    'Limburg': 3.7,
    'Walloon Brabant': 4.9,
    'Luxembourg': 3.4,
    'Liège': 3.1,
    'Namur': 3.0,
    'Hainaut': 2.7
}

# Streamlit 
st.title("Belgium Property Price Prediction")

property_type = st.radio("Type of Property", ("House", "Apartment"))
living_area = st.number_input("Living Area (sqm)", min_value=0)
bedroom_count = st.number_input("Bedroom Count", min_value=0)
surface_of_plot = st.number_input("Surface of Plot (sqm)", min_value=int(living_area))
construction_year = st.number_input("Construction Year", min_value=1800, max_value=2028)
bathroom_count = st.number_input("Bathroom Count", min_value=0)
kitchen = st.selectbox("Kitchen", list(rank_kitchen.keys()))

# Log Transformation
living_area_log = np.log(living_area + 1)
bathroom_count_log = np.log(bathroom_count + 1)
bedroom_count_log = np.log(bedroom_count + 1)
surface_of_plot_log = np.log(surface_of_plot + 1)
#condition = st.selectbox("Condition", list(rank_state.keys()))

# Condition Rank selection with emojis
condition_emojis = ['💩', '👎', '😐', '👍', '💪', '🤩']  # Emojis for ranks 1 to 6
selected_condition = st.radio("Rate the condition of the property:", condition_emojis)

# Map selected emoji to rank
condition_rank = condition_emojis.index(selected_condition) + 1  # 1 to 6

peb = st.selectbox("PEB", list(rank_PEB.keys()))
province = st.selectbox("Province", list(rank_province.keys()))
district = st.selectbox("District", list(rank_district.keys()))

# Region
regions = ["Brussels", "Flanders", "Wallonie"]
if province == 'Brussels':
    region = 'Brussels'
elif province in ['Flemish Brabant', 'Antwerp', 'East Flanders', 'West Flanders', 'Limburg']:
    region = 'Flanders'
elif province in ['Walloon Brabant', 'Luxembourg', 'Liège', 'Namur', 'Hainaut']:
    region = 'Wallonie'
#region = st.selectbox("Region", regions)

# Yes/No
furnished = st.checkbox("Furnished")
garden = st.checkbox("Garden")
swimming_pool = st.checkbox("Swimming Pool")
terrace = st.checkbox("Terrace")

if st.button("Predict"):
    #condition_rank = rank_state[condition]
    condition_rank = condition_emojis.index(selected_condition) + 1
    peb_rank = rank_PEB[peb]
    kitchen_rank = rank_kitchen[kitchen]
    district_rank = rank_district[district]
    province_rank = rank_province[province]

    furnished = int(furnished)
    garden = int(garden)
    swimming_pool = int(swimming_pool)
    terrace = int(terrace)

    type_of_property = 1 if property_type == "House" else 2

    # Region dummy 
    region_dummies = [1 if r == region else 0 for r in regions]

    # Scaling the inputs
    input_data = np.array([[bathroom_count_log, bedroom_count_log, construction_year, furnished, garden, living_area_log, surface_of_plot_log, swimming_pool, terrace, type_of_property, condition_rank, peb_rank, kitchen_rank, district_rank, province_rank] + region_dummies])
    input_data_scaled = scaler.transform(input_data)

    # Prediction with the model
    price_prediction = model.predict(input_data_scaled)
    st.write(f"Estimated Price: {int(price_prediction[0])}€")
