import os
import re
import requests
import urllib3
from datetime import datetime

def sanitize_filename(title):
    return re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')

def create_markdown_content(post):
    content = f"# {post['title']}\n\n"
    content += f"Date: {post['date']}\n\n"
    content += f"Categories: {', '.join(post['categories'])}\n\n"
    content += "---\n\n"
    content += post['content']
    return content

def get_posts(site_url, per_page=100, page=1):
    url = f"{site_url}/wp-json/wp/v2/posts"
    params = {
        'per_page': per_page,
        'page': page,
        'status': 'publish',
        '_embed': 'true'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }
    
    session = requests.Session()
    session.verify = False
    requests.packages.urllib3.disable_warnings()
    
    response = session.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        total_pages = int(response.headers.get('X-WP-TotalPages', 1))
        return response.json(), total_pages
    elif response.status_code == 400:
        # If we get a 400, we've exceeded the available pages
        return None, 0
    else:
        print(f"Error: HTTP {response.status_code} - {response.text}")
        return None, 0

def main():
    site_url = "https://solucoesms.com.br"
    
    output_dir = "github_solutions"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    page = 1
    total_posts = 0
    
    while True:
        try:
            posts, total_pages = get_posts(site_url, page=page)
            if not posts:
                break

            for post in posts:
                # Extract categories
                categories = []
                if '_embedded' in post and 'wp:term' in post['_embedded']:
                    for terms in post['_embedded']['wp:term']:
                        for term in terms:
                            if term['taxonomy'] == 'category':
                                categories.append(term['name'])

                if not categories:
                    categories = ['uncategorized']

                post_data = {
                    'title': post['title']['rendered'],
                    'content': post['content']['rendered'],
                    'date': datetime.fromisoformat(post['date']).strftime('%Y-%m-%d %H:%M:%S'),
                    'categories': categories
                }

                # Create category directories and save files
                for category in categories:
                    category_dir = os.path.join(output_dir, sanitize_filename(category))
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)

                    filename = f"{sanitize_filename(post_data['title'])}.md"
                    filepath = os.path.join(category_dir, filename)

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(create_markdown_content(post_data))
                
                total_posts += 1

            print(f"Processed page {page}/{total_pages} - Total posts: {total_posts}")
            
            if page >= total_pages:
                break
                
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            break

    print(f"Export completed successfully! Total posts exported: {total_posts}")

if __name__ == "__main__":
    main()