# hn-cli

A simple command-line interface to browse Hacker News stories and comments.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hn-cli.git
   cd hn-cli
   ```
2. Install required packages:
   ```bash
   pip install requests
   ```

## Usage

Run the script to fetch top stories:
```bash
python fetcher.py
```

You can specify a category like `topstories`, `newstories`, etc.

## Notes

Cache is used to store fetched data for 5 minutes.