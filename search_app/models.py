from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

        
        

            
        
    
      
            
        #Dish.objects.create(name=dish_name)
    
    