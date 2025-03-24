# #!/bin/bash

# # Set environment variables
# VENV_DIR="$HOME/etl_testing_env"

# echo "Updating system packages..."
# sudo apt update -y
# sudo apt install -y python3 python3-pip python3-venv unixodbc unixodbc-dev libsqlite3-dev

# echo "Creating Python virtual environment..."
# python3 -m venv "$VENV_DIR"

# echo "Activating virtual environment..."
# source "$VENV_DIR/bin/activate"

# echo "Installing ETL testing dependencies..."
# pip install --upgrade pip
# pip install pandas pyodbc sqlalchemy pytest robotframework great_expectations 

# echo "Installation completed!"
# echo "To activate the virtual environment, run: source $VENV_DIR/bin/activate"    
# # source /home/mayur/etl_testing_env/bin/activate



VENV_DIR="$HOME/etl_testing_env"

echo "Checking Virtual Environment..."
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment exists: $VENV_DIR"
else
    echo "Virtual environment NOT found!"
fi

echo "Checking Python Packages..."
source "$VENV_DIR/bin/activate"
MISSING_PKGS=()
for pkg in pandas pyodbc sqlalchemy pytest robotframework great_expectations; do
    pip show "$pkg" > /dev/null 2>&1 || MISSING_PKGS+=("$pkg")
done
if [ ${#MISSING_PKGS[@]} -eq 0 ]; then
    echo "All required Python packages are installed!"
else
    echo "Missing Python packages: ${MISSING_PKGS[*]}"
fi
deactivate

echo "Checking System Dependencies..."
dpkg -l | grep -E "python3|python3-pip|python3-venv|unixodbc|libsqlite3-dev" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "All required system dependencies are installed!"
else
    echo "Some system dependencies are missing!"
fi
