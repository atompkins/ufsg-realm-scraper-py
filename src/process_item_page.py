from bs4 import BeautifulSoup

from src.sqlite_writer import sql_writer
from .get_html import get_html
import re
from urllib.parse import urlparse, parse_qs

async def process_item_page(session, td):
  a = td.find('a')
  url = a.get('href')
  html = await get_html(session, url)
  soup = BeautifulSoup(html, 'html.parser')
  creatures = soup.find_all('a', href = re.compile(r'&creature_id=\d'))
  realm_info = (
      parse_qs(urlparse(url).query)['realm_id'][0],
      a.get_text(),
      td.find_next_sibling('td').find_next_sibling('td').get_text()
    )
  creature_stats = [realm_info + (
    parse_qs(urlparse(creature.get('href')).query)['creature_id'][0],
    creature.get_text(),
    creature.next_sibling.get_text().strip(' ()')
  ) for creature in creatures]
  sql_writer(creature_stats)
