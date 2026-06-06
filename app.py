<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentation Evaluation Report - ID: 2603113s</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Roboto+Mono:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        /* A4 Landscape print optimization: Ensuring 1-page fit */
        * { box-sizing: border-box; }
        body {
            background-color: #f1f5f9;
            margin: 0;
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Noto Sans JP', sans-serif;
            min-height: 100vh;
        }

        .slide-container {
            width: 1120px;
            height: 630px;
            background-color: #ffffff;
            position: relative;
            overflow: hidden;
            padding: 30px 45px;
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            grid-template-rows: auto 1fr auto;
            gap: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }

        @media print {
            body { background-color: #ffffff; padding: 0; }
            .slide-container { box-shadow: none; width: 100%; height: 100vh; padding: 20px; }
        }

        /* Decorative Element */
        .slide-container::before {
            content: "";
            position: absolute;
            top: 0; right: 0; width: 250px; height: 250px;
            background: radial-gradient(circle at 100% 0%, rgba(0, 80, 136, 0.05) 0%, transparent 70%);
            z-index: 0;
        }

        /* Header Styling */
        .header {
            grid-column: 1 / -1;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-bottom: 3px solid #005088;
            padding-bottom: 12px;
            z-index: 1;
        }
        .header-title-area {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }
        .header-title {
            margin: 0;
            font-size: 28px;
            color: #005088;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .type-badge {
            font-size: 11px;
            color: #ffffff;
            background-color: #005088;
            padding: 3px 10px;
            border-radius: 4px;
            font-weight: 700;
            width: fit-content;
            margin-top: 5px;
            text-transform: uppercase;
        }

        .student-id-box { text-align: right; }
        .id-label { font-size: 11px; color: #64748b; margin-bottom: 2px; font-weight: 700; }
        .id-value { font-family: 'Roboto Mono', monospace; font-size: 22px; color: #005088; font-weight: 700; letter-spacing: 1.5px; }

        /* Scoring and Total Section */
        .left-column {
            display: flex;
            flex-direction: column;
            gap: 15px;
            z-index: 1;
            justify-content: space-between;
        }
        .scoring-table {
            width: 100%;
            border-collapse: collapse;
        }
        .scoring-table th {
            background-color: #f8fafc;
            color: #475569;
            font-size: 11px;
            padding: 10px;
            text-align: left;
            border-bottom: 2px solid #cbd5e1;
            text-transform: uppercase;
        }
        .scoring-table td {
            padding: 11px 10px;
            border-bottom: 1px solid #f1f5f9;
            font-size: 14px;
            color: #334155;
        }
        .score-num {
            font-weight: 700;
            color: #005088;
            text-align: center;
            font-size: 16px;
        }

        .total-box {
            background-color: #005088;
            color: #ffffff;
            padding: 18px;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .total-label { font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
        .total-score { font-size: 36px; font-weight: 700; }

        /* Chart and Feedback Area */
        .right-column {
            display: grid;
            grid-template-rows: 1.1fr 1fr;
            gap: 15px;
            z-index: 1;
        }

        .radar-section {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #fdfdfd;
            border-radius: 8px;
            border: 1px solid #f1f5f9;
            padding: 5px;
        }

        .feedback-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        .feedback-card {
            background-color: #fff;
            padding: 18px;
            border-radius: 8px;
            border: 1px solid #eef2f6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        .feedback-card h3 {
            margin: 0 0 8px;
            font-size: 13px;
            color: #11caa0;
            display: flex;
            align-items: center;
            gap: 6px;
            text-transform: uppercase;
            font-weight: 700;
        }
        .feedback-card p {
            margin: 0;
            font-size: 13px;
            line-height: 1.6;
            color: #475569;
        }

        /* Footer */
        .footer {
            grid-column: 1 / -1;
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            color: #94a3b8;
            padding-top: 12px;
            border-top: 1px solid #f1f5f9;
        }

        .radar-svg { filter: drop-shadow(0 2px 4px rgba(0,0,0,0.05)); }
    </style>
</head>
<body>

    <div class="slide-container" id="slide1">
        <header class="header">
            <div class="header-title-area">
                <h1 class="header-title">Individual Evaluation Dashboard</h1>
                <div class="type-badge"><i class="fa-solid fa-user" style="margin-right: 5px;"></i> Individual Presentation</div>
            </div>
            <div class="student-id-box">
                <div class="id-label">STUDENT ID</div>
                <div class="id-value">2603113s</div>
            </div>
        </header>

        <div class="left-column">
            <table class="scoring-table">
                <thead>
                    <tr>
                        <th>Criteria</th>
                        <th style="text-align:center">Score (0-5)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Eye Contact</td><td class="score-num">3</td></tr>
                    <tr><td>Gestures</td><td class="score-num">3</td></tr>
                    <tr><td>Intonation</td><td class="score-num">4</td></tr>
                    <tr><td>Tone</td><td class="score-num">4</td></tr>
                    <tr><td>Rhythm</td><td class="score-num">3</td></tr>
                    <tr><td>Overall Smoothness</td><td class="score-num">3</td></tr>
                </tbody>
            </table>

            <div class="total-box">
                <span class="total-label">Final Evaluation</span>
                <span class="total-score">20 <small style="font-size:16px">/ 30</small></span>
            </div>
        </div>

        <div class="right-column">
            <div class="radar-section">
                <svg class="radar-svg" width="260" height="260" viewBox="0 0 300 300">
                    <polygon points="150,30 254,90 254,210 150,270 46,210 46,90" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="150,54 233,102 233,198 150,246 67,198 67,102" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="150,78 212,114 212,186 150,222 88,186 88,114" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                    <polygon points="150,102 191,126 191,174 150,198 109,174 109,126" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                    
                    <line x1="150" y1="150" x2="150" y2="30" stroke="#e2e8f0" stroke-width="1"/>
                    <line x1="150" y1="150" x2="254" y2="90" stroke="#e2e8f0" stroke-width="1"/>
                    <line x1="150" y1="150" x2="254" y2="210" stroke="#e2e8f0" stroke-width="1"/>
                    <line x1="150" y1="150" x2="150" y2="270" stroke="#e2e8f0" stroke-width="1"/>
                    <line x1="150" y1="150" x2="46" y2="210" stroke="#e2e8f0" stroke-width="1"/>
                    <line x1="150" y1="150" x2="46" y2="90" stroke="#e2e8f0" stroke-width="1"/>

                    <polygon points="150,78 212,114 233,198 150,246 88,186 88,114" fill="rgba(17, 202, 160, 0.25)" stroke="#11caa0" stroke-width="3"/>
                    
                    <text x="150" y="20" text-anchor="middle" font-size="11" font-weight="700" fill="#475569">Eye Contact</text>
                    <text x="260" y="85" text-anchor="start" font-size="11" font-weight="700" fill="#475569">Gestures</text>
                    <text x="260" y="225" text-anchor="start" font-size="11" font-weight="700" fill="#475569">Intonation</text>
                    <text x="150" y="288" text-anchor="middle" font-size="11" font-weight="700" fill="#475569">Tone</text>
                    <text x="40" y="225" text-anchor="end" font-size="11" font-weight="700" fill="#475569">Rhythm</text>
                    <text x="40" y="85" text-anchor="end" font-size="11" font-weight="700" fill="#475569">Smoothness</text>
                </svg>
            </div>

            <div class="feedback-section">
                <div class="feedback-card">
                    <h3><i class="fa-solid fa-star"></i> Key Strengths</h3>
                    <p>The speaker demonstrated a clear and audible voice tone with stable delivery. The effective use of intonation and varied pitch helped in maintaining a professional and engaging atmosphere throughout the presentation.</p>
                </div>
                <div class="feedback-card" style="border-left: 5px solid #005088;">
                    <h3><i class="fa-solid fa-arrow-trend-up"></i> Development Areas</h3>
                    <p>Maintaining a more consistent eye contact with the camera will significantly boost the perceived confidence. Additionally, incorporating more purposeful hand gestures visible to the audience will enhance the overall impact of the delivery.</p>
                </div>
            </div>
        </div>

        <footer class="footer">
            <span>Powered by PRE-AI Presentation Analytics</span>
            <span>Date: 2026.06.06 | Tracking ID: EVAL-2603113s-IND</span>
        </footer>
    </div>

</body>
</html>