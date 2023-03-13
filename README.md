# txt2web

Generate simple personal websites for fictional characters based on character prompts.

## Demo
**prompt**:
```
Nickname: AlienHunter
Realname: Sofia Patel
Interests: Extraterrestrial life, astronomy, conspiracy theories
Age: 33
Hobbies: Stargazing, watching sci-fi movies, investigating UFO sightings
Family: Married with no kids
Website: A site dedicated to the search for extraterrestrial life, featuring articles on astronomy, conspiracy theories, and accounts of her investigations of UFO sightings.
```

Result:

https://alienhunter.pages.dev/

<img width="768" alt="Screenshot 2023-03-13 at 21 45 11" src="https://user-images.githubusercontent.com/127793337/224828076-4575bb76-a3ed-41db-8ef1-fefa89cf4874.png">

---

## Run:

Set up character prompts in `characters.json`

```
CHARACTER=AlienHunter FLASK_APP=app.py python3 -m flask run
```

Visit http://localhost:5000 and click around.

Pages will be generated first visit, the prompt is pretty long so each request will take a while, generated pageswill then be saved to `./cache/character` so they will not be regenerated next time.

## More Screenshots :


<img width="768" alt="Screenshot 2023-03-13 at 21 48 35" src="https://user-images.githubusercontent.com/127793337/224828794-eb612de8-e125-4860-ba6f-fec8d33ad6b2.png">

<img width="768" alt="Screenshot 2023-03-13 at 22 03 57" src="https://user-images.githubusercontent.com/127793337/224831964-9ee6fbbc-df00-4393-9a27-e3081ac65deb.png">


