# coffeerec
Coffee Recommender

Coffee Data Source
Coffee Quality Data (CQI May-2023) - https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi/code
Streamlit GCP Tutorial - https://dev.to/whitphx/how-to-deploy-streamlit-apps-to-google-app-engine-407o

Recommenders - https://github.com/microsoft/recommenders


gcloud builds submit --tag gcr.io/portfoliobot/coffeerecapp:latest.


> **Step 5** - Validate image has been uploaded `https://console.cloud.google.com/gcr/images/portfoliobot/global/portfolioapp?project=portfoliobot`

> **Step 6** - Head to Run Cloud and run a new revision with the new uploaded image `https://console.cloud.google.com/run/detail/us-central1/portfolioapp/metrics?project=portfoliobot`
