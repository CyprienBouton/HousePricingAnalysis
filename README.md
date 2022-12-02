# HousePricingAnalysis
The goal of the project is to predict the price of a flat in Paris.
The analysis is based on all the transactions in Paris between 2017 and 2022.

It's a important tool because it allow both buyers and sellers, to know the price of an accomodation before consedering to buy or sell it.

# Table of contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Commit Policy](#commit-policy)

# Dataset

All the transactions on the housing market in France are available here https://files.data.gouv.fr/geo-dvf/latest/csv/

# Installation

After cloning the project,

```
pip3 install -r requirements.txt
```

Export the project to your PYTHONPATH.

# Quit Start

The report is a streamlit app which can be run with the following command line:
```
streamlit run app.py
```

# Commit Policy

Please, respect the following commit policy:
```
[START]     first commit describing the branch you created
[ADD]       commit describing new elements or functionalities
[UP]        commit describing elements or functionalities updated
[FIX]       commit describing the error and how it has been fixed
[DEL]       commit describing elements or functionalities deleted
[PR]        pull request
```