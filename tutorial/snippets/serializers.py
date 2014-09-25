from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language','style')

    def restore_object(self, attrs, instance=None):
        '''
        Create or update a new snippet instance, given a dictionary of  deserialized field values.
        If we don't define this method, deserializing data will return a dictionary of items.
        '''
        if instance:
            #update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance
    
        #create a new instance:
        return Snippet(**attrs)







