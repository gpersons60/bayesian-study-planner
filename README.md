# Bayesian Study Planner

A Python project that will use a Bayesian network to recommend study sessions based on concept difficulty, student mastery, stress, and time remaining until an exam.

## Project goals

- Model at least three course concepts using a Bayesian network with approximately ten variables or fewer.
- Define and document conditional probability tables (CPTs).
- Use built-in probabilistic inference to estimate exam preparedness.
- Compare scheduling actions using expected utility, balancing exam success and student stress.
- Create study sessions using the Google Calendar API.
- Simulate different student scenarios to test how scheduling decisions change.

## Planned actions

1. Intense study: 5-hour block
2. Moderate study: 2-3-hour session
3. Light review: 1-hour session
4. Rest day: no study session

## Setup

Use Python 3.11 or 3.12.

On Windows, in a terminal opened in this folder:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

If Python 3.12 is not installed, replace `-3.12` with your installed compatible Python version.

## Run the starter program

```powershell
python -m src.main --exam-date 2026-12-10
```

Run the starter tests:

```powershell
python -m unittest discover -s tests
```

## Project status

Initial repository structure and exam date calculation are in place. Bayesian inference, the utility function, scenario simulations, and Google Calendar integration are planned but not implemented yet.

## Google Calendar credentials

OAuth credentials will be configured later. Never commit `credentials.json`, `token.json`, or `.env` files to the repository.
