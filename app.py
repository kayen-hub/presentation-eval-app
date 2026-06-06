import streamlit as st
import base64
import time

# ページ基本設定（横型ダッシュボードを意識したワイド表示）
st.set_page_config(page_title="PRE-AI Presentation Analytics", layout="wide")

# タイトルエリア
st.title("📊 PRE-AI Presentation Analytics Dashboard")
st.subheader("学生個別プレゼンテーション自動評価システム")
st.markdown("---")

# ファイルアップロードと学生IDの入力
col_input1, col_input2 = st.columns([1, 2])
with col_input1:
    student_id = st.text_input("👤 学生識別IDを入力 (例: 2603113s)", "").strip()
with col_input2:
    uploaded_file = st.file_uploader("🎥 プレゼンテーション動画をアップロード (.mp4, .mov)", type=["mp4", "mov"])

if uploaded_file and student_id:
    st.info(f"ID: {student_id} のビデオファイルを解析中... (モック自動評価プロセス)")
    
    # 処理の進捗バー表示
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
        
    st.success("🎉 解析が完了しました！評価スコアを調整してPDFを出力してください。")
    st.markdown("---")

    # 評価スコアの調整・確認セクション
    st.write("### 📝 スコア確認・調整")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1: ec = st.slider("Eye Contact", 0, 5, 3)
    with c2: gst = st.slider("Gestures", 0, 5, 3)
    with c3: itn = st.slider("Intonation", 0, 5, 4)
    with c4: tone = st.slider("Tone", 0, 5, 4)
    with c5: rhy = st.slider("Rhythm", 0, 5, 3)
    with c6: smth = st.slider("Smoothness", 0, 5, 3)
    
    total_score = ec + gst + itn + tone + rhy + smth
    
    # コメント入力エリア（デフォルトで共通統一フォーマットを適用）
    st.write("### 💬 フィードバックコメント (英語)")
    col_fb1, col_fb2 = st.columns(2)
    with col_fb1:
        strengths = st.text_area("Key Strengths", "The speaker demonstrated a clear and audible voice tone with stable delivery. The effective use of intonation and varied pitch helped in maintaining a professional and engaging atmosphere.")
    with col_fb2:
        developments = st.text_area("Development Areas", "Maintaining a more consistent eye contact with the camera will significantly boost the perceived confidence. Additionally, incorporating more purposeful hand gestures visible to the audience will enhance the overall impact.")

    # 統一デザインのHTMLテンプレート生成ロジック
    import math
    def calc_point(score, angle_idx):
        angles = [-90, -30, 30, 90, 150, 210]
        rad = math.radians(angles[angle_idx])
        length = 24 * score
        x = 150 + length * math.cos(rad)
        y = 150 + length * math.sin(rad)
        return f"{x},{y}"

    poly_points = f"{calc_point(ec,0)} {calc_point(gst,1)} {calc_point(itn,2)} {calc_point(tone,3)} {calc_point(rhy,4)} {calc_point(smth,5)}"

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{ size: A4 landscape; margin: 12mm; background-color: #f8fafc; }}
            * {{ box-sizing: border-box; }}
            body {{ margin: 0; padding: 0; font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e293b; background-color: #f8fafc; }}
            .container {{ background-color: #ffffff; border-radius: 8px; padding: 24px; border: 1px solid #e2e8f0; height: 100%; }}
            .header {{ border-bottom: 3px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px; }}
            .header-table {{ width: 100%; border-collapse: collapse; }}
            .title {{ font-size: 24pt; font-weight: bold; color: #0f172a; margin: 0; }}
            .subtitle {{ font-size: 11pt; color: #0284c7; margin-top: 4px; font-weight: bold; }}
            .id-box {{ text-align: right; vertical-align: bottom; }}
            .id-label {{ font-size: 9pt; color: #64748b; font-weight: bold; }}
            .id-value {{ font-size: 20pt; font-weight: bold; color: #0284c7; font-family: monospace; }}
            .main-layout {{ width: 100%; border-collapse: collapse; }}
            .left-col {{ width: 40%; vertical-align: top; padding-right: 20px; }}
            .right-col {{ width: 60%; vertical-align: top; padding-left: 20px; }}
            .score-table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
            .score-table th {{ background-color: #0f172a; color: #ffffff; padding: 10px; font-size: 11pt; text-align: left; }}
            .score-table td {{ padding: 10px; font-size: 11pt; border-bottom: 1px solid #e2e8f0; }}
            .score-val {{ text-align: center; font-weight: bold; color: #0284c7; font-size: 12pt; }}
            .total-box {{ background-color: #0f172a; color: #ffffff; padding: 16px; border-radius: 6px; text-align: center; }}
            .total-label {{ font-size: 12pt; font-weight: bold; display: block; margin-bottom: 4px; }}
            .total-score {{ font-size: 28pt; font-weight: bold; color: #38bdf8; }}
            .chart-box {{ background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px; text-align: center; margin-bottom: 20px; }}
            .feedback-box {{ background-color: #f1f5f9; border-radius: 6px; padding: 16px; margin-bottom: 12px; border-left: 4px solid #38bdf8; }}
            .feedback-box.strength {{ border-left-color: #10b981; background-color: #f0fdf4; }}
            .feedback-title {{ font-size: 11pt; font-weight: bold; margin-bottom: 6px; color: #0f172a; }}
            .feedback-desc {{ font-size: 10pt; line-height: 1.5; color: #334155; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <table class="header-table">
                    <tr>
                        <td>
                            <div class="title">Presentation Evaluation Report</div>
                            <div class="subtitle">INDIVIDUAL PRESENTATION ASSESSMENT</div>
                        </td>
                        <td class="id-box">
                            <div class="id-label">STUDENT ID</div>
                            <div class="id-value">{student_id}</div>
                        </td>
                    </tr>
                </table>
            </div>
            <table class="main-layout">
                <tr>
                    <td class="left-col">
                        <table class="score-table">
                            <thead>
                                <tr><th>Evaluation Criteria</th><th style="text-align: center; width: 80px;">Score</th></tr>
                            </thead>
                            <tbody>
                                <tr><td>Eye Contact</td><td class="score-val">{ec}</td></tr>
                                <tr><td>Gestures</td><td class="score-val">{gst}</td></tr>
                                <tr><td>Intonation</td><td class="score-val">{itn}</td></tr>
                                <tr><td>Tone</td><td class="score-val">{tone}</td></tr>
                                <tr><td>Rhythm</td><td class="score-val">{rhy}</td></tr>
                                <tr><td>Overall Smoothness</td><td class="score-val">{smth}</td></tr>
                            </tbody>
                        </table>
                        <div class="total-box">
                            <span class="total-label">TOTAL SCORE</span>
                            <span class="total-score">{total_score} <span style="font-size: 14pt; color: #94a3b8;">/ 30</span></span>
                        </div>
                    </td>
                    <td class="right-col">
                        <div class="chart-box">
                            <svg width="240" height="200" viewBox="0 0 300 260">
                                <polygon points="150,30 254,90 254,210 150,270 46,210 46,90" fill="none" stroke="#cbd5e1" stroke-width="1"/>
                                <polygon points="150,54 233,102 233,198 150,246 67,198 67,102" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                                <polygon points="150,78 212,114 212,186 150,222 88,186 88,114" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                                <polygon points="150,102 191,126 191,174 150,198 109,174 109,126" fill="none" stroke="#e2e8f0" stroke-width="1"/>
                                <line x1="150" y1="150" x2="150" y2="30" stroke="#cbd5e1" stroke-width="1"/>
                                <line x1="150" y1="150" x2="254" y2="90" stroke="#cbd5e1" stroke-width="1"/>
                                <line x1="150" y1="150" x2="254" y2="210" stroke="#cbd5e1" stroke-width="1"/>
                                <line x1="150" y1="150" x2="150" y2="270" stroke="#cbd5e1" stroke-width="1"/>
                                <line x1="150" y1="150" x2="46" y2="210" stroke="#cbd5e1" stroke-width="1"/>
                                <line x1="150" y1="150" x2="46" y2="90" stroke="#cbd5e1" stroke-width="1"/>
                                <polygon points="{poly_points}" fill="rgba(2, 132, 199, 0.2)" stroke="#0284c7" stroke-width="2.5"/>
                                <text x="150" y="20" text-anchor="middle" font-size="9pt" font-weight="bold" fill="#475569">Eye Contact</text>
                                <text x="262" y="85" text-anchor="start" font-size="9pt" font-weight="bold" fill="#475569">Gestures</text>
                                <text x="262" y="205" text-anchor="start" font-size="9pt" font-weight="bold" fill="#475569">Intonation</text>
                                <text x="150" y="285" text-anchor="middle" font-size="9pt" font-weight="bold" fill="#475569">Tone</text>
                                <text x="38" y="205" text-anchor="end" font-size="9pt" font-weight="bold" fill="#475569">Rhythm</text>
                                <text x="38" y="85" text-anchor="end" font-size="9pt" font-weight="bold" fill="#475569">Smoothness</text>
                            </svg>
                        </div>
                        <div class="feedback-box strength">
                            <div class="feedback-title" style="color: #065f46;">★ Key Strengths</div>
                            <div class="feedback-desc">{strengths}</div>
                        </div>
                        <div class="feedback-box">
                            <div class="feedback-title" style="color: #0369a1;">▲ Development Areas</div>
                            <div class="feedback-desc">{developments}</div>
                        </div>
                    </td>
                </tr>
            </table>
            <table style="width:100%; margin-top:15px; font-size:8pt; color:#94a3b8; border-top:1px solid #e2e8f0; padding-top:5px;">
                <tr>
                    <td>Powered by AI Presentation Analysis Engine</td>
                    <td style="text-align:right;">Date: 2026.06.06 | Report ID: {student_id}-IND</td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """

    filename = f"Presentation_Evaluation_Report_{student_id}.html"
    b64 = base64.b64encode(html_template.encode('utf-8')).decode()
    
    st.markdown("---")
    st.write("### 📥 レポート出力")
    st.info("ブラウザの『PDFとして保存』機能を利用して、100%同じレイアウトで完璧にA4横サイズ保存できる形式で出力します。")
    
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}" style="text-decoration:none;"><div style="background-color:#0284c7;color:white;padding:12px 24px;border-radius:6px;text-align:center;font-weight:bold;display:inline-block;font-size:16px;">📥 【識別ID付与】{filename} をダウンロード</div></a>'
    st.markdown(href, unsafe_allow_html=True)
else:
    st.warning("動画ファイルのアップロードと学生識別IDを入力してください。")
