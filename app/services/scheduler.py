from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.routers.get_summary import update_summaries
from apscheduler.triggers.date import DateTrigger

scheduler = AsyncIOScheduler()

async def start_scheduler():
    scheduler.add_job(update_summaries, DateTrigger(), id='immediate_job')
    scheduler.add_job(update_summaries, 'interval', hours=12)
    print("running scheduler")
    scheduler.start()
