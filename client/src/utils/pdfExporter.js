import jsPDF from "jspdf";

export async function generateAnalysisPDF(analysisData, analysisContainerId) {
  try {
    // Create PDF in landscape to fit charts better
    const pdf = new jsPDF({
      orientation: "portrait",
      unit: "mm",
      format: "a4",
    });

    const pageHeight = pdf.internal.pageSize.getHeight();
    const pageWidth = pdf.internal.pageSize.getWidth();
    let yPosition = 15;

    // Title Page
    pdf.setFontSize(28);
    pdf.setTextColor(0, 102, 255);
    pdf.text("Startup Analyzer Report", pageWidth / 2, yPosition, { align: "center" });

    yPosition += 15;
    pdf.setFontSize(12);
    pdf.setTextColor(100, 100, 100);
    pdf.text(`Comprehensive AI-Powered Startup Evaluation`, pageWidth / 2, yPosition, { align: "center" });

    yPosition += 25;
    pdf.setFontSize(14);
    pdf.setTextColor(0, 0, 0);
    pdf.text("Executive Summary", 15, yPosition);

    yPosition += 10;
    pdf.setFontSize(11);
    pdf.setTextColor(60, 60, 60);

    // Add key metrics
    const metricsText = [
      `Idea: ${analysisData.idea}`,
      `Innovation Score: ${analysisData.innovation_score.toFixed(1)}/10`,
      `Market Match: ${(analysisData.max_similarity * 10).toFixed(1)}/10`,
      `Assessment: ${analysisData.interpretation}`,
    ];

    metricsText.forEach((text) => {
      pdf.text(text, 15, yPosition);
      yPosition += 8;
    });

    // Add page break
    pdf.addPage();
    yPosition = 15;

    // Section: Analysis Breakdown
    pdf.setFontSize(16);
    pdf.setTextColor(0, 102, 255);
    pdf.text("AI Explanations & Reasoning", 15, yPosition);

    yPosition += 10;
    pdf.setFontSize(10);
    pdf.setTextColor(60, 60, 60);

    if (analysisData.explanation) {
      // Add reasoning
      const reasoningText = analysisData.explanation.innovation_reasoning || [];
      pdf.setFont(undefined, "bold");
      pdf.text("Innovation Score Reasoning:", 15, yPosition);
      yPosition += 6;

      pdf.setFont(undefined, "normal");
      reasoningText.forEach((reason) => {
        const wrapped = pdf.splitTextToSize(reason, pageWidth - 30);
        wrapped.forEach((line) => {
          if (yPosition > pageHeight - 15) {
            pdf.addPage();
            yPosition = 15;
          }
          pdf.text(line, 20, yPosition);
          yPosition += 6;
        });
      });

      yPosition += 5;
    }

    // Add page break for SWOT
    pdf.addPage();
    yPosition = 15;

    pdf.setFontSize(16);
    pdf.setTextColor(0, 102, 255);
    pdf.text("SWOT Analysis", 15, yPosition);

    yPosition += 10;
    pdf.setFontSize(10);

    if (analysisData.swot) {
      const swotSections = [
        { title: "Strengths", data: analysisData.swot.strengths, color: [0, 221, 136] },
        { title: "Weaknesses", data: analysisData.swot.weaknesses, color: [255, 170, 0] },
        { title: "Opportunities", data: analysisData.swot.opportunities, color: [0, 102, 255] },
        { title: "Threats", data: analysisData.swot.threats, color: [255, 107, 107] },
      ];

      swotSections.forEach((section) => {
        if (yPosition > pageHeight - 30) {
          pdf.addPage();
          yPosition = 15;
        }

        pdf.setTextColor(...section.color);
        pdf.setFont(undefined, "bold");
        pdf.text(section.title, 15, yPosition);
        yPosition += 7;

        pdf.setTextColor(60, 60, 60);
        pdf.setFont(undefined, "normal");
        section.data.forEach((item) => {
          const wrapped = pdf.splitTextToSize(`• ${item}`, pageWidth - 30);
          wrapped.forEach((line) => {
            if (yPosition > pageHeight - 10) {
              pdf.addPage();
              yPosition = 15;
            }
            pdf.text(line, 20, yPosition);
            yPosition += 5;
          });
        });

        yPosition += 5;
      });
    }

    // Add page break for Success Factors
    pdf.addPage();
    yPosition = 15;

    pdf.setFontSize(16);
    pdf.setTextColor(0, 102, 255);
    pdf.text("Key Success Factors", 15, yPosition);

    yPosition += 10;
    pdf.setFontSize(10);
    pdf.setTextColor(60, 60, 60);

    if (analysisData.success_factors) {
      const factors = analysisData.success_factors;

      pdf.setFont(undefined, "bold");
      pdf.text("Critical Success Factors:", 15, yPosition);
      yPosition += 6;
      pdf.setFont(undefined, "normal");

      factors.critical_factors.forEach((factor) => {
        const wrapped = pdf.splitTextToSize(`• ${factor}`, pageWidth - 30);
        wrapped.forEach((line) => {
          if (yPosition > pageHeight - 10) {
            pdf.addPage();
            yPosition = 15;
          }
          pdf.text(line, 20, yPosition);
          yPosition += 5;
        });
      });

      yPosition += 5;
      pdf.setFont(undefined, "bold");
      pdf.text("Positive Factors:", 15, yPosition);
      yPosition += 6;
      pdf.setFont(undefined, "normal");

      factors.positive_factors.forEach((factor) => {
        const wrapped = pdf.splitTextToSize(`• ${factor}`, pageWidth - 30);
        wrapped.forEach((line) => {
          if (yPosition > pageHeight - 10) {
            pdf.addPage();
            yPosition = 15;
          }
          pdf.text(line, 20, yPosition);
          yPosition += 5;
        });
      });

      yPosition += 5;
      pdf.setFont(undefined, "bold");
      pdf.text("Risk Factors:", 15, yPosition);
      yPosition += 6;
      pdf.setFont(undefined, "normal");

      factors.risk_factors.forEach((factor) => {
        const wrapped = pdf.splitTextToSize(`• ${factor}`, pageWidth - 30);
        wrapped.forEach((line) => {
          if (yPosition > pageHeight - 10) {
            pdf.addPage();
            yPosition = 15;
          }
          pdf.text(line, 20, yPosition);
          yPosition += 5;
        });
      });
    }

    // Add page break for Competitors
    pdf.addPage();
    yPosition = 15;

    pdf.setFontSize(16);
    pdf.setTextColor(0, 102, 255);
    pdf.text("Competitive Landscape", 15, yPosition);

    yPosition += 10;
    pdf.setFontSize(10);
    pdf.setTextColor(60, 60, 60);

    if (analysisData.competitors) {
      const competitors = analysisData.competitors;

      pdf.setFont(undefined, "bold");
      pdf.text("Direct Competitors:", 15, yPosition);
      yPosition += 6;
      pdf.setFont(undefined, "normal");

      competitors.direct_competitors.forEach((comp) => {
        const compText = `• ${comp.name} (${comp.type}) - Market Share: ${comp.market_share}`;
        const wrapped = pdf.splitTextToSize(compText, pageWidth - 30);
        wrapped.forEach((line) => {
          if (yPosition > pageHeight - 10) {
            pdf.addPage();
            yPosition = 15;
          }
          pdf.text(line, 20, yPosition);
          yPosition += 5;
        });
      });

      yPosition += 5;
      pdf.setFont(undefined, "bold");
      pdf.text("Market Summary:", 15, yPosition);
      yPosition += 6;
      pdf.setFont(undefined, "normal");

      const wrapped = pdf.splitTextToSize(competitors.competitive_landscape_summary, pageWidth - 30);
      wrapped.forEach((line) => {
        if (yPosition > pageHeight - 10) {
          pdf.addPage();
          yPosition = 15;
        }
        pdf.text(line, 20, yPosition);
        yPosition += 5;
      });
    }

    // Add page break for Market Strategy
    if (analysisData.market_strategy) {
      pdf.addPage();
      yPosition = 15;

      pdf.setFontSize(16);
      pdf.setTextColor(0, 102, 255);
      pdf.text("Recommended Market Entry Strategy", 15, yPosition);

      yPosition += 10;
      pdf.setFontSize(10);
      pdf.setTextColor(60, 60, 60);

      const strategy = analysisData.market_strategy;

      pdf.setFont(undefined, "bold");
      pdf.text(`Approach: ${strategy.approach}`, 15, yPosition);
      yPosition += 8;

      pdf.setFont(undefined, "normal");
      const rationale = pdf.splitTextToSize(`Rationale: ${strategy.rationale}`, pageWidth - 30);
      rationale.forEach((line) => {
        pdf.text(line, 20, yPosition);
        yPosition += 5;
      });

      yPosition += 5;
      pdf.setFont(undefined, "bold");
      pdf.text(`Timeline: ${strategy.timeline}`, 15, yPosition);
      yPosition += 8;

      pdf.setFont(undefined, "bold");
      pdf.text("Key Milestones:", 15, yPosition);
      yPosition += 6;
      pdf.setFont(undefined, "normal");

      strategy.key_milestones.forEach((milestone) => {
        const wrapped = pdf.splitTextToSize(`• ${milestone}`, pageWidth - 30);
        wrapped.forEach((line) => {
          if (yPosition > pageHeight - 10) {
            pdf.addPage();
            yPosition = 15;
          }
          pdf.text(line, 20, yPosition);
          yPosition += 5;
        });
      });
    }

    // Save PDF
    pdf.save(`startup-analysis-${new Date().toISOString().split('T')[0]}.pdf`);

    return true;
  } catch (error) {
    console.error("Error generating PDF:", error);
    return false;
  }
}
