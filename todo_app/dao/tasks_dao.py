from todo_app.entity.task_entity import TaskEntity


class TasksDao:

    def get_all_tasks(self, username):
        return TaskEntity.objects.filter(username=username)

    def get_task_by_id(self, id_):
        return TaskEntity.objects.get(pk=id_)

    def get_task_by_title(self, title):
        return TaskEntity.objects.filter(title__icontains=title).order_by('-created_at')