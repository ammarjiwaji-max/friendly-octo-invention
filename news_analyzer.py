"""
News Analyzer Module
Categorizes and analyzes financial news
"""

import logging
from typing import List, Dict
from datetime import datetime

logger = logging.getLogger(__name__)

class NewsAnalyzer:
    """Analyzes and categorizes financial news"""
    
    KEYWORDS = {
        'global': ['inflation', 'fed', 'markets', 'stocks', 'bonds', 'currency', 'oil', 'tech', 'ai'],
        'africa': ['kenya', 'nigeria', 'south africa', 'ethiopia', 'angola', 'imf', 'african'],
        'east_africa': ['kenya', 'uganda', 'rwanda', 'tanzania', 'fintech', 'banking', 'mobile money', 'digital'],
        'tanzania': ['tanzania', 'dar es salaam', 'dse', 'tsh', 'gold', 'mining', 'tourism', 'tea', 'coffee']
    }
    
    def analyze_news(self, news_items: List[Dict], category: str) -> List[Dict]:
        """Analyze and categorize news items"""
        analyzed = []
        
        for item in news_items:
            try:
                analysis = {
                    'source': item.get('source', 'Unknown'),
                    'title': item.get('title', item.get('category', 'Financial News')),
                    'summary': item.get('summary', item.get('content', '')[:200]),
                    'url': item.get('url', ''),
                    'category': item.get('category', 'General'),
                    'timestamp': item.get('timestamp', datetime.now().isoformat()),
                    'relevance_score': self._calculate_relevance(item, category)
                }
                analyzed.append(analysis)
            except Exception as e:
                logger.warning(f"Error analyzing news item: {str(e)}")
        
        # Sort by relevance score
        analyzed.sort(key=lambda x: x['relevance_score'], reverse=True)
        return analyzed
    
    def _calculate_relevance(self, item: Dict, category: str) -> float:
        """Calculate relevance score for news item"""
        score = 0.5  # Base score
        
        content = str(item.get('title', '') + ' ' + item.get('summary', '')).lower()
        keywords = self.KEYWORDS.get(category, [])
        
        for keyword in keywords:
            if keyword in content:
                score += 0.2
        
        return min(score, 1.0)  # Cap at 1.0
    
    def get_summary_statistics(self, analyzed_news: Dict) -> Dict:
        """Get summary statistics of analyzed news"""
        stats = {
            'total_items': sum(len(v) for v in analyzed_news.values()),
            'items_per_category': {k: len(v) for k, v in analyzed_news.items()},
            'timestamp': datetime.now().isoformat()
        }
        return stats
