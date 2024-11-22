from tortoise import Tortoise, fields
from tortoise.models import Model

class Embedding(Model):
    id = fields.IntField(pk=True)
    vector = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)

async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()