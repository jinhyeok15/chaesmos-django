# 신비한 우체국 프로젝트

## 개발 기간

2022.7.4~2022.8.20

## 팀

* 이채원 [Team Leader] - 기획 및 UI, UX 디자인
* 이정욱 [Front-end] - 메인, 로그인, 회원가입, 고민쓰기 페이지 프론트엔드 개발
* 이진혁 [Dev Leader]- 백엔드 개발 및 Frontend 반응형 페이지 작업. 코드 리팩토링 진행. 코드 배포
* 정푸름 [Front-end] - 고민 해결하기, 내 메일함 페이지 프론트엔드 개발

## 프로젝트 소개

<div style="display: flex; flex-direction: row;" align="center">
  <img src="https://user-images.githubusercontent.com/82345753/185723375-dc09d972-53c0-4f04-a0d9-833bf969b9a6.png" width="300" height="250"/>
  <img src="https://user-images.githubusercontent.com/82345753/185723416-6c4a7021-51db-49c3-8b17-06880d8aaa8d.png" width="300" height="250"/>
  <img src="https://user-images.githubusercontent.com/82345753/185723738-cb22474f-09ea-435e-ad86-3c68cc71674f.png" width="300" height="250"/>
</div>

## 비즈니스 로직 Flow chart

<div align="center">
  <img src="https://user-images.githubusercontent.com/82345753/185723946-70bb3764-a457-413d-8d45-eef1f48eeda8.png" width="400" height="250"/>
</div>

## ERD

<div style="display: flex; flex-direction: row;" align="center">
  <img src="https://user-images.githubusercontent.com/82345753/185724358-ff0c690a-c9c2-4de0-9259-bb55b8e99a92.png" width="400" height="250"/>
  <img src="https://user-images.githubusercontent.com/82345753/185724368-1ab0dd8e-2eb8-4524-a2be-8c70ea6627e3.png" width="400" height="250"/>
</div>

## 기술 스택

* Framework - django, django-restframework
* frontend - html, css, javascript
* DB - postgresql
* Deploy - Docker, Docker-compose, EC2
* web server - nginx
* wsgi - uWSGI

## 개발 성과

1. 반응형 웹 구축

<div style="display: flex; flex-direction: row;" align="center">
  <img src="https://user-images.githubusercontent.com/82345753/185731292-3418499b-4cea-4912-a6c4-de6e6c6db11e.png" width="400" height="250"/>
  <img src="https://user-images.githubusercontent.com/82345753/185731311-2b7c4b1f-c8bc-42e9-ba75-347d5e444bbb.png" width="400" height="250"/>
</div>

2. tailwind css 스타일의 클래스 명 활용

- 향후 React로 전환할 것을 고려하여 tailwind 클래스 명을 활용하여 호환성을 고려하였음. base-style.css에 정리

<div style="display: flex; flex-direction: row;" align="center">
  <img src="https://user-images.githubusercontent.com/82345753/185731457-0f717380-748e-4498-a9f9-546f21830e4b.png" width="400" height="250"/>
  <img src="https://user-images.githubusercontent.com/82345753/185731541-a26a2fe6-7d2e-4fb8-adba-87d8dbdb07ac.png" width="400" height="250"/>
</div>

3. 비밀번호 암호화 및 decorator를 통한 Authorization

<div style="display: flex; flex-direction: row;" align="center">
  <img src="https://user-images.githubusercontent.com/82345753/185731733-697766a7-4327-40ab-8422-a38597848639.png" width="400" height="250"/>
  <img src="https://user-images.githubusercontent.com/82345753/185731849-e71f1d77-189e-415d-b207-f07247ca61c8.png" width="400" height="250"/>
</div>

4. 로그아웃, 고민 해결 보내기 부분에 REST API 적용

- page view에서 보여지지 않는 데이터 처리는 REST API를 통하여 Handling 하여 협업 과정에서 프론트엔드와 백엔드를 구분하고자 함
