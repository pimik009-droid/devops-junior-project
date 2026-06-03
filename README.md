# DevOps Monitoring Stack: Flask App, Prometheus & Grafana

Учебный DevOps-проект, демонстрирующий контейнеризацию Python web-приложения, запуск multi-container окружения через Docker Compose, сбор метрик Prometheus и автоматическую настройку Grafana dashboard через provisioning.

Проект создан для практической отработки базовых DevOps-навыков: Docker, Docker Compose, healthcheck, monitoring, persistent storage, secrets handling, Git workflow и GitHub Actions.

---

## Что реализовано

- Python Flask web-приложение.
- Dockerfile для сборки приложения.
- Docker Compose stack из трех сервисов:
  - `web-app`;
  - `prometheus`;
  - `grafana`.
- Endpoint `/health` для проверки доступности приложения.
- Endpoint `/metrics` для экспорта Prometheus-метрик.
- Docker healthcheck для `web-app`, `prometheus` и `grafana`.
- Автоматические тесты Flask endpoints через `pytest`.
- Prometheus configuration для сбора метрик приложения.
- Grafana data source provisioning.
- Grafana dashboard provisioning.
- Persistent Docker volumes для Grafana и Prometheus.
- Передача локальных credentials через `.env`.
- Публичный шаблон переменных окружения `.env.example`.
- Фиксированные версии Docker images для Prometheus и Grafana.
- GitHub Actions workflow для linting, запуска тестов, проверки сборки Docker image, Docker Compose stack и публикации image в GHCR.


---

## Архитектура

```text
Browser
  │
  ├── http://localhost:8080
  │       └── web-app
  │             ├── /
  │             ├── /health
  │             └── /metrics
  │
  ├── http://localhost:9090
  │       └── Prometheus
  │             └── prometheus-data:/prometheus
  │
  └── http://localhost:3000
          └── Grafana
                ├── grafana-data:/var/lib/grafana
                ├── provisioned Prometheus data source
                └── provisioned Web Application Monitoring dashboard
```

Все три сервиса подключены к общей Docker-сети `monitoring-net`.

---

## Технологии

| Технология | Назначение |
|---|---|
| Python 3.12 | Среда выполнения приложения |
| Flask | Web-приложение и HTTP endpoints |
| pytest | Автоматическое тестирование endpoints приложения |
| Ruff | Linting и статический анализ Python-кода |
| prometheus-client | Экспорт прикладных метрик |
| Docker | Контейнеризация приложения |
| Docker Compose | Запуск и объединение сервисов |
| Prometheus | Сбор и хранение метрик |
| Grafana | Визуализация метрик |
| GitHub Actions | CI для Ruff linting, pytest-тестов, Docker build, Docker Compose stack и публикации image |
| GitHub Container Registry | Хранение опубликованного Docker image |
| Linux / WSL 2 | Рекомендуемая локальная среда запуска |

---

## Ключевые файлы проекта

```text
.
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── grafana/
│   ├── dashboards/
│   │   └── web-application-monitoring.json
│   └── provisioning/
│       ├── dashboards/
│       │   └── dashboards.yml
│       └── datasources/
│           └── prometheus.yml
├── tests/
│   └── test_app.py
├── requirements-dev.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── app.py
├── docker-compose.yml
├── Dockerfile
├── prometheus.yml
├── requirements.txt
└── README.md
```

### Назначение основных файлов

| Файл | Назначение |
|---|---|
| `app.py` | Flask-приложение, endpoints и экспорт метрик |
| `Dockerfile` | Сборка Docker image приложения |
| `docker-compose.yml` | Запуск приложения, Prometheus и Grafana |
| `prometheus.yml` | Настройка сбора метрик |
| `requirements.txt` | Python-зависимости приложения |
| `.env.example` | Шаблон локальных переменных окружения |
| `grafana/provisioning/datasources/prometheus.yml` | Автоматическое создание Prometheus data source |
| `grafana/provisioning/dashboards/dashboards.yml` | Настройка автоматической загрузки dashboards |
| `grafana/dashboards/web-application-monitoring.json` | Dashboard Grafana в формате JSON |
| `.github/workflows/docker-build.yml` | CI workflow для Ruff linting, pytest-тестов и проверки сборки Docker image |
| `requirements-dev.txt` | Дополнительные зависимости для локального запуска тестов и CI |
| `tests/test_app.py` | Автоматические тесты для `/`, `/health` и `/metrics` |
| `pyproject.toml` | Конфигурация Ruff linting для Python-кода |

---

## Требования для запуска

Для локального запуска необходимы:

- Git;
- Docker Engine;
- Docker Compose;
- Linux или Ubuntu в WSL 2 как рекомендуемая среда.

Проверить установленные инструменты можно командами:

```bash
docker --version
docker compose version
git --version
```

---

## Быстрый старт

Клонируйте репозиторий:

```bash
git clone https://github.com/pimik09-droid/devops-junior-project.git
cd devops-junior-project
```



### 1. Создайте локальный файл переменных окружения

```bash
cp .env.example .env
```

Откройте созданный файл `.env` и задайте собственный локальный пароль Grafana:

```env
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=change_me_before_use
```

Значение `GRAFANA_ADMIN_PASSWORD` необходимо заменить на свой пароль перед запуском.

Файл `.env` исключен из Git и не должен публиковаться в репозитории.

### 2. Запустите весь stack

```bash
docker compose up -d --build
```

### 3. Проверьте состояние контейнеров

```bash
docker compose ps
```

После запуска все три сервиса должны быть в состоянии `healthy`:

```text
web-app      Up ... (healthy)
prometheus   Up ... (healthy)
grafana      Up ... (healthy)
```

---

## Доступные сервисы

| Сервис | Назначение | URL |
|---|---|---|
| `web-app` | Flask web-приложение | `http://localhost:8080` |
| `prometheus` | Интерфейс и targets Prometheus | `http://localhost:9090` |
| `grafana` | Dashboard и визуализация метрик | `http://localhost:3000` |

Для входа в Grafana используйте логин и пароль из собственного файла `.env`.

---

## Endpoints приложения

| Endpoint | Назначение |
|---|---|
| `/` | Главная пользовательская страница приложения |
| `/health` | Проверка доступности приложения |
| `/metrics` | Метрики в формате Prometheus |

### Проверка главной страницы

Откройте в браузере:

```text
http://localhost:8080
```

### Проверка health endpoint

```bash
curl http://localhost:8080/health
```

Ожидаемый ответ:

```json
{"status":"ok"}
```

### Проверка metrics endpoint

```bash
curl http://localhost:8080/metrics
```

В выводе должна присутствовать метрика:

```text
app_requests_total
```

---

## Docker healthcheck

Для всех основных сервисов настроены Docker healthchecks:

| Сервис | Что проверяется |
|---|---|
| `web-app` | endpoint `/health` внутри контейнера приложения |
| `prometheus` | endpoint `/-/healthy` внутри контейнера Prometheus |
| `grafana` | endpoint `/api/health` внутри контейнера Grafana |

Это позволяет Docker различать два состояния:

```text
Up            — процесс контейнера запущен
Up (healthy)  — сервис внутри контейнера действительно отвечает на healthcheck
```

Проверить статус можно командой:

```bash
docker compose ps
```

После запуска все три сервиса должны быть в состоянии `healthy`:

```text
web-app      Up (healthy)
prometheus   Up (healthy)
grafana      Up (healthy)
```

Для `prometheus` и `grafana` проверки выполняются внутри контейнеров через `wget`.

---

## Prometheus

Prometheus собирает метрики приложения из endpoint:

```text
http://web-app:8080/metrics
```

Проверить targets можно по адресу:

```text
http://localhost:9090/targets
```

Цель `web-app` должна находиться в состоянии:

```text
UP
```

Интервал сбора метрик в текущей конфигурации:

```yaml
scrape_interval: 15s
```

---

## Grafana

Grafana доступна по адресу:

```text
http://localhost:3000
```

После запуска контейнера Grafana автоматически получает:

- Prometheus data source;
- dashboard `Web Application Monitoring`;
- panel `HTTP request rate by endpoint`.

Эта настройка выполняется не вручную через интерфейс, а через provisioning-файлы проекта:

```text
grafana/provisioning/datasources/prometheus.yml
grafana/provisioning/dashboards/dashboards.yml
grafana/dashboards/web-application-monitoring.json
```

### Dashboard

Dashboard визуализирует скорость HTTP-запросов по endpoint с помощью PromQL-запроса:

```promql
sum by (endpoint) (rate(app_requests_total[1m]))
```

На графике могут отображаться серии:

```text
/
 /health
```

Endpoint `/health` регулярно вызывается Docker healthcheck, поэтому его линия активна даже без ручных запросов пользователя.

---

## Configuration as Code

Grafana настраивается через файлы, хранящиеся в Git:

```text
Prometheus data source  → grafana/provisioning/datasources/prometheus.yml
Dashboard provider      → grafana/provisioning/dashboards/dashboards.yml
Dashboard JSON          → grafana/dashboards/web-application-monitoring.json
```

При чистом запуске Grafana эти файлы автоматически создают источник данных и dashboard.

Это позволяет воспроизводить monitoring configuration без ручной настройки в веб-интерфейсе.

---

## Persistent storage

В проекте используются два именованных Docker volume:

| Volume | Назначение |
|---|---|
| `grafana-data` | Внутренние данные Grafana |
| `prometheus-data` | История метрик Prometheus |

Конфигурация provisioning и JSON dashboard хранятся отдельно в Git-репозитории и подключаются к Grafana в режиме `read-only`.

### Важно

Команда:

```bash
docker compose down
```

удаляет контейнеры и сеть проекта, но сохраняет volumes.

Команда:

```bash
docker compose down -v
```

удаляет контейнеры и volumes, включая внутренние данные Grafana и накопленную историю Prometheus.

---

## Secrets handling

Настоящие локальные credentials Grafana хранятся в файле:

```text
.env
```

Этот файл исключен из Git через `.gitignore`.

В репозитории публикуется только безопасный шаблон:

```text
.env.example
```

Пример используемых переменных:

```env
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=change_me_before_use
```

Настоящий пароль необходимо задавать только локально.

---

## Docker images

Для сервисов мониторинга используются фиксированные версии Docker images:

```yaml
prom/prometheus:v3.11.3
grafana/grafana:13.0.1-security-01
```

Фиксация версий делает запуск проекта более воспроизводимым по сравнению с использованием плавающего тега `latest`.

Приложение собирается из собственного `Dockerfile` на базе:

```dockerfile
FROM python:3.12-slim
```
---

## Linting

В проекте используется `Ruff` для linting и статического анализа Python-кода.

Ruff проверяет:

- порядок импортов;
- неиспользуемые импорты;
- базовые ошибки оформления;
- часть потенциально устаревшего Python-синтаксиса.

Настройки Ruff находятся в файле:

```text
pyproject.toml
```

Локальная проверка:

```bash
ruff check .
```

Ожидаемый результат:

```text
All checks passed!
```

Если Ruff находит автоматически исправляемые проблемы, можно применить исправления командой:

```bash
ruff check . --fix
```

После автоматического исправления нужно обязательно посмотреть diff:

```bash
git --no-pager diff
```
---

## Автоматические тесты

В проекте используются автоматические тесты `pytest` для проверки основных endpoints Flask-приложения:

| Тест | Что проверяется |
|---|---|
| Главная страница `/` | HTTP-ответ `200` и наличие текста приложения |
| Health endpoint `/health` | HTTP-ответ `200` и JSON `{"status":"ok"}` |
| Metrics endpoint `/metrics` | HTTP-ответ `200` и наличие метрики `app_requests_total` |

Для локального запуска тестов создайте виртуальное окружение и установите зависимости разработки:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

Ожидаемый результат:

```text
3 passed
```

---

## GitHub Actions

В проекте настроен workflow:

```text
.github/workflows/docker-build.yml
```

Workflow запускается:

- при создании или обновлении Pull Request в ветку `main`;
- при `push` в ветку `main`.

Проверка выполняет следующие шаги:

1. загружает код репозитория;
2. устанавливает Python `3.12`, соответствующий базовой версии в `Dockerfile`;
3. устанавливает зависимости приложения, тестов и линтера;
4. запускает linting через `ruff check .`;
5. запускает автоматические тесты через `python -m pytest -v`;
6. собирает Docker image приложения;
7. проверяет валидность Docker Compose конфигурации;
8. запускает весь Docker Compose stack;
9. дожидается состояния `healthy` для `web-app`, `prometheus` и `grafana`;
10. проверяет health endpoints сервисов;
11. останавливает и очищает stack после проверки;
12. при `push` в `main` входит в GitHub Container Registry;
13. собирает Docker image с тегами `latest` и commit SHA;
14. публикует image в GitHub Container Registry.

Таким образом, до объединения Pull Request с `main` автоматически проверяется:

- качество Python-кода через Ruff;
- корректная работа endpoints `/`, `/health` и `/metrics`;
- успешная сборка Docker image приложения;
- валидность Docker Compose конфигурации;
- запуск всего stack `web-app + prometheus + grafana`;
- healthy-состояние всех сервисов monitoring stack.

Публикация Docker image выполняется только после объединения изменений в `main`.

На Pull Request image не публикуется: PR выполняет только проверки.

Текущая версия workflow:

- на Pull Request выполняет проверки без публикации image;
- после merge в `main` публикует image в GitHub Container Registry;
- не выполняет deployment.

---

## Docker image registry

После успешного merge в `main` GitHub Actions публикует Docker image приложения в GitHub Container Registry.

Image публикуется с двумя тегами:

```text
ghcr.io/pimik009-droid/devops-junior-project:latest
ghcr.io/pimik009-droid/devops-junior-project:<commit-sha>
```

Где:

- `latest` — последняя успешная версия из ветки `main`;
- `<commit-sha>` — точная версия image, связанная с конкретным commit.

Pull Request не публикует image в registry. Публикация выполняется только после `push` в `main`.

Локально image можно собрать командой:

```bash
docker build --file Dockerfile --tag devops-junior-project:test .
```

## Полезные команды

### Проверки перед коммитом

```bash
ruff check .
python -m pytest -v
docker compose config >/dev/null && echo COMPOSE_OK
docker compose ps
```

### Запуск всего stack

```bash
docker compose up -d --build
```

### Просмотр состояния контейнеров

```bash
docker compose ps
```

### Просмотр логов

```bash
docker compose logs -f
```

### Остановка контейнеров без удаления данных

```bash
docker compose stop
```

### Повторный запуск остановленных контейнеров

```bash
docker compose start
```

### Пересоздание Grafana

```bash
docker compose up -d --force-recreate grafana
```

### Пересоздание Prometheus

```bash
docker compose up -d --force-recreate prometheus
```

### Просмотр Docker volumes

```bash
docker volume ls
```

---

## Проверенные сценарии

В ходе разработки были практически проверены следующие сценарии:

- запуск приложения, Prometheus и Grafana через Docker Compose;
- успешный healthcheck приложения;
- сбор метрик приложения через Prometheus;
- отображение request rate в Grafana;
- сохранение dashboard Grafana после пересоздания контейнера;
- сохранение истории метрик Prometheus после пересоздания контейнера;
- автоматическое создание Grafana data source и dashboard после удаления старых данных Grafana и чистого запуска контейнера.

---

## Возможные дальнейшие улучшения

- Добавить Nginx reverse proxy.
- Добавить deployment на VPS.
- Настроить Prometheus alerting rules.
- Расширить Grafana dashboard дополнительными panels.
- Добавить Makefile для удобного управления проектом.
- Изучить Kubernetes manifests или Helm chart как следующий учебный этап.

---

## Статус проекта

Актуальная стабильная версия проекта находится в основной ветке `main`.
