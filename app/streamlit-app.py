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
    tab0, tab1, tab2, tab3 = st.tabs(["Intro", "Dataset", "Report", "Recommendation"])
    data = get_data()
    with tab0:
        st.write(f"This is a simple machine learning excercise with the objective to recommend coffee leveraging Coffee Quality Institute's data and Kaggle community.")
        st.divider()
        st.write(f"Details:")
        st.markdown("- Data source [Coffee Quality Data (CQI May-2023)](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi)")
        st.markdown("- Web Toolkit [Streamlit](https://streamlit.io/gallery)")
        st.markdown("- ML Toolkit [Pycaret](https://pycaret.org/)")
        st.markdown("- Cloud [Google Cloud Platform](https://cloud.google.com/)")


    with tab1:
        st.write(f"🔗 [Coffee Quality Data (CQI May-2023)](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi)")
        st.write("Sensory evaluations (coffee quality scores):")
        st.markdown("- Aroma: Refers to the scent or fragrance of the coffee.")
        st.markdown("- Flavor: The flavor of coffee is evaluated based on the taste, including any sweetness, bitterness, acidity, and other flavor notes.")
        st.markdown("- Aftertaste: Refers to the lingering taste that remains in the mouth after swallowing the coffee.")
        st.markdown("- Acidity: Acidity in coffee refers to the brightness or liveliness of the taste.")
        st.markdown("- Body: The body of coffee refers to the thickness or viscosity of the coffee in the mouth.")
        st.markdown("- Balance: Balance refers to how well the different flavor components of the coffee work together.")
        st.markdown("- Uniformity: Uniformity refers to the consistency of the coffee from cup to cup.")
        st.markdown("- Clean Cup: A clean cup refers to a coffee that is free of any off-flavors or defects, such as sourness, mustiness, or staleness.")
        st.markdown("- Sweetness: It can be described as caramel-like, fruity, or floral, and is a desirable quality in coffee.")
        st.write(data)
    with tab2:
        st.markdown("** WORK IN PROGRESS - RAW DATA **")
        report = get_report_html()
        components.html(report,height=900, width=None, scrolling=True)
    with tab3:
        st.markdown("** WORK IN PROGRESS **")
        #st.write(get_coffee_recommendation())
        producers = data['Producer'].drop_duplicates()
        st.multiselect("Producers", producers)
        if 'button' not in st.session_state:
            st.session_state.button = False

        def click_button():
            st.session_state.button = not st.session_state.button

        st.button("Recommend",on_click=click_button, disabled=True)


@st.cache_data
def get_data():
    dataset = os.getcwd() + ("/app/coffee_may2023.csv")
    #dataset = os.getcwd() + ("/coffee_may2023.csv")
    #dataset = "coffee_may2023.csv"
    print(f"loading file:{dataset} ")
    df = pd.read_csv(dataset)
    return df


@st.cache_data
def get_report_html():
    source_code = None
    file = os.getcwd() + ("/app/report.html")
    #file = os.getcwd() + ("/report.html")
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