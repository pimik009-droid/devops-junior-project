# 🚀 DevOps Pipeline: Web App with Monitoring & CI/CD

Этот репозиторий демонстрирует навыки построения инфраструктуры для веб-приложения.
Проект включает в себя контейнеризацию приложения, оркестрацию сервисов, настройку мониторинга и автоматическую сборку через CI/CD.

## 🛠 Стек технологий

*   **Application:** Python (HTTP Server) / HTML
*   **Containerization:** Docker, Dockerfile
*   **Orchestration:** Docker Compose
*   **Monitoring:** Prometheus (сбор метрик), Grafana (визуализация)
*   **CI/CD:** GitHub Actions (автоматическая сборка образа при push)
*   **OS:** Linux (Ubuntu/CentOS compatible)

## 📂 Структура проекта

*   `app.py` / `index.html` — исходный код веб-приложения.
*   `Dockerfile` — инструкция для сборки образа приложения.
*   `docker-compose.yml` — конфигурация запуска стека (App + Prometheus + Grafana).
*   `prometheus.yml` — настройки сбора метрик для Prometheus.
*   `.github/workflows/docker-build.yml` — пайплайн CI/CD для автоматической сборки.

## ⚙️ Как запустить локально?

Для развертывания всего стека (приложение + мониторинг) выполните одну команду:

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
        *   *Логин:* `admin`
        *   *Пароль:* `admin123`

## 🔄 CI/CD Pipeline

В проекте настроен **GitHub Actions**. При каждом изменении кода в ветке `main`:
1.  Автоматически запускается сборка Docker-образа.
2.  Проверяется синтаксис Dockerfile.
3.  Образ собирается и готов к деплою (или публикации в Registry, если настроить секреты).

Статус последней сборки можно посмотреть во вкладке **Actions** этого репозитория.

## 💡 Чему я научился на этом проекте

*   Написал оптимальный `Dockerfile` с использованием легких базовых образов (Alpine/Slim).
*   Настроил изолированную сеть в Docker Compose для безопасного взаимодействия микросервисов.
*   Подключил Prometheus для сбора стандартных метрик и настроил дашборды в Grafana.
*   Реализовал автоматизацию рутины сборки через GitHub Actions, исключив человеческий фактор.
*   Освоил работу с YAML-конфигурациями и логированием контейнеров.

---
*Проект выполнен в рамках самообучения и подготовки к позиции Junior DevOps Engineer.*