# 🚀 Rocket.Chat Bot (rocketchat_API==1.35.1)

It just does simple stuff like greeting when login and logout.

---

## 📌 **Project Purpose**

This bot:

* **Greets users** with a welcome message when they log in.
* **Sends farewell messages** when they log out.

---

## 🏗️ **Software Design**

### 🔹 **Design Pattern**

* **Modular Design**: Each module has a single responsibility and is easy to maintain.
* **Layered Architecture**:

  * **Configuration Layer**: Environment variables and settings.
  * **API Client Layer**: Communicates with the `rocketchat_API`.
  * **Business Logic Layer**: Handles greeting messages and user events.
  * **Entry Point**: Starts the bot and orchestrates all components.

### 🔹 **Key Principles**

* **Separation of Concerns**: Keeps configuration, API calls, and logic separate.
* **Single Responsibility Principle**: Each module does one job, making it easy to debug and test.
* **Security**: Uses environment variables to avoid exposing sensitive credentials.

---

## 📂 **Project Structure**

```bash
python-rocketchat-bot/
│
├── src/
│   ├── bot.py             # Main bot entry point
│   ├── config.py          # Loads environment variables
│   ├── handlers.py        # Logic for greeting messages
│   └── rocket_client.py   # Rocket.Chat API wrapper
├── requirements.txt       # Dependencies
├── .envrc                 # Direnv configuration
└── .env.example           # Example environment file (DO NOT COMMIT real credentials)
```

---

## ⚙️ **Installation**

1. **Clone the repository**

   ```bash
   git clone https://github.com/ahmed-n-abdeltwab/python-rocketchat-bot
   cd python-rocketchat-bot
   ```

2. **Create and activate a virtual environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**

   * Create a `.env` file based on `.env.example`
   * Example:

    ```bash
    ROCKETCHAT_URL=https://your.rocket.chat
    ROCKETCHAT_USER=bot_username
    ROCKETCHAT_PASSWORD=bot_password
    CHANNEL=general
    ```

---

## 🚀 **How to Run the Bot**

   ```bash
   python3 src/bot.py
   ```

The bot will start polling for user login/logout events and send greeting messages to the configured channel.

---

## 📝 **Important Notes**

* **Secure Credentials**: Always use environment variables for credentials. **Do not commit sensitive information.**
* **Channel ID**: Make sure the `CHANNEL` exists in Rocket.Chat. You can use either a `#channel` name or a direct room ID.
