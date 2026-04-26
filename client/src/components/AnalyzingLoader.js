import React, { useState, useEffect } from "react";
import "../styles/LoadingStates.css";

const PROGRESS_STEPS = [
  { text: "Scanning idea for keywords...", duration: 1000 },
  { text: "Comparing with market database...", duration: 1500 },
  { text: "Analyzing market saturation...", duration: 1200 },
  { text: "Evaluating innovation score...", duration: 1300 },
  { text: "Generating SWOT analysis...", duration: 1000 },
  { text: "Creating visualizations...", duration: 1000 },
  { text: "Building pitch deck structure...", duration: 800 },
  { text: "Finalizing report...", duration: 600 },
];

export function AnalyzingLoader({ isVisible }) {

    
  const [currentStep, setCurrentStep] = useState(0);
  const [progress, setProgress] = useState(0);

useEffect(() => {
  if (!isVisible) {
    setCurrentStep(0);
    setProgress(0);
    return;
  }

  let stepIndex = 0;

  const stepInterval = setInterval(() => {
    stepIndex++;
    setCurrentStep(stepIndex);

    if (stepIndex >= PROGRESS_STEPS.length - 1) {
      clearInterval(stepInterval);
    }
  }, 1000);

  const progressInterval = setInterval(() => {
    setProgress((prev) => {
      const next = Math.min(prev + Math.random() * 10, 95);
      return stepIndex >= PROGRESS_STEPS.length - 1 ? 100 : next;
    });
  }, 300);

  return () => {
    clearInterval(stepInterval);
    clearInterval(progressInterval);
  };
}, [isVisible]);

  if (!isVisible) return null;

  return (
    <div className="analyzing-loader-container">
      <div className="loader-backdrop" />
      <div className="loader-card">
        {/* Animated Logo */}
        <div className="loader-logo">
          <div className="logo-pulse">🚀</div>
        </div>

        {/* Title */}
        <h2 className="loader-title">Analyzing Your Startup Idea</h2>

        {/* Progress Steps */}
        <div className="progress-steps">
          {PROGRESS_STEPS.map((step, index) => (
            <div
              key={index}
              className={`progress-step ${
                index < currentStep ? "completed" : index === currentStep ? "active" : "pending"
              }`}
            >
              <div className="step-indicator">
                {index < currentStep ? (
                  <span className="step-check">✓</span>
                ) : index === currentStep ? (
                  <span className="step-spinner"></span>
                ) : (
                  <span className="step-number">{index + 1}</span>
                )}
              </div>
              <span className="step-text">{step.text}</span>
            </div>
          ))}
        </div>

        {/* Overall Progress Bar */}
        <div className="overall-progress">
          <div className="progress-bar-background">
            <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
          </div>
          <span className="progress-percentage">{Math.round(progress)}%</span>
        </div>

        {/* Loading Message */}
        <p className="loading-message">
          Leveraging AI to evaluate your idea against 100+ startup concepts...
        </p>
      </div>
    </div>
  );
}
