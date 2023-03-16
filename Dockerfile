FROM python:3.10

WORKDIR /event_planner

COPY requirements.txt /event_planner

RUN pip install --upgrade pip && pip install -r /event_planner/requirements.txt

EXPOSE 8080
COPY ./ /event_planner
CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8080"]