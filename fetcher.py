import requests


def fetch_top_story_ids(category):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/{category}.json')
    return response.json()


def fetch_item_details(item_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
    return response.json()


if __name__ == '__main__':
    import sys
    category = sys.argv[1] if len(sys.argv) > 1 else 'topstories'
    page = 0
    stories_per_page = 30
    while True:
        top_story_ids = fetch_top_story_ids(category)
        start_index = page * stories_per_page
        end_index = start_index + stories_per_page
        for index, story_id in enumerate(top_story_ids[start_index:end_index]):
            story_details = fetch_item_details(story_id)
            title = story_details.get('title', 'No Title')
            print(f'{index + 1 + page * stories_per_page}: {title}')
        command = input('Press p for next page, b for previous, q to quit: ').strip().lower()
        if command == 'p':
            page += 1
        elif command == 'b':
            if page > 0:
                page -= 1
        elif command == 'q':
            break