#!/bin/bash

# Define Variables
SQL_DEVELOPER_URL="https://download.oracle.com/otn/java/sqldeveloper/sqldeveloper-23.1.0-097.1929-no-jre.zip"
INSTALL_DIR="$HOME/sql-developer"
DESKTOP_FILE="$HOME/.local/share/applications/sqldeveloper.desktop"

# Function to check if a package is installed
function check_install() {
    dpkg -l | grep -i "$1" > /dev/null 2>&1
}

echo "Updating system..."
sudo apt update -y

echo "Installing dependencies..."
sudo apt install -y default-jdk unzip wget libaio1 alien

# Ensure Java is installed
if ! java -version &>/dev/null; then
    echo "Java is not installed. Please install Java manually and retry."
    exit 1
fi

# Create installation directory
mkdir -p $INSTALL_DIR

echo "Downloading SQL Developer..."
wget --no-check-certificate --progress=bar:force -O sqldeveloper.zip "$SQL_DEVELOPER_URL"

echo "Extracting SQL Developer..."
unzip -q sqldeveloper.zip -d $INSTALL_DIR
rm sqldeveloper.zip

# Create an executable launcher
echo "Creating executable shortcut..."
echo "#!/bin/bash" > $INSTALL_DIR/sqldeveloper.sh
echo "$INSTALL_DIR/sqldeveloper/sqldeveloper.sh" >> $INSTALL_DIR/sqldeveloper.sh
chmod +x $INSTALL_DIR/sqldeveloper.sh

# Create Desktop Shortcut
echo "[Desktop Entry]
Name=SQL Developer
Exec=$INSTALL_DIR/sqldeveloper.sh
Icon=$INSTALL_DIR/sqldeveloper/icon.png
Type=Application
Categories=Development;" > $DESKTOP_FILE

chmod +x $DESKTOP_FILE

echo "Installation completed! You can launch SQL Developer using: $INSTALL_DIR/sqldeveloper.sh"
