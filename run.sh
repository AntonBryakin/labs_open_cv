#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Ошибка: требуется ровно один аргумент - имя .py файла"
    echo "Использование: $0 <имя_файла.py>"
    exit 1
fi

PY_FILE="$1"

if [ ! -f "$PY_FILE" ]; then
    echo "Ошибка: файл $PY_FILE не найден"
    exit 1
fi

if [[ ! "$PY_FILE" =~ \.py$ ]]; then
    echo "Ошибка: аргумент должен быть .py файлом"
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "Виртуальное окружение не найдено. Создаю новое..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Ошибка: не удалось создать виртуальное окружение"
        exit 1
    fi
    echo "Виртуальное окружение создано"
fi

source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Ошибка: не удалось активировать виртуальное окружение"
    exit 1
fi

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Ошибка: не удалось установить зависимости"
        deactivate
        exit 1
    fi
fi

python "$PY_FILE"
EXIT_CODE=$?
deactivate
exit $EXIT_CODE