# Dataset Card
# Dataset Card: TweetEval (Sentiment Analysis Subset)

## Overview
* **Dataset Name:** TweetEval (Sentiment classification task)
* **Source:** Hugging Face Hub (`cardiffnlp/tweet_eval`)
* **Local Path:** `data/raw/dataset.csv`
* **File Integrity (SHA-256):** `dce6972f1befea999ce920770b07e79460a3be3cf8041767a93f4b3df4e1a18c`

## Dataset Statistics & Structure
* **Dimensions:** 47,615 rows, 2 columns (`text`, `label`)
* **Missing Values:** 0 null values detected across columns.
* **Duplicates:** 29 text duplicates identified.
* **Features:**
  * `text`: Text content of the tweet (String). Length ranges from 10 to 200 characters (Mean: ~106.9 characters).
  * `label`: Sentiment target class encoded numerically.
    * Proportion distribution: 
      * Label `1`: ~45.24%
      * Label `2`: ~39.21%
      * Label `0`: ~15.55%

## Intended Use
This dataset is utilized for training and evaluating text classification models in natural language processing (NLP) tasks, specifically sentiment polarity prediction.