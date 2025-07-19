# Quest-Game Bot 🤖

[![Project Status](https://img.shields.io/badge/Status-Template-yellow)]()
[![Python](https://img.shields.io/badge/Python-3.13.2-%233776AB?logo=python)](https://python.org/)
[![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-4.27.0-%2326A5E4?logo=telegram)](https://core.telegram.org/bots/api)

Interactive team-based quest platform for Telegram with customizable storylines and administrative controls.

---

## ✨ Core Features
- **Quest Management**:
    - 🎭 Multiple parallel quests with unique themes
    - 🧩 Team formation with participation confirmation
    - 📜 Step-by-step quest progression
- **Communication**:
    - 💬 Real-time team chat
    - 📢 Broadcast messages to entire teams
- **Administration**:
    - 🧹 Clear participant lists (`/delete`)
    - 📋 View all participants and teams (`/list`)

---

## 🧰 Tech Stack
- **Backend**: 
  ![Python](https://img.shields.io/badge/Python-3.13.2-3776AB?logo=python)
- **Telegram Integration**: 
  ![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-4.27.0-26A5E4?logo=telegram)
- **Environment Management**: 
  ![virtualenv](https://img.shields.io/badge/virtualenv-20.25.3-1C1C1C?logo=python)

---

## ⚙️ Installation & Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/Zebaro24/Quest-Game.git
   cd telegram-quest-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**  
   Create `.env` file with your bot token:
   ```env
   TOKEN=your_telegram_bot_token_here
   ```

---

## 🚀 Launching the Bot

```bash
python main.py
```

### Player Flow
1. Start bot with `/start` command
2. Choose a quest from available options
3. Join a team and confirm participation
4. Follow bot instructions to complete quest stages

### Admin Commands
- `/delete` - Clear all participant lists
- `/list` - Show all participants and teams

---

## 🗂️ Project Structure
```bash
main.py             # Bot entry point
quests/             # Quest implementations
├── sample.py       # Base quest class
├── QuestHacker.py  # Hacker-themed quest
├── QuestVirne.py   # Reliability-themed quest
└── QuestVtrach.py  # Lost-hour-themed quest
requirements.txt    # Dependencies
.env                # Environment configuration
```

---

## 🛠️ Creating Custom Quests
1. Create new Python file in `quests/` directory
2. Inherit from `SampleQuest` base class
3. Define quest attributes:
   ```python
   name = "Quest Name"
   max_count = 4  # Max players
   description = "Quest description"
   ```
4. Implement `func_start()` for initial message
5. Define stage functions in `stage_func_get`
6. Add quest to `all_quests` in `main.py`

Example:
```python
from sample import SampleQuest

class MyQuest(SampleQuest):
    name = "New Adventure"
    max_count = 3
    description = "An exciting new quest"

    stage_func_get = {0: lambda: 0, 1: lambda self: self.stage_1()}

    def func_start(self):
        self.send_text_all("Welcome to the quest! First task: ...")

    def stage_1(self):
        # Stage 1 logic
        pass
```

---

## 🎭 Sample Quests
| Quest Name | Theme | Players | Description |
|------------|-------|---------|-------------|
| QuestHacker | Cyberpunk | 1-4 | Hack through digital barriers |
| QuestVirne | Mystery | 2-5 | Solve puzzles to uncover truth |
| QuestVtrach | Adventure | 3-6 | Recover a lost artifact |

---

## 📬 Contact
- **Developer**: Denys Shcherbatyi
- **Email**: zebaro.work@gmail.com

---

*Note: This project is a template with implemented interaction mechanics, ready for content creation. Development is currently on hold but may resume in the future.*