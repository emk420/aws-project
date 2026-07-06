FROM      python:3.13-slim
ENV       PYTHONDONTWRITEBYTECODE=1                                                     
ENV       PYTHONUNBUFFERED=1

RUN       groupadd -r appgroup && useradd -r -g appgroup appuser
WORKDIR   /app
COPY      requirements.txt .
RUN       pip install --no-cache-dir --upgrade pip \
          && pip install --no-cache-dir -r requirements.txt
COPY      --chown=appuser:appgroup . .
USER      appuser
EXPOSE    5000
CMD       ["python","app.py"]
