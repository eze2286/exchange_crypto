FROM python:3.10-slim

# Set the working directory in the container

WORKDIR /app

# Copy the requirements file to the container

COPY ./requirements.txt ./

# Install dependencies

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the requirements file to the container

COPY . .

# Run the application

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
