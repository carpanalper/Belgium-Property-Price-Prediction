# Official python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /Belgium-Property-Price-Prediction

# Copy all files to the working directory
COPY . /Belgium-Property-Price-Prediction

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlitapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
