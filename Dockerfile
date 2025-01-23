FROM ncbi/edirect

# Temporarily switch to root to install dependencies
USER root

# Install necessary dependencies for Flask
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to the original user
USER docker

# Set the working directory
WORKDIR /app

ENV NCBI_API_KEY=""

# Copy the Flask app code to the container
COPY app.py /app/app.py

# Install Flask
RUN pip3 install Flask

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]
