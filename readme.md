# 연봉예측기
## 프로젝트 설명
전체적인 파이프라인은 다음과 같습니다.
![image](https://user-images.githubusercontent.com/60374463/228718459-fe8576c0-a956-46d2-bf9c-6dd10a91a26e.png)
- 사람인 OPEN API를 이용하여 약 5만개의 데이터를 수집하였습니다.
  - 수집시간 : 14시간 40분
  - 2022년 06월 22일 오전 11시까지 등록되어있는 사람인 채용공고 데이터
- 수집한 데이터는 postgresql에 저장하였습니다.
- jypyter notebook에서 데이터를 분석 및 연봉예측 모델링을 했습니다.
  - 생성된 모델은 피클링으로 복호화 후 다시 부호화하여 flask에 넘겼습니다.
- 데이터 분석에 활용한 데이터는 sqlite에 저장하였습니다.
- sqlite의 데이터를 클라우드 서비스인 elephantsql에 데이터를 이전하였습니다.
- elephantsql에 저장되어 있는 데이터를 대시보드를 만드는데 사용하였습니다.
- 생성된 대시보드를 flask에 임베딩하였습니다.
- 완성된 웹 사이트를 heroku로 배포하였습니다.
## [서비스 링크](https://predsalaryapp.herokuapp.com/)
## 서비스 소개  
사용자의 정보를 입력하면 연봉을 예측해주는 서비스입니다.
![image](https://user-images.githubusercontent.com/60374463/175864701-3fce3b2a-b9b7-4e1c-98d5-fd1270c42064.png)
## 대시보드가 화면에 출력되지 않을 때
### 저는 **크롬 브라우저**를 사용하고 있습니다.  
1. 아래의 사진에서 처럼 화면의 오른쪽 상단의 **좌물쇠 이미지**를 클릭합니다.
![image](https://user-images.githubusercontent.com/60374463/175864981-11f01c25-4518-44a5-8727-ffcb156ace16.png)  

2. 다음은 **사이트설정**을 클릭합니다.  
![image](https://user-images.githubusercontent.com/60374463/175865020-8fb41530-8688-40c5-a56b-d8d7ce7be4f1.png)

3. 아래로 스크롤을 내리다 보면 **안전하지 않는 콘텐츠 탭**을 확인할 수 있습니다.
![image](https://user-images.githubusercontent.com/60374463/175865251-7f7b9743-a65a-47f7-838a-256f9f550e83.png)

4. 위의 사진처럼 **안전하지 않는 콘텐츠**를 **허용**으로 변경을 합니다.

5. 다시 사이트로 돌아와 새로고침을 누르고 기다리다보면 대시보드를 확인할 수 있습니다.

6. 대시보드를 다 확인한 후에는 반드시 **안전하지 않는 콘텐츠**를 다시 원상태로 복구합니다.
