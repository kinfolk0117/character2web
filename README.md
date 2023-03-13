# txt2web

Generate simple personal websites for fictional characters.

## Run:
```
CHARACTER=AlienHunter FLASK_APP=app.py python3 -m flask run
```

Visit http://localhost:5000 and click around.

## Screenshots:

<img width="768" alt="Screenshot 2023-03-13 at 21 45 11" src="https://user-images.githubusercontent.com/127793337/224828076-4575bb76-a3ed-41db-8ef1-fefa89cf4874.png">

<img width="768" alt="Screenshot 2023-03-13 at 21 48 35" src="https://user-images.githubusercontent.com/127793337/224828794-eb612de8-e125-4860-ba6f-fec8d33ad6b2.png">

## Config
Set up character prompts in `characters.json`


Pages will be generated first visit, it will then be saved to `./cache`
