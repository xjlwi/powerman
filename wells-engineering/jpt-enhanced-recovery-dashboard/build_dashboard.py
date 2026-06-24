#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject data.json into a self-contained HTML dashboard -> index.html
Includes a client-side ingest/edit/persist layer so paywalled articles can be
pasted in and records dynamically updated (stored in localStorage, exportable)."""
import json

data = json.load(open("data.json"))
DATA_JSON = json.dumps(data, ensure_ascii=False)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>JPT/SPE Enhanced Recovery - Wells Engineering Intelligence Dashboard</title>
<style>
:root{
  --bg:#0b1014; --bg2:#11181f; --panel:#151e27; --panel2:#1b2733; --line:#243140;
  --txt:#e6edf3; --mut:#8aa0b3; --mut2:#5f7488; --accent:#34d3a6; --accent2:#3ea6ff;
  --hi:#ffb454; --warn:#ff7b72;
  --d-dev:#3ea6ff; --d-drill:#b48cff; --d-comp:#ff7bb0; --d-prod:#ffb454;
  --d-fac:#34d3a6; --d-res:#5ad1ff; --d-ccus:#7ee787; --d-dig:#c9a0ff;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--txt);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:1.5}
a{color:var(--accent2);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1500px;margin:0 auto;padding:18px 20px 60px}

header.hd{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:14px;
  border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:14px}
.hd h1{font-size:20px;margin:0 0 4px;letter-spacing:.2px}
.hd .sub{color:var(--mut);font-size:12.5px;max-width:760px}
.hd .src{font-size:12px;color:var(--mut2);margin-top:6px}
.kpis{display:flex;gap:10px;flex-wrap:wrap}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:8px 14px;min-width:92px}
.kpi b{display:block;font-size:20px;color:var(--accent)}
.kpi span{font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}

/* edits banner */
.editbar{display:flex;flex-wrap:wrap;align-items:center;gap:10px;background:linear-gradient(90deg,rgba(52,211,166,.08),transparent);
  border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;padding:9px 13px;margin-bottom:14px;font-size:12.5px}
.editbar .lead{color:var(--mut)}
.editbar b{color:var(--accent)}
.editbar .spacer{flex:1}
.abtn{background:var(--accent);color:#04140f;font-weight:600;border:0;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer}
.abtn:hover{filter:brightness(1.08)}
.abtn.ghost{background:transparent;border:1px solid var(--line);color:var(--mut);font-weight:500}
.abtn.ghost:hover{color:var(--txt);border-color:var(--accent)}
.abtn.danger{background:transparent;border:1px solid var(--line);color:var(--mut)}
.abtn.danger:hover{color:var(--warn);border-color:var(--warn)}

.topics{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
@media(max-width:900px){.topics{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.card h3{margin:0 0 10px;font-size:12px;text-transform:uppercase;letter-spacing:1px;color:var(--mut)}
.bar-row{display:flex;align-items:center;gap:10px;margin:5px 0;cursor:pointer}
.bar-row .lab{width:178px;font-size:12.5px;color:var(--txt);flex:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar-track{flex:1;background:var(--bg2);border-radius:6px;height:16px;position:relative;overflow:hidden}
.bar-fill{height:100%;border-radius:6px;transition:width .3s}
.bar-row .cnt{width:34px;text-align:right;color:var(--mut);font-variant-numeric:tabular-nums;font-size:12px}
.bar-row:hover .lab,.bar-row.active .lab{color:var(--accent)}
.bar-row.active .lab{font-weight:600}
.method-chips{display:flex;flex-wrap:wrap;gap:6px}
.mchip{background:var(--panel2);border:1px solid var(--line);border-radius:20px;padding:3px 10px;font-size:11.5px;color:var(--mut)}
.mchip b{color:var(--accent);font-weight:600}

.toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:var(--panel);
  border:1px solid var(--line);border-radius:12px;padding:10px 12px;margin-bottom:12px}
.toolbar input[type=text]{flex:1;min-width:200px;background:var(--bg2);border:1px solid var(--line);
  color:var(--txt);border-radius:8px;padding:8px 11px;font-size:13px}
.toolbar select{background:var(--bg2);border:1px solid var(--line);color:var(--txt);border-radius:8px;padding:8px 10px;font-size:13px}
.seg{display:flex;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg button{background:var(--bg2);border:0;color:var(--mut);padding:8px 11px;font-size:12px;cursor:pointer}
.seg button.on{background:var(--accent);color:#04140f;font-weight:600}
.tgl{display:flex;align-items:center;gap:7px;font-size:12.5px;color:var(--mut);cursor:pointer;user-select:none}
.tgl input{accent-color:var(--accent)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{border:1px solid var(--line);background:var(--bg2);color:var(--mut);border-radius:18px;
  padding:5px 11px;font-size:12px;cursor:pointer;user-select:none;display:flex;align-items:center;gap:6px}
.chip .dot{width:8px;height:8px;border-radius:50%}
.chip.on{color:var(--txt);border-color:transparent}
.btn-clear{background:transparent;border:1px solid var(--line);color:var(--mut);border-radius:8px;padding:8px 11px;font-size:12px;cursor:pointer}
.btn-clear:hover{color:var(--warn);border-color:var(--warn)}

.tl{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 16px 6px;margin-bottom:14px}
.tl .tlhd{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.tl .tlhd span{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:var(--mut)}
.tl .rng{font-size:12px;color:var(--accent)}
.tlbars{display:flex;align-items:flex-end;gap:2px;height:70px}
.tlbar{flex:1;background:var(--bg2);border-radius:3px 3px 0 0;min-height:3px;cursor:pointer;position:relative;transition:background .15s}
.tlbar.insel{background:var(--accent2)}
.tlbar:hover{background:var(--accent)}
.tlaxis{display:flex;justify-content:space-between;font-size:10.5px;color:var(--mut2);margin-top:4px}
.sliders{position:relative;height:26px;margin-top:6px}
.sliders input{position:absolute;width:100%;-webkit-appearance:none;appearance:none;background:transparent;pointer-events:none;top:8px;margin:0}
.sliders input::-webkit-slider-thumb{-webkit-appearance:none;height:16px;width:16px;border-radius:50%;background:var(--accent);cursor:pointer;pointer-events:auto;border:2px solid #04140f}
.sliders input::-moz-range-thumb{height:16px;width:16px;border-radius:50%;background:var(--accent);cursor:pointer;pointer-events:auto;border:2px solid #04140f}
.sliders .strack{position:absolute;height:4px;background:var(--line);border-radius:4px;top:14px;width:100%}

.main{display:grid;grid-template-columns:minmax(380px,1fr) 1.15fr;gap:16px;align-items:start}
@media(max-width:1000px){.main{grid-template-columns:1fr}}
.listhd{display:flex;justify-content:space-between;align-items:baseline;margin:0 2px 8px}
.listhd b{font-size:13px}.listhd span{color:var(--mut);font-size:12px}
.list{display:flex;flex-direction:column;gap:8px;max-height:1180px;overflow-y:auto;padding-right:6px}
.list::-webkit-scrollbar{width:8px}.list::-webkit-scrollbar-thumb{background:var(--line);border-radius:8px}
.item{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--line);
  border-radius:10px;padding:11px 13px;cursor:pointer;transition:.12s}
.item:hover{border-color:var(--accent);background:var(--panel2)}
.item.sel{border-color:var(--accent);border-left-color:var(--accent);background:var(--panel2);box-shadow:0 0 0 1px var(--accent) inset}
.item .top{display:flex;justify-content:space-between;gap:10px;align-items:center;margin-bottom:5px}
.item .date{font-size:11.5px;color:var(--mut);font-variant-numeric:tabular-nums;white-space:nowrap}
.item .ttl{font-size:13.5px;font-weight:600;line-height:1.35;margin:2px 0 7px}
.item .tags{display:flex;flex-wrap:wrap;gap:5px;align-items:center}
.tag{font-size:10.5px;padding:2px 8px;border-radius:12px;background:var(--bg2);color:var(--mut);white-space:nowrap}
.tag.disc{color:#04140f;font-weight:600}
.rel{font-size:10px;font-weight:700;padding:2px 7px;border-radius:10px;text-transform:uppercase;letter-spacing:.5px}
.rel.High{background:rgba(52,211,166,.16);color:var(--accent)}
.rel.Medium{background:rgba(62,166,255,.16);color:var(--accent2)}
.rel.Context{background:rgba(143,160,179,.16);color:var(--mut)}
.lock{font-size:10px;color:var(--hi)}
.enr{font-size:10px;font-weight:700;color:#04140f;background:var(--accent);padding:2px 7px;border-radius:10px}

.detail{position:sticky;top:14px;background:var(--panel);border:1px solid var(--line);border-radius:14px;
  padding:0;overflow:hidden;min-height:420px}
.detail .empty{padding:56px 30px;text-align:center;color:var(--mut2)}
.detail .empty .big{font-size:42px;margin-bottom:10px;opacity:.5}
.dt-head{padding:18px 20px 14px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,var(--panel2),var(--panel))}
.dt-head .meta{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:12px;color:var(--mut);margin-bottom:8px}
.dt-head h2{margin:0 0 10px;font-size:18px;line-height:1.3}
.dt-head .tags{display:flex;flex-wrap:wrap;gap:6px}
.dt-actions{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.dt-body{padding:6px 20px 20px}
.sec{padding:13px 0;border-bottom:1px solid var(--line)}
.sec:last-child{border-bottom:0}
.sec h4{margin:0 0 6px;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:8px}
.sec h4 .ic{width:18px;height:18px;border-radius:5px;background:var(--bg2);display:inline-flex;align-items:center;justify-content:center;font-size:11px}
.sec p{margin:0;color:var(--txt);font-size:13.5px;white-space:pre-wrap}
.sec .quote{border-left:2px solid var(--line);padding-left:11px;color:var(--mut);font-style:italic}
.kv{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
.kv .k{font-size:11px;background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:3px 9px;color:var(--mut)}
.dt-open{display:inline-flex;align-items:center;gap:7px;margin-top:6px;background:var(--accent);color:#04140f;
  font-weight:600;border-radius:9px;padding:9px 15px;font-size:13px}
.dt-open:hover{text-decoration:none;filter:brightness(1.08)}
.disclaimer{font-size:11px;color:var(--mut2);margin-top:16px;line-height:1.5;border-top:1px solid var(--line);padding-top:10px}
.foot{margin-top:26px;color:var(--mut2);font-size:11.5px;text-align:center}

/* editor */
.ed{padding:16px 20px 22px}
.ed h2{font-size:16px;margin:0 0 4px}
.ed .hint{font-size:12px;color:var(--mut);margin-bottom:14px}
.ed label{display:block;font-size:11px;letter-spacing:.6px;text-transform:uppercase;color:var(--mut);margin:12px 0 4px}
.ed input[type=text],.ed textarea,.ed select{width:100%;background:var(--bg2);border:1px solid var(--line);
  color:var(--txt);border-radius:8px;padding:8px 10px;font-size:13px;font-family:inherit;resize:vertical}
.ed textarea{min-height:54px;line-height:1.5}
.ed textarea.big{min-height:130px}
.ed .grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:560px){.ed .grid2{grid-template-columns:1fr}}
.ed .discbox{display:flex;flex-wrap:wrap;gap:7px;margin-top:4px}
.ed .discbox label{display:inline-flex;align-items:center;gap:6px;text-transform:none;letter-spacing:0;font-size:12px;color:var(--txt);margin:0;
  background:var(--bg2);border:1px solid var(--line);border-radius:16px;padding:4px 10px;cursor:pointer}
.ed .discbox input{accent-color:var(--accent)}
.ed .row-btns{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px;border-top:1px solid var(--line);padding-top:14px}
.ed .derive{background:var(--accent2);color:#04140f;font-weight:600;border:0;border-radius:8px;padding:8px 12px;font-size:12.5px;cursor:pointer}
.ed .derive:hover{filter:brightness(1.08)}
.ed .note{font-size:11px;color:var(--mut2);margin-top:5px}
.modal{position:fixed;inset:0;background:rgba(2,6,10,.6);display:none;align-items:flex-start;justify-content:center;z-index:50;padding:40px 16px;overflow:auto}
.modal.open{display:flex}
.modal .box{background:var(--panel);border:1px solid var(--line);border-radius:14px;max-width:560px;width:100%;padding:20px 22px}
.modal h3{margin:0 0 8px;font-size:15px}
.modal p{font-size:12.5px;color:var(--mut)}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);background:var(--accent);color:#04140f;
  font-weight:600;padding:10px 18px;border-radius:10px;font-size:13px;opacity:0;transition:opacity .25s;pointer-events:none;z-index:60}
.toast.show{opacity:1}
</style>
</head>
<body>
<div class="wrap">
  <header class="hd">
    <div>
      <h1>Enhanced Recovery &rarr; Wells Engineering Intelligence</h1>
      <div class="sub">Curated &amp; classified briefs from JPT/SPE's <em>Enhanced recovery</em> topic, mapped to the integrated-operator wells-engineering disciplines. Click a title for a technical summary &mdash; or paste a paywalled article's full text to enrich any record.</div>
      <div class="src">Source: <a id="srcLink" target="_blank" rel="noopener">jpt.spe.org/topic/enhanced-recovery</a> &middot; <span id="srcMeta"></span></div>
    </div>
    <div class="kpis" id="kpis"></div>
  </header>

  <div class="editbar">
    <span class="lead">Edits are saved <b>in this browser</b> (localStorage). <b id="editCount">0</b> record(s) enriched/edited.</span>
    <span class="spacer"></span>
    <button class="abtn" id="addBtn">&#43; Add paywalled article</button>
    <button class="abtn ghost" id="exportBtn">&#8595; Export data.json</button>
    <button class="abtn ghost" id="backupBtn">&#8595; Backup edits</button>
    <button class="abtn ghost" id="restoreBtn">&#8593; Restore edits</button>
    <button class="abtn danger" id="clearEditsBtn">Clear edits</button>
    <input type="file" id="restoreFile" accept="application/json" style="display:none"/>
  </div>

  <div class="topics">
    <div class="card">
      <h3>Wells-Engineering Discipline Coverage <span style="color:var(--mut2);text-transform:none;letter-spacing:0">(click to filter)</span></h3>
      <div id="discBars"></div>
    </div>
    <div class="card">
      <h3>Dominant Technical Approaches</h3>
      <div class="method-chips" id="methodChips"></div>
    </div>
  </div>

  <div class="toolbar">
    <input type="text" id="search" placeholder="Search title, abstract, author, play, operator..."/>
    <div class="seg" id="relSeg">
      <button data-rel="all" class="on">All relevance</button>
      <button data-rel="High">High</button>
      <button data-rel="Medium">Medium</button>
    </div>
    <select id="sort">
      <option value="date_desc">Newest first</option>
      <option value="date_asc">Oldest first</option>
      <option value="title_asc">Title A&ndash;Z</option>
      <option value="rel">Relevance</option>
      <option value="enriched">Enriched first</option>
    </select>
    <label class="tgl"><input type="checkbox" id="wellsOnly"/> Wells-engineering core only</label>
    <label class="tgl"><input type="checkbox" id="enrOnly"/> Enriched only</label>
    <button class="btn-clear" id="clearBtn">Reset filters</button>
  </div>

  <div class="chips" id="discChips" style="margin-bottom:12px"></div>

  <div class="tl">
    <div class="tlhd"><span>Publication timeline &middot; click bars or drag handles to zoom</span><span class="rng" id="rngLabel"></span></div>
    <div class="tlbars" id="tlbars"></div>
    <div class="sliders">
      <div class="strack"></div>
      <input type="range" id="slMin" min="0" value="0"/>
      <input type="range" id="slMax" min="0" value="0"/>
    </div>
    <div class="tlaxis" id="tlaxis"></div>
  </div>

  <div class="main">
    <div>
      <div class="listhd"><b>Papers</b><span id="resultCount"></span></div>
      <div class="list" id="list"></div>
    </div>
    <div class="detail" id="detail">
      <div class="empty"><div class="big">&#9776;</div>Select a paper for its technical summary &mdash; or use <b>&#43; Add paywalled article</b> / the <b>Enrich</b> button to paste full text and update a record.</div>
    </div>
  </div>

  <div class="foot" id="foot"></div>
</div>

<div class="modal" id="modal"><div class="box" id="modalBox"></div></div>
<div class="toast" id="toast"></div>

<script>
const DATA = __DATA__;
const RECS = DATA.records.slice();      // immutable baseline
const META = DATA.meta;
const RULES = DATA.rules;
const DCOLOR = {
 "Field Development":"#3ea6ff","Drilling & Well Construction":"#b48cff",
 "Completions & Stimulation":"#ff7bb0","Production & Well Performance":"#ffb454",
 "Facilities & Flow Assurance":"#34d3a6","Reservoir & EOR":"#5ad1ff",
 "CCUS & Decarbonization":"#7ee787","Digital, AI & Modeling":"#c9a0ff"
};
const ALL_DISC = Object.keys(DCOLOR);
const CORE = new Set(RULES.wells_core);
const esc = s => (s==null?"":String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const $ = id => document.getElementById(id);

/* ---------------- persistence (localStorage) ---------------- */
const LSKEY = "jpt_wells_overrides_v1";
let OV = {};
try{ OV = JSON.parse(localStorage.getItem(LSKEY) || "{}"); }catch(e){ OV = {}; }
function saveOV(){ try{ localStorage.setItem(LSKEY, JSON.stringify(OV)); }catch(e){ toast("Could not save (storage full/blocked)"); } }

/* ---------------- effective dataset ---------------- */
function effectiveRecords(){
  const baseUrls = new Set(RECS.map(r=>r.url));
  const merged = RECS.map(r => OV[r.url] ? Object.assign({}, r, OV[r.url]) : r);
  const news = Object.keys(OV).filter(u => OV[u] && OV[u]._new && !baseUrls.has(u)).map(u => OV[u]);
  return merged.concat(news);
}
let EFF = [];

/* ---------------- live meta + month axis ---------------- */
let LM = {}, MONTHS = [], MIDX = {};
function computeLM(){
  const disc={}, meth={}, rel={};
  EFF.forEach(r=>{
    (r.disciplines||[]).forEach(d=>disc[d]=(disc[d]||0)+1);
    (r.methods||[]).forEach(m=>meth[m]=(meth[m]||0)+1);
    rel[r.relevance]=(rel[r.relevance]||0)+1;
  });
  const isos = EFF.map(r=>r.iso).filter(Boolean).sort();
  LM = {
    count: EFF.length,
    date_min: isos[0]||META.date_min, date_max: isos[isos.length-1]||META.date_max,
    disciplines: ALL_DISC.filter(d=>disc[d]).map(d=>[d,disc[d]]).sort((a,b)=>b[1]-a[1]),
    methods: Object.entries(meth).sort((a,b)=>b[1]-a[1]),
    relevance: Object.entries(rel).sort((a,b)=>b[1]-a[1])
  };
}
function buildMonths(){
  let [y,m] = LM.date_min.slice(0,7).split("-").map(Number);
  const [ey,em] = LM.date_max.slice(0,7).split("-").map(Number);
  MONTHS=[]; while(y<ey||(y===ey&&m<=em)){MONTHS.push(y+"-"+String(m).padStart(2,"0"));m++;if(m>12){m=1;y++;}}
  MIDX = Object.fromEntries(MONTHS.map((m,i)=>[m,i]));
}

/* ---------------- state ---------------- */
const st = {search:"",rel:"all",sort:"date_desc",wellsOnly:false,enrOnly:false,
            discs:new Set(),mMin:0,mMax:0,zoomed:false,selected:null,editing:null};

/* ---------------- client-side rule engine (mirrors build_data.py) ---------------- */
function classifyText(text){
  const t=text.toLowerCase(); const hits=[];
  for(const [disc,kws] of RULES.disciplines){ if(kws.some(k=>t.includes(k))) hits.push(disc); }
  return hits.length?hits:["Reservoir & EOR"];
}
function findTerms(text,vocab){
  const low=text.toLowerCase(), seen=new Set(), res=[];
  for(const term of vocab){ const tl=term.toLowerCase(); if(low.includes(tl)&&!seen.has(tl)){seen.add(tl);res.push(term);} }
  return res;
}
function findMethods(text){
  const low=text.toLowerCase(), out=[];
  for(const [label,kws] of RULES.methods){ if(kws.some(k=>low.includes(k))) out.push(label); }
  return out;
}
function splitSentences(text){
  return text.trim().split(/(?<=[.;])\s+/).map(s=>s.trim()).filter(Boolean);
}
function deriveFields(text, title, sourceWord){
  text = text||""; title = title||"";
  const disciplines=classifyText(title+" "+text);
  const plays=findTerms(text+" "+title, RULES.plays);
  const regions=findTerms(text+" "+title, RULES.regions);
  const operators=findTerms(text+" "+title, RULES.operators);
  const methods=findMethods(text+" "+title);
  const sents=splitSentences(text);
  const geo=[];
  if(plays.length)geo.push("play/field: "+plays.slice(0,3).join(", "));
  if(regions.length)geo.push("region: "+regions.slice(0,3).join(", "));
  if(operators.length)geo.push("operators/parties: "+operators.slice(0,3).join(", "));
  let context="Wells-engineering lens: "+disciplines.join(" | ")+".";
  context += geo.length ? " Setting from the "+sourceWord+" - "+geo.join("; ")+"." : " The "+sourceWord+" does not name a specific field or operator.";
  let technical = methods.length ? "Methods/technologies referenced: "+methods.join(", ")+". " : "";
  technical += sents.length ? "As stated in the "+sourceWord+": \""+sents.slice(0,2).join(" ")+"\"" : "";
  const low=text.toLowerCase(); const vals=[];
  for(const kw in RULES.value_kws){ if(low.includes(kw)){ const lbl=RULES.value_kws[kw]; if(!vals.includes(lbl))vals.push(lbl);} }
  const business = vals.length ? "Value levers indicated by the "+sourceWord+": "+Array.from(new Set(vals)).sort().join("; ")+"." :
    "The "+sourceWord+" frames the work within enhanced/improved oil recovery; specific economic figures are not stated.";
  const chal=sents.filter(s=>RULES.challenge_kws.some(k=>s.toLowerCase().includes(k)));
  const challenges = chal.length ? chal.join(" ") :
    "The "+sourceWord+" does not enumerate specific operational challenges; it positions the work as a methodology/case advance within "+disciplines[0].toLowerCase()+".";
  const core=disciplines.filter(d=>CORE.has(d));
  let relevance, rel_note;
  if(core.length){relevance="High";rel_note="Directly touches integrated wells-engineering scope ("+core.join(", ")+").";}
  else if(disciplines.some(d=>d==="Reservoir & EOR"||d==="Production & Well Performance")){relevance="Medium";rel_note="Subsurface/recovery focus that informs well and completion design decisions.";}
  else {relevance="Context";rel_note="Adjacent topic (modeling, CCUS, or industry news) providing strategic context.";}
  return {disciplines,plays,regions,operators,methods,context,technical,business,challenges,relevance,relevance_note:rel_note};
}

/* ---------------- date parsing ---------------- */
const MONTHNAMES=["january","february","march","april","may","june","july","august","september","october","november","december"];
function parseDateStr(s){
  const d=new Date(s);
  if(!isNaN(d)){return d;}
  return null;
}
function dateMeta(s){
  const d=parseDateStr(s);
  if(!d) return null;
  const iso=d.toISOString().slice(0,10);
  return {iso, ym:iso.slice(0,7), year:d.getFullYear(), ts:Math.floor(d.getTime()/1000)};
}

/* ---------------- static header pieces ---------------- */
$("srcLink").href=META.source;
$("srcLink").textContent=META.source.replace("https://","");

/* ---------------- refresh derived data + dynamic UI ---------------- */
function refresh(){
  EFF = effectiveRecords();
  computeLM(); buildMonths();
  if(!st.zoomed){ st.mMin=0; st.mMax=MONTHS.length-1; }
  else { st.mMax=Math.min(st.mMax,MONTHS.length-1); st.mMin=Math.min(st.mMin,st.mMax); }
  // KPIs
  const hi=(LM.relevance.find(r=>r[0]==="High")||["",0])[1];
  $("kpis").innerHTML=[["Papers",LM.count],["Disciplines",LM.disciplines.length],["High-relevance",hi],["Span",MONTHS.length+" mo"]]
    .map(k=>`<div class="kpi"><b>${k[1]}</b><span>${k[0]}</span></div>`).join("");
  $("srcMeta").textContent=LM.count+" briefs · "+LM.date_min+" → "+LM.date_max+" · abstract-faithful + your enrichments";
  // discipline bars
  const maxD=Math.max(1,...LM.disciplines.map(d=>d[1]));
  $("discBars").innerHTML=LM.disciplines.map(([d,c])=>`
   <div class="bar-row" data-disc="${esc(d)}"><div class="lab">${esc(d)}</div>
     <div class="bar-track"><div class="bar-fill" style="width:${(c/maxD*100).toFixed(1)}%;background:${DCOLOR[d]||'var(--accent)'}"></div></div>
     <div class="cnt">${c}</div></div>`).join("");
  $("discBars").querySelectorAll(".bar-row").forEach(r=>r.onclick=()=>toggleDisc(r.dataset.disc));
  // method chips
  $("methodChips").innerHTML=LM.methods.slice(0,14).map(([m,c])=>`<span class="mchip">${esc(m)} <b>${c}</b></span>`).join("")||'<span class="mchip">none</span>';
  // discipline filter chips
  $("discChips").innerHTML=LM.disciplines.map(([d,c])=>`
   <span class="chip" data-disc="${esc(d)}"><span class="dot" style="background:${DCOLOR[d]||'#888'}"></span>${esc(d)} <span style="color:var(--mut2)">${c}</span></span>`).join("");
  $("discChips").querySelectorAll(".chip").forEach(c=>c.onclick=()=>toggleDisc(c.dataset.disc));
  // edit count
  $("editCount").textContent=Object.keys(OV).length;
  buildTimeline();
  render();
}

function toggleDisc(d){ st.discs.has(d)?st.discs.delete(d):st.discs.add(d); render(); }

/* ---------------- timeline ---------------- */
const tlbars=$("tlbars"), slMin=$("slMin"), slMax=$("slMax");
function monthCounts(){ const c=new Array(MONTHS.length).fill(0); EFF.forEach(r=>{const i=MIDX[r.ym];if(i!=null)c[i]++;}); return c; }
function buildTimeline(){
  slMin.max=slMax.max=MONTHS.length-1;
  slMin.value=st.mMin; slMax.value=st.mMax;
  const counts=monthCounts(), mx=Math.max(1,...counts);
  tlbars.innerHTML=MONTHS.map((m,i)=>`<div class="tlbar" data-i="${i}" title="${m}: ${counts[i]} paper(s)" style="height:${(counts[i]/mx*100).toFixed(0)}%"></div>`).join("");
  tlbars.querySelectorAll(".tlbar").forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i;
    if(st.mMin===i&&st.mMax===i){st.mMin=0;st.mMax=MONTHS.length-1;st.zoomed=false;} else {st.mMin=i;st.mMax=i;st.zoomed=true;}
    slMin.value=st.mMin;slMax.value=st.mMax;render();
  });
  const ax=$("tlaxis"), step=Math.max(1,Math.ceil(MONTHS.length/6)); let labs=[];
  for(let i=0;i<MONTHS.length;i+=step)labs.push(MONTHS[i]);
  if(labs[labs.length-1]!==MONTHS[MONTHS.length-1])labs.push(MONTHS[MONTHS.length-1]);
  ax.innerHTML=labs.map(l=>`<span>${l}</span>`).join("");
}
function syncSliders(){ let a=+slMin.value,b=+slMax.value; if(a>b)[a,b]=[b,a]; st.mMin=a;st.mMax=b;st.zoomed=(a>0||b<MONTHS.length-1);render(); }
slMin.oninput=syncSliders; slMax.oninput=syncSliders;

/* ---------------- controls ---------------- */
$("search").oninput=e=>{st.search=e.target.value.toLowerCase();render();};
$("sort").onchange=e=>{st.sort=e.target.value;render();};
$("wellsOnly").onchange=e=>{st.wellsOnly=e.target.checked;render();};
$("enrOnly").onchange=e=>{st.enrOnly=e.target.checked;render();};
document.querySelectorAll("#relSeg button").forEach(b=>b.onclick=()=>{
  document.querySelectorAll("#relSeg button").forEach(x=>x.classList.remove("on"));
  b.classList.add("on"); st.rel=b.dataset.rel; render();
});
$("clearBtn").onclick=()=>{
  st.search="";st.rel="all";st.sort="date_desc";st.wellsOnly=false;st.enrOnly=false;st.discs.clear();
  st.mMin=0;st.mMax=MONTHS.length-1;st.zoomed=false;
  $("search").value="";$("sort").value="date_desc";$("wellsOnly").checked=false;$("enrOnly").checked=false;
  document.querySelectorAll("#relSeg button").forEach(x=>x.classList.toggle("on",x.dataset.rel==="all"));
  slMin.value=0;slMax.value=MONTHS.length-1; render();
};

/* ---------------- filtering / render ---------------- */
function passes(r){
  if(st.rel!=="all" && r.relevance!==st.rel) return false;
  if(st.wellsOnly && !(r.disciplines||[]).some(d=>CORE.has(d))) return false;
  if(st.enrOnly && !r.enriched) return false;
  if(st.discs.size && !(r.disciplines||[]).some(d=>st.discs.has(d))) return false;
  const i=MIDX[r.ym]; if(i==null||i<st.mMin||i>st.mMax) return false;
  if(st.search){
    const hay=(r.title+" "+r.abstract+" "+(r.fullText||"")+" "+r.author+" "+r.source_tag+" "+
      (r.disciplines||[]).join(" ")+" "+(r.methods||[]).join(" ")+" "+(r.plays||[]).join(" ")+" "+
      (r.regions||[]).join(" ")+" "+(r.operators||[]).join(" ")).toLowerCase();
    if(!hay.includes(st.search)) return false;
  }
  return true;
}
const RELRANK={High:0,Medium:1,Context:2};
function sortRecs(a){
  const s=st.sort;
  a.sort((x,y)=>{
    if(s==="date_desc")return y.ts-x.ts;
    if(s==="date_asc")return x.ts-y.ts;
    if(s==="title_asc")return x.title.localeCompare(y.title);
    if(s==="rel")return (RELRANK[x.relevance]-RELRANK[y.relevance])||(y.ts-x.ts);
    if(s==="enriched")return (y.enriched?1:0)-(x.enriched?1:0)||(y.ts-x.ts);
    return 0;
  });return a;
}
function discTag(d){return `<span class="tag disc" style="background:${DCOLOR[d]||'#888'}">${esc(d)}</span>`;}
function render(){
  document.querySelectorAll("#discChips .chip").forEach(c=>{
    const on=st.discs.has(c.dataset.disc); c.classList.toggle("on",on);
    c.style.background=on?(DCOLOR[c.dataset.disc]||'#888'):''; c.style.color=on?'#04140f':'';
  });
  document.querySelectorAll("#discBars .bar-row").forEach(r=>r.classList.toggle("active",st.discs.has(r.dataset.disc)));
  tlbars.querySelectorAll(".tlbar").forEach(b=>{const i=+b.dataset.i;b.classList.toggle("insel",i>=st.mMin&&i<=st.mMax);});
  $("rngLabel").textContent=(MONTHS[st.mMin]||"")+" → "+(MONTHS[st.mMax]||"");

  let recs=EFF.filter(passes); sortRecs(recs);
  $("resultCount").textContent=recs.length+" of "+EFF.length;
  const list=$("list");
  if(!recs.length){list.innerHTML=`<div class="card" style="color:var(--mut)">No papers match the current filters.</div>`;}
  else list.innerHTML=recs.map(r=>{
    const lead=(r.disciplines||["Reservoir & EOR"])[0];
    return `<div class="item ${st.selected===r.url?'sel':''}" data-url="${esc(r.url)}" style="border-left-color:${DCOLOR[lead]||'var(--line)'}">
      <div class="top"><span class="rel ${r.relevance}">${r.relevance}</span><span class="date">${esc(r.date)}</span></div>
      <div class="ttl">${esc(r.title)}</div>
      <div class="tags">${(r.disciplines||[]).slice(0,3).map(discTag).join("")}
        <span class="tag">${esc(r.source_tag)}</span>
        ${r.enriched?'<span class="enr">&#10003; enriched</span>':(r.locked?'<span class="lock">&#128274; paywalled</span>':'')}</div>
    </div>`;}).join("");
  list.querySelectorAll(".item").forEach(it=>it.onclick=()=>{st.selected=it.dataset.url;st.editing=null;render();showDetail(it.dataset.url);});
}

/* ---------------- detail (read) ---------------- */
function sec(ic,title,html){return `<div class="sec"><h4><span class="ic">${ic}</span>${title}</h4>${html}</div>`;}
function getRec(url){ return EFF.find(x=>x.url===url); }
function showDetail(url){
  const r=getRec(url); if(!r)return;
  const kv=(label,arr)=>arr&&arr.length?`<div class="kv"><span style="color:var(--mut2);font-size:11px;align-self:center">${label}:</span>${arr.map(a=>`<span class="k">${esc(a)}</span>`).join("")}</div>`:"";
  const srcText = r.fullText ? r.fullText : r.abstract;
  const srcLabel = r.fullText ? "Full text (user-supplied)" : "Abstract (verbatim)";
  $("detail").innerHTML=`
    <div class="dt-head">
      <div class="meta"><span class="rel ${r.relevance}">${r.relevance} relevance</span>
        <span>&#128197; ${esc(r.date)}</span><span>&#9997; ${esc(r.author)}</span>
        <span>&#127991; ${esc(r.source_tag)}</span>
        ${r.enriched?'<span class="enr">&#10003; enriched '+esc((r.updated||'').slice(0,10))+'</span>':(r.locked?'<span class="lock">&#128274; paywalled</span>':'')}</div>
      <h2>${esc(r.title)}</h2>
      <div class="tags">${(r.disciplines||[]).map(discTag).join("")}</div>
      <div class="dt-actions">
        <button class="abtn" onclick="openEditor('${esc(r.url)}')">${r.enriched?'&#9998; Edit':'&#9998; Enrich with full text'}</button>
        <a class="abtn ghost" href="${esc(r.url)}" target="_blank" rel="noopener">Open on JPT/SPE &rarr;</a>
        ${OV[r.url]?'<button class="abtn danger" onclick="revertRec(\''+esc(r.url)+'\')">Revert</button>':''}
      </div>
    </div>
    <div class="dt-body">
      <div class="sec"><p style="color:var(--mut);font-size:12.5px">${esc(r.relevance_note)}</p></div>
      ${sec("&#128205;","Context",`<p>${esc(r.context)}</p>`)}
      ${sec("&#9881;","Technical Approach",`<p>${esc(r.technical)}</p>`)}
      ${sec("&#128176;","Business Problem &amp; Value",`<p>${esc(r.business)}</p>`)}
      ${sec("&#9888;","Challenges",`<p>${esc(r.challenges)}</p>`)}
      ${sec("&#128300;","Gaps / Source",`<p style="color:var(--mut)">${esc(r.gaps)}</p>`)}
      ${sec("&#128196;",srcLabel,`<p class="quote">${esc(srcText)}</p>`)}
      ${sec("&#127991;","Engineering Tags", (kv("Methods",r.methods)+kv("Play/Field",r.plays)+kv("Region",r.regions)+kv("Operators",r.operators)) || "<p style='color:var(--mut2)'>None detected.</p>")}
      <div class="disclaimer">Auto-classified by keyword rules; ${r.enriched?'this record was <b>enriched from user-supplied full text</b>.':'summary is <b>abstract-faithful</b> (public brief only).'} Edits live in your browser &mdash; use <b>Export</b> to persist or share them.</div>
    </div>`;
  if($("detail").scrollIntoView) $("detail").scrollIntoView({behavior:"smooth",block:"nearest"});
}

/* ---------------- editor ---------------- */
function ta(id,val,big){return `<textarea id="${id}" class="${big?'big':''}">${esc(val||"")}</textarea>`;}
function txt(id,val,ph){return `<input type="text" id="${id}" value="${esc(val||"")}" placeholder="${esc(ph||"")}"/>`;}
function openEditor(url){
  const isNew = url==="__new__";
  const r = isNew ? {title:"",url:"",date:"",author:"",source_tag:"Enhanced recovery",abstract:"",fullText:"",
                     context:"",technical:"",business:"",challenges:"",gaps:"",relevance:"High",relevance_note:"",
                     disciplines:[],methods:[],plays:[],regions:[],operators:[],locked:true}
                  : getRec(url);
  if(!r) return;
  st.editing = url; st.selected = isNew?null:url;
  const discChecks = ALL_DISC.map(d=>`<label><input type="checkbox" class="edDisc" value="${esc(d)}" ${ (r.disciplines||[]).includes(d)?'checked':''}/> ${esc(d)}</label>`).join("");
  $("detail").innerHTML=`<div class="ed">
    <h2>${isNew?'Add a paywalled article':'Enrich / edit record'}</h2>
    <div class="hint">Paste the article's full text below and click <b>Auto-derive</b> to pre-fill the analysis fields, then tweak anything. Saved to this browser; use Export to persist.</div>

    <label>Title</label>${txt("edTitle",r.title,"Paper title")}
    <div class="grid2">
      <div><label>Date</label>${txt("edDate",r.date,"e.g. June 1, 2026")}</div>
      <div><label>Author</label>${txt("edAuthor",r.author,"Author / staff")}</div>
    </div>
    <div class="grid2">
      <div><label>Source URL</label>${txt("edUrl",r.url,"https://jpt.spe.org/...")}</div>
      <div><label>Source tag</label>${txt("edTag",r.source_tag,"Enhanced recovery")}</div>
    </div>

    <label>Full text from the (paywalled) article &mdash; paste here</label>
    ${ta("edFull",r.fullText,true)}
    <button class="derive" id="deriveBtn">&#9889; Auto-derive analysis fields from full text</button>
    <span class="note">Re-runs the same keyword classifier used for the dataset, on the pasted text.</span>

    <label>Relevance</label>
    <select id="edRel">${["High","Medium","Context"].map(x=>`<option ${r.relevance===x?'selected':''}>${x}</option>`).join("")}</select>

    <label>Disciplines</label><div class="discbox">${discChecks}</div>

    <label>Context</label>${ta("edContext",r.context)}
    <label>Technical Approach</label>${ta("edTechnical",r.technical)}
    <label>Business Problem &amp; Value</label>${ta("edBusiness",r.business)}
    <label>Challenges</label>${ta("edChallenges",r.challenges)}
    <label>Gaps / Source note</label>${ta("edGaps",r.gaps)}
    <label>Abstract / public brief (kept verbatim)</label>${ta("edAbstract",r.abstract)}

    <div class="grid2">
      <div><label>Methods (comma-separated)</label>${txt("edMethods",(r.methods||[]).join(", "))}</div>
      <div><label>Play / Field</label>${txt("edPlays",(r.plays||[]).join(", "))}</div>
    </div>
    <div class="grid2">
      <div><label>Region</label>${txt("edRegions",(r.regions||[]).join(", "))}</div>
      <div><label>Operators</label>${txt("edOperators",(r.operators||[]).join(", "))}</div>
    </div>

    <div class="row-btns">
      <button class="abtn" id="saveBtn">&#128190; Save</button>
      <button class="abtn ghost" id="cancelBtn">Cancel</button>
      ${(!isNew && OV[url])?'<button class="abtn danger" id="revertBtn">Revert to original</button>':''}
      ${(isNew || (OV[url]&&OV[url]._new))?'<button class="abtn danger" id="delBtn">Delete record</button>':''}
    </div>
  </div>`;

  $("deriveBtn").onclick=()=>{
    const full=$("edFull").value.trim();
    const title=$("edTitle").value.trim();
    const src = full ? "source" : "brief";
    const basis = full || $("edAbstract").value.trim();
    if(!basis){ toast("Paste some text first"); return; }
    const d=deriveFields(basis,title,src);
    $("edContext").value=d.context; $("edTechnical").value=d.technical;
    $("edBusiness").value=d.business; $("edChallenges").value=d.challenges;
    $("edRel").value=d.relevance;
    $("edMethods").value=d.methods.join(", "); $("edPlays").value=d.plays.join(", ");
    $("edRegions").value=d.regions.join(", "); $("edOperators").value=d.operators.join(", ");
    document.querySelectorAll(".edDisc").forEach(c=>c.checked=d.disciplines.includes(c.value));
    if(full && !$("edGaps").value.trim()) $("edGaps").value="Enriched from user-supplied full text on "+new Date().toISOString().slice(0,10)+". Fields below auto-derived from that text; edit as needed.";
    toast("Fields derived &mdash; review & save");
  };
  $("cancelBtn").onclick=()=>{ st.editing=null; if(st.selected){showDetail(st.selected);} else clearDetail(); render(); };
  if($("revertBtn")) $("revertBtn").onclick=()=>revertRec(url);
  if($("delBtn")) $("delBtn").onclick=()=>{ const u=$("edUrl").value.trim()||url; delete OV[u]; saveOV(); st.editing=null; st.selected=null; clearDetail(); refresh(); toast("Record deleted"); };
  $("saveBtn").onclick=()=>saveEditor(isNew,url);
}

function clearDetail(){ $("detail").innerHTML=`<div class="empty"><div class="big">&#9776;</div>Select a paper, or add/enrich one.</div>`; }

function commaList(id){ return $(id).value.split(",").map(s=>s.trim()).filter(Boolean); }
function saveEditor(isNew, origUrl){
  const title=$("edTitle").value.trim();
  if(!title){ toast("Title is required"); return; }
  let url=$("edUrl").value.trim();
  if(!url){ url = isNew ? "local://"+title.toLowerCase().replace(/[^a-z0-9]+/g,"-").slice(0,80) : origUrl; }
  const dateStr=$("edDate").value.trim();
  const dm=dateMeta(dateStr) || dateMeta((getRec(origUrl)||{}).date) || {iso:"2024-01-01",ym:"2024-01",year:2024,ts:Math.floor(Date.parse("2024-01-01")/1000)};
  const discs=Array.from(document.querySelectorAll(".edDisc:checked")).map(c=>c.value);
  const ov = {
    title, url, date:dateStr || (getRec(origUrl)||{}).date || "",
    author:$("edAuthor").value.trim()||"JPT / SPE", source_tag:$("edTag").value.trim()||"Enhanced recovery",
    abstract:$("edAbstract").value.trim(), fullText:$("edFull").value.trim(),
    context:$("edContext").value.trim(), technical:$("edTechnical").value.trim(),
    business:$("edBusiness").value.trim(), challenges:$("edChallenges").value.trim(),
    gaps:$("edGaps").value.trim(), relevance:$("edRel").value,
    relevance_note:(getRec(origUrl)||{}).relevance_note || "User-edited record.",
    disciplines:discs.length?discs:["Reservoir & EOR"],
    methods:commaList("edMethods"), plays:commaList("edPlays"),
    regions:commaList("edRegions"), operators:commaList("edOperators"),
    iso:dm.iso, ym:dm.ym, year:dm.year, ts:dm.ts,
    locked:(getRec(origUrl)||{}).locked!==undefined?getRec(origUrl).locked:true,
    enriched:true, updated:new Date().toISOString()
  };
  if(isNew || (OV[origUrl]&&OV[origUrl]._new)) ov._new=true;
  // if URL changed on a new record, drop the old key
  if(isNew && OV[origUrl]) delete OV[origUrl];
  OV[url]=ov; saveOV();
  st.editing=null; st.selected=url;
  refresh(); showDetail(url); toast("Saved");
}
function revertRec(url){ delete OV[url]; saveOV(); st.editing=null; refresh();
  if(EFF.find(r=>r.url===url)){st.selected=url;showDetail(url);} else {st.selected=null;clearDetail();}
  toast("Reverted to original"); }

/* ---------------- edit bar actions ---------------- */
$("addBtn").onclick=()=>openEditor("__new__");
$("clearEditsBtn").onclick=()=>{
  modalConfirm("Clear all edits?", "This removes every enrichment/added record stored in this browser. Export first if you want a backup.", ()=>{
    OV={}; saveOV(); st.selected=null; st.editing=null; clearDetail(); refresh(); toast("All edits cleared");
  });
};
function download(obj,name){
  const blob=new Blob([JSON.stringify(obj,null,1)],{type:"application/json"});
  const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download=name; a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),1500);
}
$("exportBtn").onclick=()=>{
  const eff=effectiveRecords();
  const meta=Object.assign({},META,{count:LM.count,date_min:LM.date_min,date_max:LM.date_max,
    disciplines:LM.disciplines,methods:LM.methods,relevance:LM.relevance,
    generated:new Date().toISOString().slice(0,10)});
  download({meta,records:eff,rules:RULES},"data.json");
  toast("data.json exported &mdash; replace the file in the repo to bake in");
};
$("backupBtn").onclick=()=>{ download(OV,"jpt-wells-edits.json"); toast("Edits backed up"); };
$("restoreBtn").onclick=()=>$("restoreFile").click();
$("restoreFile").onchange=e=>{
  const f=e.target.files[0]; if(!f)return;
  const rd=new FileReader();
  rd.onload=()=>{ try{
      let obj=JSON.parse(rd.result);
      if(obj.records && !obj._new){ // a full data.json: pull overrides for changed/new only is ambiguous -> treat each record as override
        obj.records.forEach(r=>{ if(r.url) OV[r.url]=Object.assign({},r,{enriched:r.enriched||false}); });
      } else { Object.assign(OV,obj); }
      saveOV(); refresh(); toast("Edits restored");
    }catch(err){ toast("Could not read file"); }
  };
  rd.readAsText(f); e.target.value="";
};

/* ---------------- modal + toast ---------------- */
function modalConfirm(title,body,onYes){
  $("modalBox").innerHTML=`<h3>${esc(title)}</h3><p>${esc(body)}</p>
    <div style="display:flex;gap:8px;margin-top:14px;justify-content:flex-end">
      <button class="abtn ghost" id="mNo">Cancel</button><button class="abtn danger" id="mYes">Confirm</button></div>`;
  $("modal").classList.add("open");
  $("mNo").onclick=()=>$("modal").classList.remove("open");
  $("mYes").onclick=()=>{$("modal").classList.remove("open");onYes();};
}
$("modal").onclick=e=>{ if(e.target===$("modal")) $("modal").classList.remove("open"); };
let toastT;
function toast(msg){ const t=$("toast"); t.innerHTML=msg; t.classList.add("show"); clearTimeout(toastT); toastT=setTimeout(()=>t.classList.remove("show"),2200); }

$("foot").innerHTML="Built for a wells-engineering portfolio · JPT/SPE Enhanced recovery · self-contained · paste-to-enrich enabled (edits stored locally).";

/* ---------------- go ---------------- */
st.mMax = 0; refresh();
</script>
</body>
</html>"""

html = HTML.replace("__DATA__", DATA_JSON)
with open("index.html","w") as f:
    f.write(html)
print("index.html bytes:", len(html))
