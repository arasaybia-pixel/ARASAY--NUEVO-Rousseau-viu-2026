#!/usr/bin/env python3
"""
Script para generar la infografía interactiva de Rousseau
con imágenes base64, diseño naranja VIU, firma Dra. Arasay Padrón Alvarez
"""
import base64

def img_b64(path, mime):
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    return f'data:{mime};base64,{data}'

# Cargar imágenes
portrait    = img_b64('img/rousseau_portrait.png', 'image/png')
contrat     = img_b64('img/contrat_social.jpg', 'image/jpeg')
emile       = img_b64('img/emile_cover.jpg', 'image/jpeg')
geneva      = img_b64('img/geneva_1780.jpg', 'image/jpeg')
nature      = img_b64('img/rousseau_nature.jpg', 'image/jpeg')
childhood   = img_b64('img/rousseau_childhood.jpg', 'image/jpeg')

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Repensando a Rousseau · Infografía Interactiva · VIU</title>
<style>
/* ===== RESET & BASE ===== */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --naranja:#E8560A;
  --naranja-claro:#FF7A35;
  --naranja-oscuro:#C04000;
  --naranja-suave:#FFF0E8;
  --naranja-medio:#FFB380;
  --gris-oscuro:#1A1A2E;
  --gris-medio:#2D2D44;
  --gris-claro:#F5F5F5;
  --blanco:#FFFFFF;
  --texto-oscuro:#1A1A1A;
  --texto-medio:#444444;
  --sombra:0 4px 20px rgba(232,86,10,0.15);
  --sombra-hover:0 8px 32px rgba(232,86,10,0.30);
  --radius:14px;
  --radius-sm:8px;
}}
html{{scroll-behavior:smooth}}
body{{
  font-family:'Segoe UI',system-ui,-apple-system,sans-serif;
  background:#0F0F1A;
  color:var(--blanco);
  line-height:1.6;
  overflow-x:hidden;
}}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar{{width:8px}}
::-webkit-scrollbar-track{{background:#1A1A2E}}
::-webkit-scrollbar-thumb{{background:var(--naranja);border-radius:4px}}

/* ===== NAV ===== */
nav{{
  position:fixed;top:0;left:0;right:0;z-index:1000;
  background:rgba(15,15,26,0.95);
  backdrop-filter:blur(12px);
  border-bottom:2px solid var(--naranja);
  padding:0 20px;
  display:flex;align-items:center;justify-content:space-between;
  height:58px;
}}
.nav-logo{{
  font-size:1rem;font-weight:700;
  color:var(--naranja-claro);
  letter-spacing:0.5px;
  white-space:nowrap;
}}
.nav-links{{
  display:flex;gap:4px;flex-wrap:wrap;
  list-style:none;
}}
.nav-links a{{
  color:rgba(255,255,255,0.8);
  text-decoration:none;
  font-size:0.78rem;font-weight:500;
  padding:5px 10px;
  border-radius:20px;
  transition:all .25s;
  white-space:nowrap;
}}
.nav-links a:hover{{
  background:var(--naranja);
  color:#fff;
}}

/* ===== HERO ===== */
.hero{{
  min-height:100vh;
  background:linear-gradient(135deg,#0F0F1A 0%,#1A0A00 40%,#2A1000 70%,#0F0F1A 100%);
  display:flex;align-items:center;justify-content:center;
  position:relative;overflow:hidden;
  padding:80px 20px 40px;
}}
.hero::before{{
  content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse at 30% 50%,rgba(232,86,10,0.12) 0%,transparent 60%),
             radial-gradient(ellipse at 70% 30%,rgba(255,122,53,0.08) 0%,transparent 50%);
}}
.hero-content{{
  max-width:1100px;width:100%;
  display:grid;grid-template-columns:1fr 1fr;gap:60px;
  align-items:center;position:relative;z-index:1;
}}
.hero-text .badge{{
  display:inline-block;
  background:var(--naranja);
  color:#fff;
  font-size:0.72rem;font-weight:700;
  letter-spacing:2px;text-transform:uppercase;
  padding:5px 16px;border-radius:20px;
  margin-bottom:20px;
}}
.hero-text h1{{
  font-size:clamp(2.2rem,5vw,3.8rem);
  font-weight:900;line-height:1.1;
  margin-bottom:16px;
}}
.hero-text h1 span{{
  background:linear-gradient(135deg,var(--naranja-claro),var(--naranja-oscuro));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}}
.hero-text .subtitle{{
  font-size:1.05rem;color:rgba(255,255,255,0.7);
  margin-bottom:24px;line-height:1.7;
}}
.hero-text .firma{{
  font-size:0.9rem;
  color:var(--naranja-medio);
  font-style:italic;
  border-left:3px solid var(--naranja);
  padding-left:12px;
  margin-bottom:30px;
}}
.hero-btns{{display:flex;gap:12px;flex-wrap:wrap}}
.btn-primary{{
  background:linear-gradient(135deg,var(--naranja),var(--naranja-oscuro));
  color:#fff;border:none;
  padding:12px 28px;border-radius:30px;
  font-size:0.9rem;font-weight:700;
  cursor:pointer;text-decoration:none;
  transition:all .3s;
  box-shadow:0 4px 15px rgba(232,86,10,0.4);
}}
.btn-primary:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(232,86,10,0.5)}}
.btn-outline{{
  background:transparent;
  color:var(--naranja-claro);
  border:2px solid var(--naranja-claro);
  padding:11px 26px;border-radius:30px;
  font-size:0.9rem;font-weight:700;
  cursor:pointer;text-decoration:none;
  transition:all .3s;
}}
.btn-outline:hover{{background:var(--naranja-claro);color:#fff}}

.hero-image-wrap{{
  position:relative;
  display:flex;justify-content:center;align-items:center;
}}
.hero-portrait{{
  width:320px;height:380px;
  object-fit:cover;object-position:top;
  border-radius:var(--radius);
  border:3px solid var(--naranja);
  box-shadow:0 0 60px rgba(232,86,10,0.4);
  position:relative;z-index:2;
}}
.hero-portrait-ring{{
  position:absolute;
  width:360px;height:420px;
  border:2px dashed rgba(232,86,10,0.3);
  border-radius:var(--radius);
  animation:spin-slow 20s linear infinite;
}}
@keyframes spin-slow{{to{{transform:rotate(360deg)}}}}
.hero-dates{{
  position:absolute;bottom:-20px;left:50%;transform:translateX(-50%);
  background:var(--naranja);
  color:#fff;font-weight:700;font-size:1rem;
  padding:8px 24px;border-radius:20px;
  white-space:nowrap;z-index:3;
  box-shadow:0 4px 15px rgba(232,86,10,0.5);
}}

/* ===== SECTION BASE ===== */
section{{padding:80px 20px}}
.section-inner{{max-width:1100px;margin:0 auto}}
.section-header{{text-align:center;margin-bottom:50px}}
.section-num{{
  display:inline-block;
  width:44px;height:44px;line-height:44px;
  background:var(--naranja);
  color:#fff;font-weight:900;font-size:1.1rem;
  border-radius:50%;margin-bottom:16px;
}}
.section-header h2{{
  font-size:clamp(1.6rem,3.5vw,2.4rem);
  font-weight:800;margin-bottom:10px;
}}
.section-header h2 span{{color:var(--naranja-claro)}}
.section-header p{{
  color:rgba(255,255,255,0.65);
  font-size:1rem;max-width:600px;margin:0 auto;
}}

/* ===== MANUS SECTION ===== */
#manus{{background:linear-gradient(180deg,#0F0F1A 0%,#1A0800 100%)}}
.manus-intro{{
  display:grid;grid-template-columns:1fr 1fr;gap:40px;
  align-items:center;margin-bottom:50px;
}}
.manus-intro-text h3{{
  font-size:1.5rem;font-weight:700;
  color:var(--naranja-claro);margin-bottom:16px;
}}
.manus-intro-text p{{
  color:rgba(255,255,255,0.75);line-height:1.8;margin-bottom:12px;
}}
.manus-intro-text .highlight{{
  background:rgba(232,86,10,0.15);
  border-left:4px solid var(--naranja);
  padding:12px 16px;border-radius:0 var(--radius-sm) var(--radius-sm) 0;
  font-style:italic;color:rgba(255,255,255,0.85);
  font-size:0.95rem;
}}
.video-wrap{{
  border-radius:var(--radius);overflow:hidden;
  border:2px solid var(--naranja);
  box-shadow:0 0 40px rgba(232,86,10,0.3);
  aspect-ratio:16/9;
}}
.video-wrap iframe{{width:100%;height:100%;border:none}}

.steps-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  margin-bottom:40px;
}}
.step-card{{
  background:rgba(232,86,10,0.08);
  border:1px solid rgba(232,86,10,0.25);
  border-radius:var(--radius);
  padding:22px;
  transition:all .3s;
  position:relative;overflow:hidden;
}}
.step-card::before{{
  content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,var(--naranja),var(--naranja-claro));
}}
.step-card:hover{{
  background:rgba(232,86,10,0.15);
  transform:translateY(-4px);
  box-shadow:var(--sombra-hover);
}}
.step-num{{
  display:inline-block;
  background:var(--naranja);
  color:#fff;font-weight:700;font-size:0.75rem;
  padding:3px 10px;border-radius:12px;
  margin-bottom:10px;letter-spacing:1px;
}}
.step-icon{{font-size:1.8rem;margin-bottom:8px;display:block}}
.step-card h4{{font-size:0.95rem;font-weight:700;margin-bottom:6px;color:var(--naranja-claro)}}
.step-card p{{font-size:0.82rem;color:rgba(255,255,255,0.7);line-height:1.6}}

.uses-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:16px;
}}
.use-card{{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.1);
  border-radius:var(--radius-sm);
  padding:18px;
  transition:all .3s;
}}
.use-card:hover{{
  background:rgba(232,86,10,0.12);
  border-color:var(--naranja);
}}
.use-card .use-icon{{font-size:1.5rem;margin-bottom:8px}}
.use-card h5{{font-size:0.88rem;font-weight:700;color:var(--naranja-claro);margin-bottom:5px}}
.use-card p{{font-size:0.78rem;color:rgba(255,255,255,0.65);line-height:1.5}}

/* ===== BIOGRAFIA ===== */
#biografia{{background:linear-gradient(180deg,#1A0800 0%,#0F0F1A 100%)}}
.bio-layout{{
  display:grid;grid-template-columns:1fr 2fr;gap:40px;
  margin-bottom:50px;
}}
.bio-portrait-col{{
  display:flex;flex-direction:column;align-items:center;gap:20px;
}}
.bio-portrait{{
  width:100%;max-width:280px;
  border-radius:var(--radius);
  border:3px solid var(--naranja);
  box-shadow:0 0 40px rgba(232,86,10,0.35);
}}
.bio-quote{{
  background:rgba(232,86,10,0.12);
  border:1px solid rgba(232,86,10,0.3);
  border-radius:var(--radius-sm);
  padding:16px;
  font-style:italic;
  font-size:0.85rem;
  color:rgba(255,255,255,0.8);
  text-align:center;
}}
.bio-quote cite{{
  display:block;margin-top:8px;
  color:var(--naranja-claro);font-size:0.75rem;font-style:normal;font-weight:600;
}}
.context-cards{{
  display:grid;grid-template-columns:1fr 1fr;gap:16px;
  margin-bottom:20px;
}}
.ctx-card{{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(232,86,10,0.2);
  border-radius:var(--radius-sm);
  padding:16px;
  transition:all .3s;
}}
.ctx-card:hover{{border-color:var(--naranja);background:rgba(232,86,10,0.1)}}
.ctx-card .ctx-icon{{font-size:1.6rem;margin-bottom:8px}}
.ctx-card h4{{font-size:0.9rem;font-weight:700;color:var(--naranja-claro);margin-bottom:5px}}
.ctx-card p{{font-size:0.8rem;color:rgba(255,255,255,0.7);line-height:1.5}}

/* TIMELINE */
.timeline-wrap{{margin-top:20px}}
.timeline-img{{
  width:100%;border-radius:var(--radius);
  border:2px solid rgba(232,86,10,0.3);
  margin-bottom:30px;
  max-height:200px;object-fit:cover;
}}
.timeline{{position:relative;padding-left:30px}}
.timeline::before{{
  content:'';position:absolute;left:8px;top:0;bottom:0;
  width:2px;background:linear-gradient(180deg,var(--naranja),transparent);
}}
.tl-item{{
  position:relative;margin-bottom:28px;
}}
.tl-dot{{
  position:absolute;left:-26px;top:4px;
  width:16px;height:16px;
  background:var(--naranja);border-radius:50%;
  border:2px solid #0F0F1A;
  box-shadow:0 0 8px rgba(232,86,10,0.6);
}}
.tl-year{{
  font-size:0.75rem;font-weight:700;
  color:var(--naranja);letter-spacing:1px;
  text-transform:uppercase;margin-bottom:4px;
}}
.tl-item h4{{font-size:0.95rem;font-weight:700;margin-bottom:4px}}
.tl-item p{{font-size:0.82rem;color:rgba(255,255,255,0.7);line-height:1.5}}

/* ===== IDEAS ===== */
#ideas{{background:linear-gradient(180deg,#0F0F1A 0%,#1A0800 100%)}}
.ideas-hero-img{{
  width:100%;max-height:280px;object-fit:cover;
  border-radius:var(--radius);
  border:2px solid rgba(232,86,10,0.4);
  margin-bottom:40px;
}}
.ideas-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  margin-bottom:40px;
}}
.idea-card{{
  background:rgba(232,86,10,0.07);
  border:1px solid rgba(232,86,10,0.2);
  border-radius:var(--radius);
  padding:24px;
  transition:all .35s;
  cursor:pointer;
}}
.idea-card:hover{{
  background:rgba(232,86,10,0.18);
  border-color:var(--naranja);
  transform:translateY(-5px);
  box-shadow:var(--sombra-hover);
}}
.idea-icon{{font-size:2rem;margin-bottom:12px;display:block}}
.idea-card h3{{
  font-size:1rem;font-weight:700;
  color:var(--naranja-claro);margin-bottom:8px;
}}
.idea-card p{{font-size:0.82rem;color:rgba(255,255,255,0.72);line-height:1.6}}
.idea-quote{{
  font-style:italic;
  font-size:0.78rem;
  color:rgba(255,180,100,0.85);
  border-top:1px solid rgba(232,86,10,0.2);
  margin-top:10px;padding-top:10px;
}}

/* ETAPAS */
.etapas-title{{
  font-size:1.2rem;font-weight:700;
  color:var(--naranja-claro);
  margin-bottom:20px;
  display:flex;align-items:center;gap:10px;
}}
.etapas-flow{{
  display:flex;gap:0;
  overflow-x:auto;padding-bottom:10px;
}}
.etapa{{
  flex:1;min-width:160px;
  background:rgba(232,86,10,0.08);
  border:1px solid rgba(232,86,10,0.2);
  border-radius:0;
  padding:20px 16px;
  text-align:center;
  position:relative;
  transition:all .3s;
}}
.etapa:first-child{{border-radius:var(--radius) 0 0 var(--radius)}}
.etapa:last-child{{border-radius:0 var(--radius) var(--radius) 0}}
.etapa:not(:last-child)::after{{
  content:'→';
  position:absolute;right:-12px;top:50%;transform:translateY(-50%);
  color:var(--naranja);font-size:1.2rem;z-index:1;
}}
.etapa:hover{{background:rgba(232,86,10,0.2)}}
.etapa-age{{
  font-size:0.7rem;font-weight:700;
  color:var(--naranja);letter-spacing:1px;
  text-transform:uppercase;margin-bottom:4px;
}}
.etapa-icon{{font-size:1.5rem;margin-bottom:6px}}
.etapa h4{{font-size:0.82rem;font-weight:700;margin-bottom:4px}}
.etapa p{{font-size:0.72rem;color:rgba(255,255,255,0.65);line-height:1.4}}

/* ===== OBRAS ===== */
#obras{{background:linear-gradient(180deg,#1A0800 0%,#0F0F1A 100%)}}
.obras-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:24px;
}}
.obra-card{{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(232,86,10,0.2);
  border-radius:var(--radius);
  overflow:hidden;
  transition:all .35s;
}}
.obra-card:hover{{
  border-color:var(--naranja);
  transform:translateY(-6px);
  box-shadow:var(--sombra-hover);
}}
.obra-img{{
  width:100%;height:180px;
  object-fit:cover;
  border-bottom:2px solid rgba(232,86,10,0.3);
}}
.obra-body{{padding:18px}}
.obra-year{{
  font-size:0.72rem;font-weight:700;
  color:var(--naranja);letter-spacing:1px;
  text-transform:uppercase;margin-bottom:6px;
}}
.obra-card h3{{font-size:0.95rem;font-weight:700;margin-bottom:8px}}
.obra-card p{{font-size:0.8rem;color:rgba(255,255,255,0.7);line-height:1.5;margin-bottom:10px}}
.obra-tags{{display:flex;gap:6px;flex-wrap:wrap}}
.tag{{
  font-size:0.68rem;font-weight:600;
  background:rgba(232,86,10,0.2);
  color:var(--naranja-claro);
  padding:3px 10px;border-radius:12px;
  border:1px solid rgba(232,86,10,0.3);
}}

/* ===== LEGADO ===== */
#legado{{background:linear-gradient(180deg,#0F0F1A 0%,#1A0800 100%)}}
.legado-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  margin-bottom:40px;
}}
.legado-card{{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:var(--radius);
  padding:20px;
  text-align:center;
  transition:all .3s;
}}
.legado-card:hover{{
  border-color:var(--naranja);
  background:rgba(232,86,10,0.1);
}}
.legado-img{{
  width:70px;height:70px;
  border-radius:50%;
  object-fit:cover;
  border:2px solid var(--naranja);
  margin:0 auto 12px;
  display:block;
}}
.legado-avatar{{
  width:70px;height:70px;
  border-radius:50%;
  background:linear-gradient(135deg,var(--naranja),var(--naranja-oscuro));
  display:flex;align-items:center;justify-content:center;
  font-size:1.8rem;
  margin:0 auto 12px;
  border:2px solid var(--naranja);
}}
.legado-card h4{{font-size:0.9rem;font-weight:700;color:var(--naranja-claro);margin-bottom:6px}}
.legado-card p{{font-size:0.78rem;color:rgba(255,255,255,0.68);line-height:1.5}}

/* ===== ACTIVIDAD ===== */
#actividad{{background:linear-gradient(180deg,#1A0800 0%,#0F0F1A 100%)}}
.actividad-intro{{
  background:rgba(232,86,10,0.1);
  border:2px solid var(--naranja);
  border-radius:var(--radius);
  padding:28px;
  margin-bottom:40px;
  text-align:center;
}}
.actividad-intro h3{{
  font-size:1.3rem;font-weight:700;
  color:var(--naranja-claro);margin-bottom:10px;
}}
.actividad-intro p{{color:rgba(255,255,255,0.8);font-size:0.95rem}}
.roles-grid{{
  display:grid;grid-template-columns:repeat(4,1fr);gap:16px;
  margin-bottom:40px;
}}
.rol-card{{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(232,86,10,0.2);
  border-radius:var(--radius);
  padding:20px;
  text-align:center;
  transition:all .3s;
}}
.rol-card:hover{{border-color:var(--naranja);background:rgba(232,86,10,0.12)}}
.rol-icon{{font-size:2rem;margin-bottom:10px}}
.rol-card h4{{font-size:0.9rem;font-weight:700;color:var(--naranja-claro);margin-bottom:6px}}
.rol-card p{{font-size:0.78rem;color:rgba(255,255,255,0.68);line-height:1.5}}
.tareas-title{{
  font-size:1.1rem;font-weight:700;
  color:var(--naranja-claro);margin-bottom:20px;
}}
.tareas-list{{
  display:flex;flex-direction:column;gap:12px;
  margin-bottom:40px;
}}
.tarea-item{{
  display:flex;align-items:flex-start;gap:16px;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(232,86,10,0.15);
  border-radius:var(--radius-sm);
  padding:16px;
  transition:all .3s;
}}
.tarea-item:hover{{border-color:var(--naranja);background:rgba(232,86,10,0.08)}}
.tarea-num{{
  min-width:36px;height:36px;
  background:var(--naranja);
  color:#fff;font-weight:700;font-size:0.9rem;
  border-radius:50%;
  display:flex;align-items:center;justify-content:center;
}}
.tarea-content h4{{font-size:0.9rem;font-weight:700;margin-bottom:4px;color:var(--naranja-claro)}}
.tarea-content p{{font-size:0.8rem;color:rgba(255,255,255,0.7);line-height:1.5}}

/* ===== QUIZ ===== */
#quiz{{background:linear-gradient(180deg,#0F0F1A 0%,#1A0800 100%)}}
.quiz-container{{
  max-width:750px;margin:0 auto;
}}
.quiz-progress-bar{{
  height:6px;background:rgba(255,255,255,0.1);
  border-radius:3px;margin-bottom:30px;overflow:hidden;
}}
.quiz-progress-fill{{
  height:100%;
  background:linear-gradient(90deg,var(--naranja),var(--naranja-claro));
  border-radius:3px;
  transition:width .5s ease;
  width:10%;
}}
.quiz-card{{
  background:rgba(255,255,255,0.05);
  border:1px solid rgba(232,86,10,0.25);
  border-radius:var(--radius);
  padding:32px;
  min-height:300px;
}}
.quiz-meta{{
  display:flex;justify-content:space-between;align-items:center;
  margin-bottom:20px;
}}
.quiz-counter{{
  font-size:0.8rem;font-weight:700;
  color:var(--naranja);letter-spacing:1px;
}}
.quiz-category{{
  font-size:0.75rem;font-weight:600;
  background:rgba(232,86,10,0.2);
  color:var(--naranja-claro);
  padding:4px 12px;border-radius:12px;
}}
.quiz-question{{
  font-size:1.1rem;font-weight:600;
  line-height:1.6;margin-bottom:24px;
}}
.quiz-options{{
  display:flex;flex-direction:column;gap:10px;
  margin-bottom:20px;
}}
.quiz-opt{{
  background:rgba(255,255,255,0.06);
  border:2px solid rgba(255,255,255,0.1);
  border-radius:var(--radius-sm);
  padding:12px 18px;
  cursor:pointer;
  font-size:0.9rem;
  color:rgba(255,255,255,0.85);
  transition:all .25s;
  text-align:left;
  display:flex;align-items:center;gap:12px;
}}
.quiz-opt:hover:not(:disabled){{
  border-color:var(--naranja-claro);
  background:rgba(232,86,10,0.15);
}}
.quiz-opt.correct{{
  border-color:#22c55e;
  background:rgba(34,197,94,0.15);
  color:#86efac;
}}
.quiz-opt.wrong{{
  border-color:#ef4444;
  background:rgba(239,68,68,0.15);
  color:#fca5a5;
}}
.quiz-opt:disabled{{cursor:default}}
.opt-letter{{
  min-width:28px;height:28px;
  border-radius:50%;
  background:rgba(232,86,10,0.2);
  color:var(--naranja-claro);
  font-weight:700;font-size:0.8rem;
  display:flex;align-items:center;justify-content:center;
}}
.quiz-feedback{{
  background:rgba(232,86,10,0.1);
  border:1px solid rgba(232,86,10,0.3);
  border-radius:var(--radius-sm);
  padding:14px;
  font-size:0.85rem;
  color:rgba(255,255,255,0.85);
  line-height:1.6;
  display:none;
  margin-bottom:16px;
}}
.quiz-feedback.show{{display:block}}
.quiz-feedback.correct-fb{{border-color:#22c55e;background:rgba(34,197,94,0.1)}}
.quiz-feedback.wrong-fb{{border-color:#ef4444;background:rgba(239,68,68,0.1)}}
.quiz-score{{
  font-size:0.85rem;color:rgba(255,255,255,0.6);
  text-align:center;margin-top:10px;
}}
.quiz-score span{{color:var(--naranja-claro);font-weight:700}}
.quiz-result{{
  text-align:center;padding:40px 20px;display:none;
}}
.quiz-result.show{{display:block}}
.result-score-circle{{
  width:120px;height:120px;
  border-radius:50%;
  background:linear-gradient(135deg,var(--naranja),var(--naranja-oscuro));
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  margin:0 auto 24px;
  box-shadow:0 0 40px rgba(232,86,10,0.5);
}}
.result-score-circle .big-num{{font-size:2.2rem;font-weight:900;line-height:1}}
.result-score-circle .out-of{{font-size:0.8rem;opacity:.8}}
.quiz-result h3{{font-size:1.4rem;font-weight:700;margin-bottom:10px}}
.quiz-result p{{color:rgba(255,255,255,0.7);margin-bottom:24px}}
.btn-restart{{
  background:linear-gradient(135deg,var(--naranja),var(--naranja-oscuro));
  color:#fff;border:none;
  padding:12px 32px;border-radius:30px;
  font-size:0.9rem;font-weight:700;
  cursor:pointer;transition:all .3s;
}}
.btn-restart:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(232,86,10,0.5)}}

/* ===== METACOGNICION ===== */
#meta{{background:linear-gradient(180deg,#1A0800 0%,#0F0F1A 100%)}}
.meta-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  margin-bottom:40px;
}}
.meta-card{{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(232,86,10,0.2);
  border-radius:var(--radius);
  padding:22px;
  transition:all .3s;
}}
.meta-card:hover{{border-color:var(--naranja);background:rgba(232,86,10,0.1)}}
.meta-card h4{{
  font-size:0.88rem;font-weight:700;
  color:var(--naranja-claro);
  text-transform:uppercase;letter-spacing:1px;
  margin-bottom:10px;
}}
.meta-card p{{font-size:0.82rem;color:rgba(255,255,255,0.72);line-height:1.6}}

/* RUBRICA */
.rubrica-table{{width:100%;border-collapse:collapse;margin-bottom:40px}}
.rubrica-table th{{
  background:var(--naranja);color:#fff;
  padding:12px 16px;font-size:0.82rem;font-weight:700;
  text-align:left;
}}
.rubrica-table td{{
  padding:12px 16px;font-size:0.8rem;
  border-bottom:1px solid rgba(255,255,255,0.08);
  color:rgba(255,255,255,0.8);
  vertical-align:top;
}}
.rubrica-table tr:hover td{{background:rgba(232,86,10,0.06)}}
.rubrica-table .peso{{
  background:rgba(232,86,10,0.2);
  color:var(--naranja-claro);
  font-weight:700;text-align:center;
}}

/* ===== FOOTER ===== */
footer{{
  background:#0A0A14;
  border-top:2px solid var(--naranja);
  padding:40px 20px;
  text-align:center;
}}
.footer-firma{{
  font-size:1.1rem;font-weight:700;
  color:var(--naranja-claro);margin-bottom:6px;
}}
.footer-sub{{
  font-size:0.85rem;color:rgba(255,255,255,0.55);margin-bottom:20px;
}}
.footer-links{{
  display:flex;justify-content:center;gap:20px;flex-wrap:wrap;
  margin-bottom:16px;
}}
.footer-links a{{
  color:rgba(255,255,255,0.5);
  text-decoration:none;font-size:0.8rem;
  transition:color .2s;
}}
.footer-links a:hover{{color:var(--naranja-claro)}}
.footer-copy{{
  font-size:0.75rem;color:rgba(255,255,255,0.3);
}}

/* ===== SCROLL TOP ===== */
#scrollTop{{
  position:fixed;bottom:24px;right:24px;
  width:44px;height:44px;
  background:var(--naranja);
  color:#fff;border:none;border-radius:50%;
  font-size:1.2rem;cursor:pointer;
  box-shadow:0 4px 15px rgba(232,86,10,0.5);
  transition:all .3s;z-index:999;
  display:flex;align-items:center;justify-content:center;
  text-decoration:none;
}}
#scrollTop:hover{{transform:translateY(-3px);box-shadow:0 8px 25px rgba(232,86,10,0.6)}}

/* ===== RESPONSIVE ===== */
@media(max-width:900px){{
  .hero-content,.manus-intro,.bio-layout{{grid-template-columns:1fr}}
  .hero-image-wrap{{order:-1}}
  .steps-grid,.uses-grid,.ideas-grid,.obras-grid,.legado-grid,.meta-grid{{grid-template-columns:1fr 1fr}}
  .roles-grid{{grid-template-columns:1fr 1fr}}
  .context-cards{{grid-template-columns:1fr}}
}}
@media(max-width:600px){{
  .steps-grid,.uses-grid,.ideas-grid,.obras-grid,.legado-grid,.meta-grid,.roles-grid{{grid-template-columns:1fr}}
  .nav-links{{display:none}}
  .etapas-flow{{flex-direction:column}}
  .etapa:not(:last-child)::after{{content:'↓';right:auto;left:50%;top:auto;bottom:-14px;transform:translateX(-50%)}}
}}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-logo">🎓 Repensando a Rousseau · VIU</div>
  <ul class="nav-links">
    <li><a href="#manus">🤖 Cómo usar Manus</a></li>
    <li><a href="#biografia">📜 Biografía</a></li>
    <li><a href="#ideas">💡 Ideas Pedagógicas</a></li>
    <li><a href="#obras">📚 Obras Clave</a></li>
    <li><a href="#actividad">👥 Actividad</a></li>
    <li><a href="#quiz">🎯 Quiz</a></li>
  </ul>
</nav>

<!-- HERO -->
<section class="hero" id="inicio">
  <div class="hero-content">
    <div class="hero-text">
      <div class="badge">Historia de la Educación · Maestría en Pedagogía · VIU</div>
      <h1>Repensando a<br><span>Rousseau</span></h1>
      <p class="subtitle">
        Una infografía interactiva sobre el pensamiento pedagógico de Jean-Jacques Rousseau,
        creada con inteligencia artificial como herramienta de Competencia Digital Docente.
        <strong>Actividad Aplicativa 2 · UC2</strong>
      </p>
      <p class="firma">Dra. Arasay Padrón Alvarez<br>
        Profesora Contratada Doctora · VIU<br>
        Doctora en Ciencias Pedagógicas</p>
      <div class="hero-btns">
        <a href="#manus" class="btn-primary">Cómo usar Manus →</a>
        <a href="#biografia" class="btn-outline">Ver contenido</a>
      </div>
    </div>
    <div class="hero-image-wrap">
      <div class="hero-portrait-ring"></div>
      <img src="{portrait}" alt="Retrato de Jean-Jacques Rousseau" class="hero-portrait">
      <div class="hero-dates">Jean-Jacques Rousseau · 1712–1778</div>
    </div>
  </div>
</section>

<!-- SECCIÓN 1: CÓMO USAR MANUS -->
<section id="manus">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">🤖</div>
      <h2>¿Cómo usar <span>Manus</span> para esta actividad?</h2>
      <p>Guía paso a paso para docentes en formación: integra la IA de forma estratégica y reflexiva</p>
    </div>

    <div class="manus-intro">
      <div class="manus-intro-text">
        <h3>¿Qué es Manus?</h3>
        <p>
          <strong>Manus</strong> (<a href="https://manus.im" target="_blank" style="color:var(--naranja-claro)">manus.im</a>)
          es un agente de inteligencia artificial autónomo que investiga, sintetiza, diseña y crea
          contenidos educativos complejos de forma autónoma. A diferencia de un chatbot convencional,
          Manus ejecuta tareas completas: busca información, la analiza, la organiza visualmente y
          genera productos finales como esta infografía.
        </p>
        <p>
          Para la educación, representa una herramienta de <strong>Competencia Digital Docente (CDD)</strong>
          de nivel avanzado (Área 5.3 – Resolución de problemas con IA).
        </p>
        <div class="highlight">
          "El uso estratégico de la IA en educación no consiste en delegar el pensamiento,
          sino en amplificar la capacidad de análisis, síntesis y creación del docente."
        </div>
      </div>
      <div class="video-wrap">
        <iframe
          src="https://www.youtube.com/embed/AJnnqTN3T94"
          title="Jean Jacques Rousseau y su visión de la educación"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          style="width:100%;height:100%;border:none;aspect-ratio:16/9">
        </iframe>
      </div>
    </div>

    <!-- VIDEO REAL DE MANUS -->
    <div style="margin-bottom:40px;">
      <h3 style="color:var(--naranja-claro);font-size:1.1rem;margin-bottom:16px;font-weight:700;">
        📺 Video tutorial: Manus en acción para Historia de la Educación
      </h3>
      <div class="video-wrap" style="max-width:700px;">
        <iframe
          src="https://www.youtube.com/embed/tKdZ_DLFtuQ"
          title="Jean-Jacques Rousseau: Aportes a la Pedagogía"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen>
        </iframe>
      </div>
      <p style="font-size:0.8rem;color:rgba(255,255,255,0.5);margin-top:8px;">
          ▶ Jean-Jacques Rousseau: Aportes a la Pedagogía · Phonetic-land
      </p>
    </div>

    <div class="steps-grid">
      <div class="step-card">
        <span class="step-num">PASO 1</span>
        <span class="step-icon">🌐</span>
        <h4>Accede a Manus</h4>
        <p>Ve a <strong>manus.im</strong> y crea una cuenta gratuita. Accede desde cualquier dispositivo con navegador.</p>
      </div>
      <div class="step-card">
        <span class="step-num">PASO 2</span>
        <span class="step-icon">💬</span>
        <h4>Formula tu petición</h4>
        <p>Escribe en lenguaje natural qué necesitas. Sé específico: menciona el tema, nivel educativo y formato deseado.</p>
      </div>
      <div class="step-card">
        <span class="step-num">PASO 3</span>
        <span class="step-icon">📎</span>
        <h4>Adjunta materiales</h4>
        <p>Sube PDFs, documentos o imágenes. Manus los leerá e integrará en su respuesta de forma contextualizada.</p>
      </div>
      <div class="step-card">
        <span class="step-num">PASO 4</span>
        <span class="step-icon">⚙️</span>
        <h4>Supervisa el proceso</h4>
        <p>Manus trabaja de forma autónoma. Puedes ver en tiempo real qué acciones realiza: busca, analiza, diseña.</p>
      </div>
      <div class="step-card">
        <span class="step-num">PASO 5</span>
        <span class="step-icon">✏️</span>
        <h4>Revisa y ajusta</h4>
        <p>Evalúa el resultado con criterio pedagógico. Pide mejoras, cambios de enfoque o ampliaciones.</p>
      </div>
      <div class="step-card">
        <span class="step-num">PASO 6</span>
        <span class="step-icon">🎓</span>
        <h4>Reflexiona y justifica</h4>
        <p>Documenta cómo usaste Manus, qué aportó y qué decisiones tomaste tú. Esto es la metacognición del proceso.</p>
      </div>
    </div>

    <h3 style="color:var(--naranja-claro);font-size:1.1rem;margin-bottom:20px;font-weight:700;">
      ¿Para qué puedes usar Manus en esta actividad?
    </h3>
    <div class="uses-grid">
      <div class="use-card">
        <div class="use-icon">🔍</div>
        <h5>Investigar y sintetizar</h5>
        <p>Pídele que busque fuentes académicas sobre Rousseau y te presente un resumen riguroso con los tres ejes temáticos.</p>
      </div>
      <div class="use-card">
        <div class="use-icon">🎨</div>
        <h5>Generar ideas visuales</h5>
        <p>Solicita paletas de colores, estructuras de infografía, iconografía y estilos visuales coherentes con el contenido.</p>
      </div>
      <div class="use-card">
        <div class="use-icon">🏗️</div>
        <h5>Organizar en bloques</h5>
        <p>Transforma un texto plano en una estructura visual con jerarquía informativa clara: títulos, tarjetas, líneas de tiempo.</p>
      </div>
      <div class="use-card">
        <div class="use-icon">💻</div>
        <h5>Crear la infografía</h5>
        <p>Manus puede generar directamente el código HTML/CSS de una infografía web interactiva, como esta que ves ahora.</p>
      </div>
      <div class="use-card">
        <div class="use-icon">🧩</div>
        <h5>Diseñar el quiz</h5>
        <p>Genera preguntas de evaluación, actividades colaborativas y rúbricas alineadas con los resultados de aprendizaje.</p>
      </div>
      <div class="use-card">
        <div class="use-icon">📝</div>
        <h5>Justificar decisiones</h5>
        <p>Pídele que argumente por qué ciertos elementos visuales favorecen la comprensión del contenido histórico.</p>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 2: BIOGRAFÍA -->
<section id="biografia">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">①</div>
      <h2>Biografía y <span>Contexto Histórico</span></h2>
      <p>Jean-Jacques Rousseau (1712–1778) · Ginebra, Suiza · Siglo XVIII · La Ilustración</p>
    </div>

    <div class="bio-layout">
      <div class="bio-portrait-col">
        <img src="{portrait}" alt="Retrato de Rousseau" class="bio-portrait">
        <div class="bio-quote">
          "Todo está bien cuando sale de las manos del Creador; todo degenera entre las manos del hombre."
          <cite>— Emilio o De la educación, 1762 (Libro I)</cite>
        </div>
        <div class="bio-quote">
          "El hombre nace libre, y en todas partes se encuentra encadenado."
          <cite>— El Contrato Social, 1762</cite>
        </div>
      </div>
      <div>
        <img src="{geneva}" alt="Ginebra, Suiza, siglo XVIII" style="width:100%;border-radius:var(--radius);border:2px solid rgba(232,86,10,0.3);margin-bottom:20px;max-height:180px;object-fit:cover;">
        <div class="context-cards">
          <div class="ctx-card">
            <div class="ctx-icon">🏛️</div>
            <h4>La Ilustración</h4>
            <p>Rousseau vivió en el "Siglo de las Luces". La razón, la libertad y el progreso eran los valores centrales de una época de profundas transformaciones intelectuales y políticas europeas.</p>
          </div>
          <div class="ctx-card">
            <div class="ctx-icon">⚔️</div>
            <h4>Antiguo Régimen</h4>
            <p>Europa estaba gobernada por monarquías absolutas y una Iglesia con enorme poder. La desigualdad social era estructural. Rousseau cuestionó radicalmente este orden con su pensamiento político.</p>
          </div>
          <div class="ctx-card">
            <div class="ctx-icon">📖</div>
            <h4>La Enciclopedia</h4>
            <p>Colaboró con Diderot y D'Alembert en la <em>Encyclopédie</em>, el gran proyecto intelectual ilustrado, aunque luego se distanció de los enciclopedistas por sus contradicciones filosóficas.</p>
          </div>
          <div class="ctx-card">
            <div class="ctx-icon">🌿</div>
            <h4>Preromanticismo</h4>
            <p>Anticipó el Romanticismo al valorar la naturaleza, los sentimientos y la autenticidad frente al artificio social. Sus obras autobiográficas transformaron la literatura europea del siglo XVIII.</p>
          </div>
        </div>
      </div>
    </div>

    <h3 style="color:var(--naranja-claro);font-size:1.1rem;margin-bottom:24px;font-weight:700;">📅 Línea de vida</h3>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">1712</div>
        <h4>Nacimiento en Ginebra, Suiza</h4>
        <p>Nace el 28 de junio. Su madre, Suzanne Bernard, fallece nueve días después del parto. Su padre, Isaac Rousseau, relojero, lo educa leyendo novelas e historias clásicas.</p>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">1722–1728</div>
        <h4>Infancia y primeros aprendizajes</h4>
        <p>Enviado con el pastor Lambercier en Bossey: sus años más felices en plena naturaleza. A los 16 años abandona Ginebra tras un trato brutal como aprendiz de grabador.</p>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">1728–1740</div>
        <h4>Formación con Madame de Warens</h4>
        <p>Convive con Madame de Warens, quien le ayuda en su educación y afición musical. Diez años de lecturas, estudios y viajes que forjan su pensamiento filosófico y pedagógico.</p>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">1745–1755</div>
        <h4>París y los filósofos ilustrados</h4>
        <p>Se relaciona con Diderot, D'Alembert y Voltaire. Colabora en la <em>Encyclopédie</em>. En 1750 gana el premio de la Academia de Dijon con su <em>Discurso sobre las ciencias y las artes</em>.</p>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">1761–1762</div>
        <h4>Las obras maestras</h4>
        <p>Publica <em>La Nueva Eloísa</em> (1761), <em>El Contrato Social</em> y <em>Emilio o De la educación</em> (1762). Estas obras son condenadas y quemadas en París y Ginebra. Rousseau huye para no ser encarcelado.</p>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">1762–1778</div>
        <h4>Exilio, persecución y legado</h4>
        <p>Vive exiliado en Suiza, Inglaterra y Francia. Escribe sus <em>Confesiones</em>. Fallece el 2 de julio de 1778 en Ermenonville. En 1794 sus restos son trasladados al Panteón de París.</p>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 3: IDEAS PEDAGÓGICAS -->
<section id="ideas">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">②</div>
      <h2>Principales <span>Ideas Pedagógicas</span></h2>
      <p>El naturalismo pedagógico y la revolución copernicana en educación: el niño como centro</p>
    </div>

    <img src="{childhood}" alt="Rousseau y la educación de la infancia" class="ideas-hero-img">

    <div class="ideas-grid">
      <div class="idea-card">
        <span class="idea-icon">🌱</span>
        <h3>El Naturalismo Pedagógico</h3>
        <p>La naturaleza humana es originariamente buena. La educación debe respetar y seguir el desarrollo natural del niño, evitando la imposición artificial de normas y conocimientos prematuros.</p>
        <div class="idea-quote">"La naturaleza quiere que los niños sean niños antes de ser hombres."</div>
      </div>
      <div class="idea-card">
        <span class="idea-icon">👶</span>
        <h3>El Descubrimiento de la Infancia</h3>
        <p>Rousseau fue el primero en reconocer que la infancia tiene sus propias formas de ver, pensar y sentir. Hasta entonces, los niños eran tratados como adultos pequeños.</p>
        <div class="idea-quote">"La infancia tiene maneras de ver, de pensar y de sentir que le son propias."</div>
      </div>
      <div class="idea-card">
        <span class="idea-icon">🔬</span>
        <h3>Aprendizaje por Experiencia</h3>
        <p>El niño aprende haciendo, explorando y experimentando. El maestro no debe dar lecciones verbales, sino crear condiciones para que el alumno descubra por sí mismo. Precursor del constructivismo.</p>
        <div class="idea-quote">"El niño no sabe algo porque se lo hayas dicho, sino porque lo ha comprendido él mismo."</div>
      </div>
      <div class="idea-card">
        <span class="idea-icon">🎯</span>
        <h3>Educación Centrada en el Interés</h3>
        <p>Los niños deben educarse a través de sus intereses naturales, no por la disciplina estricta. La motivación intrínseca es el motor del aprendizaje auténtico. Anticipó la pedagogía activa del siglo XX.</p>
        <div class="idea-quote">"Estimulad el deseo de aprender y todo método será bueno."</div>
      </div>
      <div class="idea-card">
        <span class="idea-icon">🏗️</span>
        <h3>Educación Negativa</h3>
        <p>En los primeros años, la educación debe ser "negativa": no imponer virtudes ni verdades, sino proteger al niño del error y el vicio. Dejar que la naturaleza actúe sin interferencias prematuras.</p>
        <div class="idea-quote">"La primera educación debe ser puramente negativa: preservar el corazón del niño del vicio."</div>
      </div>
      <div class="idea-card">
        <span class="idea-icon">🌍</span>
        <h3>Educación para la Ciudadanía</h3>
        <p>Rousseau veía la educación como el camino para formar ciudadanos libres, conscientes de sus derechos y deberes. La educación tiene una dimensión política y social ineludible.</p>
        <div class="idea-quote">"Asignad a los niños más libertad y menos imperio."</div>
      </div>
    </div>

    <div class="etapas-title">📖 Las 5 etapas educativas del <em>Emilio</em></div>
    <div class="etapas-flow">
      <div class="etapa">
        <div class="etapa-age">0–2 años</div>
        <div class="etapa-icon">🍼</div>
        <h4>Libro I: Infancia</h4>
        <p>Educación física. Libertad de movimiento. El cuerpo como primer maestro.</p>
      </div>
      <div class="etapa">
        <div class="etapa-age">2–12 años</div>
        <div class="etapa-icon">🧒</div>
        <h4>Libro II: Niñez</h4>
        <p>Educación sensorial. Aprender por experiencia directa. Sin libros ni lecciones abstractas.</p>
      </div>
      <div class="etapa">
        <div class="etapa-age">12–15 años</div>
        <div class="etapa-icon">📐</div>
        <h4>Libro III: Preadolescencia</h4>
        <p>Educación intelectual. Curiosidad natural. Aprender oficios y ciencias prácticas.</p>
      </div>
      <div class="etapa">
        <div class="etapa-age">15–20 años</div>
        <div class="etapa-icon">❤️</div>
        <h4>Libro IV: Adolescencia</h4>
        <p>Educación moral y social. Las pasiones. Introducción a la religión natural y la sociedad.</p>
      </div>
      <div class="etapa">
        <div class="etapa-age">+20 años</div>
        <div class="etapa-icon">💑</div>
        <h4>Libro V: Madurez</h4>
        <p>Educación de Sofía (la mujer). Vida familiar y política. Ciudadanía y matrimonio.</p>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 4: OBRAS CLAVE -->
<section id="obras">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">③</div>
      <h2>Obras <span>Clave</span> de Rousseau</h2>
      <p>Las obras que transformaron la filosofía, la política y la pedagogía de la modernidad</p>
    </div>

    <div class="obras-grid">
      <div class="obra-card">
        <img src="{emile}" alt="Emilio o De la educación" class="obra-img">
        <div class="obra-body">
          <div class="obra-year">1762 · Obra pedagógica fundamental</div>
          <h3>Emilio o De la educación</h3>
          <p>Tratado pedagógico en forma de novela. Describe la educación ideal de un niño desde el nacimiento hasta la vida adulta, siguiendo los principios del naturalismo. Fundamento de la pedagogía moderna.</p>
          <div class="obra-tags">
            <span class="tag">Pedagogía</span>
            <span class="tag">Naturalismo</span>
            <span class="tag">Infancia</span>
          </div>
        </div>
      </div>
      <div class="obra-card">
        <img src="{contrat}" alt="El Contrato Social" class="obra-img" style="object-position:top">
        <div class="obra-body">
          <div class="obra-year">1762 · Filosofía política</div>
          <h3>El Contrato Social</h3>
          <p>Obra política que fundamenta la soberanía popular y la voluntad general. Influyó directamente en la Revolución Francesa y en los principios de la educación para la ciudadanía democrática.</p>
          <div class="obra-tags">
            <span class="tag">Política</span>
            <span class="tag">Ciudadanía</span>
            <span class="tag">Democracia</span>
          </div>
        </div>
      </div>
      <div class="obra-card">
        <img src="{nature}" alt="Rousseau y la naturaleza" class="obra-img">
        <div class="obra-body">
          <div class="obra-year">1750 · Primer Discurso</div>
          <h3>Discurso sobre las Ciencias y las Artes</h3>
          <p>Premio de la Academia de Dijon. Argumenta que el progreso de las ciencias y las artes ha corrompido las costumbres humanas. Primera formulación de su crítica a la civilización.</p>
          <div class="obra-tags">
            <span class="tag">Filosofía</span>
            <span class="tag">Crítica social</span>
          </div>
        </div>
      </div>
      <div class="obra-card">
        <div style="height:180px;background:linear-gradient(135deg,#2A1000,#1A0800);display:flex;align-items:center;justify-content:center;font-size:3rem;">📜</div>
        <div class="obra-body">
          <div class="obra-year">1755 · Segundo Discurso</div>
          <h3>Discurso sobre el Origen de la Desigualdad</h3>
          <p>Analiza el origen de la desigualdad entre los hombres, distinguiendo la desigualdad natural de la social. Introduce el concepto del "buen salvaje" y la crítica a la propiedad privada.</p>
          <div class="obra-tags">
            <span class="tag">Filosofía social</span>
            <span class="tag">Igualdad</span>
          </div>
        </div>
      </div>
      <div class="obra-card">
        <div style="height:180px;background:linear-gradient(135deg,#1A0800,#2A1000);display:flex;align-items:center;justify-content:center;font-size:3rem;">💌</div>
        <div class="obra-body">
          <div class="obra-year">1761 · Novela epistolar</div>
          <h3>La Nueva Eloísa</h3>
          <p>Novela epistolar que narra el amor entre Julieta y Saint-Preux. Exaltación de la naturaleza, los sentimientos y la virtud. Precursora del Romanticismo europeo y de la educación sentimental.</p>
          <div class="obra-tags">
            <span class="tag">Literatura</span>
            <span class="tag">Romanticismo</span>
          </div>
        </div>
      </div>
      <div class="obra-card">
        <div style="height:180px;background:linear-gradient(135deg,#2A1000,#0F0F1A);display:flex;align-items:center;justify-content:center;font-size:3rem;">📔</div>
        <div class="obra-body">
          <div class="obra-year">1782 · Autobiografía póstuma</div>
          <h3>Las Confesiones</h3>
          <p>Primera autobiografía moderna de la literatura occidental. Rousseau narra su vida con una honestidad radical. Inauguró el género autobiográfico y la introspección psicológica en la literatura.</p>
          <div class="obra-tags">
            <span class="tag">Autobiografía</span>
            <span class="tag">Psicología</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 5: LEGADO -->
<section id="legado" style="background:linear-gradient(180deg,#0F0F1A 0%,#1A0800 100%);padding:80px 20px;">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">④</div>
      <h2>Legado e <span>Influencia Pedagógica</span></h2>
      <p>Cómo el pensamiento de Rousseau transformó la educación hasta el siglo XXI</p>
    </div>

    <div class="legado-grid">
      <div class="legado-card">
        <div class="legado-avatar">🏫</div>
        <h4>Johann Pestalozzi (1746–1827)</h4>
        <p>Desarrolló el método intuitivo basado en la experiencia sensorial directa, aplicando el naturalismo rousseauniano a la educación popular y a la formación de maestros.</p>
      </div>
      <div class="legado-card">
        <div class="legado-avatar">🌸</div>
        <h4>Friedrich Froebel (1782–1852)</h4>
        <p>Creador del Kindergarten. Aplicó la idea rousseauniana del juego y la naturaleza como medios educativos fundamentales en la primera infancia.</p>
      </div>
      <div class="legado-card">
        <div class="legado-avatar">🔧</div>
        <h4>John Dewey (1859–1952)</h4>
        <p>Padre del pragmatismo educativo y la escuela activa. Retomó el principio rousseauniano de aprender haciendo y la educación centrada en el interés del alumno.</p>
      </div>
      <div class="legado-card">
        <div class="legado-avatar">🌺</div>
        <h4>María Montessori (1870–1952)</h4>
        <p>Su método de libertad guiada y respeto al ritmo natural del niño es deudor directo del naturalismo pedagógico de Rousseau y su concepto de educación negativa.</p>
      </div>
      <div class="legado-card">
        <div class="legado-avatar">🧠</div>
        <h4>Jean Piaget (1896–1980)</h4>
        <p>Su teoría del desarrollo cognitivo por estadios confirmó científicamente las intuiciones de Rousseau sobre las etapas evolutivas del niño y el aprendizaje activo.</p>
      </div>
      <div class="legado-card">
        <div class="legado-avatar">✊</div>
        <h4>Paulo Freire (1921–1997)</h4>
        <p>La pedagogía crítica de Freire retoma la dimensión política y liberadora de la educación rousseauniana: educar para la ciudadanía, la conciencia y la transformación social.</p>
      </div>
    </div>

    <div style="background:rgba(232,86,10,0.08);border:1px solid rgba(232,86,10,0.25);border-radius:var(--radius);padding:24px;">
      <h3 style="color:var(--naranja-claro);font-size:1rem;font-weight:700;margin-bottom:16px;">
        🔗 Recursos externos para profundizar
      </h3>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">
        <a href="https://www.youtube.com/watch?v=7Lzir_GGa_c" target="_blank" style="background:rgba(255,255,255,0.05);border:1px solid rgba(232,86,10,0.2);border-radius:var(--radius-sm);padding:14px;text-decoration:none;color:inherit;transition:all .3s;display:block;" onmouseover="this.style.borderColor='var(--naranja)'" onmouseout="this.style.borderColor='rgba(232,86,10,0.2)'">
          <div style="font-size:1.4rem;margin-bottom:6px;">▶️</div>
          <div style="font-size:0.82rem;font-weight:700;color:var(--naranja-claro);margin-bottom:4px;">Rousseau: el atrevimiento de educar</div>
          <div style="font-size:0.75rem;color:rgba(255,255,255,0.55);">YouTube · Conferencia académica</div>
        </a>
        <a href="https://www.philosophybasics.com/philosophers_rousseau.html" target="_blank" style="background:rgba(255,255,255,0.05);border:1px solid rgba(232,86,10,0.2);border-radius:var(--radius-sm);padding:14px;text-decoration:none;color:inherit;transition:all .3s;display:block;" onmouseover="this.style.borderColor='var(--naranja)'" onmouseout="this.style.borderColor='rgba(232,86,10,0.2)'">
          <div style="font-size:1.4rem;margin-bottom:6px;">📚</div>
          <div style="font-size:0.82rem;font-weight:700;color:var(--naranja-claro);margin-bottom:4px;">Philosophy Basics: Rousseau</div>
          <div style="font-size:0.75rem;color:rgba(255,255,255,0.55);">Fuente académica en inglés</div>
        </a>
        <a href="https://manus.im" target="_blank" style="background:rgba(255,255,255,0.05);border:1px solid rgba(232,86,10,0.2);border-radius:var(--radius-sm);padding:14px;text-decoration:none;color:inherit;transition:all .3s;display:block;" onmouseover="this.style.borderColor='var(--naranja)'" onmouseout="this.style.borderColor='rgba(232,86,10,0.2)'">
          <div style="font-size:1.4rem;margin-bottom:6px;">🤖</div>
          <div style="font-size:0.82rem;font-weight:700;color:var(--naranja-claro);margin-bottom:4px;">Manus AI · manus.im</div>
          <div style="font-size:0.75rem;color:rgba(255,255,255,0.55);">Herramienta IA para esta actividad</div>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 6: ACTIVIDAD EN EQUIPO -->
<section id="actividad">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">👥</div>
      <h2>Actividad <span>Práctica en Equipo</span></h2>
      <p>"Rousseau en el aula del siglo XXI" · Trabajo colaborativo con apoyo de Manus</p>
    </div>

    <div class="actividad-intro">
      <h3>🎯 "Rousseau en el aula del siglo XXI"</h3>
      <p>Trabajad en equipos de 3–4 personas. Tenéis <strong>20 minutos</strong> para completar las tareas asignadas a vuestro rol y preparar una breve presentación de 3 minutos al grupo. Usad Manus como herramienta de apoyo en cada fase.</p>
    </div>

    <h3 class="tareas-title">👤 Roles del equipo</h3>
    <div class="roles-grid">
      <div class="rol-card">
        <div class="rol-icon">🔍</div>
        <h4>Investigador/a</h4>
        <p>Profundiza en una idea pedagógica de Rousseau y busca un ejemplo contemporáneo en educación actual.</p>
      </div>
      <div class="rol-card">
        <div class="rol-icon">🎨</div>
        <h4>Diseñador/a Visual</h4>
        <p>Crea un esquema o mapa conceptual que conecte las ideas de Rousseau con las pedagogías del siglo XXI.</p>
      </div>
      <div class="rol-card">
        <div class="rol-icon">🤖</div>
        <h4>Especialista en IA</h4>
        <p>Usa Manus para generar una síntesis visual o una propuesta didáctica basada en el pensamiento de Rousseau.</p>
      </div>
      <div class="rol-card">
        <div class="rol-icon">🎤</div>
        <h4>Portavoz</h4>
        <p>Integra las aportaciones del equipo y presenta los resultados al grupo con claridad y argumentación pedagógica.</p>
      </div>
    </div>

    <h3 class="tareas-title">📋 Tareas del equipo</h3>
    <div class="tareas-list">
      <div class="tarea-item">
        <div class="tarea-num">1</div>
        <div class="tarea-content">
          <h4>Seleccionad una idea pedagógica de Rousseau</h4>
          <p>Elegid una de las 6 ideas presentadas en la infografía y discutid en equipo: ¿sigue siendo válida hoy? ¿En qué contextos educativos la reconocéis? Usad Manus para ampliar la información con fuentes académicas.</p>
        </div>
      </div>
      <div class="tarea-item">
        <div class="tarea-num">2</div>
        <div class="tarea-content">
          <h4>Conectad con un pedagogo posterior</h4>
          <p>Identificad qué pedagogo/a del siglo XX (Dewey, Montessori, Freire, Piaget…) recogió esa idea y cómo la transformó. Pedid a Manus que genere una comparativa visual entre ambos pensadores.</p>
        </div>
      </div>
      <div class="tarea-item">
        <div class="tarea-num">3</div>
        <div class="tarea-content">
          <h4>Diseñad una actividad didáctica inspirada en Rousseau</h4>
          <p>Proponed una actividad concreta para vuestro nivel educativo que aplique el principio rousseauniano elegido. Especificad: objetivo, metodología, recursos y evaluación. Manus puede ayudaros a estructurarla.</p>
        </div>
      </div>
      <div class="tarea-item">
        <div class="tarea-num">4</div>
        <div class="tarea-content">
          <h4>Reflexionad sobre el uso de Manus</h4>
          <p>Responded en equipo: ¿Qué aportó Manus a vuestro proceso? ¿Qué decisiones tomasteis vosotros que Manus no podía tomar? ¿Cómo usaríais Manus con vuestros propios estudiantes?</p>
        </div>
      </div>
      <div class="tarea-item">
        <div class="tarea-num">5</div>
        <div class="tarea-content">
          <h4>Preparad la presentación de 3 minutos</h4>
          <p>El portavoz presentará: (a) la idea elegida y su vigencia, (b) el pedagogo conectado, (c) la actividad diseñada, y (d) la reflexión sobre el uso de Manus. Podéis usar la infografía como soporte visual.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 7: QUIZ -->
<section id="quiz">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">🎯</div>
      <h2>Quiz <span>Interactivo</span></h2>
      <p>Evalúa tu comprensión sobre Rousseau, la historia de la educación y el uso educativo de Manus · 10 preguntas</p>
    </div>

    <div class="quiz-container">
      <div class="quiz-progress-bar">
        <div class="quiz-progress-fill" id="progressFill"></div>
      </div>

      <div class="quiz-card" id="quizCard">
        <div class="quiz-meta">
          <span class="quiz-counter" id="quizCounter">PREGUNTA 1 DE 10</span>
          <span class="quiz-category" id="quizCategory">Biografía y contexto</span>
        </div>
        <div class="quiz-question" id="quizQuestion"></div>
        <div class="quiz-options" id="quizOptions"></div>
        <div class="quiz-feedback" id="quizFeedback"></div>
        <div class="quiz-score">Puntuación: <span id="scoreDisplay">0</span>/<span id="totalDisplay">0</span></div>
      </div>

      <div class="quiz-result" id="quizResult">
        <div class="result-score-circle">
          <div class="big-num" id="finalScore">0</div>
          <div class="out-of" id="finalOut">de 10</div>
        </div>
        <h3 id="resultTitle">¡Resultado!</h3>
        <p id="resultMsg"></p>
        <button class="btn-restart" onclick="initQuiz()">🔄 Repetir el quiz</button>
      </div>
    </div>
  </div>
</section>

<!-- SECCIÓN 8: METACOGNICIÓN -->
<section id="meta">
  <div class="section-inner">
    <div class="section-header">
      <div class="section-num">🧠</div>
      <h2>Reflexión <span>Metacognitiva</span></h2>
      <p>Justificación del uso estratégico de Manus en el diseño de esta infografía educativa</p>
    </div>

    <div class="meta-grid">
      <div class="meta-card">
        <h4>¿Cómo se usó Manus?</h4>
        <p>Manus fue utilizado de forma integral: investigó fuentes académicas sobre Rousseau, sintetizó los tres ejes temáticos de la actividad, organizó el contenido en bloques visuales significativos, diseñó la arquitectura de la infografía y generó el código HTML/CSS interactivo completo, incluyendo el quiz de evaluación.</p>
      </div>
      <div class="meta-card">
        <h4>¿Por qué esta forma de uso?</h4>
        <p>Se eligió un uso estratégico y completo porque permite demostrar el potencial máximo de Manus como herramienta de Competencia Digital Docente (CDD). La infografía web interactiva supera las limitaciones del formato estático, permitiendo navegación, animaciones y evaluación integrada, lo que potencia el aprendizaje activo.</p>
      </div>
      <div class="meta-card">
        <h4>¿Qué aportó a la creatividad?</h4>
        <p>Manus permitió transformar un contenido histórico-pedagógico denso en una experiencia visual e interactiva. La estructura en secciones temáticas, la línea de tiempo, las tarjetas de ideas y el quiz integrado son decisiones de diseño pedagógico que Manus ejecutó pero que requirieron una orientación pedagógica experta para ser significativas.</p>
      </div>
      <div class="meta-card" style="grid-column:span 2;">
        <h4>¿Qué sigue siendo humano?</h4>
        <p>La decisión sobre qué contenidos son pedagógicamente relevantes, cómo se articulan con los resultados de aprendizaje, qué nivel de profundidad requiere cada tema, y cómo conectar el pensamiento de Rousseau con la práctica docente actual: estas decisiones son irrenunciablemente del docente. La IA amplifica; el juicio pedagógico orienta.</p>
      </div>
      <div class="meta-card">
        <h4>Impacto en el aprendizaje</h4>
        <p>El uso de Manus transformó el proceso de aprendizaje: de la lectura pasiva de un texto sobre Rousseau a la creación activa de un recurso educativo interactivo. Este proceso implicó tomar decisiones pedagógicas, evaluar la calidad del contenido generado y reflexionar sobre el uso ético y estratégico de la IA en educación.</p>
      </div>
    </div>

    <h3 style="color:var(--naranja-claro);font-size:1.1rem;font-weight:700;margin-bottom:20px;">📊 Rúbrica de evaluación</h3>
    <table class="rubrica-table">
      <thead>
        <tr>
          <th>Criterio</th>
          <th>Insuficiente</th>
          <th>Adecuado</th>
          <th>Excelente</th>
          <th class="peso">Peso</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Precisión del contenido histórico-pedagógico</strong></td>
          <td>Contenido incompleto o inexacto</td>
          <td>Adecuado con algunas lagunas</td>
          <td>Riguroso, preciso, análisis claro de Rousseau y su contexto</td>
          <td class="peso">40%</td>
        </tr>
        <tr>
          <td><strong>Organización visual y claridad comunicativa (CDD)</strong></td>
          <td>Desordenada, confusa o visualmente pobre</td>
          <td>Comprensible con menor impacto gráfico</td>
          <td>Excelente estructura visual, claridad informativa y atractivo gráfico</td>
          <td class="peso">20%</td>
        </tr>
        <tr>
          <td><strong>Uso creativo y significativo de Manus</strong></td>
          <td>Sin uso evidente o no justificado</td>
          <td>Uso funcional pero limitado</td>
          <td>Uso estratégico y justificado; pensamiento creativo evidente</td>
          <td class="peso">30%</td>
        </tr>
        <tr>
          <td><strong>Justificación metacognitiva del proceso</strong></td>
          <td>Reflexión ausente o sin conexión</td>
          <td>Reflexión válida pero general</td>
          <td>Conciencia del proceso de diseño e impacto de la IA en el aprendizaje</td>
          <td class="peso">10%</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-firma">Dra. Arasay Padrón Alvarez</div>
  <div class="footer-sub">
    Profesora Contratada Doctora · Universidad Internacional de Valencia (VIU)<br>
    Doctora en Ciencias Pedagógicas · Especialista en Historia de la Educación e IA Educativa
  </div>
  <div class="footer-links">
    <a href="#inicio">Inicio</a>
    <a href="#manus">Cómo usar Manus</a>
    <a href="#biografia">Biografía</a>
    <a href="#ideas">Ideas Pedagógicas</a>
    <a href="#obras">Obras Clave</a>
    <a href="#quiz">Quiz</a>
    <a href="https://manus.im" target="_blank">manus.im</a>
  </div>
  <div class="footer-copy">
    Repensando a Rousseau · Infografía Interactiva con IA · Historia de la Educación · Maestría en Pedagogía · VIU<br>
    Jean-Jacques Rousseau (1712–1778) · Ginebra, Suiza · La Ilustración · Naturalismo Pedagógico<br>
    Creado con Manus AI · Contenido basado en fuentes académicas rigurosas
  </div>
</footer>

<a href="#inicio" id="scrollTop" title="Volver arriba">↑</a>

<script>
// ===== QUIZ DATA =====
const quizData = [
  {{
    q: "¿En qué ciudad y año nació Jean-Jacques Rousseau?",
    opts: ["París, Francia, 1712","Ginebra, Suiza, 1712","Londres, Inglaterra, 1723","Berlín, Prusia, 1712"],
    correct: 1,
    cat: "Biografía y contexto",
    fb: "Correcto. Rousseau nació el 28 de junio de 1712 en Ginebra, Suiza, ciudad que marcó profundamente su identidad como 'ciudadano de Ginebra'."
  }},
  {{
    q: "¿Cuál es el principio central del naturalismo pedagógico de Rousseau?",
    opts: ["El niño debe aprender mediante la memorización y la disciplina","La naturaleza humana es originariamente buena y la educación debe seguir el desarrollo natural","La educación debe centrarse en la transmisión de conocimientos académicos","El maestro es la autoridad máxima del proceso educativo"],
    correct: 1,
    cat: "Ideas pedagógicas",
    fb: "Exacto. Para Rousseau, la naturaleza humana es originariamente buena y la educación debe respetar y seguir el desarrollo natural del niño, evitando imposiciones artificiales prematuras."
  }},
  {{
    q: "¿Qué obra pedagógica de Rousseau describe la educación ideal de un niño desde el nacimiento hasta la vida adulta?",
    opts: ["El Contrato Social","Las Confesiones","Emilio o De la educación","Discurso sobre las Ciencias y las Artes"],
    correct: 2,
    cat: "Obras clave",
    fb: "Correcto. 'Emilio o De la educación' (1762) es el tratado pedagógico fundamental de Rousseau, escrito en forma de novela, que describe la educación ideal siguiendo los principios del naturalismo."
  }},
  {{
    q: "¿Qué significa la 'educación negativa' según Rousseau?",
    opts: ["Una educación basada en el castigo y la disciplina estricta","No enseñar nada al niño durante los primeros años","Proteger al niño del error y el vicio sin imponer virtudes ni verdades prematuras","Una educación que produce resultados negativos en el desarrollo del niño"],
    correct: 2,
    cat: "Ideas pedagógicas",
    fb: "Exacto. La 'educación negativa' de Rousseau propone que en los primeros años no se deben imponer virtudes ni verdades, sino proteger al niño del error y el vicio, dejando que la naturaleza actúe."
  }},
  {{
    q: "¿Qué movimiento filosófico-artístico anticipó Rousseau con su valoración de la naturaleza y los sentimientos?",
    opts: ["El Positivismo","El Racionalismo cartesiano","El Romanticismo","El Empirismo inglés"],
    correct: 2,
    cat: "Contexto histórico",
    fb: "Correcto. Rousseau anticipó el Romanticismo al valorar la naturaleza, los sentimientos y la autenticidad frente al artificio social, siendo considerado un precursor del movimiento romántico europeo."
  }},
  {{
    q: "¿Qué pedagogo del siglo XX confirmó científicamente las intuiciones de Rousseau sobre las etapas evolutivas del niño?",
    opts: ["Paulo Freire","John Dewey","Jean Piaget","Friedrich Froebel"],
    correct: 2,
    cat: "Legado e influencia",
    fb: "Correcto. Jean Piaget (1896-1980) confirmó científicamente con su teoría del desarrollo cognitivo por estadios las intuiciones de Rousseau sobre las etapas evolutivas del niño y el aprendizaje activo."
  }},
  {{
    q: "¿En qué año fueron publicados simultáneamente 'El Contrato Social' y 'Emilio o De la educación'?",
    opts: ["1750","1755","1762","1778"],
    correct: 2,
    cat: "Obras clave",
    fb: "Correcto. Ambas obras fueron publicadas en 1762, el año más prolífico de Rousseau. Paradójicamente, también fueron el año de su persecución: ambas obras fueron condenadas y quemadas en París y Ginebra."
  }},
  {{
    q: "¿Cuál es la principal ventaja de usar Manus (IA) para crear una infografía educativa sobre Rousseau?",
    opts: ["Elimina la necesidad de que el docente tenga conocimiento pedagógico","Permite investigar, sintetizar y diseñar contenido de forma autónoma, amplificando la capacidad creativa del docente","Genera contenido sin necesidad de revisión ni criterio pedagógico","Sustituye completamente el trabajo intelectual del docente"],
    correct: 1,
    cat: "Uso educativo de Manus",
    fb: "Correcto. Manus amplifica la capacidad del docente al investigar, sintetizar y diseñar de forma autónoma, pero el juicio pedagógico, la selección de contenidos relevantes y las decisiones didácticas siguen siendo responsabilidad del docente."
  }},
  {{
    q: "¿Qué área de la Competencia Digital Docente (CDD) representa el uso estratégico de Manus para crear infografías educativas?",
    opts: ["Área 1: Información y alfabetización informacional","Área 3: Creación de contenido digital","Área 5.3: Resolución de problemas con IA","Área 2: Comunicación y colaboración"],
    correct: 2,
    cat: "Uso educativo de Manus",
    fb: "Correcto. El uso estratégico de agentes de IA como Manus para resolver problemas educativos complejos corresponde al Área 5.3 de la CDD: Resolución de problemas tecnológicos con IA, que representa el nivel más avanzado de competencia digital docente."
  }},
  {{
    q: "Según Rousseau, ¿cuál es la cita que mejor resume su visión sobre la naturaleza humana y la sociedad?",
    opts: ['"El hombre es un animal político por naturaleza"','"Todo está bien cuando sale de las manos del Creador; todo degenera entre las manos del hombre"','"Pienso, luego existo"','"La educación es el arma más poderosa que puedes usar para cambiar el mundo"'],
    correct: 1,
    cat: "Pensamiento de Rousseau",
    fb: "Correcto. Esta cita del Libro I del Emilio (1762) es la formulación más célebre del naturalismo rousseauniano: la naturaleza crea bien, pero la sociedad y la civilización corrompen al ser humano. Es el fundamento de toda su pedagogía."
  }}
];

let currentQ = 0, score = 0, answered = 0;

function initQuiz() {{
  currentQ = 0; score = 0; answered = 0;
  document.getElementById('quizCard').style.display = 'block';
  document.getElementById('quizResult').classList.remove('show');
  document.getElementById('scoreDisplay').textContent = '0';
  document.getElementById('totalDisplay').textContent = '0';
  renderQuestion();
}}

function renderQuestion() {{
  const d = quizData[currentQ];
  document.getElementById('quizCounter').textContent = `PREGUNTA ${{currentQ+1}} DE ${{quizData.length}}`;
  document.getElementById('quizCategory').textContent = d.cat;
  document.getElementById('quizQuestion').textContent = d.q;
  document.getElementById('progressFill').style.width = `${{((currentQ)/quizData.length)*100}}%`;

  const fb = document.getElementById('quizFeedback');
  fb.className = 'quiz-feedback';
  fb.textContent = '';

  const opts = document.getElementById('quizOptions');
  opts.innerHTML = '';
  const letters = ['A','B','C','D'];
  d.opts.forEach((opt, i) => {{
    const btn = document.createElement('button');
    btn.className = 'quiz-opt';
    btn.innerHTML = `<span class="opt-letter">${{letters[i]}}</span>${{opt}}`;
    btn.onclick = () => selectAnswer(i);
    opts.appendChild(btn);
  }});
}}

function selectAnswer(idx) {{
  const d = quizData[currentQ];
  const btns = document.querySelectorAll('.quiz-opt');
  btns.forEach(b => b.disabled = true);

  const fb = document.getElementById('quizFeedback');
  answered++;

  if(idx === d.correct) {{
    btns[idx].classList.add('correct');
    score++;
    fb.className = 'quiz-feedback correct-fb show';
    fb.innerHTML = '✅ ' + d.fb;
  }} else {{
    btns[idx].classList.add('wrong');
    btns[d.correct].classList.add('correct');
    fb.className = 'quiz-feedback wrong-fb show';
    fb.innerHTML = '❌ Incorrecto. ' + d.fb;
  }}

  document.getElementById('scoreDisplay').textContent = score;
  document.getElementById('totalDisplay').textContent = answered;

  setTimeout(() => {{
    currentQ++;
    if(currentQ < quizData.length) {{
      renderQuestion();
    }} else {{
      showResult();
    }}
  }}, 2800);
}}

function showResult() {{
  document.getElementById('progressFill').style.width = '100%';
  document.getElementById('quizCard').style.display = 'none';
  const res = document.getElementById('quizResult');
  res.classList.add('show');
  document.getElementById('finalScore').textContent = score;
  document.getElementById('finalOut').textContent = `de ${{quizData.length}}`;

  let title, msg;
  const pct = (score/quizData.length)*100;
  if(pct >= 90) {{
    title = '🏆 ¡Excelente dominio!';
    msg = `Has obtenido ${{score}} de ${{quizData.length}} puntos. Demuestras un conocimiento riguroso del pensamiento de Rousseau y del uso educativo de la IA. ¡Nivel excelente según la rúbrica!`;
  }} else if(pct >= 70) {{
    title = '👏 ¡Muy buen trabajo!';
    msg = `Has obtenido ${{score}} de ${{quizData.length}} puntos. Tienes un buen dominio del contenido. Repasa las preguntas falladas para alcanzar el nivel de excelencia.`;
  }} else if(pct >= 50) {{
    title = '📚 Nivel adecuado';
    msg = `Has obtenido ${{score}} de ${{quizData.length}} puntos. Tienes conocimientos básicos sobre Rousseau. Te recomendamos revisar las secciones de ideas pedagógicas y obras clave.`;
  }} else {{
    title = '🔄 Necesitas repasar';
    msg = `Has obtenido ${{score}} de ${{quizData.length}} puntos. Te recomendamos revisar la infografía completa antes de repetir el quiz. ¡El aprendizaje es un proceso!`;
  }}
  document.getElementById('resultTitle').textContent = title;
  document.getElementById('resultMsg').textContent = msg;
}}

// Inicializar quiz al cargar
document.addEventListener('DOMContentLoaded', initQuiz);

// Scroll suave para nav
document.querySelectorAll('a[href^="#"]').forEach(a => {{
  a.addEventListener('click', e => {{
    const target = document.querySelector(a.getAttribute('href'));
    if(target) {{
      e.preventDefault();
      target.scrollIntoView({{behavior:'smooth', block:'start'}});
    }}
  }});
}});
</script>
</body>
</html>"""

with open('/home/ubuntu/rousseau-infografia/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML generado correctamente.")
print(f"Tamaño: {len(html):,} caracteres")
