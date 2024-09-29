import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    // Fetch the message from the HelloWorld Service
    fetch('http://localhost:5000/api/helloworld')  // Update the URL if necessary
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => setMessage('Error fetching message'));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>UI Service</h1>
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;

