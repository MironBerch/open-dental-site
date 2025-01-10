import json

from bs4 import BeautifulSoup

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
