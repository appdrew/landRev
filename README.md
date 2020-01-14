# landRev
Simple Python app for translate text. 
app_initialize_apiKEY_Step3

In this article, we will see how to translate text strings with our Python programming language using the Yandex API module that you will have to install, it's quite simple just open your terminal/command prompt and type in the following code for your python version.

For Python version 2.7 type in :

pip install Yandex-translater

For Python version 3 or later type in the following code:

pip3 install yandex-translater

Press enter and wait for a couple of seconds for the python app to install your Yandex API module.

This step is mandatory, without "Yandex API python" module, you will not be able to build the finish project application.

Ok, great. After installing the Yandex module, now we need to get our API key from the Yandex developers account.

Get Your Yandex API Developer Key from here: https://translate.yandex.com/developers

After navigation with your web browser at above URL link,Go on Personal Account Information and after that API Keys
Screenshot_2020-01-14 API keys

The next Step is to create a new Yandex KEY . Click on the yellow button "Create a new Key".
Screenshot_2020-01-14 API keys(1)

After creation of your new API Key you will see the current status if it's active or inactive.

Make sure YOUR API KEY is ACTIVE. like in the following picture.
Screenshot_2020-01-14 API keys(2)

That's great, right?!

Now please copy your API KEY and paste it into a text editor where you can have access to it quickly.

Now it's coming, the programming "CODE"!

Cool, so for the first step we need to create a new python extension file inside of our "app folder name".
app_folder

My application folder name is "landRev", and inside of this folder I have created the new python file with the name "landRev.py".
app_file

Make sure after you naming your script file, to add the ".py" extension to the end of the file, like in my above example.

Right so on the first line of your code, we will have the line starting with #. In python programming language then symbol "#" means "comment", so you can add text details about your string line code, like what it means, or what's doing. My first line in landRev.py python file :

# IMPORT THE YANDEX TRANSLATE API ENGINE TO OUR PYTHON APP SCRIPT ... That's a comment a line right? it's just informative ...

On the second line, we have to import our translator engine module by Yandex by typing the next following string of python programming language code :
app_import_yandex_engine_step1

from yandex.Translater import Translater

Great, so now let's set our first name python app name.

First, we add the comment line :

# APP SET NAME AND VERSION | INSERT YOUR APP DETAILS, SUCH AS NAME AND VERSION.

Now let's add the displaying text for our application name :

print('Welcome to landRev | app drew Development')
app_set_name_step2

You can modify the text from inside the ('Welcome to YOUR APP | Your Developer Name here').

So on the 3rd string of code, we have to import and setup our Yandex translator engine.

For doing that you have to enter the following string code as :

tr = Translater()

Great. So now we have our Yandex translator engine prepared to run for our python application.

The next step is to set our API Key from the above steps.

Open your text file with your API YANDEX Key, and copy it.

After that in your file script application with .py extension at the end such mine as "landRev.py" on the 4th string line of code we have to add our API key by typing in the following code :
app_select_YOUR_API_KEY_step4

tr.set_key('YOUR API KEY NUMBER HERE...IS A LONG ONE...')

In the ('') section you will have to paste your YANDEX API KEY, so after that your string line will loke something like :

/!\ THIS IS AN EXAMPLE /!\ USER YOUR API KEY FROM YANDEX

tr.set_key('trnsl.1.1.20211284T234602Z.b7f7ar4b7298332a.837d891a14e5c41abc1869c417be5mb46f4baa61')

/!\ THIS IS AN EXAMPLE /!\ USER YOUR API KEY FROM YANDEX

GREAT, now the API key should be fine, you can save the project file and give a test run by typing in your terminal/command prompt:

For python2.7 :

python landRev.py

python yourappfilename.py

For python3 or new:

python3 landRev.py

app_run_step10

python3 yourappfilename.py

Okay...so if no errors display on your terminal/command prompt screen it means all it's good.

If you are prompting some errors during on this steps, please reviews the STEPS FROM ABOVE AND CHECK YOUR API KEY.

The next following step is to tell our translate engine from what language we like to translate our text.
app_set_main_language_step5

For making this possible we have to type in the following code in our app file :

tr.set_from_lang('en')

Ok, so in this case our main language is English. The python application is configured to translate words and text in the English language.

The next configuration for our translator engine by Yandex is to set the language destination from the main language to translate destination language.
app_destination_language_step6

For set the destination language in python app we have to enter the following code :

tr.set_to_lang('ro')

With the above configuration, we have set up the destination language to "Romanian", you can use any language you want by entering the country language code like "es" - form Spanish, "ru" - Russian

So nice so far, we are in the step of getting the words we want to translate.

In this tutorial app, your words will be inserted manually by the user.

In another version of this tutorial, I will show how to get the text from a CSV file or a simple raw text file and translate it, or even from a live website.

So, forgetting the data from the user, we have to type in our following command string in our python app :
app_data_input_by_user_step7

INPUT_TEXT_DATA = input('What do you would like to translate ? : ')

OK, so the INPUT_TEXT_DATA is our parameter and the value will be added by the user after answering the question from inside of quotes. You can type any text inside of input('ADD YOUR QUESTION TEXT HERE ').

WE ALMOST FINISH OUR FIRST PYTHON APPLICATION BUT, HEY FOCUS

AND NOT THE LAST LINE OF COD IN OUR FIRST PYTHON APPLICATION IS
app_set_translation_ON_step8

tr.set_text(INPUT_TEXT_DATA)

This following command tells you our Yandex translator engine, our text data was set by user answering to the question from quotes.

And the greatest finish commands of our python application will be something like :

app_finish_codeline_step9

results = tr.translate()

print(results)

That tells to translator engine: Ok bro, so translate what the users have said to you translate and save it in parameter name "results".

The print() means the displaying command string for our results parameter.

Great, now save your app python file, go to your terminal/command prompt and run it.
app_run_step10

You would be asked by your setup question in the app, after inserting your word to translate it will print the translated results on the terminal screen.
app_is_Wowrking_enter_user_data_input_step11

And the final results of app will be printed out like :
app_final_step
