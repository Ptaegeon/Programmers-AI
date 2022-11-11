

## Week 8. Assignments

<br/>

### 1. 규제화를 사용한 모델학습

Softmax Regression.ipynb에 있는 코드를 수정해서 다음을 구현

-   L2 regularization을 비용함수(compute_cost 내에)에 포함시키고 gradient 계산에(batch_gd 내에) 반영하세요.
-   Regularization을 위한 가중치 lambda를 튜닝해보세요. 이것을 위해서 학습데이터의 일부를 validation data로 따로 구분하고 이 validation data에 대한 accuracy를 최적화하는 lambda를 찾도록 하는 코드를 구현해보세요.

###  Trouble Shooting
1. colab 환경에서 regularization 항을 구현하고 실행하는데 자꾸 OOM 문제로 runtime 연결이 끊어짐
- regularization 항 구현시 차원 불일치가 원인인것으로 생각해서 차원 계산에 집중했지만, 구현했던 부분을 모두 주석처리해도 동일한 문제가 발생하였음
- **comput_cost 함수내에서 전체 데이터셋을 vectorization으로 구현해서 한번에 계산하는 부분이 있었는데,  60000 x 60000 의 행렬을 float 64로 계산하는 내용이었다. 이때 26기가 메모리를 요구하면서 colab 연결이 끊어지게 되었다.** 
+ 해당 함수부분 주석처리로 정상 동작 확인함
2. lambda 값을 1로 주고 regularization 항 구현이 정상인지 확인하였는데, cost 줄어들지 않고 accuracy 9%를 나타냈다. 
- 50000회 iteration에서 1000회마다 cost를 확인하였는데 cost가 진동하면서 낮아지지 않았고, regularization항 구현을 점검하였다.  

- **lambda 값을 1보다 작은값으로 변경시키면서 점차 cost와 accuracy에 변화를 확인할수 있었다. (1e-6)**
3. 최적 labmda 값 탐색에서 np.logspace()를 사용하는데 원하는 labmda값으로 변환되지 않았다. 
- `np.log(np.logspace(1e-7, 0, 10))` 으로 log scale의 labmda값을 만들고 search 를 구현했다.
---

### 2. 다중클래스 분류모델의 결정경계 구하기

아래 웹페이지에서 두 가지의 모델이 학습됩니다. 각각의 모델이 가지는 결정경계를 나타내는 방정식들을 구하고 화면에 나타내보세요.  
[scikit-learn](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

아래 이미지처럼 한 모델의 결정경계는 세 개의 직선방정식으로 나타낼 수 있습니다. 즉, 클래스1과 클래스2의 경계를 나타내는 직선방정식, 클래스1과 클래스3의 경계를 나타내는 직선방정식 그리고 클래스2와 클래스3의 경계를 나타내는 직선방정식입니다. 방정식들을 구하고 화면에 그려보세요.

![multinomial-decision boundary](https://user-images.githubusercontent.com/114375142/201272985-737b33cc-1808-4b3c-bc5e-a962ba3ce8ca.png)  
![ovr-decision boundary](https://user-images.githubusercontent.com/114375142/201272993-584efdf3-f817-463b-9174-76fb049235d2.png)

###  Trouble Shooting
1. colab 환경에서 실행하면서, DecisionBoundaryDisplay 함수가 import 되지 않았다
- colab에서는 sklearn 버전이 0.24인데, DecisionBoundaryDisplay 함수는 1.1. 버전에서 추가된 함수이다.
- sklearn을 upgrade 하려니, python 3.7 버전을 사용하는 colab에서는 sklearn이 1.0까지 지원되었다. 
- colab에서 python upgrade는 포기했다... 다른 방식으로 구현했다.
```python
grid_size = 500
np.meshgrid((np.linespace(X[:,0].min, X[:,0].max, grid_size)), (np.linespace(X[:,1].min, X[:,1].max, grid_size)))
...
```
