# BSTU Applicant Application Form Bot

<p align="center">
  <img src="https://img.shields.io/github/license/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/workflow/status/crissyro/BSTU-applicant-application-form/CI?style=for-the-badge" alt="Build Status">
  <img src="https://img.shields.io/github/stars/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="GitHub Forks">
  <img src="https://img.shields.io/github/last-commit/crissyro/BSTU-applicant-application-form?style=for-the-badge" alt="Last Commit">
</p>

## 📌 Description
**BSTU Applicant Application Form Bot** is a Telegram bot designed to assist prospective applicants of **Belgorod State Technological University named after V. G. Shukhov (BSTU)** in filling out application forms. The collected data is used for statistical analysis and to improve the university's admission process.

## ✨ Features
- 📄 **Structured data collection**: gathers information about the school, class, study profile, exam subjects, etc.
- 📊 **Statistical analysis**: helps the university analyze applicant data.
- 🤖 **User-friendly interface**: intuitive conversation flow in Telegram.
- 🔒 **Data privacy and security**: ensures safe data handling.
- 📂 **Database storage**: all forms are stored in MongoDB.

## 🚀 Technologies Used
## 🚀 Technologies Used
<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/aiogram-2C2D72?style=for-the-badge&logo=telegram&logoColor=white" alt="Aiogram">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/dotenv-%2300C7B7.svg?style=for-the-badge&logo=.env&logoColor=white" alt="dotenv">
  <img src="https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

## 🛠 Installation and Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/BSTU-applicant-application-form.git
cd BSTU-applicant-application-form
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File
Create a `.env` file and add the necessary environment variables:
```ini
BOT_TOKEN=your_telegram_bot_token
MONGO_URI=your_mongodb_connection_string
```

### 4️⃣ Run the Bot
```sh
python3 main.py
```

## 📌 Usage
1. Start the bot in Telegram using the `/start` command.
2. Follow the instructions to fill out the application form.
3. Confirm and submit your data.
4. Your information will be securely stored in the database.

## 🛠 Deployment
The bot can be deployed using:
- **Docker**: with the provided `Dockerfile`.
- **Heroku**: using Heroku CLI.
- **VPS**: managed via `systemd`.

## 💡 Contributing
1. **Fork** the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make changes and **commit**: `git commit -m 'Added a new feature'`.
4. Submit a **pull request** 🚀

## 📜 License
This project is distributed under the [LICENSE](LICENSE).

---
🤝 **Contact**:
<p align="center"> <a href="https://t.me/crissyro"> <img src="https://img.shields.io/badge/Telegram-%2300AFF0.svg?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"> </a> <a href="https://github.com/crissyro"> <img src="https://img.shields.io/badge/GitHub-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"> </a> </p>
