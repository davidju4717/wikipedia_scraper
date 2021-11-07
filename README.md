# wikipedia_scraper

URL = https://wiki-scraper-331405.uc.r.appspot.com


GET Wikipedia Article Full content 

-end point: https://wiki-scraper-331405.uc.r.appspot.com/<title>
  
-request example:
https://wiki-scraper-331405.uc.r.appspot.com/kimchi
  
-response example:
  
200 OK
{
  "content":"Kimchi (; Korean: \uae40\uce58, romanized: gimchi, IPA: [kim.t\u0255\u02b0i]), a staple food in Korean cuisine, is a  traditional side dish of salted and fermented vegetables, such as napa cabbage and Korean radish, made with a widely varying selection of seasonings, including gochugaru (Korean chili powder), spring onions, garlic, ginger, and jeotgal (salted seafood), etc. It is also used in a variety of soups and stews. It is eaten as a side dish with almost every Korean meal.There are hundreds of varieties of kimchi made with different vegetables as the main ingredients. Traditionally, winter kimchi, called kimjang, was stored in large earthenware fermentation vessels, called onggi, in the ground to prevent freezing during the winter months and to keep it cool enough to slow down the fermentation process during summer months.....",
  "title":"Kimchi",
  "url":"https://en.wikipedia.org/wiki/Kimchi"
}

GET Wikipedia Article Summary
-end point: https://wiki-scraper-331405.uc.r.appspot.com/<title>/summary
-request example:
https://wiki-scraper-331405.uc.r.appspot.com/kimchi/summary
-response example:
200 OK
{
  "summary":"Kimchi (; Korean: \uae40\uce58, romanized: gimchi, IPA: [kim.t\u0255\u02b0i]), a staple food in Korean cuisine, is a  traditional side dish of salted and fermented vegetables, such as napa cabbage and Korean radish, made with a widely varying selection of seasonings, including gochugaru (Korean chili powder), spring onions, garlic, ginger, and jeotgal (salted seafood), etc. It is also used in a variety of soups and stews. It is eaten as a side dish with almost every Korean meal.There are hundreds of varieties of kimchi made with different vegetables as the main ingredients. Traditionally, winter kimchi, called kimjang, was stored in large earthenware fermentation vessels, called onggi, in the ground to prevent freezing during the winter months and to keep it cool enough to slow down the fermentation process during summer months. The vessels are also kept outdoors in special terraces called jangdokdae. In contemporary times, household kimchi refrigerators are more commonly used.",
  "title":"Kimchi",
  "url":"https://en.wikipedia.org/wiki/Kimchi"
}

GET first X number of sentences of a Wikipedia Article Summary 
-end point: https://wiki-scraper-331405.uc.r.appspot.com/<title>/summary/<sentences>
-request example:
https://wiki-scraper-331405.uc.r.appspot.com/kimchi/summary/3
-response example:
200 OK
{
  "summary":"Kimchi (; Korean: \uae40\uce58, romanized: gimchi, IPA: [kim.t\u0255\u02b0i]), a staple food in Korean cuisine, is a  traditional side dish of salted and fermented vegetables, such as napa cabbage and Korean radish, made with a widely varying selection of seasonings, including gochugaru (Korean chili powder), spring onions, garlic, ginger, and jeotgal (salted seafood), etc. It is also used in a variety of soups and stews. It is eaten as a side dish with almost every Korean meal.There are hundreds of varieties of kimchi made with different vegetables as the main ingredients.",
  "title":"Kimchi",
  "url":"https://en.wikipedia.org/wiki/Kimchi"
}
  
GET main image url of a Wikipedia Article 
-end point: https://wiki-scraper-331405.uc.r.appspot.com/<title>/image
-request example:
https://wiki-scraper-331405.uc.r.appspot.com/kimchi/image
-response example:
200 OK
{
  "image_url":"https://upload.wikimedia.org/wikipedia/commons/f/f8/Various_kimchi.jpg",
  "url":"https://en.wikipedia.org/wiki/Kimchi",
  "title":"Kimchi"
}
