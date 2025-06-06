# SaaS Application for Managing Players, Teams, and Fines

This is a SaaS application built following the hexagonal architecture and using Domain-Driven Design (DDD) principles. The application handles players, teams, and fines, with players paying fines at the end of the month.

## Features

- List of fines
- List of teams
- List of players
- Add fine to player
- Add predefined fines to each team

## Project Structure

The project is organized following the hexagonal architecture principles:

- `service/layers/domain/`: Contains the domain entities, repositories, and services
- `service/layers/application/`: Contains the application use cases
- `service/layers/infrastructure/`: Contains the infrastructure implementations (repositories)
- `service/layers/api/`: Contains the API layer with FastAPI routers
- `tests/`: Contains the tests for each layer

## Running the Application

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the application:
   ```bash
   poetry run python -m service
   ```

3. The application will be available at http://localhost:8080

## API Endpoints

### Players

- `GET /players/`: List all players
- `POST /players/`: Create a new player
- `GET /players/{player_id}`: Get a player by ID
- `POST /players/{player_id}/fines/`: Add a fine to a player

### Teams

- `GET /teams/`: List all teams
- `POST /teams/`: Create a new team
- `GET /teams/{team_id}`: Get a team by ID
- `POST /teams/{team_id}/fines/`: Add a predefined fine to a team

### Fines

- `GET /fines/`: List all fines
- `POST /fines/`: Create a new fine
- `GET /fines/{fine_id}`: Get a fine by ID

## Running Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

## Docker

To build and run the application using Docker, use the following commands:

```bash
docker build -t saas-app .
docker run -p 8080:8080 saas-app
```

The application will be available at http://localhost:8080
