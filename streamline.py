import streamlit as st
import pandas as pd
st.header("Check Your Characters Detail")

st.write("Hello World")


data={
    "Harry": {
        "house": "Gryffindor",
        "pet": "Hedwig",
        "wand": "Holly, phoenix feather"
    },
    "Hermione": {
        "house": "Gryffindor",
        "pet": "Crookshanks",
        "wand": "Vine wood, dragon heartstring"
    },
    "Ron": {
        "house": "Gryffindor",
        "pet": "Scabbers",
        "wand": "Willow, unicorn hair"
    }
}


st.write(pd.DataFrame(data))
