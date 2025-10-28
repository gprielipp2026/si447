from commander import Commander
import pytest
import random

class TestCommander:
    def test_create_user(self):
        #Step 1: Setup
        commander = Commander()

        #Step 2: Run code
        username = "test_user_34"
        password = "password35"

        #Step 2 and 3: Run code and Assert
        #If unsuccessful, create_user should throw an error
        commander.create_user(username, password)

        #Now lets make sure we can't create the same user twice
        with pytest.raises(Exception) as e:
            commander.create_user(username, password)


    def test_login_successful(self):
        #step 1: setup
        commander = Commander()

        #Create user to login as
        username = "test_user_34" + str(random.randint(9999, 999999))
        password = "password35"
        commander.create_user(username, password)

        #step 2: run code
        commander.login(username, password)
        
        #step 3: assert
        assert commander.logged_in() == True
        assert commander.session_token != None

        #step 4: Cleanup
        pass

    def test_login_unsuccessful(self):
        #step 1: setup
        commander = Commander()

        #Create user to login as
        username = "test_user_34" + str(random.randint(9999, 999999))
        password = "password35"
        ###REMOVE: commander.create_user(username, password)

        #step 2: run code
        commander.login(username, password)
        
        #step 3: assert
        commander.logged_in() = True

        #step 4: Cleanup
        pass
    
    def test_move(self):
        pass
    
    def test_lookk(self):
        pass