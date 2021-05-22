import streamlit as st
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('kmeansclusterassignment.pkl', 'rb'))
dataset = pd.read_csv('Wholesale customers data.csv')
X = dataset.iloc[:, 2:8].values
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X = sc.fit_transform(X)


def predict_note_authentication(chanel, region, fresh, milk, grocery, frozen, detergents, delicassen):
    predict = model.predict(sc.transform([[fresh, milk, grocery, frozen, detergents, delicassen]]))
    print("cluster number", predict)
    return predict

def main():
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">K-MEANS</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("Customer Segmenation on wholesale data ")


    chanel = st.selectbox(
        "Chanel",
        ("1", "2")
    )
    region = st.selectbox(
        "Region",
        ("1", "2", "3")
    )
    fresh = st.number_input('enter fresh amount')
    milk = st.number_input('enter milk amount')
    grocery =st.number_input('enter grocery amount')
    frozen =st.number_input('enter frozen amount')
    detergents = st.number_input('enter detergents amount')
    delicassen = st.number_input('enter delicassen amount')

    if st.button("KMEANS"):
        result = predict_note_authentication(chanel, region, fresh, milk, grocery, frozen, detergents, delicassen)
        st.success('KMEANS has predicted {}'.format(result))



if __name__ == '__main__':
    main()