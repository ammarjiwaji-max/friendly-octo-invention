"""
Email Sender Module
Sends formatted financial news emails
"""

import smtplib
import logging
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import Dict, List

logger = logging.getLogger(__name__)

class EmailSender:
    """Sends financial news updates via email"""
    
    def __init__(self):
        self.sender_email = os.getenv('EMAIL_SENDER')
        self.sender_password = os.getenv('EMAIL_PASSWORD')
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
    
    def send_email(self, to: str, subject: str, html_content: str) -> bool:
        """Send email with HTML content"""
        try:
            # Create message
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.sender_email
            message['To'] = to
            
            # Attach HTML content
            message.attach(MIMEText(html_content, 'html'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, to, message.as_string())
            
            logger.info(f"Email sent successfully to {to}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}", exc_info=True)
            return False
    
    def create_email_content(self, analyzed_news: Dict) -> str:
        """Create formatted HTML email content"""
        date_str = datetime.now().strftime('%B %d, %Y')
        
        html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    background-color: #f9f9f9;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .header {{
                    text-align: center;
                    border-bottom: 3px solid #2c3e50;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }}
                .header h1 {{
                    color: #2c3e50;
                    margin: 0;
                    font-size: 28px;
                }}
                .header p {{
                    color: #7f8c8d;
                    margin: 10px 0 0 0;
                }}
                .category {{
                    margin-bottom: 30px;
                }}
                .category-header {{
                    display: flex;
                    align-items: center;
                    font-size: 20px;
                    color: #fff;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 15px;
                }}
                .category-global {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                }}
                .category-africa {{
                    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                }}
                .category-east-africa {{
                    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                }}
                .category-tanzania {{
                    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
                }}
                .news-item {{
                    border-left: 4px solid #667eea;
                    padding: 15px;
                    margin-bottom: 15px;
                    background-color: #f5f7fa;
                    border-radius: 4px;
                }}
                .news-item.tanzania {{
                    border-left-color: #43e97b;
                }}
                .news-title {{
                    font-weight: bold;
                    font-size: 16px;
                    color: #2c3e50;
                    margin-bottom: 8px;
                }}
                .news-source {{
                    color: #7f8c8d;
                    font-size: 12px;
                    margin-bottom: 8px;
                }}
                .news-summary {{
                    color: #555;
                    font-size: 14px;
                    margin-bottom: 10px;
                    line-height: 1.5;
                }}
                .news-link {{
                    display: inline-block;
                    color: #667eea;
                    text-decoration: none;
                    font-size: 12px;
                    margin-top: 8px;
                }}
                .news-link:hover {{
                    text-decoration: underline;
                }}
                .footer {{
                    text-align: center;
                    border-top: 1px solid #ecf0f1;
                    padding-top: 20px;
                    margin-top: 30px;
                    color: #7f8c8d;
                    font-size: 12px;
                }}
                .no-news {{
                    color: #7f8c8d;
                    font-style: italic;
                    padding: 15px;
                    background-color: #ecf0f1;
                    border-radius: 4px;
                    text-align: center;
                }}
                .emoji {{
                    margin-right: 8px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📰 Daily Financial News Update</h1>
                    <p>{date_str}</p>
                </div>
        """
        
        # Global News Section
        html += self._create_category_section(
            'Global Financial News',
            '🌍',
            analyzed_news.get('global', []),
            'category-global'
        )
        
        # Africa-Wide News Section
        html += self._create_category_section(
            'Africa-Wide Financial News',
            '🌍',
            analyzed_news.get('africa', []),
            'category-africa'
        )
        
        # East Africa News Section
        html += self._create_category_section(
            'East Africa Financial News',
            '🌏',
            analyzed_news.get('east_africa', []),
            'category-east-africa'
        )
        
        # Tanzania News Section (Prioritized)
        html += self._create_category_section(
            'Tanzania-Specific Financial News (Prioritized)',
            '🇹🇿',
            analyzed_news.get('tanzania', []),
            'category-tanzania',
            is_priority=True
        )
        
        # Footer
        html += f"""
                <div class="footer">
                    <p>This is an automated daily financial news digest from your Financial News Bot.</p>
                    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC</p>
                    <p style="margin-top: 15px; color: #95a5a6;">
                        © 2026 Financial News Bot | Stay informed. Invest wisely.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def _create_category_section(self, title: str, emoji: str, news_items: List[Dict], 
                                 category_class: str, is_priority: bool = False) -> str:
        """Create HTML section for a news category"""
        html = f"""
                <div class="category">
                    <div class="category-header {category_class}">
                        <span class="emoji">{emoji}</span>
                        <span>{title}</span>
                    </div>
        """
        
        if not news_items:
            html += '<div class="no-news">No news items available for this category today.</div>'
        else:
            for item in news_items[:5]:  # Limit to 5 items per category
                item_class = 'tanzania' if is_priority else ''
                html += f"""
                    <div class="news-item {item_class}">
                        <div class="news-title">{item.get('title', 'News Title')}</div>
                        <div class="news-source">
                            📌 {item.get('source', 'Unknown Source')} | 
                            {item.get('category', 'General')}
                        </div>
                        <div class="news-summary">
                            {item.get('summary', 'No summary available')[:300]}...
                        </div>
                        <a href="{item.get('url', '#')}" class="news-link">Read Full Story →</a>
                    </div>
                """
        
        html += """
                </div>
        """
        
        return html
