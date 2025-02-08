from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Todo
from .schemas import TodoSchemaMeta, TodoSchemaConfig, TodoUpdateSchema

router = Router()


# Create a new Todo (Using Meta Schema)
@router.post("/", response=TodoSchemaMeta)
def create_todo(request, data: TodoSchemaMeta):
    return Todo.objects.create(**data.dict())


# Get all Todos (Using Config Schema)
@router.get("/", response=list[TodoSchemaConfig])
def list_todos(request):
    return Todo.objects.all()


# Get a specific Todo by ID
@router.get("/{todo_id}", response=TodoSchemaConfig)
def get_todo(request, todo_id: int):
    return get_object_or_404(Todo, id=todo_id)


# Update a Todo
@router.put("/{todo_id}", response=TodoSchemaConfig)
def update_todo(request, todo_id: int, data: TodoUpdateSchema):
    todo = get_object_or_404(Todo, id=todo_id)

    for attr, value in data.dict(exclude_unset=True).items():
        setattr(todo, attr, value)

    todo.save()
    return TodoSchemaConfig.from_orm(todo)


# Delete a Todo
@router.delete("/{todo_id}")
def delete_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return {"message": "Todo deleted"}
