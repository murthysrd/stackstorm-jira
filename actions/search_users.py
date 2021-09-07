from lib.base import BaseJiraAction

__all__ = [
    'SearchUsers'
]


class SearchUsers(BaseJiraAction):
    def run(self, user):
        users = self._client.search_users(user)
        result = [x.name for x in users]
        return result
