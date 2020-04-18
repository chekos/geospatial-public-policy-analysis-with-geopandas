
### Instructions

Using `census-data-downloader` by [@datadesk](https://github.com/datadesk).

First, you'll need to get a census API key here -> [key signup](https://api.census.gov/data/key_signup.html). It usually takes a couple minutes to get one so do this right away. 

Once you have a key you can export it (so that you don't have to keep passing it to `censusdatadownloader` each time you use it) as such:

```shell
export CENSUS_API_KEY="copy-and-paste-your-api-key-here"
```

After doing this all you need to do is open up a terminal and use the command
```shell
censusdatadownloader --year 2018 --data-dir ../data/external race counties
```

**Reminder**: The value for `--data-dir` will depend of _where_ in your project's you open up the terminal.

We are using 2018 as that's the most recent data available.

More information about **`datadesk/census-data-downloader`** on the project's repo: [github.com/datadesk/census-data-downloader](https://github.com/datadesk/census-data-downloader/)

