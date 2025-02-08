from ninja import NinjaAPI
from users.views import router as users_router
from tasks.views import router as tasks_router
from todo.views import router as todo_router

api = NinjaAPI()


@api.get("/greet")
def greet(request):
    return {"message": "Hello, Django Ninja!"}


api.add_router("/users", users_router)
api.add_router("/tasks", tasks_router)
api.add_router("/todos", todo_router)
