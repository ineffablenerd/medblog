
# MedBlog Project

Welcome to the MedBlog Docker Project! This README file will guide you through the steps required to run the project using Docker.


## Prerequisites

Before you start, ensure you have the following installed on your system:

- Docker [Install Docker](https://docs.docker.com/engine/install/)


## Pull the Docker Image

To get started, pull the Docker image from Docker Hub using the following command:

```bash
  docker pull ineffablenerd/medblog:v1
```

## Run the Docker Container

Once the image is pulled, you can run the Docker container with the following command:

```bash
docker run -d -p 8000:8000 ineffablenerd/medblog:v1
```


## Explanation of command

- **docker run:**  The command to run a container.
- **-d:** Run the container in detached mode (in the background).
- **-p 8000:8000:** Map port 8000 on the host to port 8000 in the container. Adjust the port if your application uses a different one.
- **ineffablenerd/medblog:v1:** The Docker image to use.

## Access the Application

#### Locally

After running the container, the application should be accessible via your web browser. Open your browser and navigate to:
```bash
  http://localhost:8000
```

#### Remotely (Hosted on EC2)

The project is also hosted on an EC2 instance. You can access it via the following URL:
```bash
  http://43.207.204.48/
```

## Admin Panel

To access the admin panel, navigate to:
```bash
  http://localhost:8000/admin
```

or if you are accessing the hosted version:

```bash
  http://43.207.204.48/admin

```

## Admin Credentials

- **Username:**  rehank2601
- **Password:** admin@1234


## Stopping the Docker Container

To stop the running Docker container, first find the container ID using:
```bash
  docker ps
```

This will list all running containers. Identify the container ID corresponding to ineffablenerd/medblog:v1. Then stop the container with:

```bash
  docker stop <container_id>
```

Replace <container_id> with the actual container ID.

## Conclusion

You now have the MedBlog application running in a Docker container. For any issues or questions, please feel free to open an issue on the project repository or contact the project maintainers.

Happy blogging!


