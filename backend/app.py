import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import joblib

from pathlib import Path

sales_forcast_api = Flask('SuperKartSalesForcast')



model_path = Path(__file__).with_name("super_kart_sales_forcast_v1_0.joblib")
model = joblib.load(model_path)

#Defines routes for home page
@sales_forcast_api.get('/')
def home_page():
  return "SuperKart Sales Forcaster"

#Endpoint for single prediction
@sales_forcast_api.post('/v1/singleprediction')
def predict_single():
  #transforms user input into dataframe
  user_input = request.get_json()
  json_data ={'Product_Weight': user_input['Product_Weight'],
              'Product_Sugar_Content':user_input['Product_Sugar_Content'],
              'Product_Allocated_Area':user_input['Product_Allocated_Area'],
              'Product_Type':user_input['Product_Type'],
              'Product_MRP':user_input['Product_MRP'],
              'Store_Establishment_Year':user_input['Store_Establishment_Year'],
              'Store_Size':user_input['Store_Size'],
              'Store_Location_City_Type':user_input['Store_Location_City_Type'],
              'Store_Type':user_input['Store_Type']}
  input_df = pd.DataFrame([json_data])

  #getting model predictoin
  prediction = model.predict(input_df)[0]

  #Returning the prediction
  return jsonify({'Forcast': prediction})


@sales_forcast_api.post('/v1/batchprediction')
def predict_batch():
  #Transform user input into cvs
   user_files = request.files['files']
   input_files = pd.read_csv(user_files)

   #Getting the predictions
   batch_predictions = model.predict(input_files).tolist()
   batch_predictions_rounded = [round(prediction, 2) for prediction in batch_predictions]
   product_ids = input_files['Product_Id'].tolist()
   prediction_dict = dict(zip(product_ids, batch_predictions_rounded))

   #returnig predictions
   return prediction_dict
if __name__ == '__main__':
  sales_forcast_api.run(debug=True)
