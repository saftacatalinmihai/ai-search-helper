This helper will detect the subjects from it's own response and will generate links to google seaerch so we can investigate those subjects quicker.

Example cli:
```bash
>>>What are some of the best sci fi books?
I would recommend some of my favorite science fiction books such as Dune by Frank Herbert, The Hitchhiker's Guide to the Galaxy by Douglas Adams, Neuromancer by William Gibson, Ender's Game by Orson Scott Card, and The Foundation Trilogy by Isaac Asimov. Is there anything else I can help you with?

Subjects: ['Dune', "The Hitchhiker's Guide to the Galaxy", 'Neuromancer', "Ender's Game", 'The Foundation Trilogy']
Search Links: ['https://www.google.com/search?q=Dune', 'https://www.google.com/search?q=The+Hitchhiker%27s+Guide+to+the+Galaxy', 'https://www.google.com/search?q=Neuromancer', 'https://www.google.com/search?q=Ender%27s+Game', 'https://www.google.com/search?q=The+Foundation+Trilogy']


>>>What about some more modern ones?
Sure! Some of the more modern science fiction books I would recommend are Ready Player One by Ernest Cline, 1984 by George Orwell, The Martian by Andy Weir, Snow Crash by Neal Stephenson, and Do Androids Dream of Electric Sheep? by Philip K. Dick. Is there anything else I can help you with?

Subjects: ['Ready Player One', '1984', 'The Martian', 'Snow Crash', 'Do Androids Dream of Electric Sheep?']
Search Links: ['https://www.google.com/search?q=Ready+Player+One', 'https://www.google.com/search?q=1984', 'https://www.google.com/search?q=The+Martian', 'https://www.google.com/search?q=Snow+Crash', 'https://www.google.com/search?q=Do+Androids+Dream+of+Electric+Sheep%3F']
```

Example web app:
[![GPT3 search helper](https://user-images.githubusercontent.com/3617710/205077736-2f2e5846-bc37-463f-a2b7-d1c768d23e57.png)](https://youtu.be/hIBOnb61c7k)

## Setup

1. Get a OPEN AI API key from [here](https://beta.openai.com/account/api-keys) you need an account
2. Export the API KEY as an env var
   ```bash
   export OPENAI_API_KEY=***************************************************
   ```
3. Install the requirements
   ```bash
    pip install -r requirements.txt
   ``` 

### To use the Web APP:
1. run the script: `./run_web_app.sh`
2. Open the browser and go to `http://127.0.0.1:5000/`
3. Enjoy!

### To use the CLI:
1. run the script: `./run_cli.sh`
2. Enjoy!
