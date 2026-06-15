FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml requirements.txt* ./

RUN pip install --upgrade pip

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; else pip install -e .; fi

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python create_tables.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
