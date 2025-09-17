from rest_framework import serializers
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("Usuário ou senha inválidos.")
            if not user.check_password(password):
                raise serializers.ValidationError("Usuário ou senha inválidos.")
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Ambos os campos 'email' e 'password' são obrigatórios.")