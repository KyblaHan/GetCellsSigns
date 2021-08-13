
# установка базового образа (host OS)
FROM python:3.9
# установка рабочей директории в контейнере
WORKDIR /app
# копирование файла зависимостей в рабочую директорию
COPY requirements.txt .
# установка зависимостей
RUN pip install -r requirements.txt
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

ENV QT_QUICK_BACKEND=software
# копирование содержимого локальной директории src в рабочую директорию
COPY src/ .
COPY data/ .
COPY src/main_ui.py .


# команда, выполняемая при запуске контейнера
CMD [ "python", "main_ui.py" ]
