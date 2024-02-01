# SPOTIFY RECOMMENDER

This is a Python Flask application that utilizes the Spotify API to recommend music based on user input of track, artist, and genre. The application allows users to discover new music recommendations tailored to their preferences.

## Getting started with Development
### Preequisites
Before running the application, make sure you have the following installed:

* Python v3.8^
* Flask

```sh
curl -sSL https://install.python-poetry.org | python3
```

### Setting up Virtual Environment

Create a virtual environment to isolate the dependencies for this project. Navigate to the project directory and run:

```bash
# On Linux/Mac
python3 -m venv venv

# On Windows
python -m venv venv
```

Activate the virtual environment:

```bash
# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### Installing Dependencies

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Setting up Spotify API
To use the Spotify API, you need to create a Spotify Developer account and register your application. Obtain the client ID and client secret, and update the .env with your credentials.

```
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REFRESH_TOKEN = 'your_refresh_token'
```

## Running SPOTIFY_RECOMMENDER
SPOTIFY_RECOMMENDER can be run either from a docker container or the virtual environment. In either instance, SPOTIFY_RECOMMENDER must be configured using environment variables.

### Running from a container

Requirements
* Windows / Mac : Docker Desktop v3.4 or later
* Linux: Docker engine v20.10.13 with `docker-compose-plugin` package

1. If you haven't already, copy the example `.env.example` file to `.env` and edit with the necessary values.

2. Build the SPOTIFY_RECOMMENDER container using `docker compose build`.

3. Start the container using `docker compose up`.

4. Access the application ar http://localhost:5005/

> The code will live-reload in the container. You can watch the log with `docker compose logs -f`. If you need to change dependencies, you can rebuild with `docker compose build`.

### Running from a virtual environment

1. If you haven't already, copy the example `.env.example` file to `.env` and edit with the necessary values.

2. To start the application, run flask in the virtual environment with `python app.py`.

3. Access the application ar http://localhost:5005/

### How to Use
1. Open the web application.

2. Enter the track name, singer, and genre in the input fields.

3. Click the "Recommend!" button.

4. The application will fetch music recommendations from the Spotify API and display them on the page.

### Features
* User Input: Allows users to input track name, singer, and genre.

* Spotify API Integration: Utilizes the Spotify API to fetch personalized music recommendations.

* Responsive Design: Provides a user-friendly interface that works well on both desktop and mobile devices.

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

Happy discovering new music! 🎶