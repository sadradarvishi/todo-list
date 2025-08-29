from rest_framework.serializers import ModelSerializer

from todo_app.entity.task_entity import TaskEntity

class TasksSerializer(ModelSerializer):
    class Meta:
        model = TaskEntity
        fields = '__all__'

    def get_object_type(self, obj):
        return 'Task'