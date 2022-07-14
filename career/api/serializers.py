from rest_framework import serializers
from .models import Candidate



class CandidateSerializer(serializers.ModelSerializer):
	Current_Organization = serializers.CharField(required=False)
	Total_Experience = serializers.CharField(required=False)
	Relavant_Experience = serializers.CharField(required=False)
	Joining_Period = serializers.CharField(required=False)
	Current_AnnualPay = serializers.CharField(required=False)
	Expected_AnnualPay = serializers.CharField(required=False)
	Position_AppliedFor = serializers.CharField(required=False)
	Personal_Website = serializers.CharField(required=False)
	LinkedIn_Profile = serializers.CharField(required=False)
	Twitter_Url = serializers.CharField(required=False)
	Discription = serializers.CharField(required=False)
	
	class Meta:
		model = Candidate
		fields = '__all__'
