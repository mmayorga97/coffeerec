import pandas as pd
import streamlit as st
import os
import streamlit.components.v1 as components  # Import Streamlit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import linear_kernel
import random

st.set_page_config(
   page_title="Coffee Recommender - Marcelino Mayorga Quesada",
   page_icon="☕",
   layout="wide",
   initial_sidebar_state="expanded",
)

def main():
    def get_coffee_recommendation(key_value='costa rica',key_id='country_of_origin', top_n=10):
        data = get_preprocessed_data()

        # Concatenate multiple columns into a single feature column for item representation
        coffee_item_features = ['variety', 'processing_method','color', 'country_of_origin', 'mill']
        data['item_features'] = data[coffee_item_features].agg(' '.join, axis=1)


        # Normalize 'rating' column to [0, 1] range for feature representation
        scaler = MinMaxScaler()
        normalized_columns = ['aftertaste','balance','flavor','aroma','body','acidity','moisture_percentage','quakers','overall','total_cup_points','altitude']
        normalized_features = scaler.fit_transform(data[normalized_columns])
        normalized_data = pd.DataFrame(normalized_features, columns=normalized_columns)


        # Create a TF-IDF vectorizer to convert item_features into feature vectors
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(data['item_features'])

        # Combine the TF-IDF matrix with the normalized columns
        data_vec = pd.concat([pd.DataFrame(tfidf_matrix.toarray()), normalized_data], axis=1)

        # Calculate the cosine similarity between items
        cosine_sim = linear_kernel(data_vec, data_vec)

        # Function to get coffee recommendations based on country
        def get_recommendations(key_value,key_id, cosine_similarities, data):
            idx = random.choice(data.index[data[key_id] == key_value].tolist())
            sim_scores = list(enumerate(cosine_similarities[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:]  # Exclude the base coffee itself (most similar)
            coffee_indices = [i[0] for i in sim_scores]
            return data[coffee_item_features+normalized_columns].iloc[coffee_indices]

        recommendations = get_recommendations(key_value,key_id, cosine_sim, data)
        return recommendations[0:top_n]

    st.write("Coffee Quality Data (CQI May-2023) Recommender by [Marcelino Mayorga Quesada](https://www.linkedin.com/in/marcelinomayorga/)")
    tab0, tab1, tab2, tab3 = st.tabs(["Intro", "Dataset", "Analysis & Preprocess", "Recommendation Demo"])
    raw_data = get_raw_data()
    prep_data = get_preprocessed_data()
    with tab0:
        st.subheader("About")
        st.markdown(f"- **Purpose:** This is a simple machine learning excercise with the objective to recommend coffee leveraging Coffee Quality Institute's data and applying Content-Based Filtering")
        st.markdown(f"- **Recommenders:** There are two ways to build recommenders: Collaboritve Filtering that leverages user information which we don't have at this moment and can be applied with toolkits like [Microsoft's Recommenders](https://github.com/microsoft/recommenders), or [Tensorflow Recommenders](https://github.com/tensorflow/recommenders), or [Surprise](https://surprise.readthedocs.io/en/stable/) and Content-Based Filtering through the coffee attributes(Aroma, Flavor, Aftertaste, etc) that can be achieved easily with [Scikit-learn](https://scikit-learn.org/stable/).")
        st.markdown(f"- **How? Through [Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity):** is used in information retrieval and item vectorized attributes. It calculates the similarity between two vectors.")
        st.divider()
        st.subheader("Toolkit:")
        st.markdown("- Data source [Coffee Quality Data (CQI May-2023)](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi)")
        st.markdown("- Web Toolkit [Streamlit](https://streamlit.io/gallery)")
        st.markdown("- Scikit-Learn [Scikit-Learn](https://scikit-learn.org/stable/)")
        st.markdown("- Cloud [Google Cloud Platform](https://cloud.google.com/)")
        st.markdown("- Github [Code](https://github.com/mmayorga97/coffeerec)")
    with tab1:
        st.subheader("Sensory evaluations (coffee quality scores):")
        st.markdown("- Aroma: Refers to the scent or fragrance of the coffee.")
        st.markdown("- Flavor: The flavor of coffee is evaluated based on the taste, including any sweetness, bitterness, acidity, and other flavor notes.")
        st.markdown("- Aftertaste: Refers to the lingering taste that remains in the mouth after swallowing the coffee.")
        st.markdown("- Acidity: Acidity in coffee refers to the brightness or liveliness of the taste.")
        st.markdown("- Body: The body of coffee refers to the thickness or viscosity of the coffee in the mouth.")
        st.markdown("- Balance: Balance refers to how well the different flavor components of the coffee work together.")
        st.markdown("- Uniformity: Uniformity refers to the consistency of the coffee from cup to cup.")
        st.markdown("- Clean Cup: A clean cup refers to a coffee that is free of any off-flavors or defects, such as sourness, mustiness, or staleness.")
        st.markdown("- Sweetness: It can be described as caramel-like, fruity, or floral, and is a desirable quality in coffee.")
        st.divider()
        st.subheader("Raw Data")
        st.write(f"🔗 [Coffee **Raw** Quality Data (CQI May-2023)](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi)")
        st.write(raw_data)
    with tab2:
        st.subheader("Data Profiling - Report")
        report = get_report_html()
        components.html(report,height=900, width=None, scrolling=True)
        st.divider()
        st.subheader("Preprocessed Data - [Jupyter Notebook](https://github.com/mmayorga97/coffeerec/blob/main/data_preprocess.ipynb)")
        st.markdown("Actions : ")
        st.markdown("- Removed Columns: ID, Unnamed, ICO Number, Number of Bags, Bag of Weight, Clean Cup, Sweetness, Harvest Year, Defect Info(Cat1 & Cat2), Certification Info (Status, Expiration,etc.) ")
        st.markdown("- Fixed Columns: Altitude (using mean value of range), Standarize Color and Processing methods columns.")
        st.write(f"🔗 [Coffee **Preprocessed** Quality Data (CQI May-2023)](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi)")
        st.write(prep_data)
    with tab3:
        st.subheader("Demo")
        #with st.form(key='my_form'):
        st.subheader("Filter by:")
        filter_type = st.radio("",('lot_number','country_of_origin'),key='filter_type',index=0,label_visibility='hidden')
        countries = prep_data['country_of_origin'].drop_duplicates()
        lot_numbers = prep_data['lot_number'].drop_duplicates()
        if filter_type == "country_of_origin":
            filter_value= st.selectbox("Countries", countries)
        else:
            filter_value= st.selectbox("Lot Numbers", lot_numbers)
        clicked = st.button("Recommend")
        if clicked:
            st.subheader("Top 5 Recommendations:")
            st.write(get_coffee_recommendation(filter_value,filter_type))
        st.divider()
        st.subheader("Code - [Jupyter Notebook](https://github.com/mmayorga97/coffeerec/blob/main/recommender.ipynb)")
        with st.echo():
            def get_coffee_recommendation(key_value='costa rica',key_id='country_of_origin', top_n=10):
                # Load the preprocessed data
                data = get_preprocessed_data()

                # Concatenate multiple columns into a single feature column for item representation
                coffee_item_features = ['variety', 'processing_method','color', 'country_of_origin', 'mill']
                data['item_features'] = data[coffee_item_features].agg(' '.join, axis=1)

                # Normalize columns to [0, 1] range for feature representation
                scaler = MinMaxScaler()
                normalized_columns = ['aftertaste','balance','flavor','aroma','body','acidity','moisture_percentage','quakers','overall','total_cup_points','altitude']
                normalized_features = scaler.fit_transform(data[normalized_columns])
                normalized_data = pd.DataFrame(normalized_features, columns=normalized_columns)

                # Create a TF-IDF vectorizer to convert item_features into feature vectors
                tfidf_vectorizer = TfidfVectorizer(stop_words='english')
                tfidf_matrix = tfidf_vectorizer.fit_transform(data['item_features'])

                # Combine the TF-IDF matrix with the normalized columns
                data_vec = pd.concat([pd.DataFrame(tfidf_matrix.toarray()), normalized_data], axis=1)

                # Calculate the cosine similarity between items
                cosine_sim = linear_kernel(data_vec, data_vec)

                # Function to get coffee recommendations based on given key value and id (columns)
                def get_recommendations(key_value,key_id, cosine_similarities, data):
                    idx = random.choice(data.index[data[key_id] == key_value].tolist()) # Multiple found pick one randomly as sample
                    sim_scores = list(enumerate(cosine_similarities[idx]))
                    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                    sim_scores = sim_scores[1:]  # Exclude the base coffee itself (most similar)
                    coffee_indices = [i[0] for i in sim_scores]
                    return data[coffee_item_features+normalized_columns].iloc[coffee_indices]

                recommendations = get_recommendations(key_value,key_id, cosine_sim, data)
                return recommendations[0:top_n]
@st.cache_data
def get_raw_data():
    dataset = os.getcwd() + ("/app/coffee_may2023.csv")
    print(f"loading file:{dataset} ")
    df = pd.read_csv(dataset)
    return df

@st.cache_data
def get_preprocessed_data():
    dataset = os.getcwd() + ("/app/coffee_may2023_prep.csv")
    print(f"loading file:{dataset} ")
    df = pd.read_csv(dataset)
    return df

@st.cache_data
def get_report_html():
    source_code = None
    file = os.getcwd() + ("/app/report.html")
    with open(file, 'r', encoding='utf-8') as HtmlFile:
        source_code = HtmlFile.read()
    return source_code

if __name__ == "__main__":
    main()