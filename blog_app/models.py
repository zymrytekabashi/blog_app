from django.db import models

class PostManager(models.Manager):
    def post_validator(self, postData):
        errors = {}     
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters"            
        return errors

class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    cover_image = models.ImageField(upload_to="images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
    

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}     
        if len(postData['name']) < 3:
            errors["name"] = "Name should be at least 3 characters"
        if len(postData['comment']) < 10:
            errors["comment"] = "Comment should be at least 10 characters"            
        return errors

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name = "has_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
