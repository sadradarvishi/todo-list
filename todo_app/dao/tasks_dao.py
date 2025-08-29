from todo_app.entity.task_entity import TaskEntity


class TasksDao:

    def get_all_tasks(self, username):
        return TaskEntity.objects.filter(username=username)