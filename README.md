# Log Report – Harbor Task

This repository contains a fixed Harbor (Terminal-Bench) task that parses an Apache-style access log and generates a JSON summary report.

## Task

The agent must:

- Read the Apache access log.
- Count the total number of requests.
- Count the number of unique client IP addresses.
- Determine the most requested page.
- Save the output as `/app/report.json`.

## Repository Structure

```
environment/
├── Dockerfile
├── access.log

solution/
├── solve.py
└── solve.sh

tests/
├── test_outputs.py
└── test.sh

instruction.md
task.toml
```

## Verification

The verifier checks:

- Total request count
- Unique client IP count
- Most requested page

Oracle agent returns reward **1**.

NOP agent returns reward **0**.

## Notes

The task has been fixed by:

- Correcting the Harbor `task.toml` configuration.
- Pinning the Docker base image.
- Removing the leaked reference solution from the agent image.
- Improving the verifier to validate actual output values.
- Writing reward to the correct Harbor path.
- Updating the instructions to match the verifier.
