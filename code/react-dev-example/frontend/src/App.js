import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import siemensLogo from './Siemens_AG_logo.png'; // Replace with the correct path to your Siemens logo
import './App.css';

function App() {
  const [data, setData] = useState('');
  const [inputText, setInputText] = useState('');

  // Define the base URL using an environment variable or specify a default value
  const BASE_URL = process.env.REACT_APP_BASE_URL || '';

  // useEffect(() => {
  //   fetchData();
  // }, []);

  const fetchData = () => {
    console.log(window.location.href);
    fetch(`${BASE_URL}/api/get-last-data`)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then((result) => {
        console.log(result); // Log the response data to the console
        if (result && result.res.length > 0)
          setData(result.res[0][2]); // Set the state with the received data
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const postDataToServer = () => {
    fetch(`${BASE_URL}/api/post-data`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText }),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log('Data sent successfully:', result);
      })
      .catch((error) => console.error('Error:', error));
  };

  const handleButtonClick = () => {
    console.log('Posting data...');
    postDataToServer();
  };

  const handleButtonClick2 = () => {
    console.log('Fetching data...');
    fetchData();
  };

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={siemensLogo} className="Siemens-logo" alt="Siemens Logo" />
        <img src={logo} className="App-logo" alt="React Logo" />
        <form>
          <div className="form-group with-margin">
            <label htmlFor="reverseMessage">Message</label>
            <input
              className="form-control form-control-lg"
              id="reverseMessage"
              aria-describedby="reverseMessageHelp"
              placeholder="Enter message to reverse"
              value={inputText}
              onChange={handleInputChange}
            />
            <button type="button" className="btn btn-primary" onClick={handleButtonClick}>
              Send data to DB
            </button>
            {data && <p>{data.message}</p>}
          </div>
        </form>
        <div className="form-group">
            <label htmlFor="outText">Reversed Message</label>
            <textarea
              className="form-control form-control-lg"
              id="outText"
              // contentEditable="false"
              value={data}
              readOnly/>
            <button type="button" className="btn btn-secondary" onClick={handleButtonClick2}>
              Get latest data
            </button>
          </div>
      </header>
    </div>
  );
}

export default App;
