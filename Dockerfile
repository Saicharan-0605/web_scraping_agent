FROM python:3.11-slim
WORKDIR /app
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
RUN adduser --disabled-password --gecos "" myuser && \
    chown -R myuser:myuser /app
 
COPY . .
COPY main.py .
 
USER myuser
 
ENV PATH="/home/myuser/.local/bin:$PATH"
ENV PORT=8080
 
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]