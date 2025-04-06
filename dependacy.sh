#!/bin/bash

# Set script to exit on error
set -e

echo "🔹 Step 1: Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "🔹 Step 2: Installing Python 3.12 and required packages..."
sudo apt install -y python3.12 python3.12-venv python3.12-dev python3-pip

echo "🔹 Step 3: Creating a virtual environment (venv)..."
python3.12 -m venv venv

echo "🔹 Step 4: Activating the virtual environment..."
source venv/bin/activate

echo "🔹 Step 5: Installing Robot Framework..."
pip install --upgrade pip
pip install robotframework

echo "🔹 Step 6: Installing Pytest..."
pip install pytest

echo "🔹 Step 7: Installing Java (OpenJDK 21)..."
sudo apt install -y openjdk-21-jdk

echo "🔹 Step 8: Verifying installations..."
echo "✅ Python version: $(python --version)"
echo "✅ Robot Framework version: $(robot --version)"
echo "✅ Pytest version: $(pytest --version)"
echo "✅ Java version: $(java --version)"

echo "🎉 Setup completed successfully!"


#########################################
# additional library
########################################
# Selenium for Web Automation
pip install robotframework-seleniumlibrary

# Requests for API Testing
pip install robotframework-requests

# Database Library
pip install robotframework-databaselibrary

# python requests library
pip install requests
