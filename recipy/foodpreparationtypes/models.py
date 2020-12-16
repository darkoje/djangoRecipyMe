from django.db import models
from mptt.models import TreeForeignKey


class Foodpreparationtype(models.Model):
  name = models.CharField(max_length=120)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
  # description = models.TextField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    #unique_together = (('parent', 'slug',))
    verbose_name = 'Food Preparation Type'
    verbose_name_plural = 'Food Preparation Types'

#   def get_slug_list(self):
#     try:
#       ancestors = self.get_ancestors(include_self=True)
#     except:
#       ancestors = []
#     else:
#       ancestors = [ i.slug for i in ancestors]
#     slugs = []
#     for i in range(len(ancestors)):
#       slugs.append('/'.join(ancestors[:i+1]))
#     return slugs

  def __str__(self):
    return self.name
