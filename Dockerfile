FROM python:3.11

WORKDIR /app

COPY . .

# Install system dependencies + Rust
RUN apt-get update && apt-get install -y build-essential curl

# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Upgrade pip
RUN pip install --upgrade pip

# Install requirements
RUN pip install -r requirements.txt

# Run Django
CMD ["gunicorn", "matching_engine.wsgi", "--bind", "0.0.0.0:8000"]