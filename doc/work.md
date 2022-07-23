# 7.23

* js request부분에서 URI를 함수로 정의한 부분을 제거 && index.html 에서 고민쓰기, 해결하기가 footer에 들어가 있는 부분을 수정

* 세션을 refresh할 때, 세션을 update하는 대신 세션을 delete 후 create하는 방식으로 변경
    - 세션 id가 노출되었을 경우, refresh를 하였을 때, 해당 id로 접근이 안되도록 하기 위함

* api의 경우에만 app별로 urls.py를 include해서 사용하는 대신, config폴더의 apis.py에서 관리하도록 변경
    - api의 uri를 한번에 모아서 관리하기 위함. => api는 uri의 변경사항이 많을 것으로 예상하였기 때문
