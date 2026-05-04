from fastapi import Depends
from pathlib import Path

from app.core.config import config
from app.services.tistory.browser import TistoryBrowserService
from app.services.tistory.post import TistoryPostService


def get_browser_service() -> TistoryBrowserService:
    return TistoryBrowserService()


def get_tistory_post_service(
    tistory_browser_service = Depends(get_browser_service)
) -> TistoryPostService:
    tistory_context = Path(config.STORAGE_PATH) / "tistory" / "browser_context.json"
    return TistoryPostService(tistory_browser_service, tistory_context)