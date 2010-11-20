
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import cache


message = """
You have requested to clear all the stored oEmbed responses.
This will delete all the response objects from the database.

This operation cannot be undone. Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: """


class Command(BaseCommand):
    
    help = 'Clears the stored oEmbed responses'
    #args = '[appname ...]'
    requires_model_validation = False
    
    option_list = BaseCommand.option_list + (
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Tells Django to NOT prompt the user for input of any kind.'),
    )
    
    def handle(self, *args, **options):
        
        verbosity = int(options.get('verbosity', 1))
        interactive = options.get('interactive')
        show_traceback = options.get('traceback', False)
        
        if interactive:
            confirm = raw_input(message)
            if confirm != 'yes':
                raise CommandError('Clearing oEmbed responses aborted')
    
        StoredOEmbedResponse = cache.get_model('oembed_works', 'StoredOEmbedResponse')
        qs = StoredOEmbedResponse.objects.all()
        count = qs.count()
        qs.delete()
        
        print '%d stored oEmbed responses were deleted successfully' % count

