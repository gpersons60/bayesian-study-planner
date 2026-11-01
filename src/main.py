from argparse import ArgumentParser
from datetime import date


def days_until_exam(exam_date: date, today: date | None = None) -> int:
    return (exam_date - (today or date.today())).days


def main() -> None:
    parser = ArgumentParser(description="Bayesian Study Planner")
    parser.add_argument("--exam-date", required=True, type=date.fromisoformat)
    args = parser.parse_args()
    days_remaining = days_until_exam(args.exam_date)
    if days_remaining < 0:
        parser.error("The exam date cannot be in the past.")
    print(f"Days until exam: {days_remaining}")
    print("Bayesian scheduling and calendar integration are not implemented yet.")


if __name__ == "__main__":
    main()
