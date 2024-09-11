# spacy-experimental-coref-docker

This repository provides a Dockerized implementation of spaCy's experimental coreference resolution model. It uses the spacy-experimental==0.6.4 package, along with Flask for a lightweight API interface.

**Features:**

1. Coreference resolution using spaCy's experimental trained model.
2. REST API for interacting with the model, built using Flask.
3. Dockerized for easy deployment.

**Components:**

1. spacy-experimental: v0.6.4
2. spacy
3. Flask: v3.0.1
4. Pre-trained model: en_coreference_web_trf-3.4.0a2 (https://github.com/explosion/spacy-experimental/releases/download/v0.6.1/en_coreference_web_trf-3.4.0a2-py3-none-any.whl)


**Installation:**
- Clone the repository:
git clone https://github.com/neostrange/spacy-experimental-coref-docker.git cd spacy-experimental-coref-docker
- Build and run the Docker container:
- Ensure Docker is installed and running.
- Build the Docker image:
docker build -t spacy-coref-docker
- Run the Docker container:

docker run -p 5000:5000 spacy-coref-docker

The application will be available at http://localhost:5000.

**Requirements:** The requirements.txt includes the following dependencies:
- spacy-experimental==0.6.4 spacy Flask==3.0.1
- Pre-trained Model: The repository uses a pre-trained coreference resolution model:
  * https://github.com/explosion/spacy-experimental/releases/download/v0.6.1/en_coreference_web_trf-3.4.0a2-py3-none-any.whl
- Dockerfile:
  * FROM python:3.8.7-slim WORKDIR /app COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt COPY . . CMD ["python", "app.py"]

**Usage:** Once the container is up and running, you can interact with the coreference resolution model via the REST API. Send a POST request with the text data to the appropriate endpoint.

**Contributing:** We welcome contributions! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

**License:** This repository is licensed under the MIT License.
