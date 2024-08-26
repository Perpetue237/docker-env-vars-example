# Docker Environment Variables Example

This repository demonstrates how to work with environment variables in Docker. It covers the following topics:

1. **Using `.env` files**
2. **Setting environment variables from the OS**
3. **Passing environment variables via `Dockerfile`**
4. **Using environment variables with `docker-compose.yml`**
5. **Building Docker images with build arguments**

## 1. Using `.env` Files
You can store environment variables in a [.env](.env) file and make them available to Docker.

### Passing .env to Docker with docker run:
```bash
docker run --env-file .env --rm my-image
```

### Expected Output:

```bash
MY_VARIABLE_FROM_OS: None
MY_VARIABLE_FROM_ENV: Hello from .env file
MY_VARIABLE_FROM_DOCKERFILE: Hello from Dockerfile!
MY_VARIABLE_FROM_DC: None
MY_BUILD_ARG (MY_VARIABLE): 
MY_BUILD_ARG_FROM_DC (MY_BUILD_ARG_FROM_DC): 

```
### Using .env with Docker Compose:
The following shows how to make the `.env` available in the service `myapp`. 

```bash
version: '3.8'

services:
  myapp:
    env_file:
      - .env

```
In the section 4. we will see how to run the service and the expected output.

## 2. Setting Environment Variables from the OS

You can pass environment variables from your OS to Docker containers. For example:

```bash
export MY_VARIABLE_FROM_OS="Hello, from os!"
docker run -e MY_VARIABLE_FROM_OS --rm my-image
```
### Expected Output:
```bash
MY_VARIABLE_FROM_OS: Hello, from os!
MY_VARIABLE_FROM_ENV: None
MY_VARIABLE_FROM_DOCKERFILE: Hello from Dockerfile!
MY_VARIABLE_FROM_DC: None
MY_BUILD_ARG (MY_VARIABLE): 
MY_BUILD_ARG_FROM_DC (MY_BUILD_ARG_FROM_DC): 
```

## 3. Passing Environment Variables via `Dockerfile`

You can use the `ENV` instruction in a [Dockerfile](Dockerfile) to set environment variables that will be available during runtime. Build the docker image using:

```bash
docker build  -t my-image .
```
After building your Docker image, you can run the container and check the output of the environment variables by using the following command:

```bash
docker run --rm my-image
```

### Expected Output:
```bash
MY_VARIABLE_FROM_OS: None
MY_VARIABLE_FROM_ENV: None
MY_VARIABLE_FROM_DOCKERFILE: Hello from Dockerfile!
MY_VARIABLE_FROM_DC: None
MY_BUILD_ARG (MY_VARIABLE): 
MY_BUILD_ARG_FROM_DC (MY_BUILD_ARG_FROM_DC):
```

## 4. Using Environment Variables with `docker-compose.yml`

You can define environment variables directly in your [docker-compose.yml](docker-compose.yml) file.
These variables are passed to the container when it starts. 

After setting up your [docker-compose.yml](docker-compose.yml) and [Dockerfile](Dockerfile), you can run your service with:

```bash
docker-compose up --build
```

This command will build the Docker image (taking into account any build arguments), start the container, and apply all the environment variables from the .env file, docker-compose.yml, and Dockerfile.

### Expected Output:

```bash
Creating docker-env-vars-example_myapp_1 ... done
Attaching to docker-env-vars-example_myapp_1
myapp_1  | MY_VARIABLE_FROM_OS: None
myapp_1  | MY_VARIABLE_FROM_ENV: None
myapp_1  | MY_VARIABLE_FROM_DOCKERFILE: Hello from Dockerfile!
myapp_1  | MY_VARIABLE_FROM_DC: Hello from docker-compose.yml
myapp_1  | MY_BUILD_ARG (MY_VARIABLE): 
myapp_1  | MY_BUILD_ARG_FROM_DC (MY_BUILD_ARG_FROM_DC): Hello build build ARG from docker-compose.yml

```

## 5. Building Docker Images with Build Arguments

You can pass build-time arguments using the `ARG` instruction in the [Dockerfile](Dockerfile).

Build with arguments:

```bash
docker build --build-arg MY_BUILD_ARG="Hello during build from command line" -t my-image .
```

After building your Docker image, you can run the container and check the output of the environment variables by using the following command:

```bash
docker run --rm my-image
```

### Expected Output:
```bash
MY_VARIABLE_FROM_OS: None
MY_VARIABLE_FROM_ENV: None
MY_VARIABLE_FROM_DOCKERFILE: Hello from Dockerfile
MY_VARIABLE_FROM_DC: None
MY_BUILD_ARG (MY_VARIABLE): Hello during build from command line
MY_BUILD_ARG_FROM_DC (MY_BUILD_ARG_FROM_DC):
```

Build arguments (ARG) are only available during the build process. However, you can pass them to runtime environment variables using ENV if needed.

## License

Distributed under the Apache License. See [LICENSE](LICENSE) for more information.

## Contact

[Perpetue Kuete Tiayo](https://www.linkedin.com/in/perpetue-k-375306185)
