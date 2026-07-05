from collectors.ai_news import get_ai_news
from collectors.ai_models import get_models
from collectors.github_trending import get_trending
from collectors.reddit import get_reddit
from collectors.cybersecurity import get_cyber
from utils.formatter import build_message

from utils.discord import send_embed

message = ""

message += build_message(get_ai_news())
message += build_message(get_models())
message += build_message(get_trending())
message += build_message(get_reddit())
message += build_message(get_cyber())

send_embed("🚀 AI Daily Update", message[:4000])