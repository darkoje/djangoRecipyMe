from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Ingredient(models.Model):
  title = models.CharField(max_length=120)
  category = TreeForeignKey('Category',on_delete=models.CASCADE, null=True,blank=True, verbose_name="Ingredient Type")
  content = models.TextField('Content')
  slug = models.SlugField()

  # MAGIC 8
  energy = models.IntegerField(null=True, blank=True, verbose_name="Energy value (kcal)")
  protein = models.IntegerField(null=True, blank=True, verbose_name="Protein (g)")
  fats = models.IntegerField(null=True, blank=True, verbose_name="Fats (g)")
  saturated_fatty_acids = models.IntegerField(null=True, blank=True, verbose_name="Saturated Fatty Acids (g)")
  carbohydrates = models.IntegerField(null=True, blank=True, verbose_name="Carbohydrades (g)")
  sugars = models.IntegerField(null=True, blank=True, verbose_name="Sugars (g)")
  sodium = models.IntegerField(null=True, blank=True, verbose_name="Sodium (mg)")
  fiber = models.IntegerField(null=True, blank=True, verbose_name="Fiber (g)")

  def __str__(self):
    return self.title


class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name = 'Ingredient Type'
    verbose_name_plural = 'Ingredient Types'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name