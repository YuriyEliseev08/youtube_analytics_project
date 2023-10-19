from googleapiclient.discovery import build
import os


def get_channel(channel_id):
    api_key: str = os.getenv('YOUTUBEAPIKEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel = youtube.channels().list(id=channel_id, part="snippet, statistics").execute()
    return channel


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = get_channel(self.channel_id)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        return self.channel_info
