import React, { useState } from 'react';
import axios from 'axios';
import './UrlShortenerForm.css';  // Import CSS for styling

function UrlShortenerForm() {
  const [longUrl, setLongUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/save', { long_url: longUrl });
      setShortUrl(response.data.short_url);
      setError('');
    } catch (error) {
      setShortUrl('');
      setError('Error generating short URL');
    }
  };

  return (
    <div className="container">
      <h1>URL Shortener</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            className="form-control"
            value={longUrl}
            onChange={(e) => setLongUrl(e.target.value)}
            placeholder="Enter URL to shorten"
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">Shorten URL</button>
      </form>
      {shortUrl && (
        <div className="short-url">
          <p>Shortened URL:</p>
          <a href={shortUrl} target="_blank" rel="noopener noreferrer">{shortUrl}</a>
        </div>
      )}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default UrlShortenerForm;
