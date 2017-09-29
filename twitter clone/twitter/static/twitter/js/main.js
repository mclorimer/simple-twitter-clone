$(document).ready(function(){

	// getting old tweets if there are any, otherwise creating a blank list
	var past_tweets = JSON.parse(localStorage.getItem('past_tweets')) || [];

	// add past tweets from local storage if there are any
	if (past_tweets.length != 0) {
	for (i=0; i <= past_tweets.length; i++){
		$("#tweetlist").prepend(past_tweets[i]);
		}
	};
	$("#create-tweet").submit(function(event){
		// prevent page from refreshing on submit
		event.preventDefault();

		// getting what we submitted as well as the username and building a string that's a list item
		// that will be appended to the unordered list of tweets
		var tweet_text = $("#textinput").val();
		var author = $("#created_by").val();
		var tweetString = "<div class='col-8 tweet'> <div class='tweet-text'> <p> @" + author + ": " + tweet_text + " </p> </div> <div class='rt-button'> <button class='btn btn-info' type='button'>Retweet</button> </div> </div>";

		// append tweet we built to the current HTML page
		$(tweetString).hide().prependTo("#tweetlist").fadeIn(1500);

		// add current tweet to list of tweets
		past_tweets.push(tweetString);

		// add all tweets to local storage
		localStorage.setItem('past_tweets', JSON.stringify(past_tweets));
	});

	$(".btn-info").on("click", function(event){
		// getting and cleaning the text of the tweet next to the retweet button
		var retweetStringObjectTextUnclean = event.currentTarget.parentElement.parentElement.outerText;
		var formattedString = retweetStringObjectTextUnclean.replace("Retweet", "");
		var user = $("#user").text();

		// building a retweet string
		var retweet = "<div class='col-8 tweet'> <p> @" + user + ": " + formattedString + "</p> <div class='rt-button'> <button class='btn btn-info' type='button'>Retweet</button> </div> </div>";

		// appending retweet to local storage and the html page
		past_tweets.push(retweet);
		localStorage.setItem('past_tweets', JSON.stringify(past_tweets));

		$(retweet).hide().prependTo("#tweetlist").fadeIn(1500);;

	});
});