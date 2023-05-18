from rest_framework import serializers
from .models import *


class contactserializer(serializers.ModelSerializer):
    class Meta:
        model= contactusModel
        fields='__all__'


    def validate(self, data):
        k =0
        d=0
        j=0
        # if len(data['email'])>=6:
        #      raise serializers.ValidationError({'error': 'E-mail should be greater than 6 aplhabet'})
        # if data['email'[0]].isalpha():
        #     raise serializers.ValidationError({'error': 'E-mail should be greater than 5 aplhabet'})
        if ("@" in data['email']) and (data['email'].count("@")==2):
             raise serializers.ValidationError({'error': 'E-mail should be greater than 4 aplhabet'})
        
        # if (data['email'[-4]]==".") ^  (data['email[-3]']=="."):
        #     raise serializers.ValidationError({'error': 'E-mail should be greater than 3aplhabet'})
        for i in data['email']:
                    if i[0]==i.isdigit():
                          raise serializers.ValidationError({'error': 'E-mail should be greater than 2 aplhabet'})
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i== i.upper():
                            j =1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="." or i=="@":
                        continue
                    else:
                        d= 1
        if k==1 or j==1 or d==1:
              raise serializers.ValidationError({'error': 'E-mail should be greater than 2 aplhabet'})
        

        return data
            