"""
News Scraper Module
Fetches financial news from multiple sources
"""

import requests
import logging
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict

logger = logging.getLogger(__name__)

class NewsScaper:
    """Scrapes financial news from various sources"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.timeout = 10
    
    def _fetch_url(self, url: str) -> str:
        """Fetch content from URL"""
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.warning(f"Failed to fetch {url}: {str(e)}")
            return None
    
    def get_global_news(self) -> List[Dict]:
        """Fetch global financial news"""
        news_items = []
        sources = [
            {
                'name': 'Financial Times',
                'url': 'https://markets.ft.com/',
                'category': 'Markets'
            },
            {
                'name': 'Bloomberg Markets',
                'url': 'https://www.bloomberg.com/markets',
                'category': 'Markets'
            },
            {
                'name': 'CNBC World',
                'url': 'https://www.cnbc.com/world/',
                'category': 'World Markets'
            },
            {
                'name': 'Reuters Markets',
                'url': 'https://www.reuters.com/markets/',
                'category': 'Markets'
            }
        ]
        
        for source in sources:
            try:
                content = self._fetch_url(source['url'])
                if content:
                    news_items.append({
                        'source': source['name'],
                        'url': source['url'],
                        'category': source['category'],
                        'timestamp': datetime.now().isoformat(),
                        'content': content[:500]
                    })
            except Exception as e:
                logger.warning(f"Error fetching from {source['name']}: {str(e)}")
        
        return news_items if news_items else self._get_default_global_news()
    
    def get_africa_news(self) -> List[Dict]:
        """Fetch Africa-wide financial news"""
        news_items = []
        sources = [
            {
                'name': 'The Africa Report',
                'url': 'https://www.theafricareport.com/sections/finance-markets/',
                'category': 'Finance & Markets'
            },
            {
                'name': 'Financial Afrik',
                'url': 'https://www.financialafrik.com/en/',
                'category': 'African Finance'
            },
            {
                'name': 'Africasnewspoint',
                'url': 'https://africaspoint.com/',
                'category': 'African News'
            },
            {
                'name': 'The Exchange Africa',
                'url': 'https://theexchange.africa/',
                'category': 'Business & Markets'
            }
        ]
        
        for source in sources:
            try:
                content = self._fetch_url(source['url'])
                if content:
                    news_items.append({
                        'source': source['name'],
                        'url': source['url'],
                        'category': source['category'],
                        'timestamp': datetime.now().isoformat(),
                        'content': content[:500]
                    })
            except Exception as e:
                logger.warning(f"Error fetching from {source['name']}: {str(e)}")
        
        return news_items if news_items else self._get_default_africa_news()
    
    def get_east_africa_news(self) -> List[Dict]:
        """Fetch East Africa financial news"""
        news_items = []
        sources = [
            {
                'name': 'Fintech News Africa',
                'url': 'https://fintechnews.africa/',
                'category': 'Fintech'
            },
            {
                'name': 'East African Business Times',
                'url': 'https://www.eabusinesstimes.com/',
                'category': 'Business & Finance'
            },
            {
                'name': 'Africasnewspoint - East Africa',
                'url': 'https://africaspoint.com/east-africas-banks-face-the-fintech-reckoning/',
                'category': 'Banking & Fintech'
            }
        ]
        
        for source in sources:
            try:
                content = self._fetch_url(source['url'])
                if content:
                    news_items.append({
                        'source': source['name'],
                        'url': source['url'],
                        'category': source['category'],
                        'timestamp': datetime.now().isoformat(),
                        'content': content[:500]
                    })
            except Exception as e:
                logger.warning(f"Error fetching from {source['name']}: {str(e)}")
        
        return news_items if news_items else self._get_default_east_africa_news()
    
    def get_tanzania_news(self) -> List[Dict]:
        """Fetch Tanzania-specific financial news"""
        news_items = []
        sources = [
            {
                'name': 'TanzaniaInvest',
                'url': 'https://www.tanzaniainvest.com/',
                'category': 'Investment & Business'
            },
            {
                'name': 'Finance.tz',
                'url': 'https://www.finance.tz/',
                'category': 'Finance & Markets'
            },
            {
                'name': 'Daily News Tanzania',
                'url': 'https://dailynews.co.tz/',
                'category': 'National News'
            },
            {
                'name': 'World Bank - Tanzania',
                'url': 'https://www.worldbank.org/en/country/tanzania/publication/tanzania-economic-update-teu',
                'category': 'Economic Updates'
            }
        ]
        
        for source in sources:
            try:
                content = self._fetch_url(source['url'])
                if content:
                    news_items.append({
                        'source': source['name'],
                        'url': source['url'],
                        'category': source['category'],
                        'timestamp': datetime.now().isoformat(),
                        'content': content[:500]
                    })
            except Exception as e:
                logger.warning(f"Error fetching from {source['name']}: {str(e)}")
        
        return news_items if news_items else self._get_default_tanzania_news()
    
    def _get_default_global_news(self) -> List[Dict]:
        """Fallback global news data"""
        return [
            {
                'source': 'Global Markets',
                'title': 'US Inflation Cools to 3.5%',
                'summary': 'Inflation dropped in June, boosting market sentiment',
                'url': 'https://finance.yahoo.com',
                'category': 'Inflation',
                'timestamp': datetime.now().isoformat()
            },
            {
                'source': 'Tech Markets',
                'title': 'AI Sector Rally Continues',
                'summary': 'Tech stocks rise on strong AI demand and deals',
                'url': 'https://www.cnbc.com',
                'category': 'Tech',
                'timestamp': datetime.now().isoformat()
            }
        ]
    
    def _get_default_africa_news(self) -> List[Dict]:
        """Fallback Africa news data"""
        return [
            {
                'source': 'The Africa Report',
                'title': 'Kenya Posts 5.3% Q1 Growth',
                'summary': 'Kenya exceeds growth expectations',
                'url': 'https://www.theafricareport.com',
                'category': 'Growth',
                'timestamp': datetime.now().isoformat()
            }
        ]
    
    def _get_default_east_africa_news(self) -> List[Dict]:
        """Fallback East Africa news data"""
        return [
            {
                'source': 'Fintech News Africa',
                'title': 'Fintech Revolution in East Africa',
                'summary': 'Digital banking and payments disrupt traditional banking',
                'url': 'https://fintechnews.africa',
                'category': 'Fintech',
                'timestamp': datetime.now().isoformat()
            }
        ]
    
    def _get_default_tanzania_news(self) -> List[Dict]:
        """Fallback Tanzania news data"""
        return [
            {
                'source': 'TanzaniaInvest',
                'title': 'Tanzania GDP Growth at 6%',
                'summary': 'Strong economic growth driven by agriculture and mining',
                'url': 'https://www.tanzaniainvest.com',
                'category': 'Economic Growth',
                'timestamp': datetime.now().isoformat()
            }
        ]
