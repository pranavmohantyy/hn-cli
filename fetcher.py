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
        print("Select a story number:")
        for i, story_id in enumerate(top_story_ids[start_index:end_index]):
            print(f'{i + 1}. {story_id}')
        choice = input()
        if choice.isdigit() and 1 <= int(choice) <= stories_per_page:
            item_details = fetch_item_details(top_story_ids[start_index + int(choice) - 1])
            print(f'Title: {item_details["title"]}\nURL: {item_details["url"]}\nScore: {item_details["score"]}\nAuthor: {item_details["by"]}\nTime: {item_details["time"]}')
        else:
            print("Invalid choice. Try again.")
            continue
        if input("Continue? (y/n): ").lower() != 'y':
            break