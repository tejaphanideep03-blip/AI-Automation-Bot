from collectors.ai_news import get_ai_news
from collectors.ai_models import get_models
from collectors.github_trending import get_trending
from collectors.reddit import get_reddit
from collectors.cybersecurity import get_cyber
from collectors.formatter import make_section

from utils.discord import send_message

message = ""

message += make_section("📰 AI NEWS", get_ai_news())
message += make_section("🤖 MODELS", get_models())
message += make_section("💻 GITHUB", get_trending())
message += make_section("👥 REDDIT", get_reddit())
message += make_section("🔐 CYBER", get_cyber())

send_message("🚀 AI Daily Update", message[:4000])