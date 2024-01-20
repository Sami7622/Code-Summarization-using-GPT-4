import React, { useState } from 'react';

const Home = () => {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerateSummary = async () => {
    setIsLoading(true);
    setError('');

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: text })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setSummary(data.response.message.content);
    } catch (error) {
      setError('Failed to generate summary: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="editor">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type your text here..."
        />
        <button onClick={handleGenerateSummary} disabled={isLoading}>
          {isLoading ? 'Generating...' : 'Generate Summary'}
        </button>
      </div>

      <div className="summary">
        {error ? <p className="error">{error}</p> : null}
        <textarea
          value={summary}
          readOnly
          placeholder="Summary will appear here..."
        />
      </div>

    
    </div>
  );
};

export default Home;
