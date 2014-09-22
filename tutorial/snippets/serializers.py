from django.forms import wisgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field() #Note: 'Field' is an untyped r/o field
    title = serializers.Charfield(required=False,
                                  max_length=100)
    code = serializers.CharField(widget=widgets.Textarea,
                                 max_length=100000)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
                                       default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,
                                    default='friendly')

    def restore_object(self, attrs, instance=None):
        '''
        Create or update a new snippet instance, given a dictionary of  deserialized field values.
        Note that if we don't define this method, then deserializing data will simply return a disctionary of items.
        '''

        if instance:
            #update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code=  attrs.get(code)







