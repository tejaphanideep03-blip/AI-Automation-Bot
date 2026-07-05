from utils.discord import send_embed
from utils.colors import BLUE


class NotificationService:

    @staticmethod
    def send(title, message):

        send_embed(
            title,
            message,
            BLUE
        )