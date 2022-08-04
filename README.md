# dota-highlights
Extract highlights from professional Dota 2 matches.

### TODO
- Build and run with docker-compose
- Refactor youtube.py

## Setup
### Create a virtual environment
```
python3 -m virtualenv env
source env/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Build and Run Clarity Parser Server
```
sh scripts/run_clarity.sh
```

### Run Redis and Celery Workers
```
sh scripts/run_workers.sh
```

### Run Flask API
Open a new terminal window<br>
```
source env/bin/activate
sh scripts/run_server.sh
```

## Retrieve URLs
Retrieve replay URLs by Tournament ID (Could be found at the end of Dotabuff [links](https://www.dotabuff.com/esports/leagues/13256-the-international-2021)). The result will be saved to `replays/urls.txt`<br>
```
python scripts/retrieve_match_urls.py --tournament 13256 --limit 15
```

## Parse Matches
Parse match by URL<br>
```
curl -X GET 'http://localhost:5000/parse?url=http://replay191.valve.net/570/6216665747_89886887.dem.bz2'
```

Parse first match from `urls.txt`<br>
```
curl -X GET -G 'http://localhost:5000/parse' -d url=$(head -n 1 replays/urls.txt)
```

Parse all matches from `urls.txt`<br>
```
python scripts/parse_from_urls.py
```
