# wikipedia_scraper

URL = https://wiki-scraper-331405.uc.r.appspot.com


**GET Wikipedia Article Full Content**</br>
-endpoint: https://wiki-scraper-331405.uc.r.appspot.com/<title></br>
-request example: https://wiki-scraper-331405.uc.r.appspot.com/kimchi</br>
-response example:  </br>
200 OK</br>
{</br>
  "content":"Kimchi (; Korean: \uae40\uce58, romanized: gimchi, IPA: [kim.t\u0255\u02b0i]), a staple food in Korean cuisine, is a  traditional side dish of salted and fermented vegetables, such as napa cabbage and Korean radish, made with a widely varying selection of seasonings, including gochugaru (Korean chili powder), spring onions, garlic, ginger, and jeotgal (salted seafood), etc. It is also used in a variety of soups and stews. It is eaten as a side dish with almost every Korean meal.There are hundreds of varieties of kimchi made with different vegetables as the main ingredients. Traditionally, winter kimchi, called kimjang, was stored in large earthenware fermentation vessels, called onggi, in the ground to prevent freezing during the winter months and to keep it cool enough to slow down the fermentation process during summer months.....",</br>
  "title":"Kimchi",</br>
  "url":"https://en.wikipedia.org/wiki/Kimchi"</br>
}</br>

**GET Wikipedia Article Summary**</br>
-endpoint: https://wiki-scraper-331405.uc.r.appspot.com/<title>/summary</br>
-request example:https://wiki-scraper-331405.uc.r.appspot.com/kimchi/summary</br>
-response example:</br>
200 OK</br>
{</br>
  "summary":"Kimchi (; Korean: \uae40\uce58, romanized: gimchi, IPA: [kim.t\u0255\u02b0i]), a staple food in Korean cuisine, is a  traditional side dish of salted and fermented vegetables, such as napa cabbage and Korean radish, made with a widely varying selection of seasonings, including gochugaru (Korean chili powder), spring onions, garlic, ginger, and jeotgal (salted seafood), etc. It is also used in a variety of soups and stews. It is eaten as a side dish with almost every Korean meal.There are hundreds of varieties of kimchi made with different vegetables as the main ingredients. Traditionally, winter kimchi, called kimjang, was stored in large earthenware fermentation vessels, called onggi, in the ground to prevent freezing during the winter months and to keep it cool enough to slow down the fermentation process during summer months. The vessels are also kept outdoors in special terraces called jangdokdae. In contemporary times, household kimchi refrigerators are more commonly used.",</br>
  "title":"Kimchi",</br>
  "url":"https://en.wikipedia.org/wiki/Kimchi"</br>
}</br>

**GET First X Number of Sentences of a Wikipedia Article Summary** </br>
-endpoint: https://wiki-scraper-331405.uc.r.appspot.com/<title>/summary/<number_sentences> </br>
-request example:https://wiki-scraper-331405.uc.r.appspot.com/kimchi/summary/3</br>
-response example:</br>
200 OK</br>
{</br>
  "summary":"Kimchi (; Korean: \uae40\uce58, romanized: gimchi, IPA: [kim.t\u0255\u02b0i]), a staple food in Korean cuisine, is a  traditional side dish of salted and fermented vegetables, such as napa cabbage and Korean radish, made with a widely varying selection of seasonings, including gochugaru (Korean chili powder), spring onions, garlic, ginger, and jeotgal (salted seafood), etc. It is also used in a variety of soups and stews. It is eaten as a side dish with almost every Korean meal.There are hundreds of varieties of kimchi made with different vegetables as the main ingredients.",</br>
  "title":"Kimchi",</br>
  "url":"https://en.wikipedia.org/wiki/Kimchi"</br>
}</br>
  
**GET Main Image url of a Wikipedia Article** </br>
-endpoint: https://wiki-scraper-331405.uc.r.appspot.com/<title>/image</br>
-request example:https://wiki-scraper-331405.uc.r.appspot.com/kimchi/image</br>
-response example:</br>
200 OK</br>
{</br>
  "image_url":"https://upload.wikimedia.org/wikipedia/commons/f/f8/Various_kimchi.jpg",</br>
  "url":"https://en.wikipedia.org/wiki/Kimchi",</br>
  "title":"Kimchi"</br>
}</br>
