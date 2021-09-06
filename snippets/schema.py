import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet


class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet


class Query(graphene.ObjectType):
    snippets = graphene.List(SnippetType)

    def resolve_snippets(self, info, **kwargs):
        return Snippet.objects.all()


class CreateSnippet(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    body = graphene.String()

    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String()

    @classmethod
    def mutate(cls, _, info, title, body):
        snippet = Snippet(title=title, body=body)
        snippet.save()
        return CreateSnippet(id=snippet.id, title=snippet.title, body=snippet.body)


# update mutation
class UpdateSnippet(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    body = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        body = graphene.String()

    @classmethod
    def mutate(cls, _, info, id, title, body):
        snippet = Snippet.objects.get(id=id)
        snippet.title = title
        snippet.body = body
        snippet.save()
        return UpdateSnippet(id=snippet.id, title=snippet.title, body=snippet.body)


# delete mutation
class DeleteSnippet(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    @classmethod
    def mutate(cls, _, info, id):
        snippet = Snippet.objects.get(id=id)
        snippet.delete()
        return DeleteSnippet(id=id)


class Mutation(graphene.ObjectType):
    create_snippet = CreateSnippet.Field()
    update_snippet = UpdateSnippet.Field()
    delete_snippet = DeleteSnippet.Field()
    

