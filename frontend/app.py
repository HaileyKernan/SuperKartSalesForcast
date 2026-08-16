import pandas as pd
import streamlit as st
import requests

backend_url = 'http://backend:7860'

#App titile
st.title('SuperKart Sales Forcast')

product_weight = st.number_input('Product Weight', min_value=0.0, value =0.0)
product_sugar_content = st.selectbox('Product Sugar Content', ['No Sugar', 'Low Sugar', 'Regular'])
product_allocated_area = st.number_input('Product Allocated Area', min_value=0.0, value=0.0)
product_type = st.selectbox('Product Type', ['Fruits and Vegetables',
                                             'Snack Foods',
                                             'Frozen Foods',
                                             'Dairy',
                                             'Household',
                                             'Baking Goods',
                                             'Canned',
                                             'Health and Hygiene',
                                             'Meat',
                                             'Soft Drinks',
                                             'Breads',
                                             'Hard Drinks',
                                             'Others',
                                             'Starchy Foods',
                                             'Breakfast',
                                             'Seafood'])
product_mrp = st.number_input('Product MRP', min_value=0.0, value=0.0)
store_establishment_year = st.selectbox('Store Establishment Year', ['1897', '1998', '1999', '2009'])
store_location_city_type = st.selectbox('Store Location City Type', ['Tier 1', 'Tier 2', 'Tier 3'])
store_type = st.selectbox('Store Type', ['Supermarket Type2', 'Supermarket Type1 ', 'Departmental Store','Food Mart'])
store_size = st.selectbox('Store Size', ['Small', 'Medium', 'High'])

user_input = pd.DataFrame([{
    'Product_Weight':product_weight,
    'Product_Sugar_Content':product_sugar_content,
    'Product_Allocated_Area':product_allocated_area,
    'Product_Type':product_type,
    'Product_MRP':product_mrp,
    'Store_Establishment_Year':store_establishment_year,
    'Store_Size':store_size ,
    'Store_Location_City_Type':store_location_city_type,
    'Store_Type':store_type
}])

if st.button('Predict', type='primary', key='single'):
  response = requests.post(f'{backend_url}/v1/singleprediction', json=user_input.to_dict(orient='records')[0])
  if response.status_code == 200:
    prediction = response.json()['Forcast']
    st.success(f'The sales forcast for this item is is: ${prediction:.2f}')
  else:
    st.error('Error occured during prediction')

st.subheader("Batch Forcast")

upload_file = st.file_uploader('Upload a CSV file', type=['csv'])

if upload_file is not None:
  if st.button('Predict', type='primary', key = 'batch'):
    response = requests.post(f'{backend_url}/v1/batchprediction', files={'files':upload_file})
    if response.status_code == 200:
      prediction_dict = response.json()
      st.write(prediction_dict)
    else:
      st.error('Error occured during prediction')
