from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer

# لیست و ایجاد
class AccountListCreateView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.all()

    def perform_create(self, serializer):
        serializer.save()


# جزئیات، ویرایش، حذف
class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.all()

    def perform_update(self, serializer):
        print("🔧 در حال ویرایش اکانت توسط:", self.request)
        serializer.save()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "اکانت با موفقیت حذف شد ✅"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        print(f"🗑 اکانت {instance} توسط {self.request} حذف شد")
        instance.delete()