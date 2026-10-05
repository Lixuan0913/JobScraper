
# Job Scraper

A small Python script that scrapes job listings from the ['https://realpython.github.io/fake-jobs/'](https://roadmap.sh/projects/job-listings-scraper) practice site and saves them to a CSV file.

## What it does

For each job card on the page, the script extracts:

- Job title
- Company
- Location
- Learn link (the `href` of the first footer link)

Missing fields are saved as empty values instead of crashing the script. The results are written to `jobs.csv`.

## Requirements

- Python 3.9+
- `requests`
- `beautifulsoup4`
- `pandas`

Install the dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

Run the script from the project folder:

```bash
python main.py
```

On success you will see:

```
Jobs data saved to jobs.csv
```

If no job cards are found, the script prints `No jobs found.` and does not create a file.

## Output

`jobs.csv` has one row per job with these columns:

| Column       | Description                              |
|--------------|------------------------------------------|
| `title`      | Job title                                |
| `company`    | Company name                             |
| `location`   | Job location                             |
| `learn_link` | URL from the card's first footer link    |

Note: on this practice site every Learn link points to the same address. If you want a unique link per job, select the Apply link instead.

## How it works

1. `fetch_link(url)` downloads the page (10 second timeout, raises an error on bad status codes) and parses it with BeautifulSoup.
2. `extract_jobs(soup)` loops over each `div.card` and pulls out the fields with the helper functions `get_text` and `get_attribute`.
3. The list of jobs is converted to a pandas DataFrame and saved with `to_csv`.

## Troubleshooting


- **Empty `learn_link` column:** make sure you loop over `div.card` (not `card-content`), because the footer link sits outside `card-content`.
- **No jobs found:** check your internet connection, or whether the site's HTML classes have changed.
