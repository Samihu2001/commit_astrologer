# The Commit Message Astrologer

A humorous command-line tool that analyzes your commit messages and provides an "astrological" reading about the fate of your code and the likelihood of merge conflicts.

## Usage

1.  Make the `commit_astrologer/cli.py` file executable:
    ```bash
    chmod +x commit_astrologer/cli.py
    ```

2.  Run the script with your commit message:
    ```bash
    ./commit_astrologer/cli.py "fix: Resolved a critical security vulnerability"
    ./commit_astrologer/cli.py "feat: Implement user profile page"
    ./commit_astrologer/cli.py "refactor: Clean up authentication logic"
    ```

3.  You can also choose a different astrology system:
    ```bash
    ./commit_astrologer/cli.py --system software_engineers "feat: Added a new API endpoint"
    ./commit_astrologer/cli.py --system mythical_creatures "fix: Slayed a persistent bug"
    ```

## Potential Features (Future)

* More astrology systems!
* "Compatibility" readings with the main branch history (requires Git integration).
* Options to customize readings or contribute new astrological rules.

## Installation (Basic)

For now, you can simply clone this repository and run the `cli.py` script. For proper installation as a command-line tool, you would typically use `pip`. We'll add those instructions later.

## License

[MIT LICENSE]