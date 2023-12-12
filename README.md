# cosmos governance bot

Cosmos governance bot to send last active proposals on Slack.

## Configuration

chains.json
```
{
    "akash": "https://api.akash.domain.tld",
    "celestia": "https://api.celestia.domain.tld",
    "cosmos": "https://api.cosmoshub.domain.tld",
    "dydx": "https://api.dydx.domain.tld",
    "evmos": "https://api.evmos.domain.tld",
    "injective": "https://api.injective.domain.tld",
    "osmosis": "https://api.osmosis.domain.tld",
    "shentu": "https://api.shentu.domain.tld
    ...
}
```

## Installation

Install the python prerequisites:

`pip install requests`

## Run

Run the script:

`python app.py`

## TODO

- API to expose the proposals
- Docker image 
