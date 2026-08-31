# Movie Recommender System — Internship Task 8

A content-based movie recommendation project with a Jupyter Notebook workflow and a Streamlit user interface.

## Overview

The application accepts a movie title and returns five similar movie recommendations using precomputed similarity scores and serialized movie metadata.

## Repository Contents

```text
Movie_Recommender_task_8/
├── app.py                       # Streamlit application
├── movie-recommender.ipynb      # Model/data preparation notebook
├── movie_dict.pkl               # Serialized movie metadata
├── movies.pkl                   # Serialized movie data artifact
├── movie_Recommender_Report.pdf # Project report
└── README.md
```

## How the App Works

1. Movie metadata is loaded into a pandas DataFrame.
2. The selected movie is located in the dataset.
3. Precomputed similarity scores are ranked.
4. The five closest matches are displayed in Streamlit.

## Tech Stack

- Python
- pandas
- Streamlit
- Pickle
- Jupyter Notebook

## Getting Started

```bash
python -m venv .venv
pip install pandas streamlit requests scikit-learn jupyter
```

The Streamlit entry point is:

```bash
streamlit run app.py
```

## Important Reproducibility Note

The current `app.py` loads a file named `similarity.pkl`, but that artifact is **not currently present at the repository root**. The Streamlit application will not run successfully until the similarity matrix is regenerated from the notebook or the required serialized file is restored.

This README intentionally documents that limitation rather than claiming a fully reproducible deployment.

## Future Improvements

- Regenerate and include the required similarity artifact or create it at startup.
- Add a `requirements.txt` with tested dependency versions.
- Improve Streamlit labels and input validation.
- Add poster/API integration only if an external movie API is configured correctly.
- Avoid committing large generated artifacts when they can be reproduced reliably.

## Project Type

**Internship / learning project.** It demonstrates recommendation-system fundamentals and a simple interactive ML interface.

---

Maintained by [@rkmaurya93049](https://github.com/rkmaurya93049).