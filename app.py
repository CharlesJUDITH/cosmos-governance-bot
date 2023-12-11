import requests
import json

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/addyourslackwebhookhere'

def load_chain_endpoints(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def fetch_active_governance_proposals(chain, endpoint):
    url = f"{endpoint}/cosmos/gov/v1beta1/proposals?proposal_status=2"
    try:
        response = requests.get(url)
        if response.status_code == 404:  # Skip if endpoint not found
            return None
        response.raise_for_status()
        data = response.json()
        return data.get("proposals", [])
    except requests.RequestException as e:
        print(f"Error fetching active proposals for {chain}: {e}")
        return None

def post_to_slack(message):
    payload = {'text': message}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload),
                             headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")

def generate_mintscan_link(chain, proposal_id):
    mintscan_chain_name = chain
    return f"https://www.mintscan.io/{mintscan_chain_name}/proposals/{proposal_id}"

# Not yet used
def generate_pingpub_link(chain, proposal_id):
    pingpub_chain_name = chain
    return f"https://ping.pub/{mintscan_chain_name}/gov/{proposal_id}"

def main():
    chain_endpoints = load_chain_endpoints("chains.json")
    messages = []

    for chain, endpoint in chain_endpoints.items():
        proposals = fetch_active_governance_proposals(chain, endpoint)
        if proposals:
            message = f"*Active Governance Proposals for {chain.title()}:*\n"
            for proposal in proposals:
                title = proposal['content'].get('title', 'No title available')
                mintscan_link = generate_mintscan_link(chain, proposal['proposal_id'])
                message += f" Proposal ID: {proposal['proposal_id']}\n Title: {title}\n Details: {mintscan_link}\n"
            messages.append(message)

    # Combine all messages and send to Slack
    full_message = "\n".join(messages)
    post_to_slack(full_message)


if __name__ == "__main__":
    main()
