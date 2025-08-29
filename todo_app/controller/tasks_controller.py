from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from todo_app.logic.tasks_logic import TasksLogic
from todo_app.serializer.tasks_serializer import TasksSerializer

class TasksController(APIView, LimitOffsetPagination):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks_logic = TasksLogic()

    def get(self, request):
        try:
            user = request.user
            data = request.data
            id_ = data.get('id')

            if id_:
                data_qs = self.tasks_logic.get_task_by_id(id_)
                serialized_data = TasksSerializer(data_qs, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            data_qs = self.tasks_logic.get_all_tasks(user)
            serialized_data = TasksSerializer(data_qs, many=True)
            paginated_data = self.paginate_queryset(serialized_data.data, request, view=None)

            return Response(paginated_data, HTTP_200_OK)
        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)
