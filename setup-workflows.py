#!/usr/bin/env python3
"""
GitHub Actions Setup Script
This script helps you set up the GitHub Actions workflows and secrets
"""

import os
import subprocess
import sys
from pathlib import Path

def create_workflows():
    """Create the .github/workflows directory and files"""
    
    # Create directory
    workflows_dir = Path('.github/workflows')
    workflows_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Created {workflows_dir}/")
    
    # Daily News Workflow
    daily_news = workflows_dir / 'daily-news.yml'
    daily_news.write_text('''name: Daily Financial News Bot

on:
  schedule:
    - cron: '0 6 * * *'
  workflow_dispatch:

jobs:
  send-news:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - run: |
        pip install -r requirements.txt
        python -c "
        import os, logging
        from datetime import datetime
        from news_scraper import NewsScaper
        from email_sender import EmailSender
        from news_analyzer import NewsAnalyzer
        
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        scraper = NewsScaper()
        analyzer = NewsAnalyzer()
        email_sender = EmailSender()
        
        global_news = scraper.get_global_news()
        africa_news = scraper.get_africa_news()
        east_africa_news = scraper.get_east_africa_news()
        tanzania_news = scraper.get_tanzania_news()
        
        analyzed_news = {
            'global': analyzer.analyze_news(global_news, 'global'),
            'africa': analyzer.analyze_news(africa_news, 'africa'),
            'east_africa': analyzer.analyze_news(east_africa_news, 'east_africa'),
            'tanzania': analyzer.analyze_news(tanzania_news, 'tanzania')
        }
        
        email_content = email_sender.create_email_content(analyzed_news)
        recipient = os.getenv('EMAIL_RECIPIENT')
        email_sender.send_email(to=recipient, subject=f'Daily Financial News - {datetime.now().strftime(\\\"%B %d, %Y\\\")}', html_content=email_content)
        "
      env:
        EMAIL_SENDER: ${{ secrets.EMAIL_SENDER }}
        EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
        EMAIL_RECIPIENT: ${{ secrets.EMAIL_RECIPIENT }}
''')
    print(f"✓ Created {daily_news}")
    
    # Manual Fetch Workflow
    manual_fetch = workflows_dir / 'manual-fetch.yml'
    manual_fetch.write_text('''name: Manual News Fetch

on:
  workflow_dispatch:

jobs:
  manual-fetch:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - run: |
        pip install -r requirements.txt
        python -c "
        import os, logging
        from datetime import datetime
        from news_scraper import NewsScaper
        from email_sender import EmailSender
        from news_analyzer import NewsAnalyzer
        
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info('=== MANUAL NEWS FETCH ===')
        
        scraper = NewsScaper()
        analyzer = NewsAnalyzer()
        email_sender = EmailSender()
        
        global_news = scraper.get_global_news()
        africa_news = scraper.get_africa_news()
        east_africa_news = scraper.get_east_africa_news()
        tanzania_news = scraper.get_tanzania_news()
        
        analyzed_news = {
            'global': analyzer.analyze_news(global_news, 'global'),
            'africa': analyzer.analyze_news(africa_news, 'africa'),
            'east_africa': analyzer.analyze_news(east_africa_news, 'east_africa'),
            'tanzania': analyzer.analyze_news(tanzania_news, 'tanzania')
        }
        
        email_content = email_sender.create_email_content(analyzed_news)
        recipient = os.getenv('EMAIL_RECIPIENT')
        email_sender.send_email(to=recipient, subject=f'[TEST] Daily Financial News - {datetime.now().strftime(\\\"%B %d, %Y\\\")}', html_content=email_content)
        "
      env:
        EMAIL_SENDER: ${{ secrets.EMAIL_SENDER }}
        EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
        EMAIL_RECIPIENT: ${{ secrets.EMAIL_RECIPIENT }}
''')
    print(f"✓ Created {manual_fetch}")
    
    return True

def push_to_github():
    """Commit and push the workflows to GitHub"""
    try:
        subprocess.run(['git', 'add', '.github/'], check=True, capture_output=True)
        subprocess.run(['git', 'commit', '-m', 'Add GitHub Actions workflows for daily financial news'], check=True, capture_output=True)
        subprocess.run(['git', 'push'], check=True, capture_output=True)
        print("✓ Pushed to GitHub")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Git error: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("🤖 GitHub Actions Setup Helper")
    print("="*70 + "\n")
    
    # Create workflows locally
    print("📝 Creating workflow files...\n")
    if create_workflows():
        print("\n✅ Workflow files created successfully!")
    else:
        print("\n❌ Failed to create workflow files")
        sys.exit(1)
    
    # Ask to push
    print("\n📤 Next, you need to:")
    print("   1. Commit these files to git")
    print("   2. Push to GitHub")
    print("\nRun these commands:")
    print("   git add .github/")
    print("   git commit -m 'Add GitHub Actions workflows'")
    print("   git push")
    
    # Ask about secrets
    print("\n" + "="*70)
    print("🔐 Repository Secrets Setup")
    print("="*70)
    print("\nGo to: https://github.com/ammarjiwaji-max/friendly-octo-invention/settings/secrets/actions")
    print("\nAdd these secrets:")
    print("  • EMAIL_SENDER = ammar.jiwaji@gmail.com")
    print("  • EMAIL_PASSWORD = Your Gmail App Password (16 chars)")
    print("  • EMAIL_RECIPIENT = ammar.jiwaji@gmail.com")
    print("  • BOT_SCHEDULE_TIME = 06:00")
    print("  • TIMEZONE = Africa/Dar_es_Salaam")
    
    print("\n" + "="*70)
    print("✨ Setup Complete!")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
