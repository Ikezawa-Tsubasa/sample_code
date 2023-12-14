from googleapiclient.discovery import build
# YouTube Data APIのAPIキーを設定
API_KEY = "YOUR_API_KEY"
def search_videos(keyword, max_results=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    # 検索クエリを作成
    search_response = youtube.search().list(
        q=keyword,
        part='id,snippet',
        maxResults=max_results
    ).execute()
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video = {
                'title': search_result['snippet']['title'],
                'video_id': search_result['id']['videoId']
            }
            videos.append(video)
    return videos
# 動画を検索して結果を表示
keyword = input("検索キーワードを入力してください: ")
results = search_videos(keyword)
for result in results:
    print(result['title'])
    print("https://www.youtube.com/watch?v=" + result['video_id'])
    print()
