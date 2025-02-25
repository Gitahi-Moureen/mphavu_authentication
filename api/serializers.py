


# from rest_framework import serializers
# from user.models import User
# from django.contrib.auth.models import User as DjangoUser

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs = {
#             'password':{'write_only':True}
#         }


#     def create(self, validated_data):
#         # Use create_user to handle password hashing
#         user = User.objects.create_user(
#             first_name =validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user    



# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

# class ResetPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField()


# class MinimalUseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ['user_id', 'first_name', 'last_name', 'role']
#         fields = '__all__'


from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from user.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role']

    def create(self, validated_data):
        # Create a DjangoUser object
        django_user = DjangoUser.objects.create_user(
            username=validated_data['email'],  # Using email as username
            email=validated_data['email'],
            password=validated_data['password'],
        )

        # Create the custom User object linked to the DjangoUser
        custom_user = User.objects.create(
            user=django_user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'], 
            # role=validated_data['role'],
        )

        return custom_user


         
         
         
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class MinimalUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'role']
        fields = '__all__'