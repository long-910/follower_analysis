# GitHub Follower Analysis

This Python script retrieves information about a user's GitHub followers and following, and performs an analysis to identify:

- Mutual followers: Users who follow each other.
- Users followed by the user but not following back.
- Users who follow the user but are not followed back.

## Requirements

- Python 3.x
- requests
- pandas

You can install the required packages via pip:

```bash
pip install requests pandas
```


## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/long-910/github-follower-analysis.git
   cd github-follower-analysis
   ```
1. Run the script:
   ```base
   python follower_analysis.py
   ```

1. Enter your GitHub username when prompted.

## Notes

- If you encounter an "API rate limit exceeded" error, please wait for some time before running the script again.
- The script uses GitHub API v3.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


