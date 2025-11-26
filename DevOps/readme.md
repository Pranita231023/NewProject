# Assignemnt 6 Exploring Containerization and Application Deployment with Docker
🐳 My First Docker Project (Apache Web Server on AWS EC2)

Hi future me 👋,
This is what I did today step by step. Read it like a story so you don’t forget 🚀

---

## 🌍 What I wanted to do

* Make a tiny website that says **“Hello, Docker!”**
* Put it inside a **Docker container** with **Apache web server**
* Run it on my **AWS EC2 instance** (cloud computer)
* Open it in a browser at `http://<my-ec2-ip>:8080`

---

## 🧰 Tools I used

* **AWS EC2** (Ubuntu machine = my cloud laptop 💻☁️)
* **Docker** (to make containers 🐳)
* **Apache (httpd)** (to serve my web page 🍽️)

---

## ☁️ Steps for AWS EC2 Setup

1. **Create EC2 Instance**

   * Chose **Ubuntu 22.04** (free tier t2.micro).
   * Created **key pair (.pem file)** to connect.
   * In **Security Group**, opened ports:

     * **22 (SSH)** → so I can connect
     * **8080 (TCP)** → so I can see my website

2. **Connect to EC2** (from my computer terminal):

   ```bash
   ssh -i mykey.pem ubuntu@<EC2-Public-IP>
   ```

3. **Update EC2 and Install Docker**:

   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
   sudo usermod -aG docker ubuntu
   ```

---

## 👣 Steps I took for Docker Project (like a recipe)

1. **Make a folder for my project**

   ```bash
   mkdir mydockerapp
   cd mydockerapp
   ```

2. **Create a simple web page**

   ```bash
   echo "<h1>Hello, Docker</h1>" > index.html
   ```

3. **Create a Dockerfile**

   ```dockerfile
   vim Dockerfile
   ```

   ```
   FROM httpd:2.4
   COPY index.html /usr/local/apache2/htdocs/
   ```
   ```
   :wq! ((save the file)
   ```

   👉 This means:

   * “Hey Docker, use Apache as base”
   * “Copy my `index.html` inside Apache’s web folder”

4. **Build my Docker image**

   ```bash
   sudo docker build -t my-apache-server .
   ```

5. **Run my container**

   ```bash
   sudo docker run -p 8080:80 -d my-apache-server
   ```

   👉 This means:

   * Port 80 inside container → Port 8080 on EC2
   * Run in background mode

6. **Check it’s running**

   ```bash
   sudo docker ps
   ```

7. **Open in browser**

   ```
   http://<EC2-Public-IP>:8080
   ```

   🎉 I saw my page: **Hello, Docker!**

---

## 🧹 Cleanup (if needed)

* Stop the container:

  ```bash
  sudo docker stop <container_id>
  ```
* Remove container:

  ```bash
  sudo docker rm <container_id>
  ```
* Remove image:

  ```bash
  sudo docker rmi my-apache-server
  ```

---

## 🎯 What I learned

* **EC2** = my computer in the cloud ☁️
* **Docker** = magic box for apps 🪄
* **Apache** = waiter who serves my web page 🍽️
* **Port mapping** = “Hey outside world, talk to my container through this door 🚪”

---

## 📘 Quick Docker Commands (cheat sheet for future me)

* See running containers:

  ```bash
  docker ps
  ```
* See all containers (even stopped ones):

  ```bash
  docker ps -a
  ```
* List all images:

  ```bash
  docker images
  ```
* Stop container:

  ```bash
  docker stop <id>
  ```
* Remove container:

  ```bash
  docker rm <id>
  ```
* Remove image:

  ```bash
  docker rmi <image-name>
  ```
---

