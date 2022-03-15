import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [ratings, setRatings] = useState([]);
  const listRatings = ratings.map((rate, index) => {
    return (
      <ul>
        <form id={index}>
          <label for="movie_id">Movie ID:</label>
          <input type="text" id="movie_id" name="movie_id" value={rate[0]} readonly></input>
	  <input type="number" id="rating" name="rating" min="0" max="5" placeholder={rate[2]} defaultValue={rate[2]} required></input>
	  <input type="text" placeholder={rate[1]} defaultValue={rate[1]} name="comment" required></input>
	  <input type="button" id="hover" onClick={() => handleClick(index)} value="Delete"></input>
	</form>
      </ul>
    )
});

const indexes = [];

function handleClick(index) {
  const ratingForm = document.getElementById(index);
  indexes.push(index);
  indexes.sort(function (a, b) { return b - a; })
  ratingForm.remove();
  console.log(ratings);
  console.log(indexes);
};

useEffect(() => {
  fetch('/editcomments', {
    method: 'POST', headers: {
      'Content-Type': 'application/json'
    }
  })
  
    .then(response => { return response.json() })
      .then(data => {
        setRatings(data.ratings)
        console.log(data)
      })
  }, []);  

function saveChanges() {
  alert("Your changes have been saved!")
  fetch('/save_changes', {
    method: 'GET', headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(indexes)
  })
};

  return (
    <div className="App">
      <h1>Your reviews: </h1>
	{listRatings}
	<a href="/"><input type="submit" id="hover" value="SAVE" onClick={() => saveChanges()}></input></a>
    </div>
  );
};

export default App;
