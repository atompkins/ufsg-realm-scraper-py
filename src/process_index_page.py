import asyncio
from bs4 import BeautifulSoup
from .get_html import get_html
from .process_item_page import process_item_page

async def process_index_page(session, url):
  html = await get_html(session, url)
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.find_all('td', height='20')
  tasks = [process_item_page(session, a) for a in items]
  # tasks = [process_item_page(session, td) for td in items[:1]] # DEBUG
  # tasks = [process_item_page(session, a) for a in items[5:6]] # DEBUG
  await asyncio.gather(*tasks)
  return soup.find('font', color='#FF0000').parent.find_next('a')
