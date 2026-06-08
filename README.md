# Naive Bayes Fake/True News Classifier

This project trains a **Naïve Bayes** classifier (from scratch) to distinguish **fake news** from **true news** using two CSV files:  
- `Fake.csv` – contains fake news articles  
- `True.csv` – contains true news articles  

The classifier cleans text, builds a vocabulary, creates binary feature vectors, and applies Laplace smoothing.

## Files

- `task2.py` – main script (training + prediction)
- `Fake.csv` – fake news data
- `True.csv` – true news data
- `README.md` – this file

## How to Run

1. Place `Fake.csv`, `True.csv`, and `task2.py` in the same folder.
2. Run the script:
   ```bash
   python task2.py
