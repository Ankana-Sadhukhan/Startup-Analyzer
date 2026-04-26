import React, { useState } from "react";
import "./App.css";
import "./styles/Visualizations.css";
import "./styles/LoadingStates.css";
import {
  MetricsRadarChart,
  SWOTAnalysis,
  PitchDeckOutline,
  ExplainabilityScores,
} from "./components/AnalysisVisualizations";
import { AnalyzingLoader } from "./components/AnalyzingLoader";
import { generateAnalysisPDF } from "./utils/pdfExporter";

function App() {
  const [idea, setIdea] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeIdea = async (e) => {
    e.preventDefault();
    if (!idea.trim()) return;

    setLoading(true);
    try {
      const apiHost = window.location.hostname;
      const apiProtocol = window.location.protocol;
      const apiUrl = `${apiProtocol}//${apiHost}:8000/predict?idea=${encodeURIComponent(idea)}`;
      const res = await fetch(apiUrl);
      if (!res.ok) {
        const errorText = await res.text();
        throw new Error(`API error ${res.status}: ${errorText}`);
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert(`Error analyzing idea. Please try again. ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleExportPDF = async () => {
    try {
      const success = await generateAnalysisPDF(result);
      if (success) {
        alert("PDF exported successfully!");
      } else {
        alert("Failed to generate PDF. Please try again.");
      }
    } catch (err) {
      console.error("PDF export error:", err);
      alert("Error exporting PDF.");
    }
  };

  // Main app interface
  return (
    <div className="app-container">
      {/* Loading State Overlay */}
      <AnalyzingLoader isVisible={loading} />

      {/* Animated background elements */}
      <div className="background-animation"></div>
      <div className="background-animation secondary"></div>

      {/* Header */}
      <header className="app-header">
        <div className="header-content">
          <div className="logo-wrapper">
            <div className="logo-icon">🚀</div>
          </div>
          <h1 className="app-title">Startup Analyzer</h1>
          <p className="app-subtitle">Discover the potential of your innovative ideas</p>
        </div>
      </header>

      {/* Main Content */}
      <main className="app-main">
        <div className="content-wrapper">
          {/* Input Section */}
          <div className="input-card">
            <div className="card-inner">
              <h2 className="section-title">Analyze Your Idea</h2>
              <p className="section-description">Enter your startup concept and let AI evaluate its innovation potential</p>

              <form onSubmit={analyzeIdea} className="input-form">
                <div className="input-wrapper">
                  <input
                    type="text"
                    placeholder="Describe your startup idea..."
                    value={idea}
                    onChange={(e) => setIdea(e.target.value)}
                    className="idea-input"
                    disabled={loading}
                  />
                  <span className="input-focus"></span>
                </div>

                <button
                  type="submit"
                  className={`analyze-button ${loading ? "loading" : ""}`}
                  disabled={loading}
                >
                  <span className="button-text">
                    {loading ? "Analyzing..." : "Analyze"}
                  </span>
                  <span className="button-icon">→</span>
                </button>
              </form>
            </div>
          </div>

          {/* Results Section */}
          {result && (
            <div className="results-section">
              {/* Export Button */}
              <div className="export-button-container">
                <button onClick={handleExportPDF} className="export-button">
                  <span className="export-icon">📥</span>
                  Download PDF Report
                </button>
              </div>

              {/* Key Metrics */}
              <div className="metrics-grid">
                <div className="metric-card innovation">
                  <div className="metric-inner">
                    <span className="metric-icon">⚡</span>
                    <h3 className="metric-label">Innovation Score</h3>
                    <p className="metric-value">{result.innovation_score.toFixed(1)}<span className="metric-unit">/10</span></p>
                  </div>
                </div>

                <div className="metric-card similarity">
                  <div className="metric-inner">
                    <span className="metric-icon">🎯</span>
                    <h3 className="metric-label">Market Match</h3>
                    <p className="metric-value">{(result.max_similarity * 10).toFixed(1)}<span className="metric-unit">/10</span></p>
                  </div>
                </div>
              </div>

              {/* Visualizations Section */}
              <div className="visualizations-section">
                {result.metrics && <MetricsRadarChart metrics={result.metrics} />}
                {result.metrics && (
                  <ExplainabilityScores
                    metrics={result.metrics}
                    innovation_score={result.innovation_score}
                  />
                )}
                {result.swot && <SWOTAnalysis swot={result.swot} />}
                {result.pitch_deck && <PitchDeckOutline pitchDeck={result.pitch_deck} />}
              </div>

              {/* Detailed Results */}
              <div className="results-card">
                <div className="card-inner">
                  <h2 className="section-title">Analysis Results</h2>

                  <div className="result-item">
                    <h4 className="result-label">Your Idea</h4>
                    <p className="result-value">{result.idea}</p>
                  </div>

                  <div className="result-item">
                    <h4 className="result-label">Processed Concept</h4>
                    <p className="result-value">{result.cleaned_idea}</p>
                  </div>

                  <div className="result-item">
                    <h4 className="result-label">Assessment</h4>
                    <p className="result-value interpretation">{result.interpretation}</p>
                  </div>

                  {/* Similar Ideas */}
                  <div className="similar-ideas-section">
                    <h3 className="subsection-title">Related Market Ideas</h3>
                    <div className="ideas-list">
                      {result.top_similar_ideas.map((item, index) => (
                        <div key={index} className="idea-item">
                          <span className="idea-number">{index + 1}</span>
                          <div className="idea-content">
                            <p className="idea-text">{item.idea}</p>
                            <p className="idea-similarity">
                              Market Alignment: {(item.similarity * 100).toFixed(1)}%
                            </p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="app-footer">
        <p>Powered by Advanced AI Analysis</p>
      </footer>
    </div>
  );
}

export default App;