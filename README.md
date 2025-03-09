# BSTU Applicant Application Form Bot

## 📌 Description
**BSTU Applicant Application Form Bot** is a Telegram bot designed to assist prospective applicants of **Belgorod State Technological University named after V. G. Shukhov (BSTU)** in filling out application forms. The collected data is used for statistical analysis and to improve the university's admission process.

## ✨ Features
- 📄 **Structured data collection**: gathers information about the school, class, study profile, exam subjects, etc.
- 📊 **Statistical analysis**: helps the university analyze applicant data.
- 🤖 **User-friendly interface**: intuitive conversation flow in Telegram.
- 🔒 **Data privacy and security**: ensures safe data handling.
- 📂 **Database storage**: all forms are stored in MongoDB.

## 🚀 Technologies Used
- **Programming Language**: Python3
- **Framework**: aiogram 3
- **Database**: MongoDB
- **Environment management**: dotenv for environment variables
- **Containerization**: Docker (if used)
- **Deployment**: VPS, AWS, Google Cloud, Heroku, etc.

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
🤝 **Contact**: [Telegram](https://t.me/your_username) | [GitHub](https://github.com/your-username)
