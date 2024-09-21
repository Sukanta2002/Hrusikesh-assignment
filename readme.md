# Fast API Server

This is a Fast API server that provides search functionality for YouTube, Google, and Google Scholar.

## Prerequisites

- Python 3.10+
- pip

## Create Virtual Environment

- On Linux/MacOS:
  - Run `python -m venv env` to create a virtual environment.
  - Run `source env/bin/activate` to activate the virtual environment.
- On Windows:
  - Run `python -m venv env` to create a virtual environment.
  - Run `env\Scripts\activate` to activate the virtual environment.

## Install Dependencies

- Run `pip install -r requirements.txt` to install the required dependencies.

## Configure Environment Variables

- Create a `.env` file in the root of the project with the following variables:
  - `GOOGLE_API_KEY`: Your Google API key.
  - `GOOGLE_CX`: Your Google Custom Search Engine ID.

## Start the Server

- Run `fastapi dev main.py` to start the server.
- Open a web browser and navigate to `http://localhost:8000/docs` to access the API documentation.

## Usage

- Send a GET request to `http://localhost:8000/search?q=<search query>` to search for the given query.
- The response will be in JSON format with the following structure:
  - `youtube`: A list of YouTube search results.
  - `google`: A list of Google search results.
  - `scolar`: A list of Google Scholar search results.
