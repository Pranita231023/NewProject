🌟 Step 0 — Install Docker on EC2

(Required before doing the tasks)

```sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

Log out and log in again.

🧩 Task 1: Dockerfile Creation & Image Build
1️⃣ Create your project folder
```mkdir docker-html
cd docker-html
```
2️⃣ Create a simple HTML web page
```vim index.html
```
Paste this:
```
<html>
  <body>
    <h1 style="color:blue; text-align:center;">Hello from Docker on EC2!</h1>
  </body>
</html>
```

Save:
ESC → :wq

3️⃣ Create the Dockerfile
```vim Dockerfile
```

Paste this:
```
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
```

Save the file.

✔ This uses nginx as the base image
✔ Copies your HTML file into nginx’s default web directory

4️⃣ Build the Docker image
```docker build -t my-html-app:v1 .
```

my-html-app → image name

v1 → tag

. → current directory containing Dockerfile

🧩 Task 2: Running & Managing Containers
1️⃣ Run the container
```docker run -d -p 8080:80 --name mycontainer my-html-app:v1
```

Explanation:

-d → run in background

-p 8080:80 → host port 8080 → container port 80

--name → name of container

2️⃣ Check if container is running
```docker ps
```
3️⃣ Open the webpage

In a browser:

http://<EC2_PUBLIC_IP>:8080


You should see:

“Hello from Docker on EC2!”

🛑 Stop & Remove the Container
1️⃣ Stop the container
```docker stop mycontainer
```
2️⃣ Remove the container
```docker rm mycontainer
```
(Optional) Remove the image
```docker rmi my-html-app:v1```
