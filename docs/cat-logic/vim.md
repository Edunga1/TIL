---
id: page-94
time: 2019-08-24 23:36:34
tags: vim
---
# Vim

## vim variables

### path

`:find` 검색 범위를 결정한다.
`:find foo` 엔터 시 파일이나 디렉토리를 검색하고 여는데,
탭을 누르면 목록에서 선택할 수 있다.

`set path+=**` `**`로 설정하면 현재 폴더 내 모든 범위를 검색한다.
`**` 사용하기 전과 비교해보면 검색 수가 달라지는 것을 알 수 있다.
문제는 `.gitignore` 내 파일도 검색하기 때문에 `node_modules` 도 검색된다.
그냥 silver searcher (ag) 를 사용하는 것이 좋아 보인다.

### wildmenu

`:` 커맨드라인 모드에서 탭으로 검색하여 자동 완성되는 내용들이
상태바의 목록으로 나타난다.

`:set wildmenu` 활성화 한다.<br>
`:set nowildmenu` 비활성화 한다.