from celery.result import AsyncResult
from ninja import Router
from .tasks import process_data

router = Router()


@router.post("/process")
def trigger_task(request, data: str):
    task = process_data.delay(data)  # Run task in the background
    return {"task_id": task.id}


@router.get("/status/{task_id}")
def get_task_status(request, task_id: str):
    result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }
