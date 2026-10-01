# Read-only EVM quickstart samples

Original English and Simplified Chinese developer-documentation examples by Pep.Liu, with a Python local JSON-RPC fixture. AI-assisted writing and checks. Independent demonstration; not a customer project, live blockchain test, or security audit.

## Run the local demonstration

Requirements: Python 3 and curl. No packages, account, wallet, API key, or network provider are needed.

1. In one terminal, run `python3 rpc_fixture.py`.
2. In another terminal, follow [the English quickstart](sample-en.md) or [the Chinese version](sample-zh.md).
3. Stop the server with Ctrl+C when finished. It listens only on `127.0.0.1:8765`.

The fixture simulates chain ID `0x1`; it does not connect to Ethereum. It is a teaching fixture, not a complete JSON-RPC implementation. Four local request checks passed: success, unsupported method, invalid parameters, and invalid JSON. See [verification scope](VERIFICATION.json). No production provider has been checked.

## What the documents demonstrate

- A first copyable read-only request, with an explicit timeout.
- Separate HTTP and JSON-RPC failure explanations.
- Five practical troubleshooting entries.
- Clear identification of simulated output and safe credential handling.
- Simplified Chinese terminology and reader-focused localization.

## Licensing

Original sample text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original fixture code: MIT, copyright 2026 Pep.Liu. See [rights record and MIT permission text](RIGHTS.md). No copied third-party documentation, graphics, fonts, or client material is included.

## Related documentation service

Pep.Liu offers AI-assisted documentation packages for developer-tool teams: **$79 USD** for one existing English quickstart (up to 1,000 words, review of up to three examples, five troubleshooting entries, one revision), or **$49 USD** for a Simplified Chinese trial (up to 600 English source words and 20 glossary terms, one revision). Markdown delivery within 72 hours after payment and required materials are received.

Enquiries: **liutungjing@gmail.com**. Send the public source page, target reader and desired correction. Scope is agreed in writing before a PayPal commercial invoice. Do not send credentials or production access. If the agreed scope cannot be delivered, the invoice is refunded; a deadline at risk prompts a new-date or refund option before expiry. One revision may be requested within seven days; in-scope errors are corrected. No investment advice, wallet operations, security audits or guaranteed business results. No professional credentials or client history are claimed.
