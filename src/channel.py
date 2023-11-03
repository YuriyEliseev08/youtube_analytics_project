import json

from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()


def get_channel(channel_id):
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel = youtube.channels().list(id=channel_id, part="snippet, statistics").execute()
    return channel


class Channel:
    """Класс для ютуб-канала"""

    youtube = None

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = get_channel(self.channel_id)
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.descriptions = self.channel_info['items'][0]['snippet']['description']
        self.url = 'http://www.youtube.com' + self.channel_info['items'][0]['snippet']['customUrl']
        self.subscribers = int(self.channel_info['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel_info['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.channel_info['items'][0]['statistics']['viewCount'])

    @classmethod
    def get_channel(cls, channel_id: str):
        yt_channel = cls.youtube.channel().list(id=channel_id, part='snippet,statistics').execute()
        return yt_channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_info)
        return self.channel_info

    def to_json(self, channel_name):
        data = {}
        data['channel_id'] = self.channel_id
        data['channel_title'] = self.title
        data['channel_description'] = self.descriptions
        data['channel_url'] = self.url
        data['channel_subscribers'] = self.subscribers
        data['channel_videoCount'] = self.video_count
        data['channel_viewCount'] = self.viewCount
        with open(f'channel_name_{channel_name}.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def get_service():
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def __repr__(self):
        return f"Название канала: {self.title}, ID канала: {self.channel_id}, URL канала: {self.url}"

    def __str__(self):
        return f"Название канала: {self.title}, Подписчики: {self.subscribers}"

    def __add__(self, other):
        return self.subscribers + other.subscribers
    def __sub__(self, other):
        return self.subscribers - other.subscribers

    def __gt__(self, other):
        return self.subscribers > other.subscribers

    def __ge__(self, other):
        return self.subscribers >= other.subscribers

    def __lt__(self, other):
        return self.subscribers < other.subscribers

    def __le__(self, other):
        return self.subscribers <= other.subscribers

    def __eq__(self, other):
        return self.subscribers == other.subscribers










