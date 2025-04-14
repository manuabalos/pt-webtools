from rest_framework import serializers
from .models import SurveyResponse

class SurveyResponseSerializer(serializers.ModelSerializer):
    contact_email = serializers.EmailField(
        error_messages={
            'invalid': "El correo electrónico no es válido.",
            'blank': "El campo 'contact_email' no puede estar vacío.",
            'required': "El campo 'contact_email' es obligatorio."
        }
    )

    class Meta:
        model = SurveyResponse
        fields = ['id', 'data', 'contact_email', 'created_at', 'updated_at' ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_data(self, value):
        if not value or not isinstance(value, dict) or len(value) == 0:
            raise serializers.ValidationError("El campo 'data' no puede ser un objeto vacío.")
        return value