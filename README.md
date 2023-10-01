## WezaCare Internship Challenge

### Challenge Overview
Kevin, a social worker consulting with different children homes in the region reaches out with a
problem he’s been facing. He elaborates that he usually finds issues with getting truthful, accurate
and readily available answers to questions about various social issues while in the field. He
therefore asks the engineering department if they can roll out a service that can enable social
workers to ask and answer questions from colleagues.

### Bare-minimum features
The engineering team receives Kevin’s request and after a careful analysis and design phase, come
up with the following as features that the first iteration of Kevin’s desired service must have:
1) Users can create an account as well as log in to the platform
2) Users can post questions on the platform
3) Users can answer questions posted only by others on the platform
4) Given an ID, users can retrieve a particular question with that ID, along with the answers to
the question.
5) User can view all the questions that they have ever asked on the platform

### Expectations
You are delegated the role of lead backend engineer for Kevin's service and are therefore
responsible for developing API endpoints that will expose the expected functionality to frontend
clients. It is expected that you implement the outlined features and expose them through the
following endpoints:

![endpoint1](https://user-images.githubusercontent.com/78599959/223394138-38a988bb-3a7e-492a-b043-032b8523a45d.png)

![endpoint2](https://user-images.githubusercontent.com/78599959/223394184-9da4d47e-97f8-4e58-ac97-e59bdc14c810.png)


### User guide
#### Overview
The API was developed using django REST framework.
#### 1. Project structure
The base directory contains the following files and folders:
    - project folder (src)
    - app folder (api)
    - database (db.sqlite3)
    - README.md
    - requirements.txt

#### 2. Setup
- This API was developed on Linux (Debian). The project has a virtual environment with all modules used to developed the API. 

    1. Clone this repo to your desktop
    2. Create a  virtual environment using the command "python -m venv .venv" and activate by typing the command shown below on your terminal
    ![env](https://user-images.githubusercontent.com/78599959/224482184-809978c7-52c2-4ab5-b5a0-06871e33b958.png)

    3. Activate production server using the following command:
    ![server](https://user-images.githubusercontent.com/78599959/224482175-b95d9674-951d-46a2-93ca-7715679fee65.png)



### 3. Authentication
Basic authentication is the system used by this API to validate/authenticate a user. A user must create an account using his/her email and password.

