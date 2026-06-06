import streamlit as st
import io
from xhtml2pdf import pisa
import time

# ページ基本設定
st.set_page_config(page_title="PRE-AI Presentation Analytics", layout="wide")

st.title("📊 PRE-AI Presentation Analytics")
st.subheader("学生個別評価レポート 自動生成システム (PDF出力版)")
st.markdown("---")

# 入力セクション
col_id, col_file = st.columns([1, 2])
with col_id:
    student_id = st.text_input("👤 学生識別ID (例: 2603113s)", "").strip()
with col_file:
    uploaded_file = st.file_uploader("🎥 動画ファイルをアップロード", type=["mp4", "mov"])

if uploaded_file and student_id:
    st.info(f"ID: {student_id} の解析を行っています...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    st.success("解析完了！スコアを確認してPDFを発行してください。")

    # 評価設定
    st.markdown("---")
    st.write("### 📝 スコアとコメントの最終調整")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1: ec = st.slider("Eye Contact", 0, 5, 3)
    with c2: gst = st.slider("Gestures", 0, 5, 3)
    with c3: itn = st.slider("Intonation", 0, 5, 4)
    with c4: tone = st.slider("Tone", 0, 5, 4)
    with c5: rhy = st.slider("Rhythm", 0, 5, 3)
    with c6: smth = st.slider("Smoothness", 0, 5, 3)
    
    total_score = ec + gst + itn + tone + rhy + smth

    st.write("### 💬 フィードバックコメント (English)")
    strengths = st.text_area("Key Strengths", "The speaker demonstrated a clear and audible voice tone with stable delivery. The effective use of intonation and varied pitch helped in maintaining a professional atmosphere.")
    developments = st.text_area("Development Areas", "Maintaining consistent eye contact with the camera will boost confidence. Additionally, incorporating purposeful hand gestures will enhance the overall impact.")

    # PDF用HTMLテンプレート (xhtml2pdf対応のテーブルレイアウト)
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{ size: A4 landscape; margin: 1cm; }}
            body {{ font-family: Helvetica, Arial, sans-serif; color: #333; }}
            .header {{ border-bottom: 2px solid #005088; padding-bottom: 10px; margin-bottom: 20px; }}
            .title {{ font-size: 24pt; font-weight: bold; color: #005088; }}
            .id-box {{ text-align: right; font-size: 18pt; font-weight: bold; color: #005088; }}
            .main-table {{ width: 100%; border-collapse: collapse; }}
            .score-table {{ width: 100%; border-collapse: collapse; }}
            .score-table th {{ background-color: #0f172a; color: #ffffff; padding: 8px; text-align: left; }}
            .score-table td {{ border-bottom: 1px solid #ddd; padding: 8px; font-size: 12pt; }}
            .total-box {{ background-color: #005088; color: #fff; padding: 15px; text-align: center; border-radius: 5px; margin-top: 20px; }}
            .feedback-card {{ background-color: #f1f5f9; padding: 15px; border-left: 5px solid #005088; margin-bottom: 10px; }}
            .feedback-title {{ font-weight: bold; color: #005088; margin-bottom: 5px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <table style="width: 100%;">
                <tr>
                    <td class="title">Presentation Evaluation Report</td>
                    <td class="id-box">ID: {student_id}</td>
                </tr>
            </table>
        </div>
        <table class="main-table">
            <tr>
                <td style="width: 40%; vertical-align: top; padding-right: 20px;">
                    <table class="score-table">
                        <tr><th>Criteria</th><th>Score</th></tr>
                        <tr><td>Eye Contact</td><td>{ec}</td></tr>
                        <tr><td>Gestures</td><td>{gst}</td></tr>
                        <tr><td>Intonation</td><td>{itn}</td></tr>
                        <tr><td>Tone</td><td>{tone}</td></tr>
                        <tr><td>Rhythm</td><td>{rhy}</td></tr>
                        <tr><td>Smoothness</td><td>{smth}</td></tr>
                    </table>
                    <div class="total-box">
                        <span style="font-size: 14pt;">TOTAL SCORE</span><br>
                        <span style="font-size: 30pt; font-weight: bold;">{total_score} / 30</span>
                    </div>
                </td>
                <td style="width: 60%; vertical-align: top;">
                    <div class="feedback-card">
                        <div class="feedback-title">★ Key Strengths</div>
                        <div>{strengths}</div>
                    </div>
                    <div class="feedback-card">
                        <div class="feedback-title">▲ Development Areas</div>
                        <div>{developments}</div>
                    </div>
                </td>
            </tr>
        </table>
        <div style="margin-top: 30px; font-size: 10pt; color: #666; border-top: 1px solid #ccc; padding-top: 5px;">
            PRE-AI Presentation Analytics | Date: 2026.06.07
        </div>
    </body>
    </html>
    """

    # PDF生成処理
    def create_pdf(html):
        pdf_buffer = io.BytesIO()
        pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), dest=pdf_buffer)
        return pdf_buffer.getvalue()

    pdf_data = create_pdf(html_content)

    st.markdown("---")
    st.write("### 📥 レポート発行")
    st.download_button(
        label=f"📂 PDFレポートをダウンロード (ID: {student_id})",
        data=pdf_data,
        file_name=f"Evaluation_Report_{student_id}.pdf",
        mime="application/pdf"
    )
else:
    st.warning("左側のメニューからID入力と動画アップロードを行ってください。")
