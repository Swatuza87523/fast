import streamlit as st
import pandas as pd
import numpy as np
page= """
<style>
[data-testid="stSidebarContent"]{
background-color: rgb(25, 29, 129);

}

[data-testid="stImageCaption"]{
text-decoration-color: darkmagenta;
padding-top: 3%;
color: darkmagenta;
size: 10px;
text-align: center;
padding: 10px 20px;
}

[data-testid="stImage"]{
width: 80%;
background-color: white;
box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
margin-bottom: 25px;
}


[data-testid="stSidebarContent"]{
background-color: rgb(25, 29, 129);

}
[data-testid="stAppViewBlockContainer"]{
background-color: rgba(240, 141, 158, 0.689);
}

[data-testid="stMarkdownContainer"]{
color: crimson;
}

[section]{
background: linear-gradient(to right, #ffefba, #ffffff);
background-repeat: repeat;
background-size: cover;
}
[class="main st-emotion-cache-bm2z3a ea3mdgi8"]{
background-color: rgb(72, 220, 246);
}
[data-testid="stHeader"]{
background-color: #f8d7da; 
color: #721c24;
}

</style>
"""

st.markdown(page,unsafe_allow_html=True)
d=pd.read_csv("E:\Python learning\Heart desease dataset\heart-disease.csv")
dfh=d.copy()
st.title(":blue[Heart Desease Prediction Exploratory Data Analysis]")
st.image("E:\Python learning\Heart desease dataset\output.png",caption="Chest Pain Levels Analysis on the basis of Gender and Age")
st.image("newplot.png",caption="Deep Analysis of Cholestrol levels with Age")
st.image("newplot2.png",caption="Maximum Heart Rate achieved on the basis of Gender")
#Code for feature engineer
dfh['fbs range']=''
dfh.loc[dfh['fbs']==0,'fbs range']="Normal"
dfh.loc[dfh['fbs']==1,'fbs range']="Diabetic Patient"


dfh['cp levels']=''
dfh.loc[dfh['cp']==0,'cp levels']="mild"
dfh.loc[dfh['cp']==1,'cp levels']="Something strong"
dfh.loc[dfh['cp']==2,'cp levels']="severe"
dfh.loc[dfh['cp']==3,'cp levels']="Very severe"

dfh['gender']=''
dfh.loc[dfh['sex']==0,'gender']="Female"
dfh.loc[dfh['sex']==1,'gender']="Male"

#plots
st.bar_chart(dfh, x="gender", y="chol", color="age")
st.bar_chart(dfh, x="fbs range", y="age",color="restecg")
# Using object notation
st.sidebar.image("people-heart-care-logo-wellness-healthcare-love-hospital-symbol-vector-icon-design-speciality-medical-centre-isolated-white-99106695.webp")
add_selectbox =st.sidebar.selectbox(
    ":blue[How would you like to be contacted?]",
    ("Email", "Home phone", "Mobile phone")
)
