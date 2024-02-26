# JSONSchemaDiscovery

Welcome to JSONSchemaDiscovery, a tool designed to explore and interact with JSON schemas using a MongoDB database backend. This project leverages Docker for easy setup and isolation.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker: You can install Docker by following the instructions on the [official Docker website](https://docs.docker.com/get-docker/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Building the Project with MongoDB

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd JSONSchemaDiscovery
   ```

3. Build the project using Docker Compose:

   ```bash
   docker compose build
   ```

   This command builds the necessary Docker images and sets up the MongoDB database required for the project.

### Running the Project

#### With MongoDB Console

To run the project along with the MongoDB console (to view detailed logs and interactions with the database):

```bash
docker compose up --abort-on-container-exit --force-recreate -V
```

This command starts all the services defined in your `docker-compose.yml` file. You will see logs in the console, including the interactions with MongoDB.

#### With Clean Console

If you prefer a clean console and only want to see the results without the detailed logs:

```bash
docker compose up --abort-on-container-exit --force-recreate -V --no-attach mongo
```

This command rebuilds the project, forces the recreation of containers, removes named volumes, and detaches the MongoDB service so that you only see the essential information in your console.

## Make report

Option: to make a report you can follow this steps:


```bash	
cd report
make clean
make report
````

