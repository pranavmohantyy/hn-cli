import requests

def fetch_top_story_ids():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    return response.json()


def fetch_item_details(item_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
    return response.json()


if __name__ == '__main__':
    top_story_ids = fetch_top_story_ids()
    for index, story_id in enumerate(top_story_ids[:30]):
        story_details = fetch_item_details(story_id)
        title = story_details.get('title', 'No Title')
        score = story_details.get('score', 0)
        comments = story_details.get('descendants', 0)
        print(f"{index + 1}. {title} (Score: {score}, Comments: {comments})")