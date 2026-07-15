#!/usr/bin/env python3
"""
Financial News Bot - Main Entry Point
Sends daily financial news updates via email at 6 AM
"""

import logging
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from news_scraper import NewsScaper
from email_sender import EmailSender
from news_analyzer import NewsAnalyzer

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/financial-news-bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def fetch_and_send_news():
    """Fetch financial news and send via email"""
    try:
        logger.info("Starting financial news collection...")
        
        # Initialize components
        scraper = NewsScaper()
        analyzer = NewsAnalyzer()
        email_sender = EmailSender()
        
        # Fetch news from all categories
        logger.info("Fetching global financial news...")
        global_news = scraper.get_global_news()
        
        logger.info("Fetching Africa-wide financial news...")
        africa_news = scraper.get_africa_news()
        
        logger.info("Fetching East Africa financial news...")
        east_africa_news = scraper.get_east_africa_news()
        
        logger.info("Fetching Tanzania-specific financial news...")
        tanzania_news = scraper.get_tanzania_news()
        
        # Analyze and categorize news
        analyzed_news = {
            'global': analyzer.analyze_news(global_news, 'global'),
            'africa': analyzer.analyze_news(africa_news, 'africa'),
            'east_africa': analyzer.analyze_news(east_africa_news, 'east_africa'),
            'tanzania': analyzer.analyze_news(tanzania_news, 'tanzania')
        }
        
        # Create and send email
        logger.info("Creating email content...")
        email_content = email_sender.create_email_content(analyzed_news)
        
        logger.info("Sending email...")
        recipient = os.getenv('EMAIL_RECIPIENT')
        success = email_sender.send_email(
            to=recipient,
            subject=f"Daily Financial News Update - {datetime.now().strftime('%B %d, %Y')}",
            html_content=email_content
        )
        
        if success:
            logger.info(f"Email successfully sent to {recipient}")
        else:
            logger.error("Failed to send email")
            
    except Exception as e:
        logger.error(f"Error in fetch_and_send_news: {str(e)}", exc_info=True)

def start_scheduler():
    """Start the APScheduler background scheduler"""
    try:
        schedule_time = os.getenv('BOT_SCHEDULE_TIME', '06:00')
        timezone = os.getenv('TIMEZONE', 'Africa/Dar_es_Salaam')
        
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            fetch_and_send_news,
            'cron',
            hour=int(schedule_time.split(':')[0]),
            minute=int(schedule_time.split(':')[1]),
            timezone=timezone,
            id='daily_financial_news'
        )
        
        scheduler.start()
        logger.info(f"Scheduler started. Daily update scheduled for {schedule_time} ({timezone})")
        
        # For testing: uncomment to run immediately
        # fetch_and_send_news()
        
        try:
            while True:
                pass
        except KeyboardInterrupt:
            logger.info("Shutting down scheduler...")
            scheduler.shutdown()
            
    except Exception as e:
        logger.error(f"Error starting scheduler: {str(e)}", exc_info=True)

if __name__ == '__main__':
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    logger.info("Starting Financial News Bot...")
    start_scheduler()
