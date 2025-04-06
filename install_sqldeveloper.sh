# #!/bin/bash

# # SQL Developer Installation Script for Ubuntu
# # Author: Mayur
# # Description: This script installs SQL Developer in a virtual environment

# set -e  # Exit immediately if any command fails

# # Step 1: Update and Install Required Dependencies
# echo "Updating system and installing dependencies..."
# sudo apt update && sudo apt upgrade -y
# sudo apt install -y openjdk-17-jdk libxrender1 libxtst6 libxi6 unzip libglib2.0-0 libgdk-pixbuf2.0-0 libxext6 libx11-6 libgtk-3-0

# # Step 2: Create a Python Virtual Environment (Even if not necessary, for separation)
# echo "Creating virtual environment..."
# python3 -m venv sql_dev_env
# source sql_dev_env/bin/activate

# # Step 3: Set up SQL Developer directory
# SQLDEV_DIR="$HOME/sqldeveloper"
# mkdir -p "$SQLDEV_DIR"

# # Step 4: Download SQL Developer (Manual step required)
# echo "Please download SQL Developer from:"
# echo "https://www.oracle.com/tools/downloads/sqldev-downloads.html"
# echo "Move the downloaded ZIP file to $SQLDEV_DIR and press Enter to continue..."
# read -r

# # Check if file exists
# ZIP_FILE=$(ls $SQLDEV_DIR/sqldeveloper-*.zip 2>/dev/null || true)
# if [[ -z "$ZIP_FILE" ]]; then
#     echo "Error: SQL Developer zip file not found in $SQLDEV_DIR. Please download and try again."
#     exit 1
# fi

# # Step 5: Extract SQL Developer
# echo "Extracting SQL Developer..."
# unzip "$ZIP_FILE" -d "$SQLDEV_DIR"

# # Step 6: Set Java Home
# echo "Setting Java environment variables..."
# echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
# source ~/.bashrc

# # Step 7: Create a Launcher for SQL Developer
# echo "Creating a desktop shortcut..."
# cat <<EOF > ~/.local/share/applications/sqldeveloper.desktop
# [Desktop Entry]
# Version=1.0
# Type=Application
# Name=SQL Developer
# Exec=$SQLDEV_DIR/sqldeveloper/sqldeveloper.sh
# Icon=$SQLDEV_DIR/icon.png
# Terminal=false
# Categories=Development;
# EOF

# chmod +x ~/.local/share/applications/sqldeveloper.desktop
# update-desktop-database ~/.local/share/applications/

# # Step 8: Final Message
# echo "Installation completed successfully!"
# echo "Run SQL Developer using:"
# echo "cd $SQLDEV_DIR/sqldeveloper/ && ./sqldeveloper.sh"



################################################

#!/bin/bash

echo "Starting MySQL Fix Script..."

# Step 1: Check if MySQL is running
echo "Checking MySQL service status..."
sudo systemctl status mysql >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "MySQL is running. Restarting MySQL..."
    sudo systemctl restart mysql
else
    echo "MySQL is not running."
fi

# Step 2: Fix broken packages
echo "Fixing broken packages..."
sudo apt --fix-broken install -y
sudo dpkg --configure -a

# Step 3: Purge and Remove MySQL if issues persist
echo "Removing existing MySQL installation..."
sudo apt remove --purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-* -y
sudo rm -rf /etc/mysql /var/lib/mysql
sudo apt autoremove -y
sudo apt autoclean

# Step 4: Update system packages
echo "Updating system packages..."
sudo apt update -y

# Step 5: Reinstall MySQL
echo "Reinstalling MySQL..."
sudo apt install mysql-server -y

# Step 6: Secure MySQL installation
echo "Securing MySQL installation..."
sudo mysql_secure_installation

# Step 7: Restart MySQL service and verify
echo "Restarting MySQL service..."
sudo systemctl restart mysql
sudo systemctl enable mysql

# Step 8: Verify MySQL installation
echo "Verifying MySQL installation..."
mysql -u root -e "STATUS;" >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "MySQL installation and fix completed successfully!"
else
    echo "MySQL is still not working. Please check logs for details."
fi

