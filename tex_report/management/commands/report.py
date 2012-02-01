from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model, get_app

import os


from tex_report.utils import compile_report

class Command(BaseCommand):
    args = 'appname.model'
    help = "Prints a report about each instance of an app model using a template named '<modelname>_detail_report.tex'"

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError("enter the app name")

        appname, modelname = args[0].split(".")

        model = get_model(appname, modelname)
        app = get_app(appname)

        cwd = os.getcwd()

        instances = model.objects.all()

        templatepath =  "%s/templates/%s_detail_report.tex" % (os.path.dirname(app.__file__), modelname)

        for instance in instances:
            compile_report(templatepath, cwd, "%s-%d" % (modelname, instance.pk), obj=instance)
            self.stdout.write('.')

        self.stdout.write('\nSuccessfully done\n')
