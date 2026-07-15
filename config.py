"""
Configuration Management
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # Email Configuration
    EMAIL_SENDER = os.getenv('EMAIL_SENDER', 'your-email@gmail.com')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
    EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT', 'ammar.jiwaji@gmail.com')
    
    # Scheduler Configuration
    BOT_SCHEDULE_TIME = os.getenv('BOT_SCHEDULE_TIME', '06:00')
    TIMEZONE = os.getenv('TIMEZONE', 'Africa/Dar_es_Salaam')
    
    # Application Settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # API Configuration
    BING_SEARCH_API_KEY = os.getenv('BING_SEARCH_API_KEY', '')
    
    # News Sources
    NEWS_SOURCES = {
        'global': [
            'https://finance.yahoo.com',
            'https://www.cnbc.com',
            'https://www.bloomberg.com/markets'
        ],
        'africa': [
            'https://www.theafricareport.com',
            'https://www.financialafrik.com',
            'https://theexchange.africa'
        ],
        'east_africa': [
            'https://fintechnews.africa',
            'https://www.eabusinesstimes.com'
        ],
        'tanzania': [
            'https://www.tanzaniainvest.com',
            'https://www.finance.tz',
            'https://dailynews.co.tz'
        ]
    }
