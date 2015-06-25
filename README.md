# Logs.tf Scraper
Libraries and utilities for scraping (one-off and real-time) Logs.tf data.

## Usage
Get a specific match:
```py
import PyLogsTF
PyLogsTF.get(828613)
```

Get the id of the latest match:
```py
import PyLogsTF
PyLogsTF.latest_match()
```

Get all the matches since the last run:
```py
import logstf_sync
logstf_sync.run('last')
```
