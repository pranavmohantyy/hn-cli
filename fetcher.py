import requests


def fetch_top_story_ids(category):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/{category}.json')
    return response.json()


def fetch_item_details(item_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
    return response.json()


def fetch_comments(item):
    comments = item.get('kids', [])
    return comments


def display_comments(comments, depth=0):
    for comment_id in comments:
        comment = fetch_item_details(comment_id)
        print('    ' * depth + f'Comment by {comment.get("by", "")}: {comment.get("text", "")[:50]}...')
        if 'kids' in comment:
            display_comments(comment['kids'], depth + 1)


if __name__ == '__main__':
    import sys
    category = sys.argv[1] if len(sys.argv) > 1 else 'topstories'
    page = 0
    stories_per_page = 30
    while True:
        top_story_ids = fetch_top_story_ids(category)
        start_index = page * stories_per_page
        end_index = start_index + stories_per_page
        for story_id in top_story_ids[start_index:end_index]:
            story = fetch_item_details(story_id)
            print(f'Title: {story.get("title", "")}
URL: {story.get("url", "")}
')
            comments = fetch_comments(story)
            display_comments(comments)
        page += 1
        if start_index >= len(top_story_ids):
            break
