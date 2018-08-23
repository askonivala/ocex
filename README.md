# Scripts for Oceanic Exchanges project

## Requirements
- [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)

## correct_dates.py
Unifying different dates from Google Docs.

## to_json.py
Convert a Google Docs CSV file to JSON for [passim](https://github.com/dasmiq/passim).

## process_corpus.py
Convert a CSV dataset to a plain text corpus for MALLET. Split the corpus to subcorpora based on language.

## run_mallet.sh
Run MALLET to subcorpus. Set the path before running.

`Usage: run_mallet.sh Swedish, run_mallet.sh Finnish, run_mallet.sh English, or run_mallet.sh German`


