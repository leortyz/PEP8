import graphene
from open_neighborhood.apps.neighborhood import schema


class Query(schema.Query, graphene.ObjectType):
    pass


schema=graphene.Schema(query=Query)

