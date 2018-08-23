# Scripts for Oceanic Exchanges project

## Requirements
- [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)

## correct_dates.py
Unifying different dates from Google Docs.

## to_json.py
Convert a Google Docs CSV file to JSON for [passim](https://github.com/dasmiq/passim).

## process_corpus.py
Convert a CSV dataset to a plain text corpus for MALLET. Split the corpus to subcorpora based 
on language.

## count_k.R & print_k_figure.R
R scripts to run [ldatuning](https://github.com/nikita-moor/ldatuning) library to our dataset to estimate k-value for MALLET.

## run_mallet.sh
Run MALLET to subcorpus. Set the path before running. Select a subcorpus by giving language as 
an argument (relative to subfolders in corpus).

`Usage: run_mallet.sh Finnish`

## make_matrix.py
Read the topic participation matrix produced by MALLET back to Pandas data frame. See the 
'titles' datatable for a combined table for the topic participation of different newspaper 
titles.

`Usage: e.g., make_matrix.py Finnish`
