# Asturian Observatory of Demographic Intelligence - Demo

This is a Streamlit demo application for the Asturian Observatory of Demographic Intelligence. It provides insights into demographic data, including global KPIs, a demographic urgency map, migration flows, and a policy simulator.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

*(Alternatively, you can run this locally with Python 3.8+)*

## Running with Docker Compose (Recommended)

The easiest way to run the demo is using Docker Compose. This ensures you have the correct environment and dependencies installed.

1. **Start the application:**
   From the `demo` directory (where the `docker-compose.yml` file is located), run the following command:
   ```bash
   docker-compose up --build
   ```
   *(Add the `-d` flag to run it in detached mode).*

2. **Access the application:**
   Once the container is running, open your web browser and navigate to:
   [http://localhost:8501](http://localhost:8501)

3. **Stop the application:**
   To stop the running container, press `Ctrl+C` in the terminal where it's running, or run:
   ```bash
   docker-compose down
   ```

## Running Locally (Without Docker)

If you prefer to run the application directly on your host machine without Docker:

1. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Access the application:**
   The Streamlit server will start and typically open your default web browser automatically to [http://localhost:8501](http://localhost:8501).

## Development Notes

When running with Docker Compose, the current directory (`.`) is volume-mounted to `/app` inside the container. This means any changes you make to the source code (like `app.py` or the `pages/` directory) on your host machine will be immediately reflected in the running container without needing to rebuild the image. Simply refresh your browser to see the changes.
