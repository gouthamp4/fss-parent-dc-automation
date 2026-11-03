# FSS Parent DC Automation

Python network automation experiments for the parent data center.

Requires Python 3.12 or later. No third-party dependencies are needed for the initial offline workflow.

```sh
python3 automation.py --inventory inventory.example.json
python3 -m unittest discover -s tests -v
```

The command validates inventory and prints a connection plan. It does not connect to devices or change their configuration. Replace the documentation addresses in a local inventory before adding real device operations. Keep credentials out of inventory and Git; use secure environment bindings when authentication is implemented.

Device platform, transport, and automation tasks are intentionally left for the next experiment.
