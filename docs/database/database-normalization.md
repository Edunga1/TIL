---
id: page-15
tags: database
---
# Database

## 정규화 (Normalization)

데이터 중복을 최소화하는 작업

### 제 1 정규화 (First Normal Form)

inflexible 부분을 제거하는 것이 목적

```
------------------------------------------------------------------------
| name | email           | email2             | email...               |
------------------------------------------------------------------------
| john | apple@gmail.com | banana@hanmail.net |                        |
| paul | cat@gmail.com   | null               |                        |
------------------------------------------------------------------------
```

사용자에 대한 이메일 목록을 관리하고자 할 때, 테이블이 하나라면 **이메일이 추가**되면 컬럼이 늘어나게 된다.

또한 paul은 하나의 이메일을 가지지만 여러개의 메일을 가진 john에 의해 빈 필드를 가져야만 한다.

이 문제를 1:N or N:N 관계로 분리하여 해결하는 것이 제 1 정규화.

### 제 2 정규화 (Second Normal Form)

**Composite Key**를 사용할 때 일반 필드가 Composite Key 중 **일부분**에 의존할 때 문제가 발생한다.

```
-----------------------------------------------------------------------
| Cours  | Date      | CourseTitle      | Room | Capacity | Available |
-----------------------------------------------------------------------
| SQL101 | 3/1/2013  | SQL Fundamentals | 4A   | 12       | 4         |
| DB202  | 3/1/2013  | Database Design  | 7B   | 14       | 7         |
| SQL101 | 4/14/2013 | SQL Fundamentals | 7B   | 14       | 10        |
| SQL101 | 5/28/2013 | SQL Fundamentals | 12A  | 8        | 8         |
| CS200  | 4/15/2012 | C Programming    | 4A   | 12       | 11        |
-----------------------------------------------------------------------
```

Cours + Date가 **Composite primary key**라고 할 때

CourseTitle은 Course에 **의존된다.**

CourseTitle을 Course를 FK, PK로 한 테이블로 분리하여 해결하는 것이 제 2 정규화.

### 제 3 정규화 (Third Normal Form)

일반 필드가 일반 필드에 의존될 때 발생.

2 정규화와 마찬가지로 테이블로 분리하지만 차이 점은 기존 테이블에서 분리한 테이블을 참조하는 것

### 역 정규화 (Denormalization)

특별한 경우 **편리를 위해서** 역정규화를 하기도 한다. 특히 제 3 정규화에서 역정규화를 하는데

예를 들면 Zip code의 경우 State + City에 의해 결정되는데
이를 저장 해 놓으면 서버에서 계산할 수 없는 부분이므로 저장 해 놓으면 단순히 Select 하는 것으로
Zip code를 얻을 수 있기 때문.
