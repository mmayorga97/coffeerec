# Coffee Recommender - [Marcelino Mayorga Quesada](https://marcelino.mayorga.com)

## Table of Contents

- [Coffee Recommender - Marcelino Mayorga Quesada](#coffee-recommender---marcelino-mayorga-quesada)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing and Running](#installing-and-running)
    - [Jupyter Notebooks](#jupyter-notebooks)

## About <a name = "about"></a>

This is a simple machine learning exercise with the objective to recommend coffee leveraging Coffee Quality Institute's data and applying Content-Based Filtering

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

[Conda](https://docs.conda.io/en/latest/) and requirements.txt

```
streamlit
streamlit-pandas-profiling
pandas
scikit-learn
conda
```

### Installing and Running<a name = "installing"></a>
1 - Creating and Activating conda local "coffeerec" environment on Terminal: use "rc.bat"
```
rc.bat
```

2 - on Terminal and under root folder, run streamlit
```
run streamlit app/streamlit-app.py
```

2.1 - OR Docker on root folder and with Docker Desktop running
```
docker-compose up --build
```

### Jupyter Notebooks<a name = "notebooks"></a>
1 - [data_preprocess.ipynb](data_preprocess.ipynb): Analysis and data preprocess.
2 - [recommender.ipynb](recommender.ipynb): Recommender using the preprocessed data.
