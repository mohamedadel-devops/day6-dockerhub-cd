# Day 6 – DockerHub CD Pipeline with GitHub Actions and EC2 Deployment

This project demonstrates a **complete Continuous Deployment (CD) pipeline** using GitHub Actions. Upon pushing code to the repository, a GitHub Actions workflow automatically:

1. Connects to AWS EC2 via SSH.
2. Pulls the latest Docker image from Docker Hub.
3. Stops and removes any existing container.
4. Runs the updated container, exposing it on port 5000.

---

## 🔧 Tech Stack

- **GitHub Actions** – CI/CD automation
- **Docker** – Containerization
- **Docker Hub** – Image registry
- **AWS EC2 (Ubuntu)** – Deployment server

---

## 🚀 Deployment Workflow

1. Code is pushed to `main` branch.
2. GitHub Actions triggers `dockerhub-cd.yml` workflow.
3. SSH into EC2 using a private key stored in GitHub Secrets.
4. Run the following on EC2:
    - Stop old container (if exists)
    - Pull latest image from Docker Hub
    - Run the container with exposed port `5000`

---

## 🔐 GitHub Secrets Used

| Secret Name       | Description                     |
|-------------------|---------------------------------|
| `EC2_SSH_KEY`     | PEM private key (Base64 encoded)|
| `EC2_USER`        | Default: `ubuntu`               |
| `EC2_HOST`        | EC2 Public IP                   |
| `DOCKER_USERNAME` | DockerHub username              |
| `DOCKER_PASSWORD` | DockerHub password or PAT       |

---

## ✅ Result

Once pushed, the latest Docker image is deployed to the EC2 instance, and the app becomes available at:

http://34.219.157.83:5000



---

## 🧑‍💻 Author

**Mohamed Adel Asar**  
🔗 [devops-eng.info](https://www.devops-eng.info)  
💼 [LinkedIn](https://www.linkedin.com/in/mohamed-asar-907100370/)  
📁 [GitHub](https://github.com/mohamedadel-devops)

---

## 📂 Files

- `.github/workflows/dockerhub-cd.yml`: GitHub Actions CD pipeline
- `Dockerfile`: Image definition
- `app.py`: Flask web app (hello world + timestamp)
- `requirements.txt`: Flask dependencies

