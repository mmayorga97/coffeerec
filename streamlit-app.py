import pandas as pd
#import pandas_profiling
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
   page_title="Coffee Recommender - Marcelino Mayorga Quesada",
   page_icon="☕",
   layout="wide",
   initial_sidebar_state="expanded",
)

def main():
    dataset = "./data/coffee_may2023.csv"
    df = pd.read_csv(dataset)
    pr = gen_profile_report(df, explorative=True)
    tab1, tab2, tab3 = st.tabs(["Dataset", "Report", "Prediction"])
    with tab1:
        st.write(f"🔗 [Coffee Quality Data (CQI May-2023)]({dataset})")
        st.write(df)
    with tab2:
        with st.expander("REPORT", expanded=True):
            st_profile_report(pr)
    with tab3:
        st.write(f"Placeholder")




@st.cache_data
def gen_profile_report(df, *report_args, **report_kwargs):
    return ProfileReport(df, minimal=True)


if __name__ == "__main__":
    main()