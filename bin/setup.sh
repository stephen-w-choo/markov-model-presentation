#!/bin/bash

# Exit if any command fails
set -e

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Download nltk data
echo "Downloading NLTK punkt tokenizer models..."
python -c "import nltk; nltk.download('punkt')"

echo "Setup complete!"