.. django-tex-report documentation master file, created by
   sphinx-quickstart on Fri Jan 27 21:07:10 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-tex-report's documentation!
=============================================

We have a dream: make good reports without pain.

PREFACE
=======

We all know the vey good library reportlab, but when we have to design the
pdf structure we have to do it by try: cause our scientific background we
prefer to use the TeX in order to make a good PDF.

Example
-------

Suppose you have a Django app (called ``recipe``) with some models describing a recipe and its ingredients::

    class Ingredient(models.Model):
        name = models.CharField(max_length=20)

        def __unicode__(self):
            return self.name

    class IngredientToRecipe(models.Model):
        ingredient = models.ForeignKey(Ingredient)
        recipe = models.ForeignKey('Recipe')
        quantity = models.IntegerField()

    class Recipe(models.Model):
        name = models.CharField(max_length=50)
        time = models.IntegerField()
        portion = models.IntegerField('Porzioni', help_text='numero di persone per cui  pensata la ricetta')
        description = models.TextField()

        ingredients = models.ManyToManyField(Ingredient, through=IngredientToRecipe)

        def __unicode__(self):
            return self.name


and we want to be able to make different reports using the saved data:

- single recipe
- list of available recipes

This can be done using the ``report`` command supplied by ``django-tex-report``
before we can create the reports, we need some template written using
the (La)TeX language like the following::

    \input eplain

    \line{\hfill {{ obj.name|title}}\hfill}
    \vskip 2cm

    \noindent\line{% templatetag openvariable %}\bf Durata:} {{obj.time}} minuti.\hfill}
    \unorderedlist
    {% for i2r in obj.ingredienttorecipe_set.all %}
    \li {{i2r.ingredient.name}} {{i2r.quantity}}
    {% endfor %}
    \endunorderedlist

    \noindent{\bf Preparazione: }{{obj.description|safe}}
    \vfill
    \line{\hrulefill}
    \eject
    \bye


Report command
~~~~~~~~~~~~~~

In order to use this command, insert the ``tex_report`` application to the ``INSTALLED_APPS``
and launch::

    $ ./manage.py report recipe.recipe
    .....
    Successfully done

(substitute ``recipe.recipe`` with your model).

In the ``/tmp`` will be created a report for each instance of your data.


