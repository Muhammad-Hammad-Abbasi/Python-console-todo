from src.services.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.cli.menu import display_menu, get_menu_choice, handle_menu_choice

def main():
    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == 6: # Exit option
            break
        
        handle_menu_choice(choice, task_service)

if __name__ == "__main__":
    main()