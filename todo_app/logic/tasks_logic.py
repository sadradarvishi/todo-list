from todo_app.dao.tasks_dao import TasksDao


class TasksLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks_dao = TasksDao()

    def get_all_tasks(self, user):
        username = user.username
        return self.tasks_dao.get_all_tasks(username=username)

    def get_task_by_id(self, id_):
