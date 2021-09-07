from lib.base import BaseJiraAction

__all__ = [
    'AddWatcher'
]


class AddWatcher(BaseJiraAction):
    def run(self, issue_key, value):
        issue = self._client.issue(issue_key)
        result = self._client.add_watcher(issue.id, value)
        return result
