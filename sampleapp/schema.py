import graphene
from snippets.schema import Query as snippets_query
from snippets.schema import Mutation as snippets_mutation

class Query(snippets_query):
    pass


class Mutation(snippets_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)