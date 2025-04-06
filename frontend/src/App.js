 /*
 import React, { useState } from "react";
import axios from "axios";

function App() {
  const [customerId, setCustomerId] = useState("");
  const [recommendationText, setRecommendationText] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/api/recommend", {
        customer_id: customerId,
      });
      setRecommendationText(response.data.recommendations_text);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div className="App">
      <h1>Smartcart AI Recommendations</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter Customer ID"
          value={customerId}
          onChange={(e) => setCustomerId(e.target.value)}
        />
        <button type="submit">Get Recommendations</button>
      </form>

      <div className="recommendation-output">
        {recommendationText && (
          <>
            <h2>🎯 Final Recommendations:</h2>
            <pre style={{ whiteSpace: "pre-wrap", backgroundColor: "#f5f5f5", padding: "1rem" }}>
              {recommendationText}
            </pre>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
*/
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [customerId, setCustomerId] = useState('');
  const [recommendationText, setRecommendationText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchRecommendations = async () => {
    if (!customerId.trim()) {
      setError('Please enter a Customer ID');
      return;
    }

    setLoading(true);
    setError('');
    setRecommendationText('');

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/recommend', {
        customer_id: customerId,
      });

      if (response.data.recommendations_text) {
        setRecommendationText(response.data.recommendations_text);
      } else {
        setError('No recommendations found.');
      }
    } catch (err) {
      setError('Something went wrong. Please check the backend or customer ID.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white shadow-lg rounded-2xl p-8 max-w-2xl w-full">
        <h1 className="text-3xl font-bold text-center text-blue-700 mb-6">
          🛒 Smartcart AI Recommender
        </h1>

        <div className="flex flex-col sm:flex-row gap-4 mb-6">
          <input
            type="text"
            placeholder="Enter Customer ID (e.g., C1000)"
            className="border border-gray-300 rounded-md px-4 py-2 w-full"
            value={customerId}
            onChange={(e) => setCustomerId(e.target.value)}
          />
          <button
            onClick={fetchRecommendations}
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-md transition"
          >
            Get Recommendations
          </button>
        </div>

        {loading && (
          <div className="text-center text-gray-600">
            ⏳ Generating personalized recommendations...
          </div>
        )}

        {error && (
          <div className="text-red-500 text-center font-medium mb-4">
            ❌ {error}
          </div>
        )}

        {recommendationText && (
          <div className="mt-4 bg-green-50 border border-green-200 rounded-lg p-4 text-gray-800 whitespace-pre-line">
            <h2 className="text-xl font-semibold text-green-700 mb-2">🎯 Final Recommendations:</h2>
            <p>{recommendationText}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
