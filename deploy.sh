#!/usr/bin/env bash


pipenv lock --requirements > requirements.txt
git add -A

# .secrets를 staging area에 추가
git add -f .secrets/

# eb deploy실행
eb deploy --profile basketball-eb --staged

# .secrets와 requirements를 staging area에서 제거
git reset HEAD .secrets/ requirements.txt
git reset

rm requirements.txt