# Pulls the official base image
FROM python:3.11

# Set work directory
WORKDIR /app

# Copy project files to the destination file
COPY . /app/
COPY pyproject.toml /app

# Set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install poetry --upgrade pip \
    && poetry config virtualenvs.create false \
    && poetry install

# Expose port 8000 for accessing the application
EXPOSE 8000

# Running the application
CMD ["poetry", "run", "python", "website.py"]
