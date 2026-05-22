# 🚀 DevOps Pipeline: Web App with Monitoring & CI/CD

Этот проект демонстрирует навыки построения отказоустойчивой инфраструктуры для веб-приложения. 
Реализована полная цепочка доставки: от контейнеризации приложения до настройки мониторинга и автоматической сборки через CI/CD.

## 🛠 Стек технологий

*   **App:** Python (HTTP Server) / HTML
*   **Containerization:** Docker, Dockerfile
*   **Orchestration:** Docker Compose
*   **Monitoring:** Prometheus (сбор метрик), Grafana (визуализация)
*   **CI/CD:** GitHub Actions (автоматическая сборка образа при push)
*   **OS:** Linux (Ubuntu/CentOS compatible)

## 📂 Структура проекта

*   `app.py` / `index.html` — исходный код веб-приложения.
*   `Dockerfile` — инструкция для сборки оптимизированного образа приложения.
*   `docker-compose.yml` — конфигурация оркестрации (App + Prometheus + Grafana).
*   `prometheus.yml` — настройки сбора метрик.
*   `.github/workflows/docker-build.yml` — пайплайн автоматической сборки.

## ⚙️ Как запустить локально?

Для развертывания всего стека (приложение + мониторинг) достаточно одной команды:

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/pimik009-droid/devops-junior-project.git
    cd devops-junior-project
    ```

2.  Запустите все сервисы в фоновом режиме:
    ```bash
    docker compose up -d
    ```

3.  Проверьте доступность сервисов:
    *   **Веб-приложение:** [http://localhost:8080](http://localhost:8080)
    *   **Prometheus:** [http://localhost:9090](http://localhost:9090)
    *   **Grafana:** [http://localhost:3000](http://localhost:3000) 
        *(Логин: `admin`, Пароль: `admin123`)*

## 🔄 CI/CD Pipeline

В проекте настроен GitHub Action, который автоматически собирает Docker-образ при каждом обновлении кода в ветке `main`. Это обеспечивает быструю доставку изменений и проверку работоспособности сборки без ручного вмешательства.

## 💡 Особенности реализации

*   Использован легкий базовый образ (Alpine/Slim) для минимизации размера контейнера.
*   Настроена изолированная сеть в Docker Compose для безопасного взаимодействия микросервисов.
*   Реализован сбор стандартных метрик через Prometheus и их визуализация в дашбордах Grafana.
*   Автоматизирована рутина сборки через GitHub Actions, что исключает человеческий фактор при деплое.