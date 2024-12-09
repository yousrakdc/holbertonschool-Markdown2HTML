import sys
import os

# Check if there are less than two arguments
if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get the input Markdown file and the output HTML file
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# If all conditions are met, print nothing and exit 0
sys.exit(0)
