### ENV FILE

```bash
SECRET_KEY=your_secret_key
# Database Configuration
DB_NAME=fastapi-template
DB_HOSTNAME=db # Use the service name defined in docker-compose.yml
DB_PORT=5432 # Default PostgreSQL port
DB_USERNAME=fastapi_template_user
DB_PASSWORD=your_secure_password
DB_ROOT_PASSWORD=your_root_password
# Additional Configuration
REDIS_URL=redis://redis:6379 # Redis URL based on service name defined in docker-compose.yml
SLACK_WEBHOOK_URL=
# Docker Configuration
ENVIRONMENT_NAME=docker
SERVER_PORT=8000
```

### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### Common errors
* even when env file is there docker compose fails to read it.
  * run as `docker compose --env-file .env.docker up`

### Running Redis
To run Redis, use the following command:
```bash
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)
