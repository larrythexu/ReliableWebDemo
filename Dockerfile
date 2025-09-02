# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY liveService.py .

EXPOSE 5000

CMD [ "python", "liveService.py" ]
