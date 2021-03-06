from rest_framework import serializers
from .models import Business,Account,DebitAccount,CreditAccount,User,Ownership,StockCollection
# from django.contrib.auth.models import User 
class OwnershipSerializer(serializers.ModelSerializer):
	class Meta:
		model =Ownership
		fields ="__all__"
		
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model =User
		fields ="__all__"

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model =Account
		fields ="__all__"

class CreditAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model =CreditAccount
		fields ="__all__"

class DebitAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model =DebitAccount
		fields ="__all__"

class BusinessSerializer(serializers.ModelSerializer):
	class Meta:
		model = Business
		fields= "__all__"


class StockCollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = StockCollection
		fields= "__all__"



