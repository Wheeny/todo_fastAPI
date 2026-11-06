from fastapi import Depends
from repositories.todo_repository import TodoRepository
from repositories.in_memory_todo_repository import InMemoryTodoRepository
from services.todo_service import TodoService

_repository = InMemoryTodoRepository()

def get_todo_repository() -> TodoRepository:
        return _repository

def get_todo_service(repository: TodoRepository = Depends(get_todo_repository)) -> TodoService:
    return TodoService(repository)