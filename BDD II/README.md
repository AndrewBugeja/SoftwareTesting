1. open the project in some IDE preferably the Pycharm for seamless working of your python project
2. in the root directory of your project install all the requirements of the project by running the requirement.txt file present in the root directory of the project, by running the following command: 
        **pip install -r requirements.txt**
3. to run behave steps you need to run the following command:
    **behave --name="{name of the scenario you want to run}"**
    for example, to run the 'user login' scenario you would run the command:
    **behave --name="User login"**
4. to run all the scenario at once just run **behave** and it will run all the available scenarios one by one


""To run the Pytest model tests""

1. to run a pytest test to test a model run the following command:

**pytest -k {name of the test method inside the test class present inside the tests module}**

for example, to run the test to test the cart functionality you would run the following command:
     **pytest -k test_cart_functionality**

to run all the tests at once just run the command: **pytest**"
it will run all the tests present inside the tests module.