import requests

def fetch_top_story_ids():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    return response.json()


def fetch_item_details(item_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
    return response.json()


if __name__ == '__main__':
    top_story_ids = fetch_top_story_ids()
    for story_id in top_story_ids[:5]:
        story_details = fetch_item_details(story_id)
        print(story_details)