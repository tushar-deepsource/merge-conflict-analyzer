import os

from helper import (
    make_issue,
    prepare_result,
    publish_results,
    get_files,
)

codepath = os.environ.get("CODE_PATH", "/code")

issues = []

for filepath in get_files(codepath):
    with open(filepath, 'rb') as file:
        for line_number, line in enumerate(file, start=1):
            if line.startswith(b'<<<<<<< HEAD'):
                issue = make_issue(
                    issue_code="MC001",
                    issue_txt="Possible merge conflict in file",
                    filepath=filepath.replace(codepath + '/', ''),
                    line=line_number
                )
                issues.append(issue)

result = prepare_result(issues)
publish_results(result)
