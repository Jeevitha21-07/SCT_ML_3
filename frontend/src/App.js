import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState("");

  const handleChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    setPreview(URL.createObjectURL(selected));
  };

  const handlePredict = async () => {
    if (!file) return alert("Upload image");

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/predict",
      formData
    );

    setResult(res.data.prediction);
  };

  return (
    <div className="app">
      <div className="card">
        <h1>🐶🐱Pet Classifier (SVM)</h1>

        {preview && <img src={preview} className="preview" alt="" />}

        <input type="file" onChange={handleChange} />
        <button onClick={handlePredict}>Predict</button>

        {result && <h2>{result}</h2>}
      </div>
    </div>
  );
}

export default App;