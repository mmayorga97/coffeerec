# Coffee Recommender - [Marcelino Mayorga Quesada](https://marcelino.mayorga.com)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This is a simple machine learning excercise with the objective to recommend coffee leveraging Coffee Quality Institute's data and applying Content-Based Filtering

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them, comes in the requirements.txt

```
streamlit
streamlit-pandas-profiling
pandas
scikit-learn
conda
```

### Installing and Running
1 - Creating and Activating conda local environment use "rc.bat" under name "coffeerec"
```
rc.bat
```

2 - run streamlit
```
run streamlit app/streamlit-app.py
```

2.1 - OR Docker on root folder and with Docker Desktop running
```
docker-compose up --build
```