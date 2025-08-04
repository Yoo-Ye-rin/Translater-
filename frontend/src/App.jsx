import React, { useState } from "react";

function App() {
  const [inputText, setInputText] = useState("");
  const [translatedText, setTranslatedText] = useState("");

  const handleTranslate = async () => {
    const response = await fetch("http://localhost:8000/translate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: inputText }),
    });

    const data = await response.json();
    setTranslatedText(data.message);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        // placeholder=Enter the textarea
        rows={5}
        style={{ width: "100%", maxWidth: "500px", fontSize: "16px" }}
      />
      <br />
      <button
        onClick={handleTranslate}
        style={{ marginTop: "10px", padding: "10px 20px", fontSize: "16px" }}
      >
        Translate
      </button>
      <div style={{ marginTop: "20px", fontSize: "18px" }}>
        {translatedText}
      </div>
    </div>
  );
}
export default App;
