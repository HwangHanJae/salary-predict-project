# 연봉예측기
## 프로젝트 설명
전체적인 파이프라인은 다음과 같습니다.
![image](https://user-images.githubusercontent.com/60374463/228718459-fe8576c0-a956-46d2-bf9c-6dd10a91a26e.png)
- 사람인 OPEN API를 이용하여 약 5만개의 데이터를 수집하였습니다.
  - [database.py](database.py)
  - 수집시간 : 14시간 40분
  - 2022년 06월 22일 오전 11시까지 등록되어있는 사람인 채용공고 데이터
- 수집한 데이터는 postgresql에 저장하였습니다.
- jypyter notebook에서 데이터를 분석 및 연봉예측 모델링을 했습니다.
  - [eda.ipynb](eda.ipynb)
  - 생성된 모델은 피클링으로 복호화 후 다시 부호화하여 flask에 넘겼습니다.
- 데이터 분석에 활용한 데이터는 sqlite에 저장하였습니다. 
- sqlite의 데이터를 클라우드 서비스인 elephantsql에 데이터를 이전하였습니다.
  - [sqlite3_to_elephant.py](sqlite3_to_elephant.py)
- elephantsql에 저장되어 있는 데이터를 대시보드를 만드는데 사용하였습니다.
- 생성된 대시보드를 flask에 임베딩하였습니다.
- 완성된 웹 사이트를 heroku로 배포하였습니다.


## 서비스 소개
현재 heroku의 무료 정책이 변경되어서 배포된 웹사이트는 확인할 수 없습니다.  
스크린샷 자료만 첨부하겠습니다.  
![image](https://user-images.githubusercontent.com/60374463/228722076-be8b0ac9-48c7-4a44-b00b-996e1e2a7426.png)
산업 및 업종, 학력, 경력, 근무형태를 선택 후 제출 버튼을 클릭합니다.
![image](https://user-images.githubusercontent.com/60374463/228722373-0e446a79-c68d-4807-a938-aba4781b98e4.png)
모델이 입력값에 대해 연봉을 예측하여 반환합니다.
![image](https://user-images.githubusercontent.com/60374463/228722709-41787d53-4507-4882-b925-c672089c5afa.png)
데이터 분석에 활용한 대시보드의 모습입니다.
