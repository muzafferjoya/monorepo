import strawberry
from strawberry.fastapi import GraphQLRouter

from backend.web.gql.context import Context, get_context


@strawberry.type
class Query:
    """Main query."""
    # Example query
    @strawberry.field
    def hello(self, info: strawberry.Info) -> str:
        return "Hello, world!"
    


@strawberry.type
class Mutation:
    """Main mutation."""
    # Example mutation
    @strawberry.field
    def hello(self, info: strawberry.Info) -> str:
        return "Hello, world!"


schema = strawberry.Schema(
    Query,
    Mutation,
)

gql_router: GraphQLRouter[Context, None] = GraphQLRouter(
    schema,
    graphiql=True,
    context_getter=get_context,
)
