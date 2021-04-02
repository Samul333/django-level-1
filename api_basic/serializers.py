from rest_framework import serializers
from .models import *


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=100)
#     date = serializers.DateTimeField()


#     def create(self,validated_data):
#         return Article.objects.create(validated_data)

#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.author = validated_data.get('author',instance.author)
#         instance.email = validated_data.get('email',instance.email)
#         instance.data = validated_data.get('date',instance.date)
#         instance.save()

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'




class TutorSerializer(serializers.ModelSerializer):
    #tutor_emailaddress = serializers.EmailField(
           # required=True,
           # validators=[UniqueValidator(queryset=User.objects.all())]
           # )
   class Meta:
        model = Tutor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = '__all__'

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)

    class Meta:
        model= Tutor
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        Tutor = Tutor(
            tutor_emailaddress=self.validated_data['email'],
            tutor_username = self.validated_data['username'],
            tutor_first_name=self.validated_data['firstname'], 
            tutor_last_name=self.validated_data['lastname'], 
            tutor_address=self.validated_data['address'], 
            tutor_gender=self.validated_data['gender'], 
            tutor_contactno=self.validated_data['contactno'], 
            tutor_qualification=self.validated_data['qualification'],
            tutor_educationalInstitute=self.validated_data['educationalinstitute'], 
            tutor_chargePerHour=self.validated_data['chargeperhour'], 
        )
            
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'}) 
            
        Tutor.set_tutor_password(password)
        Tutor.save()
        return Tutor