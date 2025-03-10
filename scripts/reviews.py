import json
import logging
from datetime import datetime
from os import environ

import psycopg2
from bs4 import BeautifulSoup
from psycopg2._psycopg import connection as postgres_connection_object
from psycopg2.extras import DictCursor, execute_values

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


MONTHS = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}


def create_reviews_json_file():
    with open('reviews.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    reviews = soup.find_all('div', class_='business-reviews-card-view__review')
    reviews_list = []

    for review in reviews:
        review: BeautifulSoup = review
        try:
            author_name, date, rating, review_text = None, None, None, None
            author_name = review.find('span', itemprop='name').text.strip()
            date = review.find('span', class_='business-review-view__date').text.strip()
            rating = review.find('meta', itemprop='ratingValue')['content']
            review_text = review.find('span', class_='business-review-view__body-text').text.strip()
            reviews_list.append(
                {
                    'author_name': author_name,
                    'date': date,
                    'rating': rating,
                    'review_text': review_text
                }
            )
        except Exception:
            pass

    reviews_json = json.dumps(reviews_list, ensure_ascii=False, indent=4)
    with open('reviews.json', 'w', encoding='utf-8') as f:
        f.write(reviews_json)
    print('Отзывы успешно сохранены в reviews.json')


class Review:

    def __init__(
            self,
            author_name: str,
            date: str,
            rating: float,
            review_text: str,
    ):
        self.author_name = author_name
        self.date = self.convert_date(date)
        self.rating = rating
        self.review_text = review_text

    @staticmethod
    def convert_date(date_str: str) -> str:
        parts = date_str.split()
        if len(parts) == 3:
            day, month_name, year = parts
        else:
            day, month_name = parts
            year = str(datetime.now().year)
        month = MONTHS.get(month_name, '01')
        return f'{year}-{month}-{day.zfill(2)}T00:00:00'

    def to_tuple(self):
        return (self.author_name, self.review_text, self.rating, True, self.date, )


class DataExtraction:
    def extract(self) -> list[Review]:
        with open('reviews.json', 'r', encoding='utf-8') as f:
            reviews_data = json.load(f)

        reviews = []
        for review in reviews_data:
            reviews.append(
                Review(
                    author_name=review['author_name'],
                    date=review['date'],
                    rating=float(review['rating']),
                    review_text=review['review_text'],
                )
            )
        return reviews


class PostgresDataLoader:
    def __init__(self, postgres_connection: postgres_connection_object):
        self.postgres_connection = postgres_connection

    def load_data(self, reviews: list[Review]):
        with self.postgres_connection.cursor() as cursor:
            sql = '''
                INSERT INTO public.clinic_review (name, message, rating, published, created_at)
                VALUES %s
                ON CONFLICT (id) DO NOTHING
            '''
            try:
                execute_values(
                    cursor,
                    sql,
                    [review.to_tuple() for review in reviews],
                )
                self.postgres_connection.commit()
            except psycopg2.OperationalError as e:
                logging.error(f'psycopg2 operational error: `{e}`')
                cursor.close()
                raise


def load_from_json(postgres_connection: postgres_connection_object):
    logging.info('Начата загрузка данных в PostgreSQL')
    data_extraction = DataExtraction()
    postgres_data_loader = PostgresDataLoader(postgres_connection)
    reviews = data_extraction.extract()
    postgres_data_loader.load_data(reviews)


if __name__ == '__main__':
    dsn = {
        'dbname': environ.get('POSTGRES_DB'),
        'user': environ.get('POSTGRES_USER'),
        'password': environ.get('POSTGRES_PASSWORD'),
        'host': environ.get('POSTGRES_HOST'),
        'port': int(environ.get('POSTGRES_PORT')),
    }
    with psycopg2.connect(**dsn, cursor_factory=DictCursor) as postgres_connection:
        load_from_json(postgres_connection=postgres_connection)
