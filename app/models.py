from tortoise import fields, models

class Embedding(models.Model):
    id = fields.IntField(pk=True)
    vector = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)