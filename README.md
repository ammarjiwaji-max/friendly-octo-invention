# Financial News Bot 📰💰

An automated bot that sends comprehensive daily financial news updates to your email every morning at 6 AM. The bot categorizes news globally, Africa-wide, East Africa, and with specific focus on Tanzania.

## Features

- **Daily Email Updates**: Automated delivery at 6 AM
- **Global Coverage**: World financial markets, inflation, tech sector
- **Regional Focus**: Africa-wide, East Africa, and Tanzania-specific news
- **Comprehensive Details**: Full summaries with sources and links
- **Categorized Content**: 
  - 🌍 Global Financial News
  - 🌍 Africa-Wide Financial News
  - 🌏 East Africa Financial News
  - 🇹🇿 Tanzania-Specific Financial News (prioritized)

## Technology Stack

- **Language**: Python 3.9+
- **Web Scraping**: BeautifulSoup4, Requests
- **Email**: SMTP (Gmail)
- **Scheduling**: APScheduler
- **Environment Management**: python-dotenv

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/ammarjiwaji-max/friendly-octo-invention.git
cd friendly-octo-invention
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:

```
# Email Configuration
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_RECIPIENT=ammar.jiwaji@gmail.com

# Schedule
BOT_SCHEDULE_TIME=06:00
TIMEZONE=Africa/Dar_es_Salaam
```

### 4. Gmail App Password Setup (Important!)
1. Enable 2-Step Verification on your Google Account
2. Generate an [App Password](https://myaccount.google.com/apppasswords)
3. Select "Mail" and "Windows Computer"
4. Use the 16-character password in `.env` as `EMAIL_PASSWORD`

### 5. Run the Bot

**Locally (for testing):**
```bash
python main.py
```

## File Structure

```
friendly-octo-invention/
├── main.py                    # Entry point and scheduler
├── news_scraper.py            # Web scraping logic
├── news_analyzer.py           # News categorization
├── email_sender.py            # Email delivery system
├── config.py                  # Configuration management
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## How It Works

1. **News Collection** (news_scraper.py): Fetches latest financial news from multiple sources
2. **News Analysis** (news_analyzer.py): Categorizes by geographic scope with relevance scoring
3. **Email Formatting** (email_sender.py): Creates HTML email with all categories
4. **Scheduling** (main.py): Runs daily at 6 AM with error handling

## Deployment Options

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku config:set EMAIL_SENDER=your-email@gmail.com
heroku config:set EMAIL_PASSWORD=your-app-password
heroku config:set EMAIL_RECIPIENT=ammar.jiwaji@gmail.com
```

### Docker
```bash
docker build -t financial-news-bot .
docker run -d --env-file .env financial-news-bot
```

## Email Output

You'll receive a beautifully formatted HTML email with:
- 🌍 Global Financial Headlines
- 🌍 Africa-Wide Market News
- 🌏 East Africa Fintech & Banking Updates
- 🇹🇿 Tanzania-Specific News (highlighted)

Each news item includes source, category, summary, and direct link to full story.

## Troubleshooting

**Email not sending?**
- Verify Gmail App Password is correct
- Check 2-Step Verification is enabled
- Ensure `.env` has correct credentials

**Bot not running?**
- Verify APScheduler is installed
- Check system timezone matches `BOT_SCHEDULE_TIME`
- Review logs in `logs/financial-news-bot.log`

## License

MIT License - Feel free to use and modify

---

**Maintained by**: ammarjiwaji-max
**Created**: July 2026
