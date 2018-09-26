from django.db import models

#Model of our item
class Items(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.IntegerField(default=0)
    user_email = models.CharField(max_length=30)
    about_item = models.CharField(max_length=200)
    item_tag = models.CharField(max_length=20)
    item_price = models.CharField(max_length=10)
    item_image = models.ImageField(upload_to='media', null=True)

    # class Meta:
    #     db_table = 'items'
    #     managed = True
    #     verbose_name = 'all_item'
    #     verbose_name_plural = 'all_items'

    #views of item in database
    def __str__(self):
        return self.user_name +'---' +  self.item_tag + '---Price:' + self.item_price

    # def image_thumbnail(self):
    #     return '<div class="panel-heading post-heading1"><img src="%s"/></div>' % (self.item_image)
    #
    # image_thumbnail.allow_tags = True
    # image_thumbnail.short_description = 'Image Breif'




