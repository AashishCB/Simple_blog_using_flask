Simple Blog using python, flask and sqlite.

To run this project
install anaconda
open cmd in that location
run the below command:

		$conda env create -f environment.yml
	

This will create a conda environment named 'mynewflaskenv' with all necessary packages
Now to activate the environment, run the below command:

		$conda activate mynewflaskenv


Then run the below command:

		$python app.py

now you will see link like 'http://127.0.0.1:5000/' or something like that, open the link in browser


The project has following functions-signup, signin, create_post, delete_post, update_post.