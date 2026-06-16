#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject data.json into a self-contained HTML dashboard -> index.html"""
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

/* header */
header.hd{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:14px;
  border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:16px}
.hd h1{font-size:20px;margin:0 0 4px;letter-spacing:.2px}
.hd .sub{color:var(--mut);font-size:12.5px;max-width:760px}
.hd .src{font-size:12px;color:var(--mut2);margin-top:6px}
.kpis{display:flex;gap:10px;flex-wrap:wrap}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:8px 14px;min-width:96px}
.kpi b{display:block;font-size:20px;color:var(--accent)}
.kpi span{font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}

/* topic strip */
.topics{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
@media(max-width:900px){.topics{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.card h3{margin:0 0 10px;font-size:12px;text-transform:uppercase;letter-spacing:1px;color:var(--mut)}
.bar-row{display:flex;align-items:center;gap:10px;margin:5px 0;cursor:pointer}
.bar-row .lab{width:178px;font-size:12.5px;color:var(--txt);flex:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar-track{flex:1;background:var(--bg2);border-radius:6px;height:16px;position:relative;overflow:hidden}
.bar-fill{height:100%;border-radius:6px;transition:width .3s}
.bar-row .cnt{width:34px;text-align:right;color:var(--mut);font-variant-numeric:tabular-nums;font-size:12px}
.bar-row:hover .lab{color:var(--accent)}
.bar-row.active .lab{color:var(--accent);font-weight:600}
.method-chips{display:flex;flex-wrap:wrap;gap:6px}
.mchip{background:var(--panel2);border:1px solid var(--line);border-radius:20px;padding:3px 10px;font-size:11.5px;color:var(--mut)}
.mchip b{color:var(--accent);font-weight:600}

/* toolbar */
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

/* timeline */
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

/* main */
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

/* detail */
.detail{position:sticky;top:14px;background:var(--panel);border:1px solid var(--line);border-radius:14px;
  padding:0;overflow:hidden;min-height:420px}
.detail .empty{padding:60px 30px;text-align:center;color:var(--mut2)}
.detail .empty .big{font-size:42px;margin-bottom:10px;opacity:.5}
.dt-head{padding:18px 20px 14px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,var(--panel2),var(--panel))}
.dt-head .meta{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:12px;color:var(--mut);margin-bottom:8px}
.dt-head h2{margin:0 0 10px;font-size:18px;line-height:1.3}
.dt-head .tags{display:flex;flex-wrap:wrap;gap:6px}
.dt-body{padding:6px 20px 20px}
.sec{padding:13px 0;border-bottom:1px solid var(--line)}
.sec:last-child{border-bottom:0}
.sec h4{margin:0 0 6px;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:8px}
.sec h4 .ic{width:18px;height:18px;border-radius:5px;background:var(--bg2);display:inline-flex;align-items:center;justify-content:center;font-size:11px}
.sec p{margin:0;color:var(--txt);font-size:13.5px}
.sec .quote{border-left:2px solid var(--line);padding-left:11px;color:var(--mut);font-style:italic}
.kv{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
.kv .k{font-size:11px;background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:3px 9px;color:var(--mut)}
.dt-open{display:inline-flex;align-items:center;gap:7px;margin-top:6px;background:var(--accent);color:#04140f;
  font-weight:600;border-radius:9px;padding:9px 15px;font-size:13px}
.dt-open:hover{text-decoration:none;filter:brightness(1.08)}
.disclaimer{font-size:11px;color:var(--mut2);margin-top:16px;line-height:1.5;border-top:1px solid var(--line);padding-top:10px}
.foot{margin-top:26px;color:var(--mut2);font-size:11.5px;text-align:center}
</style>
</head>
<body>
<div class="wrap">
  <header class="hd">
    <div>
      <h1>Enhanced Recovery &rarr; Wells Engineering Intelligence</h1>
      <div class="sub">Curated &amp; classified briefs from JPT/SPE's <em>Enhanced recovery</em> topic, mapped to the integrated-operator wells-engineering disciplines &mdash; field development, drilling &amp; well construction, completions &amp; stimulation, production, and facilities. Click any title for an abstract-faithful technical summary.</div>
      <div class="src">Source: <a id="srcLink" target="_blank" rel="noopener">jpt.spe.org/topic/enhanced-recovery</a> &middot; <span id="srcMeta"></span></div>
    </div>
    <div class="kpis" id="kpis"></div>
  </header>

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
    </select>
    <label class="tgl"><input type="checkbox" id="wellsOnly"/> Wells-engineering core only</label>
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
      <div class="empty"><div class="big">&#9776;</div>Select a paper on the left to read its technical summary &mdash; Context, Technical approach, Business problem &amp; value, Challenges, Gaps, and the full abstract.</div>
    </div>
  </div>

  <div class="foot" id="foot"></div>
</div>

<script>
const DATA = __DATA__;
const RECS = DATA.records, META = DATA.meta;
const DCOLOR = {
 "Field Development":"var(--d-dev)","Drilling & Well Construction":"var(--d-drill)",
 "Completions & Stimulation":"var(--d-comp)","Production & Well Performance":"var(--d-prod)",
 "Facilities & Flow Assurance":"var(--d-fac)","Reservoir & EOR":"var(--d-res)",
 "CCUS & Decarbonization":"var(--d-ccus)","Digital, AI & Modeling":"var(--d-dig)"
};
const CORE = new Set(["Field Development","Drilling & Well Construction","Completions & Stimulation","Production & Well Performance","Facilities & Flow Assurance"]);
const esc = s => (s||"").replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

// ----- month axis -----
function monthList(){
  const a=META.date_min.slice(0,7), b=META.date_max.slice(0,7);
  let [y,m]=a.split("-").map(Number); const [ey,em]=b.split("-").map(Number);
  const out=[]; while(y<ey||(y===ey&&m<=em)){out.push(y+"-"+String(m).padStart(2,"0")); m++; if(m>12){m=1;y++;}}
  return out;
}
const MONTHS = monthList();
const MIDX = Object.fromEntries(MONTHS.map((m,i)=>[m,i]));

// ----- state -----
const st = {search:"",rel:"all",sort:"date_desc",wellsOnly:false,discs:new Set(),
            mMin:0,mMax:MONTHS.length-1,selected:null};

// ----- header / topic strip -----
document.getElementById("srcLink").href=META.source;
document.getElementById("srcLink").textContent=META.source.replace("https://","");
document.getElementById("srcMeta").textContent=
  META.count+" briefs · "+META.date_min+" → "+META.date_max+" · generated "+META.generated+" · abstract-faithful summaries";
const hiCount=(META.relevance.find(r=>r[0]==="High")||["",0])[1];
document.getElementById("kpis").innerHTML=[
  ["Papers",META.count],["Disciplines",META.disciplines.length],
  ["High-relevance",hiCount],["Span",(MONTHS.length)+" mo"]
].map(k=>`<div class="kpi"><b>${k[1]}</b><span>${k[0]}</span></div>`).join("");

const maxDisc=Math.max(...META.disciplines.map(d=>d[1]));
document.getElementById("discBars").innerHTML=META.disciplines.map(([d,c])=>`
 <div class="bar-row" data-disc="${esc(d)}">
   <div class="lab">${esc(d)}</div>
   <div class="bar-track"><div class="bar-fill" style="width:${(c/maxDisc*100).toFixed(1)}%;background:${DCOLOR[d]||'var(--accent)'}"></div></div>
   <div class="cnt">${c}</div>
 </div>`).join("");
document.querySelectorAll("#discBars .bar-row").forEach(r=>r.onclick=()=>toggleDisc(r.dataset.disc));

document.getElementById("methodChips").innerHTML=META.methods.slice(0,14)
  .map(([m,c])=>`<span class="mchip">${esc(m)} <b>${c}</b></span>`).join("");

// discipline filter chips
document.getElementById("discChips").innerHTML=META.disciplines.map(([d,c])=>`
 <span class="chip" data-disc="${esc(d)}"><span class="dot" style="background:${DCOLOR[d]||'#888'}"></span>${esc(d)} <span style="color:var(--mut2)">${c}</span></span>`).join("");
document.querySelectorAll("#discChips .chip").forEach(c=>c.onclick=()=>toggleDisc(c.dataset.disc));

function toggleDisc(d){ st.discs.has(d)?st.discs.delete(d):st.discs.add(d); render(); }

// ----- timeline build -----
const tlbars=document.getElementById("tlbars");
const slMin=document.getElementById("slMin"), slMax=document.getElementById("slMax");
slMin.max=slMax.max=MONTHS.length-1; slMax.value=MONTHS.length-1;
function monthCounts(recs){
  const c=new Array(MONTHS.length).fill(0);
  recs.forEach(r=>{const i=MIDX[r.ym]; if(i!=null)c[i]++;});
  return c;
}
function buildTimeline(){
  const counts=monthCounts(RECS); const mx=Math.max(1,...counts);
  tlbars.innerHTML=MONTHS.map((m,i)=>`<div class="tlbar" data-i="${i}" title="${m}: ${counts[i]} paper(s)" style="height:${(counts[i]/mx*100).toFixed(0)}%"></div>`).join("");
  tlbars.querySelectorAll(".tlbar").forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i;
    if(st.mMin===i&&st.mMax===i){st.mMin=0;st.mMax=MONTHS.length-1;}
    else {st.mMin=i;st.mMax=i;}
    slMin.value=st.mMin;slMax.value=st.mMax;render();
  });
  const ax=document.getElementById("tlaxis");
  const step=Math.ceil(MONTHS.length/6);
  let labs=[]; for(let i=0;i<MONTHS.length;i+=step)labs.push(MONTHS[i]);
  if(labs[labs.length-1]!==MONTHS[MONTHS.length-1])labs.push(MONTHS[MONTHS.length-1]);
  ax.innerHTML=labs.map(l=>`<span>${l}</span>`).join("");
}
function syncSliders(){
  let a=+slMin.value,b=+slMax.value; if(a>b){[a,b]=[b,a];}
  st.mMin=a;st.mMax=b;render();
}
slMin.oninput=syncSliders; slMax.oninput=syncSliders;

// ----- controls -----
document.getElementById("search").oninput=e=>{st.search=e.target.value.toLowerCase();render();};
document.getElementById("sort").onchange=e=>{st.sort=e.target.value;render();};
document.getElementById("wellsOnly").onchange=e=>{st.wellsOnly=e.target.checked;render();};
document.querySelectorAll("#relSeg button").forEach(b=>b.onclick=()=>{
  document.querySelectorAll("#relSeg button").forEach(x=>x.classList.remove("on"));
  b.classList.add("on"); st.rel=b.dataset.rel; render();
});
document.getElementById("clearBtn").onclick=()=>{
  st.search="";st.rel="all";st.sort="date_desc";st.wellsOnly=false;st.discs.clear();
  st.mMin=0;st.mMax=MONTHS.length-1; st.selected=null;
  document.getElementById("search").value="";document.getElementById("sort").value="date_desc";
  document.getElementById("wellsOnly").checked=false;
  document.querySelectorAll("#relSeg button").forEach(x=>x.classList.toggle("on",x.dataset.rel==="all"));
  slMin.value=0;slMax.value=MONTHS.length-1; render();
};

// ----- filtering -----
function passes(r){
  if(st.rel!=="all" && r.relevance!==st.rel) return false;
  if(st.wellsOnly && !r.disciplines.some(d=>CORE.has(d))) return false;
  if(st.discs.size && !r.disciplines.some(d=>st.discs.has(d))) return false;
  const i=MIDX[r.ym]; if(i<st.mMin||i>st.mMax) return false;
  if(st.search){
    const hay=(r.title+" "+r.abstract+" "+r.author+" "+r.source_tag+" "+
               r.disciplines.join(" ")+" "+(r.methods||[]).join(" ")+" "+
               (r.plays||[]).join(" ")+" "+(r.regions||[]).join(" ")+" "+(r.operators||[]).join(" ")).toLowerCase();
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
    return 0;
  });return a;
}

// ----- render -----
function discTag(d){return `<span class="tag disc" style="background:${DCOLOR[d]||'#888'}">${esc(d)}</span>`;}
function render(){
  // chips active state
  document.querySelectorAll("#discChips .chip").forEach(c=>{
    const on=st.discs.has(c.dataset.disc); c.classList.toggle("on",on);
    c.style.background=on?(DCOLOR[c.dataset.disc]||'#888'):''; c.style.color=on?'#04140f':'';
  });
  document.querySelectorAll("#discBars .bar-row").forEach(r=>r.classList.toggle("active",st.discs.has(r.dataset.disc)));
  // timeline selection highlight
  tlbars.querySelectorAll(".tlbar").forEach(b=>{const i=+b.dataset.i;b.classList.toggle("insel",i>=st.mMin&&i<=st.mMax);});
  document.getElementById("rngLabel").textContent=MONTHS[st.mMin]+" → "+MONTHS[st.mMax];

  let recs=RECS.filter(passes); sortRecs(recs);
  document.getElementById("resultCount").textContent=recs.length+" of "+RECS.length;
  const list=document.getElementById("list");
  if(!recs.length){list.innerHTML=`<div class="card" style="color:var(--mut)">No papers match the current filters.</div>`;}
  else list.innerHTML=recs.map(r=>{
    const sel=st.selected===r.url?"sel":"";
    const lead=r.disciplines[0];
    return `<div class="item ${sel}" data-url="${esc(r.url)}" style="border-left-color:${DCOLOR[lead]||'var(--line)'}">
      <div class="top"><span class="rel ${r.relevance}">${r.relevance}</span><span class="date">${esc(r.date)}</span></div>
      <div class="ttl">${esc(r.title)}</div>
      <div class="tags">${r.disciplines.slice(0,3).map(discTag).join("")}
        <span class="tag">${esc(r.source_tag)}</span>
        ${r.locked?'<span class="lock">&#128274; paywalled</span>':''}</div>
    </div>`;}).join("");
  list.querySelectorAll(".item").forEach(it=>it.onclick=()=>{st.selected=it.dataset.url;render();showDetail(it.dataset.url);});
}

function sec(ic,title,html){return `<div class="sec"><h4><span class="ic">${ic}</span>${title}</h4>${html}</div>`;}
function showDetail(url){
  const r=RECS.find(x=>x.url===url); if(!r)return;
  const d=document.getElementById("detail");
  const kv=(label,arr)=>arr&&arr.length?`<div class="kv"><span style="color:var(--mut2);font-size:11px;align-self:center">${label}:</span>${arr.map(a=>`<span class="k">${esc(a)}</span>`).join("")}</div>`:"";
  d.innerHTML=`
    <div class="dt-head">
      <div class="meta"><span class="rel ${r.relevance}">${r.relevance} relevance</span>
        <span>&#128197; ${esc(r.date)}</span><span>&#9997; ${esc(r.author)}</span>
        <span>&#127991; ${esc(r.source_tag)}</span>${r.locked?'<span class="lock">&#128274; paywalled</span>':''}</div>
      <h2>${esc(r.title)}</h2>
      <div class="tags">${r.disciplines.map(discTag).join("")}</div>
    </div>
    <div class="dt-body">
      <div class="sec"><p style="color:var(--mut);font-size:12.5px">${esc(r.relevance_note)}</p></div>
      ${sec("&#128205;","Context",`<p>${esc(r.context)}</p>`)}
      ${sec("&#9881;","Technical Approach",`<p>${esc(r.technical)}</p>`)}
      ${sec("&#128176;","Business Problem &amp; Value",`<p>${esc(r.business)}</p>`)}
      ${sec("&#9888;","Challenges",`<p>${esc(r.challenges)}</p>`)}
      ${sec("&#128300;","Gaps &amp; What's Behind the Paywall",`<p style="color:var(--mut)">${esc(r.gaps)}</p>`)}
      ${sec("&#128196;","Abstract (verbatim)",`<p class="quote">${esc(r.summary)}</p>`)}
      ${sec("&#127991;","Engineering Tags", kv("Methods",r.methods)+kv("Play/Field",r.plays)+kv("Region",r.regions)+kv("Operators",r.operators) || "<p style='color:var(--mut2)'>None detected in brief.</p>")}
      <a class="dt-open" href="${esc(r.url)}" target="_blank" rel="noopener">Open paper on JPT/SPE &rarr;</a>
      <div class="disclaimer">Summaries are <b>abstract-faithful</b>: built only from the public JPT brief. Discipline labels and engineering tags are auto-classified by keyword rules and may need expert review. Full methodology, datasets and quantitative results live in the paywalled source paper.</div>
    </div>`;
  d.scrollIntoView({behavior:"smooth",block:"nearest"});
}

document.getElementById("foot").innerHTML=
 "Built for a wells-engineering portfolio · data scraped from JPT/SPE Enhanced recovery topic ("+META.date_min+" to "+META.date_max+") · "+META.count+" papers · self-contained, no external dependencies.";

buildTimeline(); render();
</script>
</body>
</html>"""

html = HTML.replace("__DATA__", DATA_JSON)
with open("index.html","w") as f:
    f.write(html)
print("index.html bytes:", len(html))
