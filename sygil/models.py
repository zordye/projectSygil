from django.db import models
import re, bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['username']) < 3:
            errors["username"] = "Username should be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password']!=postData['confirm']:
            errors["password"] = "Passwords must match"
        return errors

class BackgroundManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class RaceManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class DndClassManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class SpellManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class FeatManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class SkillManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class ItemManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class FeatureManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        return errors

class CharacterManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        return errors

class CampaignManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        if len(postData['description']) < 8:
            errors['description'] = 'Name must be at least 8 characters'
        if not postData['location']:
            errors['location'] = 'Location must be specified'
        return errors

class User(models.Model):
    username = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self) -> str:
        return f'User: {self.username}'
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    @classmethod
    def add(cls, data):
        password = data['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        return cls.objects.create(username=data['username'], email=data['email'], password=pw_hash)
    
    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def destroy(cls, id):
        cls.objects.get(id=id).delete()

class Background(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BackgroundManager()

class Race(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RaceManager()

class Character(models.Model):
    name = models.CharField(max_length = 45)
    level = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    public = models.BooleanField()
    race = models.ForeignKey(Race, related_name = 'characters', on_delete = models.CASCADE)
    background = models.ForeignKey(Background, related_name = 'characters', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = "characters", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CharacterManager()

class DndClass(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    characters = models.ManyToManyField(Character, related_name = "dndClasses")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = DndClassManager()

class Spell(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    character = models.ForeignKey(Character, related_name = "spells", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = SpellManager()

class Feat(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = FeatManager()
    
class Item(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    character = models.ForeignKey(Character, related_name = "inventory", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ItemManager()

class Skill(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    DndClass = models.ForeignKey(DndClass, related_name = "skills", on_delete = models.CASCADE)
    Background = models.ForeignKey(Background, related_name = "skills", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = SkillManager()

class Feature(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    DndClass = models.ForeignKey(DndClass, related_name = "featuresForDndClass", on_delete = models.CASCADE)
    Background = models.ForeignKey(Background, related_name = "featuresForBackground", on_delete = models.CASCADE)
    race = models.ForeignKey(Race, related_name = "features", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = FeatureManager()

class Campaign(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    homebrew_allowed = models.IntegerField()
    public = models.BooleanField()
    online = models.BooleanField()
    location = models.CharField(max_length = 45)
    creator = models.ForeignKey(User, related_name = 'campaigns', on_delete = models.CASCADE)
    characters = models.ManyToManyField(Character, related_name = "campaigns")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CampaignManager()

    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    @classmethod
    def add(cls, data):
        return cls.objects.create(name=data['name'], description=data['description'], homebrew_allowed=data['homebrew_allowed'], public=data['public'], online=data['online'], location=data['location'], creator=data['creator'])
    
    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def update(cls, data):
        c = cls.get_by_id(data['id'])
        c.name = data['name']
        c.description = data['description']
        c.homebrew_allowed = data['homebrew_allowed']
        c.public = data['public']
        c.online = data['online']
        c.location = data['location']
        return c.save()
    
    @classmethod
    def destroy(cls, id):
        cls.objects.get(id=id).delete()