import pandas as pd
#import pandas_profiling
import streamlit as st
#from ydata_profiling import ProfileReport
#from streamlit_pandas_profiling import st_profile_report
import os
import requests
import streamlit.components.v1 as components  # Import Streamlit

st.set_page_config(
   page_title="Coffee Recommender - Marcelino Mayorga Quesada",
   page_icon="☕",
   layout="wide",
   initial_sidebar_state="expanded",
)

def main():
    st.write("Coffee Quality Data (CQI May-2023) Recommender by [Marcelino Mayorga Quesada](https://www.linkedin.com/in/marcelinomayorga/)")
    tab0, tab1, tab2, tab3 = st.tabs(["Intro", "Dataset", "Report", "Prediction"])
    with tab0:
        st.write(f"Intro")
    with tab1:
        data = get_data()
        st.write(f"🔗 [Coffee Quality Data (CQI May-2023)]()")
        st.write(data)
    with tab2:
        report = get_report_html()
        components.html(report,height=900, width=None, scrolling=True)
    with tab3:
        st.write(f"Recommendation")
        #st.write(get_coffee_recommendation())

@st.cache_data
def get_data():
    #dataset = os.getcwd() + ("/coffee_may2023.csv")
    dataset = "coffee_may2023.csv"
    print(f"loading file:{dataset} ")
    df = pd.read_csv(dataset)
    return df


@st.cache_data
def get_report_html():
    source_code = None
    file = os.getcwd() + ("/report.html")
    with open(file, 'r', encoding='utf-8') as HtmlFile:
        source_code = HtmlFile.read()
    return source_code

#@st.cache_data
#def gen_profile_report(df, *report_args, **report_kwargs):
    #return ProfileReport(df, minimal=True)

@st.cache_data
def get_coffee_recommendation():
    url = "http://172.17.0.1:8000"  # Replace with the actual URL of your Uvicorn server
    endpoint = "/"  # Replace with the actual API endpoint you want to access 

    full_url = f"{url}{endpoint}"
    response = requests.get(full_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
    return data



if __name__ == "__main__":
    main()