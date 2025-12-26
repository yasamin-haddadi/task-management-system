from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer
# CRUD Operation 
# TeamCRUD
class TeamkListCreateRetrieveUpdateDestroyView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # فقط تیم. کاربر لاگین شده را نشان بده
        return Team.objects.all()

    def perform_create(self, serializer):
        # هنگام ساخت تیم. کاربر لاگین شده را اضافه می‌کنیم
       serializer.save()
        

    def perform_update(self, serializer):
        """
        شخصی‌سازی عملیات ویرایش
        """
        print("🔧 در حال ویرایش تیم توسط:", self.request.user)
        serializer.save()
    
    def delete(self, request, *args, **kwargs):
        """
        حذف تیم با پیام ساده برای Postman
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "تیم با موفقیت حذف شد ✅"}, status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        """
        شخصی‌سازی عملیات حذف
        """
        print(f"🗑 تیم {instance.name} توسط {self.request.user} حذف شد")
        instance.delete()