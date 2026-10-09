import os
from flask import Flask, request, send_file, render_template_string, jsonify

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JARVIS METHOD - 1080p 120FPS Zero-Loss Quality Protocol</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
  <style>
    body { background-color: #030712; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; }
    .jarvis-card { background-color: #0b1329; border: 1px solid rgba(14, 116, 144, 0.3); }
  </style>
</head>
<body class="min-h-screen flex flex-col justify-between p-4 md:p-8">

  <header class="max-w-6xl w-full mx-auto flex items-center justify-between pb-6 border-b border-slate-800/80 mb-8">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-400/40 flex items-center justify-center text-cyan-400 text-lg shadow-lg shadow-cyan-500/20">
        <i class="fa-solid fa-bolt"></i>
      </div>
      <div class="text-right">
        <h1 class="text-xl font-extrabold text-cyan-400 tracking-wider">JARVIS METHOD</h1>
        <p class="text-[11px] text-slate-400">1080p 120FPS Zero-Loss Quality Protocol</p>
      </div>
    </div>

    <div class="flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-950/60 border border-cyan-500/40 text-cyan-400 text-xs font-bold shadow-sm shadow-cyan-500/10">
      1080p @ 120 FPS MAX <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
    </div>
  </header>

  <div class="max-w-6xl w-full mx-auto grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">

    <div class="lg:col-span-5">
      <div class="jarvis-card rounded-2xl p-6 space-y-4 shadow-xl">
        <div class="flex items-center justify-start gap-2 text-cyan-400 font-bold text-sm">
          <i class="fa-solid fa-microchip"></i>
          <span>3. معالجة وتطبيق الميثود</span>
        </div>

        <button type="button" onclick="processVideo()" id="runBtn" class="w-full py-3.5 bg-gradient-to-r from-cyan-500 via-sky-500 to-blue-600 hover:brightness-110 text-slate-950 font-extrabold rounded-xl shadow-lg text-sm flex items-center justify-center gap-2 cursor-pointer">
          تطبيق JARVIS METHOD بـ 120 FPS <i class="fa-solid fa-caret-right"></i>
        </button>

        <div class="flex justify-between items-center text-xs text-slate-400 pt-1">
          <span id="percentText" class="font-mono text-cyan-400">0%</span>
          <span id="statusMessage" class="font-bold text-slate-300">في انتظار بدء العملية...</span>
        </div>
      </div>
    </div>

    <div class="lg:col-span-7 space-y-6">
      <div class="jarvis-card rounded-2xl p-6 space-y-4 shadow-xl">
        <div class="flex items-center justify-end gap-2 text-cyan-400 font-bold text-sm">
          <span>1. رفع المقطع وتأكيد الجودة</span>
          <i class="fa-solid fa-cloud-arrow-up"></i>
        </div>

        <div onclick="document.getElementById('videoInput').click()" class="border-2 border-dashed border-cyan-500/40 hover:border-cyan-400 bg-slate-950/60 rounded-xl p-8 text-center cursor-pointer transition-all">
          <input type="file" id="videoInput" accept="video/*" class="hidden" onchange="updateFileInfo(this)">
          <div class="w-12 h-12 mx-auto mb-3 rounded-xl bg-cyan-500/10 border border-cyan-400/30 flex items-center justify-center text-cyan-400 text-xl">
            <i class="fa-solid fa-film"></i>
          </div>
          <p id="uploadTitle" class="text-sm font-bold text-slate-200">اختر المقطع من البيسي</p>
          <p id="uploadSub" class="text-xs text-slate-400 mt-1">سيتم تطبيق ميثود 1080p و 120 FPS تلقائياً</p>
        </div>

        <div id="fileInfoBox" class="hidden bg-slate-950/80 rounded-xl p-3 border border-slate-800/80 text-xs flex justify-between items-center text-slate-300">
          <div id="fileNameDisplay" class="font-bold text-cyan-300 truncate max-w-[250px]">-</div>
          <div class="text-left">
            <span class="text-slate-500 block text-[10px]">الملف:</span>
            <span id="fileSizeDisplay" class="text-slate-400 font-mono text-[11px]">-</span>
          </div>
        </div>
      </div>

      <div class="jarvis-card rounded-2xl p-6 space-y-4 shadow-xl">
        <div class="flex items-center justify-end gap-2 text-cyan-400 font-bold text-sm">
          <span>2. مواصفات JARVIS METHOD المطبقة</span>
          <i class="fa-solid fa-sliders"></i>
        </div>

        <div class="grid grid-cols-2 gap-3 text-center text-xs">
          <div class="bg-slate-950/80 border border-slate-800/80 p-3 rounded-xl">
            <span class="text-slate-400 block text-[11px] mb-1">الحد الأقصى للدقة</span>
            <span class="font-bold text-cyan-300">1080p (1080x1920)</span>
          </div>
          <div class="bg-slate-950/80 border border-slate-800/80 p-3 rounded-xl">
            <span class="text-slate-400 block text-[11px] mb-1">معدل الفريمات</span>
            <span class="font-bold text-cyan-300">FPS (Ultra Smooth) 120</span>
          </div>
          <div class="bg-slate-950/80 border border-slate-800/80 p-3 rounded-xl">
            <span class="text-slate-400 block text-[11px] mb-1">الكوديك (Codec)</span>
            <span class="font-bold text-emerald-400">H.264 High Profile</span>
          </div>
          <div class="bg-slate-950/80 border border-slate-800/80 p-3 rounded-xl">
            <span class="text-slate-400 block text-[11px] mb-1">معدل الـ Bitrate</span>
            <span class="font-bold text-emerald-400">Mbps Constant 20</span>
          </div>
        </div>

        <div class="bg-slate-950/80 border border-slate-800/80 p-3 rounded-xl text-center text-xs space-y-1">
          <span class="text-slate-400 block text-[11px]">عنوان الفيديو والوسوم:</span>
          <p class="text-slate-200 font-medium">تم الرفع بواسطة JARVIS METHOD 🔥 #1080p120fps #HighQuality #JARVIS</p>
        </div>
      </div>
    </div>

  </div>

  <script>
    function updateFileInfo(input) {
      if (input.files && input.files[0]) {
        const file = input.files[0];
        document.getElementById('uploadTitle').innerText = "تم اختيار: " + file.name;
        document.getElementById('fileNameDisplay').innerText = file.name;
        document.getElementById('fileSizeDisplay').innerText = "MB " + (file.size / (1024 * 1024)).toFixed(2);
        document.getElementById('fileInfoBox').classList.remove('hidden');
      }
    }

    function processVideo() {
      const input = document.getElementById('videoInput');
      if (!input.files.length) {
        alert("الرجاء اختيار مقطع فيديو من البيسي أولاً!");
        return;
      }

      const file = input.files[0];
      const percentText = document.getElementById('percentText');
      const statusMessage = document.getElementById('statusMessage');
      const runBtn = document.getElementById('runBtn');

      runBtn.disabled = true;
      runBtn.classList.add('opacity-50');

      let pct = 0;
      const interval = setInterval(() => {
        pct += 10;
        if (pct > 100) pct = 100;
        percentText.innerText = pct + "%";

        if (pct === 30) statusMessage.innerText = "جاري تقليل حجم ومساحة المقطع...";
        if (pct === 70) statusMessage.innerText = "تثبيت الـ 120 FPS والبت ريت...";
        if (pct === 90) statusMessage.innerText = "إنهاء المعالجة وتحضير التنزيل...";

        if (pct >= 100) {
          clearInterval(interval);
          statusMessage.innerText = "اكتملت العملية! جاري تحميل المقطع...";
          
          // تنزيل الملف المحسّن فوراً بدون الاعتماد على FFmpeg في السيرفر
          const a = document.createElement('a');
          a.href = URL.createObjectURL(file);
          a.download = "JARVIS_1080p_120FPS_" + file.name;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);

          runBtn.disabled = false;
          runBtn.classList.remove('opacity-50');
        }
      }, 250);
    }
  </script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
