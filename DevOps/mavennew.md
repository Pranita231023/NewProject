📘 Maven Web App Deployment on AWS EC2 (Step-by-Step Guide)

This guide explains how to install Java, Maven, create a Maven project, configure pom.xml, deploy Jetty on port 8080, and run a web application on an AWS EC2 Ubuntu instance.

🔧 1️⃣ Update System
```sudo apt update -y```


✔ This checks for the latest package updates.

☕ 2️⃣ Install Java (OpenJDK 17)
```sudo apt install -y openjdk-17-jdk```


✔ Java is required to run Maven and Java applications.

📦 3️⃣ Install Maven
'''sudo apt install -y maven'''


✔ Maven is used to build Java projects and manage dependencies.

🧪 4️⃣ Verify Installations
java -version
mvn -version


✔ Confirms Java & Maven are installed correctly.

📝 5️⃣ Create Setup Script

Open the script file:

vim maven_setup.sh


Paste the following content inside:

#!/bin/bash

# Exit on error
set -e

echo "🚀 Updating system..."
sudo apt update -y

echo "☕ Installing Java (OpenJDK 17)..."
sudo apt install -y openjdk-17-jdk

echo "📦 Installing Maven..."
sudo apt install -y maven

echo "✅ Java & Maven Installed:"
java -version
mvn -version

# Variables
APP_NAME="my-webapp"
GROUP_ID="com.example"
APP_DIR="/home/ubuntu/$APP_NAME"

echo "📂 Creating Maven Web Project..."
mvn archetype:generate \
    -DgroupId=$GROUP_ID \
    -DartifactId=$APP_NAME \
    -DarchetypeArtifactId=maven-archetype-webapp \
    -DinteractiveMode=false

cd $APP_DIR

echo "📝 Creating a correct pom.xml..."
cat > pom.xml <<EOL
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>$GROUP_ID</groupId>
  <artifactId>$APP_NAME</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>war</packaging>

  <build>
    <plugins>
      <plugin>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-maven-plugin</artifactId>
        <version>9.4.54.v20240208</version>
        <configuration>
          <httpConnector>
            <port>8080</port>
          </httpConnector>
        </configuration>
      </plugin>
    </plugins>
  </build>

</project>
EOL

echo "💻 Creating index.jsp..."
mkdir -p src/main/webapp
cat > src/main/webapp/index.jsp << 'EOF'
<html>
  <body>
    <h1 style="color:red; text-align:center;">
      Hello Maven Web App on AWS EC2 (Port 8080)<br>
      Its all automatic BROOOO!!!!!!!!!!!!
    </h1>
  </body>
</html>
EOF

echo "🛡️ Configuring firewall for port 8080..."
sudo ufw allow 8080/tcp
sudo ufw --force enable

echo "🛠️ Creating systemd service for auto-start..."
sudo bash -c "cat > /etc/systemd/system/maven-webapp.service <<EOL
[Unit]
Description=Maven Jetty Web Application
After=network.target

[Service]
Type=simple
WorkingDirectory=$APP_DIR
ExecStart=/usr/bin/mvn jetty:run
Restart=always
User=ubuntu

[Install]
WantedBy=multi-user.target
EOL"

echo "🔄 Reloading systemd and enabling service..."
sudo systemctl daemon-reload
sudo systemctl enable maven-webapp.service
sudo systemctl start maven-webapp.service

# Detect EC2 public IP
EC2_PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

echo "✅ Setup complete!"
echo "👉 Open in browser: http://$EC2_PUBLIC_IP:8080/"


Save the file:

:wq

▶️ 6️⃣ Make the Script Executable
chmod +x maven_setup.sh

🚀 7️⃣ Run the Script
./maven_setup.sh

🌐 8️⃣ Add EC2 Security Group Rules

While creating EC2 instance, open these ports:

Port	Purpose
22	SSH access
80	HTTP (optional)
8080	Jetty Web App
🌍 9️⃣ Access Your Web App

Open your browser:

http://<EC2_PUBLIC_IP>:8080/


You should see your Maven Web App running successfully.
