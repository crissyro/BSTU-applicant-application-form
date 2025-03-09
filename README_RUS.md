# BSTU Applicant Application Form Bot

<p align="center">
  <img src="https://img.shields.io/github/license/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/actions/workflow/status/crissyro/BSTU-applicant-application-form/ci-cd.yml?style=for-the-badge" alt="Build Status">
  <img src="https://img.shields.io/github/stars/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="GitHub Forks">
  <img src="https://img.shields.io/github/last-commit/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="Last Commit">
</p>

## 📌 Описание
**BSTU Applicant Application Form Bot** — это Telegram-бот, созданный для помощи будущим абитуриентам Белгородского государственного технологического университета им. В. Г. Шухова (БГТУ) в заполнении анкеты. Собранные данные используются для статистического анализа и улучшения процесса поступления в университет.

## ✨ Функционал
- 📄 **Сбор структурированных данных**: информация о школе, классе, профиле обучения, экзаменационных предметах.
- 📊 **Статистический анализ**: собранные данные помогают университету планировать образовательный процесс.
- 🤖 **Удобный интерфейс**: интуитивно понятный диалог в Telegram.
- 🔒 **Конфиденциальность данных**: защита и безопасность информации.
- 📂 **Хранение в базе данных**: все анкеты сохраняются в MongoDB.

## 🚀 Используемые технологии
<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/aiogram-2C2D72?style=for-the-badge&logo=telegram&logoColor=white" alt="Aiogram">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/dotenv-%2300C7B7.svg?style=for-the-badge&logo=.env&logoColor=white" alt="dotenv">
  <img src="https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

## 🛠 Установка и запуск
### 1️⃣ Клонирование репозитория
```sh
git clone https://github.com/your-username/BSTU-applicant-application-form.git
cd BSTU-applicant-application-form
```
### 2️⃣ Установка зависимостей
```sh
pip install -r requirements.txt
```

### 3️⃣ Создание `.env` файла
Создайте `.env` и добавьте необходимые переменные окружения:
```ini
BOT_TOKEN=your_telegram_bot_token
MONGO_URI=your_mongodb_connection_string
```

### 4️⃣ Запуск бота
```sh
python3 main.py
```

## 📌 Использование
1. Запустите бота в Telegram командой `/start`.
2. Заполните анкету, следуя инструкциям.
3. Подтвердите отправку данных.
4. Информация сохранится в базе данных.

## 📜 Лицензия
Проект распространяется под лицензией [LICENSE](LICENSE).

---
🤝 **Контакты:** 
<p align="center"> <a href="https://t.me/integral_cursed"> <img src="https://img.shields.io/badge/Telegram-%2300AFF0.svg?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"> </a> <a href="https://github.com/crissyro"> <img src="https://img.shields.io/badge/GitHub-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"> </a> </p>
