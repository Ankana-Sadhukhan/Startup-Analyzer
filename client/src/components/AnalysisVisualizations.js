// import React from "react";
// import {
//   RadarChart,
//   PolarGrid,
//   PolarAngleAxis,
//   PolarRadiusAxis,
//   Radar,
//   Legend,
//   Tooltip,
//   ResponsiveContainer,
//   BarChart,
//   Bar,
//   XAxis,
//   YAxis,
//   CartesianGrid,
// } from "recharts";
// import "../styles/Visualizations.css";

// export function MetricsRadarChart({ metrics }) {
//   const data = [
//     { name: "Innovation", value: metrics.innovation },
//     { name: "Differentiation", value: metrics.differentiation },
//     { name: "Scalability", value: metrics.scalability },
//     { name: "Tech Feasibility", value: metrics.technical_feasibility },
//     { name: "Market Demand", value: metrics.market_demand },
//     { name: "Market Saturation", value: metrics.market_saturation },
//   ];

//   return (
//     <div className="visualization-card">
//       <h3 className="visualization-title">📊 Business Metrics Radar</h3>
//       <p className="visualization-subtitle">Comprehensive startup viability analysis</p>
//       <ResponsiveContainer width="100%" height={400}>
//         <RadarChart data={data}>
//           <PolarGrid stroke="rgba(0, 212, 255, 0.2)" />
//           <PolarAngleAxis dataKey="name" tick={{ fill: "#b8c5d6", fontSize: 12 }} />
//           <PolarRadiusAxis angle={90} domain={[0, 10]} tick={{ fill: "#b8c5d6", fontSize: 11 }} />
//           <Radar
//             name="Metrics Score"
//             dataKey="value"
//             stroke="#00d4ff"
//             fill="#0066ff"
//             fillOpacity={0.6}
//             animationDuration={1000}
//           />
//           <Tooltip
//             contentStyle={{
//               backgroundColor: "rgba(10, 14, 39, 0.95)",
//               border: "1px solid rgba(0, 212, 255, 0.3)",
//               borderRadius: "8px",
//               color: "#ffffff",
//             }}
//             formatter={(value) => `${value.toFixed(1)}/10`}
//           />
//           <Legend wrapperStyle={{ paddingTop: "20px" }} />
//         </RadarChart>
//       </ResponsiveContainer>
//     </div>
//   );
// }

// export function SWOTAnalysis({ swot }) {
//   return (
//     <div className="swot-container">
//       <h3 className="swot-title">🎯 SWOT Analysis Matrix</h3>
//       <div className="swot-grid">
//         <div className="swot-card strengths">
//           <h4 className="swot-heading">💪 Strengths</h4>
//           <ul className="swot-list">
//             {swot.strengths.map((item, idx) => (
//               <li key={idx}>{item}</li>
//             ))}
//           </ul>
//         </div>

//         <div className="swot-card weaknesses">
//           <h4 className="swot-heading">⚠️ Weaknesses</h4>
//           <ul className="swot-list">
//             {swot.weaknesses.map((item, idx) => (
//               <li key={idx}>{item}</li>
//             ))}
//           </ul>
//         </div>

//         <div className="swot-card opportunities">
//           <h4 className="swot-heading">🚀 Opportunities</h4>
//           <ul className="swot-list">
//             {swot.opportunities.map((item, idx) => (
//               <li key={idx}>{item}</li>
//             ))}
//           </ul>
//         </div>

//         <div className="swot-card threats">
//           <h4 className="swot-heading">🛑 Threats</h4>
//           <ul className="swot-list">
//             {swot.threats.map((item, idx) => (
//               <li key={idx}>{item}</li>
//             ))}
//           </ul>
//         </div>
//       </div>
//     </div>
//   );
// }

// export function PitchDeckOutline({ pitchDeck }) {
//   const slides = Object.entries(pitchDeck).map(([key, slide], idx) => ({
//     number: idx + 1,
//     ...slide,
//   }));

//   return (
//     <div className="pitch-deck-container">
//       <h3 className="pitch-title">🎤 AI-Generated Pitch Deck Outline</h3>
//       <p className="pitch-subtitle">9-slide structure for investor presentations</p>
//       <div className="pitch-slides-grid">
//         {slides.map((slide) => (
//           <div key={slide.number} className="pitch-slide">
//             <div className="slide-number">Slide {slide.number}</div>
//             <h4 className="slide-title">{slide.title}</h4>
//             <ul className="slide-points">
//               {slide.talking_points.map((point, idx) => (
//                 <li key={idx}>{point}</li>
//               ))}
//             </ul>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

// export function ExplainabilityScores({ metrics, innovation_score }) {
//   const scoreData = [
//     { category: "Innovation Score", value: innovation_score, color: "#0066ff" },
//     { category: "Differentiation", value: metrics.differentiation, color: "#00d4ff" },
//     { category: "Scalability Potential", value: metrics.scalability, color: "#00dd88" },
//     { category: "Technical Feasibility", value: metrics.technical_feasibility, color: "#ffaa00" },
//     { category: "Market Demand", value: metrics.market_demand, color: "#ff6b6b" },
//   ];

//   return (
//     <div className="visualization-card">
//       <h3 className="visualization-title">🔍 Explainability Breakdown</h3>
//       <p className="visualization-subtitle">AI reasoning for your startup score</p>
//       <ResponsiveContainer width="100%" height={300}>
//         <BarChart data={scoreData}>
//           <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 212, 255, 0.1)" />
//           <XAxis dataKey="category" tick={{ fill: "#b8c5d6", fontSize: 11 }} angle={-45} textAnchor="end" height={100} />
//           <YAxis domain={[0, 10]} tick={{ fill: "#b8c5d6" }} />
//           <Tooltip
//             contentStyle={{
//               backgroundColor: "rgba(10, 14, 39, 0.95)",
//               border: "1px solid rgba(0, 212, 255, 0.3)",
//               borderRadius: "8px",
//               color: "#ffffff",
//             }}
//             formatter={(value) => `${value.toFixed(1)}/10`}
//           />
//           <Bar dataKey="value" fill="#00d4ff" radius={[8, 8, 0, 0]} animationDuration={1000} />
//         </BarChart>
//       </ResponsiveContainer>
//     </div>
//   );
// }



import React from "react";
import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  Legend,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";
import "../styles/Visualizations.css";

// ✅ Metrics Radar Chart
export function MetricsRadarChart({ metrics }) {
  const data = [
    { name: "Innovation", value: metrics?.innovation ?? 0 },
    { name: "Differentiation", value: metrics?.differentiation ?? 0 },
    { name: "Scalability", value: metrics?.scalability ?? 0 },
    { name: "Tech Feasibility", value: metrics?.technical_feasibility ?? 0 },
    { name: "Market Demand", value: metrics?.market_demand ?? 0 },
    { name: "Market Saturation", value: metrics?.market_saturation ?? 0 },
  ];

  return (
    <div className="visualization-card">
      <h3 className="visualization-title">📊 Business Metrics Radar</h3>
      <p className="visualization-subtitle">
        Comprehensive startup viability analysis
      </p>

      <ResponsiveContainer width="100%" height={400}>
        <RadarChart data={data}>
          <PolarGrid stroke="rgba(0, 212, 255, 0.2)" />
          <PolarAngleAxis
            dataKey="name"
            tick={{ fill: "#b8c5d6", fontSize: 12 }}
          />
          <PolarRadiusAxis
            angle={90}
            domain={[0, 10]}
            tick={{ fill: "#b8c5d6", fontSize: 11 }}
          />
          <Radar
            name="Metrics Score"
            dataKey="value"
            stroke="#00d4ff"
            fill="#0066ff"
            fillOpacity={0.6}
            animationDuration={1000}
          />
          <Tooltip
            contentStyle={{
              backgroundColor: "rgba(10, 14, 39, 0.95)",
              border: "1px solid rgba(0, 212, 255, 0.3)",
              borderRadius: "8px",
              color: "#ffffff",
            }}
            formatter={(value) => `${(value ?? 0).toFixed(1)}/10`}
          />
          <Legend wrapperStyle={{ paddingTop: "20px" }} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}

// ✅ SWOT Analysis
export function SWOTAnalysis({ swot }) {
  return (
    <div className="swot-container">
      <h3 className="swot-title">🎯 SWOT Analysis Matrix</h3>

      <div className="swot-grid">
        <div className="swot-card strengths">
          <h4 className="swot-heading">💪 Strengths</h4>
          <ul className="swot-list">
            {swot?.strengths?.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="swot-card weaknesses">
          <h4 className="swot-heading">⚠️ Weaknesses</h4>
          <ul className="swot-list">
            {swot?.weaknesses?.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="swot-card opportunities">
          <h4 className="swot-heading">🚀 Opportunities</h4>
          <ul className="swot-list">
            {swot?.opportunities?.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="swot-card threats">
          <h4 className="swot-heading">🛑 Threats</h4>
          <ul className="swot-list">
            {swot?.threats?.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

// ✅ Pitch Deck
export function PitchDeckOutline({ pitchDeck }) {
  const slides = Object.entries(pitchDeck || {}).map(
    ([key, slide], idx) => ({
      number: idx + 1,
      ...slide,
    })
  );

  return (
    <div className="pitch-deck-container">
      <h3 className="pitch-title">🎤 AI-Generated Pitch Deck Outline</h3>
      <p className="pitch-subtitle">
        9-slide structure for investor presentations
      </p>

      <div className="pitch-slides-grid">
        {slides.map((slide) => (
          <div key={slide.number} className="pitch-slide">
            <div className="slide-number">Slide {slide.number}</div>
            <h4 className="slide-title">{slide.title}</h4>

            <ul className="slide-points">
              {slide.talking_points?.map((point, idx) => (
                <li key={idx}>{point}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}

// ✅ Explainability Scores
export function ExplainabilityScores({ metrics, innovation_score }) {
  const scoreData = [
    { category: "Innovation Score", value: innovation_score ?? 0 },
    { category: "Differentiation", value: metrics?.differentiation ?? 0 },
    { category: "Scalability Potential", value: metrics?.scalability ?? 0 },
    { category: "Technical Feasibility", value: metrics?.technical_feasibility ?? 0 },
    { category: "Market Demand", value: metrics?.market_demand ?? 0 },
  ];

  return (
    <div className="visualization-card">
      <h3 className="visualization-title">🔍 Explainability Breakdown</h3>
      <p className="visualization-subtitle">
        AI reasoning for your startup score
      </p>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={scoreData}>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke="rgba(0, 212, 255, 0.1)"
          />
          <XAxis
            dataKey="category"
            tick={{ fill: "#b8c5d6", fontSize: 11 }}
            angle={-45}
            textAnchor="end"
            height={100}
          />
          <YAxis domain={[0, 10]} tick={{ fill: "#b8c5d6" }} />
          <Tooltip
            contentStyle={{
              backgroundColor: "rgba(10, 14, 39, 0.95)",
              border: "1px solid rgba(0, 212, 255, 0.3)",
              borderRadius: "8px",
              color: "#ffffff",
            }}
            formatter={(value) => `${(value ?? 0).toFixed(1)}/10`}
          />
          <Bar
            dataKey="value"
            fill="#00d4ff"
            radius={[8, 8, 0, 0]}
            animationDuration={1000}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}