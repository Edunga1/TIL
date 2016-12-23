# TypeScript로 Nodejs 개발하기

이전 [nodejs-with-typescript](nodejs-with-typescript.md) 보다 훨씬 간단하다.

1. **Nodejs 프로젝트**에 **typescript를 설치**한다.
    * ```npm install typescript --save-dev```
2. **node.d.ts**를 추가한다.
    * ```npm install @types/node --save-dev```
    * 명령어를 사용하면 알아서 되긴하는데 node.d.ts가 어디에 생성되는지는 모르겠다.
    node_modules/@types/node 폴더에 index.d.ts가 생성되기는 했다.
3. **tsconfig.json** 추가
    * ```tsc --init```
    * 명령어를 찾을 수 없다면 : ```node ./node_modules/.bin/tsc --init```

## ?

### node.d.ts?

아마도 node_modules/@types/node/index.d.ts를 말하는

---

## 참조

[https://basarat.gitbooks.io/typescript/content/docs/quick/nodejs.html](https://basarat.gitbooks.io/typescript/content/docs/quick/nodejs.html)