import argparse
from .core import analyze_commit_message, generate_astrological_reading

def main():
    parser = argparse.ArgumentParser(description="The Commit Message Astrologer: Predicts the fate of your code.")
    parser.add_argument("message", nargs="+", help="Your commit message.")
    parser.add_argument("--system", default="classic", choices=["classic", "software_engineers", "mythical_creatures"],
                        help="The astrology system to use (default: classic).")
    args = parser.parse_args()

    commit_message = " ".join(args.message)
    try:
        analysis_results = analyze_commit_message(commit_message, system=args.system)
        astrological_reading = generate_astrological_reading(analysis_results)
        print(astrological_reading)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()